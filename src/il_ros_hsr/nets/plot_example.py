import argparse, cv2, os, pickle, sys
from os.path import join
from collections import defaultdict
import numpy as np
np.set_printoptions(suppress=True, linewidth=200, precision=4)

from il_ros_hsr.nets import options as opt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')


def plot_simple_v1(model, stats_t, stats_v):
    """Simple plot to observe performance.
    """
    nrows, ncols = 1, 2
    fig, ax = plt.subplots(nrows, ncols, squeeze=False, figsize=(14*ncols,9*nrows))

    # TODO: finish implementing

    ax[0,0].set_title('Train Stats', fontsize=opt.tsize)
    ax[0,1].set_title('Valid Stats', fontsize=opt.tsize)

    # Bells and whistles
    for r in range(nrows):
        for c in range(ncols):
            leg = ax[r,c].legend(loc="best", ncol=2, prop={'size':opt.legendsize})
            for legobj in leg.legendHandles:
                legobj.set_linewidth(5.0)
            ax[r,c].tick_params(axis='x', labelsize=opt.ticksize)
            ax[r,c].tick_params(axis='y', labelsize=opt.ticksize)
    plt.tight_layout()

    # Finally, save.
    figname = join(opt.FIG_TMPDIR, 'plot_bars_coverage_v02.png')
    plt.savefig(figname)
    print("\nJust saved: {}".format(figname))


if __name__ == "__main__":
    # Perhaps make this more formalized?
    # Could alternatively save in directory corresponding to HEAD?
    if not os.path.exists(opt.FIG_TMPDIR):
        os.makedirs(opt.FIG_TMPDIR)

    HEAD  = '/nfs/diskstation/seita/bedmake_ssl'
    MODEL = 'resnet18_2018-11-16-14-27_000/'
    train_pth = join(HEAD, MODEL, 'stats_train.pkl')
    valid_pth = join(HEAD, MODEL, 'stats_valid.pkl')
    
    with open(train_pth, 'r') as fh:
        stats_train = pickle.load(fh)
    with open(valid_pth, 'r') as fh:
        stats_valid = pickle.load(fh)

    plot_simple_v1(MODEL, stats_train, stats_valid)
