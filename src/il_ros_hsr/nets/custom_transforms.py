"""Custom transformations for data processing in PyTorch.
"""
import cv2, os, sys, pickle
from os.path import join
import numpy as np
import torch
import torchvision.models as models
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import functional as F
from il_ros_hsr.nets import options as opt


class Normalize(object):
    """Normalize. LGTM.
    """
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def __call__(self, sample):
        img_t   = F.normalize(sample['img_t'],   self.mean, self.std)
        img_tp1 = F.normalize(sample['img_tp1'], self.mean, self.std)
        assert img_t.shape[0] == 3 and img_t.shape == img_tp1.shape, image.shape

        new_sample = {
            'img_t':   img_t,
            'img_tp1': img_tp1, 
            'label':   sample['label'],
        }
        return new_sample


class ToTensor(object):
    """Convert ndarrays in sample to Tensors. LGTM.
    
    Like in normal PyTorch's ToTensor() we scale pixel values to be in [0,1].
    BUT we should also scale the labels to better condition the optimization.
    """
    def __call__(self, sample):
        img_t   = sample['img_t']
        img_tp1 = sample['img_tp1']
        assert isinstance(img_t, np.ndarray), img_t

        h, w, c = img_t.shape
        # swap color axis because
        # numpy image: H x W x C
        # torch image: C X H X W
        img_t   = img_t.transpose((2, 0, 1))
        img_tp1 = img_tp1.transpose((2, 0, 1))

        # Convert to numpy, but we need to then divide by 255.
        img_t   = torch.from_numpy(img_t)
        img_tp1 = torch.from_numpy(img_tp1)
        assert isinstance(img_t, torch.ByteTensor), img_t
        assert isinstance(img_tp1, torch.ByteTensor), img_tp1
        img_t   = img_t.float().div(255)
        img_tp1 = img_tp1.float().div(255)

        # The target needs to be set in an array. Note scaling!
        # I _think_ we can scale by current width and height.
        # Also, for the angle, easier to provide the _class_.

        target = np.array([
            sample['target_xy'][0] / float(w),
            sample['target_xy'][1] / float(h),
            #sample['target_l'][0] / 20.0,
            np.argmax(sample['target_ang']), # class _index_
        ])
        label = torch.from_numpy(target)

        new_sample = {
            'img_t':   img_t,
            'img_tp1': img_tp1, 
            'label':   label,
        }
        return new_sample


class Rescale(object):
    """Rescale the image in a sample to a given size. LGTM.

    Args:
        output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same. NOTE: I am likely to
            use this only for making square images, but it might be useful to
            keep the aspect ratio for later... or we can rescale and THEN do the
            random crop after that to make it square.
    """

    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        self.output_size = output_size

    def __call__(self, sample):
        img_t   = sample['img_t']
        img_tp1 = sample['img_tp1']
        target  = sample['target_xy']

        # In cv2, image shape represents (height, width, channels).
        h, w, channels = img_t.shape
        h, w = float(h), float(w)
        assert channels == 3, channels

        if isinstance(self.output_size, int):
            if h > w:
                new_h, new_w = self.output_size * h / w, self.output_size
            else:
                new_h, new_w = self.output_size, self.output_size * w / h
        else:
            new_h, new_w = self.output_size
        new_h, new_w = int(new_h), int(new_w)

        # Daniel: tutorial said h,w but cv2.resize uses w,h ... I tested it.
        # Despite order of w,h here, for `img.shape` it's h,w,(channels). Confusing.
        img_t   = cv2.resize(img_t,   (new_w, new_h))
        img_tp1 = cv2.resize(img_tp1, (new_w, new_h))

        # Scale the target, which is the xy. Angle stays the same. For now we
        # don't change the length as we can keep it fixed.
        target_xy = ( target[0] * (new_w / w), target[1] * (new_h / h) )

        new_sample = {
            'img_t':      img_t,
            'img_tp1':    img_tp1, 
            'target_xy':  target_xy,
            'target_l':   sample['target_l'],
            'target_ang': sample['target_ang'],
            'raw_ang':    sample['raw_ang'],
        }
        return new_sample


class RandomCrop(object):
    """Crop randomly the image in a sample. LGTM.

    For this, we do similar croppings for both images.

    Args:
        output_size (tuple or int): Desired output size. If int, square crop.
    """
    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size)
        else:
            assert len(output_size) == 2
            self.output_size = output_size

    def __call__(self, sample):
        img_t   = sample['img_t']
        img_tp1 = sample['img_tp1']
        target  = sample['target_xy']
        h, w, channels = img_t.shape
        assert channels == 3, img_t.shape
        h, w = float(h), float(w)
        new_h, new_w = self.output_size

        # Intuition: we want to "remove" `w-new_w` pixels. So, starting from the
        # left, randomly pick starting point, and only go `new_w` to the right.
        top  = np.random.randint(0, h - new_h)
        left = np.random.randint(0, w - new_w)

        img_t = img_t[top: top + new_h,
                      left: left + new_w]
        img_tp1 = img_tp1[top: top + new_h,
                          left: left + new_w]
        target_x = target[0] - left
        target_y = target[1] - top

        # IMPORTANT! In detection, our targets could have been cropped out. To
        # avoid this, only crop a little bit. That way we can 'approximate' it
        # by thresholding the value to be within the image.
        target_x = min( max(target_x, 0.0), new_w )
        target_y = min( max(target_y, 0.0), new_h )

        new_sample = {
            'img_t':      img_t,
            'img_tp1':    img_tp1, 
            'target_xy':  (target_x, target_y),
            'target_l':   sample['target_l'],
            'target_ang': sample['target_ang'],
            'raw_ang':    sample['raw_ang'],
        }
        return new_sample


class CenterCrop(object):
    """Crop the image, in a *centered* manner!! Similar to RandomCrop except the
    `top` and `left` parts are determined analytically.

    Args:
        output_size (tuple or int): Desired output size. If int, square crop.
    """
    def __init__(self, output_size):
        assert isinstance(output_size, (int, tuple))
        if isinstance(output_size, int):
            self.output_size = (output_size, output_size)
        else:
            assert len(output_size) == 2
            self.output_size = output_size

    def __call__(self, sample):
        img_t   = sample['img_t']
        img_tp1 = sample['img_tp1']
        target  = sample['target_xy']
        h, w, channels = img_t.shape
        assert channels == 3, img_t.shape
        h, w = float(h), float(w)
        new_h, new_w = self.output_size

        # Intuition: we want to "remove" `w-new_w` pixels. So, starting from the
        # left, randomly pick starting point, and only go `new_w` to the right.
        # Since this is CENTERED we want to take the midpoint of these.
        top  = int((h - new_h) / 2.0)
        left = int((w - new_w) / 2.0)

        img_t = img_t[top: top + new_h,
                      left: left + new_w]
        img_tp1 = img_tp1[top: top + new_h,
                          left: left + new_w]
        target_x = target[0] - left
        target_y = target[1] - top

        # IMPORTANT! In detection, our targets could have been cropped out. To
        # avoid this, only crop a little bit. That way we can 'approximate' it
        # by thresholding the value to be within the image.
        target_x = min( max(target_x, 0.0), new_w )
        target_y = min( max(target_y, 0.0), new_h )

        new_sample = {
            'img_t':      img_t,
            'img_tp1':    img_tp1, 
            'target_xy':  (target_x, target_y),
            'target_l':   sample['target_l'],
            'target_ang': sample['target_ang'],
            'raw_ang':    sample['raw_ang'],
        }
        return new_sample


class RandomHorizontalFlip(object):
    """AKA, a flip _about_ the *VERICAL* axis. LGTM.

    If we want a 'vertical' flip (the 'intuitive' meaning) then second arg in
    `cv2.flip()` is 0, not 1.  If we flip, need to adjust label, using CURRENT
    image size, since it might have been resized earlier.

    With two images, we need the images flipped _together_, and also the action
    center changes. The direction only changes if the action was horizontal. Can
    detect this with `raw_ang`, independent of our action parameterization.
    """
    def __init__(self, flipping_ratio=0.5):
        self.flipping_ratio = 0.5

    def __call__(self, sample):
        img_t      = sample['img_t']
        img_tp1    = sample['img_tp1']
        target_xy  = sample['target_xy']
        target_ang = sample['target_ang']
        raw_ang    = sample['raw_ang']

        # Careful, names should override above values from `sample` if needed.
        if np.random.rand() < self.flipping_ratio:
            h, w, c   = img_t.shape
            target_xy = (w - target_xy[0], target_xy[1])
            img_t     = cv2.flip(img_t, 1)
            img_tp1   = cv2.flip(img_tp1, 1)

            # If direction is 0 or 180, we flip and reverse these targets.
            if raw_ang == 0:
                assert target_ang[0] == 1, target_ang
                target_ang = [0, 0, 1, 0]
            elif raw_ang == 180:
                assert target_ang[2] == 1, target_ang
                target_ang = [1, 0, 0, 0]

        new_sample = {
            'img_t':      img_t,
            'img_tp1':    img_tp1, 
            'target_xy':  target_xy,
            'target_l':   sample['target_l'],
            'target_ang': target_ang,
            'raw_ang':    raw_ang,
        }
        return new_sample


class BedGraspDataset(Dataset):
    """Custom dataset, inspired by Face Landmarks dataset."""

    def __init__(self, infodir, transform=None):
        self.infodir = infodir
        with open(self.infodir, 'r') as fh:
            self.data = pickle.load(fh)
        self.transform = transform

    def __len__(self):
        """We saved `self.data` as a list, one element per item."""
        return len(self.data)

    def __getitem__(self, idx):
        """
        Each item in `self.data` gives us sufficient information about a single
        training data point. We also need to figure out action representation.

        Currently it's one-hot for the angles. Up to debate. Rope manipulation
        paper discretized angle into 36 values (and length to 10 values).
        Action location discretized onto a 20x20 grid. They argue that
        classification lets for multimodality.
        """
        png_t, png_tp1, a_t = self.data[idx]
        img_t   = cv2.imread(png_t)
        img_tp1 = cv2.imread(png_tp1)
        assert img_t is not None and img_tp1 is not None

        target_xy = [
            float(a_t['x']),
            float(a_t['y']),
        ]
        target_l = [
            float(a_t['length'])
        ]
        target_ang = [
            float(a_t['angle'] == 0),
            float(a_t['angle'] == 90),
            float(a_t['angle'] == 180),
            float(a_t['angle'] == 270),
        ]

        # Keep `raw_ang` constant, as 0, 90, 180, 270. Do _not_ change it. The
        # network will not use it. It is for making transforms easier to write.
        sample = {
            'img_t':      img_t,
            'img_tp1':    img_tp1, 
            'target_xy':  target_xy,
            'target_l':   target_l,
            'target_ang': target_ang,
            'raw_ang':    a_t['angle']
        }

        if self.transform:
            sample = self.transform(sample)
        return sample


def _save_viz(sample, idx, istrain):
    """Save current and target images into one img."""
    img_t      = sample['img_t']
    img_tp1    = sample['img_tp1']
    target_xy  = sample['target_xy']
    target_l   = sample['target_l']
    target_ang = sample['target_ang']
    raw_ang    = sample['raw_ang']

    targ = (int(target_xy[0]), int(target_xy[1]))
    cv2.circle(img_t, center=targ, radius=2, color=opt.RED, thickness=-1)
    cv2.circle(img_t, center=targ, radius=3, color=opt.BLACK, thickness=1)

    # This is the direction. Don't worry about the length, we can't easily get
    # it in pixel space and we keep length in world-space roughly fixed anyway.
    if target_ang[0] == 1:
        offset = [50, 0]
    elif target_ang[1] == 1:
        offset = [0, -50]
    elif target_ang[2] == 1:
        offset = [-50, 0]
    elif target_ang[3] == 1:
        offset = [0, 50]
    else:
        raise ValueError(target_ang)

    goal = (targ[0] + offset[0], targ[1] + offset[1])
    int(target_xy[0]),int(target_xy[1])
    cv2.arrowedLine(img_t, targ, goal, color=opt.BLUE, thickness=2)
    cv2.putText(img=img_t, 
                text="raw ang: {}".format(raw_ang),
                org=(10,20),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                fontScale=0.75, 
                color=opt.GREEN,
                thickness=1)

    # Combine images (t,tp1) together.
    hstack = np.concatenate((img_t, img_tp1), axis=1)
    if istrain:
        head = join(opt.TRANSFORMS_TMPDIR,'train_imgs')
    else:
        head = join(opt.TRANSFORMS_TMPDIR,'valid_imgs')
    fname = join(head, 'example_{}.png'.format(str(idx).zfill(4)))
    cv2.imwrite(fname, hstack)


if __name__ == "__main__":
    """Use to debug transforms. In general don't use ToTensor or Normalize since
    that won't let us save and visualize the png images.
    """
    if not os.path.exists(opt.TRANSFORMS_TMPDIR):
        os.makedirs(opt.TRANSFORMS_TMPDIR)
        os.makedirs(join(opt.TRANSFORMS_TMPDIR,'train_imgs'))
        os.makedirs(join(opt.TRANSFORMS_TMPDIR,'valid_imgs'))
    assert os.path.exists(join(opt.TRANSFORMS_TMPDIR,'valid_imgs'))

    # To debug transformation(s), pick any one to run, get images, and save.
    transforms_train = transforms.Compose([
        Rescale((256,256)),
        RandomCrop((224,224)),
        RandomHorizontalFlip(),
        #ToTensor(),
        #Normalize(opt.MEAN, opt.STD),
    ])
    transforms_valid = transforms.Compose([
        Rescale((256,256)),
        CenterCrop((224,224)),
        #ToTensor(),
        #Normalize(opt.MEAN, opt.STD),
    ])

    TRAIN_INFO = join(opt.NEW_DATA_SSL,'train/data_train_loader.pkl')
    VALID_INFO = join(opt.NEW_DATA_SSL,'valid/data_valid_loader.pkl')
    gdata_t = BedGraspDataset(infodir=TRAIN_INFO, transform=transforms_train)
    gdata_v = BedGraspDataset(infodir=VALID_INFO, transform=transforms_valid)

    # Can debug here, but only works if we didn't call `ToTensor()` (+normalize).
    print("len(train):  {}".format(len(gdata_t)))
    print("len(valid):  {}".format(len(gdata_v)))

    for i in range(len(gdata_t)):
        _save_viz(gdata_t[i], idx=i, istrain=True)
    for i in range(len(gdata_v)):
        _save_viz(gdata_v[i], idx=i, istrain=False)

