"""For docs on saving/loading, see:
https://pytorch.org/tutorials/beginner/saving_loading_models.html
This is for quick testing, NOT for deployment with the physical HSR.
"""
import torch
from torchvision import transforms

from il_ros_hsr.nets.net import ActPredictorNet
from il_ros_hsr.nets import options as opt
from il_ros_hsr.nets import custom_transforms as CT

import argparse, copy, cv2, os, sys, pickle, json
import time, datetime
import numpy as np
from os.path import join
from collections import defaultdict


def _save_and_viz(pth_t, pth_tp1, img_t, img_tp1, out_pos, out_ang):
    """Really need to put much of this in `options.py` and reuse among scripts.
    """
    out_pos = out_pos.cpu().detach().numpy().squeeze()
    if not os.path.exists(opt.DEPLOY_TMPDIR):
        os.makedirs(opt.DEPLOY_TMPDIR)
    b_pth_t   = os.path.basename(pth_t)
    b_pth_tp1 = os.path.basename(pth_tp1)
    print("base pth_t:             {}".format(b_pth_t))
    print("base pth_tp1:           {}".format(b_pth_tp1))
    print("predicted position:     {}".format(out_pos))
    print("predicted angle logits: {}".format(out_ang))
    print("img_tp1.shape:          {}".format(img_tp1.shape))

    # --------------------------------------------------------------------------
    # The raw images
    hstack1 = np.concatenate((img_t, img_tp1), axis=1)
    fname1 = join(opt.DEPLOY_TMPDIR,'{}_v1.png'.format(b_pth_t))
    cv2.imwrite(fname1, hstack1)
    print("Look at: {}".format(fname1))

    # --------------------------------------------------------------------------
    # Transformed images, but _without_ the tensor and normalization stuff.
    transforms_valid_notensors = transforms.Compose([
        CT.Rescale((256,256)),
        CT.CenterCrop((224,224)),
    ])
    t_input = transform_imgs(img_t, img_tp1, transforms_valid_notensors)
    t_img_t   = t_input['img_t']
    t_img_tp1 = t_input['img_tp1']
    h, w, c = t_img_t.shape
    assert t_img_t.shape == t_img_tp1.shape == (224,224,3), t_img_t.shape

    # Save the _transformed_ images.
    hstack2 = np.concatenate((t_img_t, t_img_tp1), axis=1)
    fname2 = join(opt.DEPLOY_TMPDIR,'{}_v2.png'.format(b_pth_t))
    cv2.imwrite(fname2, hstack2)
    print("Look at: {}".format(fname2))

    # --------------------------------------------------------------------------
    # Overlay some stuff on the images (must de-process label, though).
    pred_pos_int = int(out_pos[0]*w), int(out_pos[1]*h)
    img = np.ascontiguousarray(t_img_t, dtype=np.uint8)
    cv2.circle(img, center=pred_pos_int, radius=2, color=opt.BLUE,  thickness=-1)
    cv2.circle(img, center=pred_pos_int, radius=3, color=opt.GREEN, thickness=1)
    cv2.putText(img=img, 
                text="pred pos: {}".format(pred_pos_int),
                org=(10,15),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                fontScale=0.5, 
                color=opt.GREEN,
                thickness=1)

    # Save _transformed_ images, WITH predicted stuff overlaid on it.
    hstack3 = np.concatenate((img, t_img_tp1), axis=1)
    fname3 = join(opt.DEPLOY_TMPDIR,'{}_v3.png'.format(b_pth_t))
    cv2.imwrite(fname3, hstack3)
    print("Look at: {}".format(fname3))

    # --------------------------------------------------------------------------
    # Finally let's save at the original resolution. This requires additional
    # de-processing of the labels. Right now I add 16 to each coordinate since I
    # know for validation, we went from (256,256) -> (224,224). Then we need to
    # do additional stuff for (256,256) -> (480,640). Will need to fix if these
    # are not the case in other scenarios ... 
    # --------------------------------------------------------------------------
    pos = (pred_pos_int[0] + 16, pred_pos_int[1] + 16)
    widthf  = 640.0 / 256.0
    heightf = 480.0 / 256.0
    pos = ( int(pos[0]*widthf), int(pos[1]*heightf) )

    img = np.copy(img_t)
    cv2.circle(img, center=pos, radius=4, color=opt.BLUE,  thickness=-1)
    cv2.circle(img, center=pos, radius=6, color=opt.GREEN, thickness=1)
    cv2.putText(img=img, 
                text="pred pos, original size: {}".format(pos),
                org=(10,15),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                fontScale=0.6, 
                color=opt.GREEN,
                thickness=1)

    # Save _transformed_ images, WITH predicted stuff overlaid on it.
    hstack4 = np.concatenate((img, img_tp1), axis=1)
    fname4 = join(opt.DEPLOY_TMPDIR,'{}_v4.png'.format(b_pth_t))
    cv2.imwrite(fname4, hstack4)
    print("Look at: {}".format(fname4))


def transform_imgs(img_t, img_tp1, transform):
    """Designed for test-time inference.
    
    During training and validation, we have a class which works by taking pickle
    file with lists of the data in training / validation, and it processes them.
    But here, we assume we want to pass a new image to the model. The issue,
    however, is that the transforms that we use for validation (which we should
    use for test-time inference on new images with no labels) rely on assuming
    we have a target. So we will just add fictional targets.

    Parameters
    ----------
    img_t, img_tp1:
        Two numpy arrays representing the two images for the network. We return
        their transformations.
    transform:
        Set of composed transforms that we used for VALIDATION.
    """
    assert img_t.shape == img_tp1.shape

    # Fictional targets so that we can apply the same validation set transforms
    # Another way is to set transform classes to optionally ignore targets?
    target_xy  = [0.0, 0.0]
    target_l   = [0.0]
    target_ang = [1.0, 0.0, 0.0, 0.0]

    # Feed through our transformations and return.
    sample = {
        'img_t':      img_t,
        'img_tp1':    img_tp1, 
        'target_xy':  target_xy,
        'target_l':   target_l,
        'target_ang': target_ang,
        'raw_ang':    -1,
    }
    sample = transform(sample)
    return sample


def deploy(act_predictor):
    """Let's see how to load just directly from two png images.
    
    In theory we should figure out what we can avoid from all the data loading
    machinery when we trained this network.
    """
    transforms_valid = transforms.Compose([
        CT.Rescale((256,256)),
        CT.CenterCrop((224,224)),
        CT.ToTensor(),
        CT.Normalize(opt.MEAN, opt.STD),
    ])

    # Pick images to try here; careful, don't pick 'boundaries' of episodes.
    pth_t   = 'ssldata2/d_img_proc_10_004.png'
    pth_tp1 = 'ssldata2/d_img_proc_10_005.png'
    img_t   = cv2.imread(pth_t)
    img_tp1 = cv2.imread(pth_tp1)

    t_input    = transform_imgs(img_t, img_tp1, transforms_valid)
    t_imgs_t   = t_input['img_t'].unsqueeze(0)
    t_imgs_tp1 = t_input['img_tp1'].unsqueeze(0)

    out_pos, out_ang = act_predictor(t_imgs_t, t_imgs_tp1)
    _save_and_viz(pth_t, pth_tp1, img_t, img_tp1, out_pos, out_ang)


if __name__ == "__main__":
    # Pick the model that we want to load.
    HEAD  = '/nfs/diskstation/seita/bedmake_ssl'
    MODEL = 'resnet18_2018-11-18-09-50_000'
    PATH  = join(HEAD, MODEL, 'act_predictor.pt')

    # Get old args we used, and put into a newer Namespace object.
    with open(join(HEAD, MODEL, 'args.json'), 'r') as fh:
        saved_args = json.load(fh)
    args = opt._json_to_args(jsonfile=saved_args)

    # Load the pretrained model. If you print state dict, these start with
    # `layer` as that was the convention with the ResNet saved models.
    model = opt.get_pretrained_model(args)

    # But now we use act predictor, with `pretrained_stem` in state dict.
    act_predictor = ActPredictorNet(model, args)
    #opt.debug_state_dict(model=act_predictor)
    act_predictor.load_state_dict(torch.load(PATH))
    act_predictor.eval()

    deploy(act_predictor)
