import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision import datasets, transforms
from torchvision.transforms import functional as F

from il_ros_hsr.nets.net import PolicyNet
from il_ros_hsr.nets import options as opt
from il_ros_hsr.nets import custom_transforms as CT

import argparse, copy, cv2, os, sys, pickle
import time, datetime
import numpy as np
from os.path import join
from collections import defaultdict


def deploy():
    """Test model deployment.
    """
    pass


if __name__ == "__main__":
    ## # --------------------------------------------------------------------------
    ## pp = argparse.ArgumentParser()
    ## pp.add_argument('--model', type=str, default='resnet18')
    ## pp.add_argument('--num_epochs', type=int, default=30)
    ## pp.add_argument('--seed', type=int, default=0)

    ## # If changing the optimizer, the learning rate must be adjusted as well.
    ## # I think ~1e-4 for Adam, ~1e-2 for SGD. Adam generally needs lower LRs.
    ## pp.add_argument('--optim', type=str, default='adam')
    ## pp.add_argument('--lrate', type=str, default=0.0001)

    ## # Rely on several options for the loss type. See `PolicyNet` for details.
    ## pp.add_argument('--model_type', type=int, default=1)

    ## args = pp.parse_args() 
    ## # --------------------------------------------------------------------------
    ## torch.manual_seed(args.seed)

    ## save_dir = opt.get_save_dir(args)
    ## print("Saving in: {}".format(save_dir))
    ## resnet = opt.get_model(args)
    ## model, stats_train, stats_valid = train(resnet, args)

    ## # https://pytorch.org/tutorials/beginner/saving_loading_models.html
    ## torch.save(model.state_dict(), join(save_dir,'model.pt'))

    ## with open(join(save_dir,'stats_train.pkl'), 'w') as fh:
    ##     pickle.dump(stats_train, fh)
    ## with open(join(save_dir,'stats_valid.pkl'), 'w') as fh:
    ##     pickle.dump(stats_valid, fh)
    ## print("Done!")
    pass
