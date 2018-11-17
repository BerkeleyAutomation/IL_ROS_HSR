"""
For docs on saving/loading, see:
https://pytorch.org/tutorials/beginner/saving_loading_models.html
"""
import torch

from il_ros_hsr.nets.net import ActPredictorNet
from il_ros_hsr.nets import options as opt
from il_ros_hsr.nets import custom_transforms as CT

import argparse, copy, cv2, os, sys, pickle, json
import time, datetime
import numpy as np
from os.path import join
from collections import defaultdict


def _json_to_args(jsonfile):
    args = argparse.Namespace()
    args.pretrained_model = jsonfile['pretrained_model']
    args.model_type       = jsonfile['model_type']
    return args


def deploy(act_predictor):
    # TODO this weekend
    pass


if __name__ == "__main__":
    # Pick the model that we want to load.
    HEAD  = '/nfs/diskstation/seita/bedmake_ssl'
    MODEL = 'resnet18_2018-11-16-16-53_000'
    PATH  = join(HEAD, MODEL, 'act_predictor.pt')

    # Get old args we used, and put into a newer Namespace object.
    with open(join(HEAD, MODEL, 'args.json'), 'r') as fh:
        saved_args = json.load(fh)
    args = _json_to_args(jsonfile=saved_args)

    # Load the pretrained model. If you print state dict, these start with
    # `layer` as that was the convention with the ResNet saved models.
    model = opt.get_pretrained_model(args)

    # But now we use act predictor, with `pretrained_stem` in state dict.
    act_predictor = ActPredictorNet(model, args)
    #opt.debug_state_dict(model=act_predictor)
    act_predictor.load_state_dict(torch.load(PATH))
    act_predictor.eval()

    # Use the act predictor somehow!
    deploy(act_predictor)
