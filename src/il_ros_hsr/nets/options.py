import torchvision.models as models
import os, datetime, json, sys

# ------------------------------------------------------------------------------
# Data paths
# ------------------------------------------------------------------------------

# For `prepare_data.py`
RAW_DATA_SSL = 'ssldata'
NEW_DATA_SSL = 'ssldata_pytorch'

# For `custom_transforms.py`, for data inspection after preparing the data.
TRANSFORMS_TMPDIR = 'tmp_transforms_test/'

# For `train_action_predictor.py`
VALID_TMPDIR = 'tmp_valid_preds/'

# For plotting
FIG_TMPDIR = 'tmp_figs/'

# ------------------------------------------------------------------------------
# Mean and std for PyTorch
# ------------------------------------------------------------------------------

# ssldata
MEAN = [0.4197973, 0.4026070, 0.4141044]
STD  = [0.4306730, 0.4403830, 0.4480426]

# ssldata2
MEAN = [0.26906217, 0.26906217, 0.26906217]
STD = [0.32756073, 0.32756073, 0.32756073]

# ------------------------------------------------------------------------------
# Colors for OpenCV, so we don't need to put in these numbers.
# ------------------------------------------------------------------------------

BLUE  = (255,0,0)
GREEN = (0,255,0)
RED   = (0,0,255)
BLACK = (0,0,0)
WHITE = (255,255,255)

# ------------------------------------------------------------------------------
# matplotlib
# ------------------------------------------------------------------------------

# Common stuff, label sizes, line width, etc.
tsize = 35
xsize = 28
ysize = 28
ticksize = 27
legendsize = 27
lw = 2

# For bar charts
bar_width = 0.35
opacity = 0.4
opacity1 = 0.5
opacity2 = 0.8
error_kw = dict(lw=4, capsize=5, capthick=3)

# ------------------------------------------------------------------------------
# Utility methods
# ------------------------------------------------------------------------------

RESNET_18 = models.resnet18(pretrained=True)
RESNET_34 = models.resnet34(pretrained=True)
RESNET_50 = models.resnet50(pretrained=True)

def get_pretrained_model(args):
    """Pre-trained model.
    """
    if args.pretrained_model == 'resnet18':
        return RESNET_18
    elif args.pretrained_model == 'resnet34':
        return RESNET_34
    elif args.pretrained_model == 'resnet50':
        return RESNET_50
    else:
        raise ValueError(args.model)


def get_save_dir(args):
    """Make save path for whatever agent we are training. Save args as well.
    """
    head    = '/nfs/diskstation/seita/bedmake_ssl'
    date    = '{}'.format( datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') )
    seedstr = str(args.seed).zfill(3)
    suffix  = "{}_{}_{}".format(args.pretrained_model, date, seedstr)
    result_path = os.path.join(head, suffix)
    assert not os.path.exists(result_path), "Error: {} exists!".format(result_path)

    os.makedirs(result_path)
    with open(os.path.join(result_path,'args.json'), 'w') as fh:
        json.dump(vars(args), fh)

    return result_path


def debug_state_dict(model):
    print("\nHere are the keys in this model's `state_dict()`:\n")
    for key in model.state_dict():
        print(key)
    print("\n")
