import torch
import torch.nn as nn
import os, sys


class PolicyNet(nn.Module):
    """The policy network, or what determines actions.

    We borrow a `model` as input, which is the pre-trained ResNet stem.  Then we
    can adjust the last layer so it doesn't go to just 2 units but more (e.g.,
    100). We can additionally define more layers after that.
    
    It's easy in `forward` to take in multiple inputs (just add more arguments)
    and to also _return_ multiple outputs.
    """

    def __init__(self, model, args):
        super(PolicyNet, self).__init__()
        self.args = args

        # Handle pre-trained stem, then FC after
        num_latent = model.fc.in_features
        model.fc = nn.Linear(num_latent, 200)
        self.pretrain_stem = model
        self.fc1 = nn.Linear(400, 200)
        self.fc2 = nn.Linear(200, 200)

        self.fc_pixel = nn.Linear(200, 2)
        self.fc_angle = nn.Linear(200, 4)


    def forward(self, x1, x2):
        x1 = self.pretrain_stem(x1) # (B,3,224,224) -> (B,200)
        x2 = self.pretrain_stem(x2) # (B,3,224,224) -> (B,200)
        x = torch.cat((x1,x2), 1)   # {(B,200),(B,200)} -> (B,400)
        x = self.fc1(x)             # (B,400) -> (B,200)
        x = self.fc2(x)             # (B,200) -> (B,200)
        assert x.shape[0] == x1.shape[0] == x2.shape[0]

        # Different design choices for the network
        args = self.args
        if args.model_type == 1:
            x_pixel = self.fc_pixel(x)
            x_angle = self.fc_angle(x)
            return (x_pixel, x_angle)
        elif args.model_type == 2:
            raise NotImplementedError()
        elif args.model_type == 3:
            raise NotImplementedError()
        else:
            raise ValueError(args.model_type)

