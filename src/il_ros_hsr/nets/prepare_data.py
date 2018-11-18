import argparse, copy, cv2, os, sys, pickle, time
import numpy as np
from os.path import join
from il_ros_hsr.nets import options as opt


def prepare_ssldata():
    """Create appropriate data for PyTorch, from Ryan's first data collection.

    As usual, need a way to provide an index into the correct file name/target.
    BTW, for training and validation splits, we should split based on EPISODES,
    not on the pooled set of images, as the data is (s_t, a_t, s_{t+1}). Think
    of it as iterating through actions, not images, but we have to _skip_
    indices which correspond to any `None` actions; those indicate episode
    transitions.

    We should assign our episodes to train/valid at random. Adjust
    `_is_validation()` if desired.

    We save the image PATHS, but do not adjust the raw images here.
    """
    def _is_validation(t):
        train_cutoff = 60
        return (t > train_cutoff)

    raw_data = join(opt.RAW_DATA_SSL,'rollout.pkl')
    assert not os.path.exists(opt.NEW_DATA_SSL), \
            "target exists, please remove it:\n\t{}".format(opt.NEW_DATA_SSL)
    os.makedirs(opt.NEW_DATA_SSL)
    path_train = join(opt.NEW_DATA_SSL,'train')
    path_valid = join(opt.NEW_DATA_SSL,'valid')
    os.makedirs(path_train)
    os.makedirs(path_valid)

    # For data loader, need to go from index to target, for BOTH train and valid.
    loader_train_path = join(opt.NEW_DATA_SSL,'train','data_train_loader.pkl')
    loader_valid_path = join(opt.NEW_DATA_SSL,'valid','data_valid_loader.pkl')
    loader_train_dict = []
    loader_valid_dict = []
    total_train = 0
    total_valid = 0

    # Information needed for computing the normalization statistics.
    numbers_0 = []
    numbers_1 = []
    numbers_2 = []

    # This is particular to Ryan's ssldata. Unfortunately some other bad cases
    # (5, 30, 69) but hopefully not a big deal. Actions were mis-labeled.
    idx_to_skip = [0, 20, 40, 60]
    idx_to_skip.append(5)
    idx_to_skip.append(30)
    idx_to_skip.append(69)

    # For Ryan's data it's a simple pickle file.
    with open(raw_data, 'r') as fh:
        data = pickle.load(fh)
        N = len(data)
        print("Just loaded: {}  (len: {})".format(raw_data, N))

        # ----------------------------------------------------------------------
        # Each `item` has 'image' and 'action' keys.
        # Due to the (s_t, a_t, s_{t+1}) nature of data, we should think of
        # this as iterating through actions. The actions are dicts like this:
        # {'y': 302, 'x': 475, 'length': 20, 'angle': 0}, angles: 0,90,180,270.
        # The `t` here is synced with `c_img_t.png`, fyi. We skip 0.
        # ----------------------------------------------------------------------
        for t in range(N-1):
            if t in idx_to_skip:
                print("skipping {}".format(t))
                #assert data[t]['action'] is None # not for 4, 28, 68
                continue
            s_t   = data[t]['image']
            a_t   = data[t]['action']
            s_tp1 = data[t+1]['image']

            # Accumulate statistics for mean and std computation across our
            # lone channel. We made values same across all three channels.
            assert s_t.shape == s_tp1.shape == (480,640,3)
            numbers_0.extend( s_t[:,:,0].flatten() )
            numbers_1.extend( s_t[:,:,1].flatten() )
            numbers_2.extend( s_t[:,:,2].flatten() )

            # Don't forget! Add info to our data loaders!! We need enough info
            # to determine a full data point, which is a pair: `(input,target)`.
            png_t   = join(opt.RAW_DATA_SSL,
                           'd_img_proc_{}.png'.format(str(t).zfill(3)))
            png_tp1 = join(opt.RAW_DATA_SSL,
                           'd_img_proc_{}.png'.format(str(t+1).zfill(3)))

            # For actions just put `a_t` here and adjust in the data loader.
            if _is_validation(t):
                loader_valid_dict.append( (png_t, png_tp1, a_t) )
                total_valid += 1
            else:
                loader_train_dict.append( (png_t, png_tp1, a_t) )
                total_train += 1

    assert len(loader_train_dict) == total_train
    assert len(loader_valid_dict) == total_valid

    with open(loader_train_path, 'w') as fh:
        pickle.dump(loader_train_dict, fh)
    with open(loader_valid_path, 'w') as fh:
        pickle.dump(loader_valid_dict, fh)

    print("done loading data, train {} & valid {} (total {})".format(
            total_train, total_valid, total_train+total_valid))
    numbers = np.array([numbers_0,numbers_1,numbers_2]) # Will be shape (3,D)
    print("numbers.shape: {}  (for channel mean/std)".format(numbers.shape))
    print("mean(numbers): {}".format(np.mean(numbers, axis=1)))
    print("std(numbers):  {}".format(np.std(numbers, axis=1)))
    print("\nBut, use this for actual mean/std because we want them in [0,256) ...")
    print("mean(scaled): {}".format(np.mean(numbers/255.0, axis=1)))
    print("std(scaled):  {}".format(np.std(numbers/255.0, axis=1)))



def prepare_ssldata2():
    """Prepare Ryan's second version of the data, which is stored slightly differently.
    """
    def _is_validation(e):
        train_cutoff = 8 # this is now an episode number.
        return (e > train_cutoff)

    raw_data = join(opt.RAW_DATA_SSL,'rollout.pkl')
    assert not os.path.exists(opt.NEW_DATA_SSL), \
            "target exists, please remove it:\n\t{}".format(opt.NEW_DATA_SSL)
    os.makedirs(opt.NEW_DATA_SSL)
    path_train = join(opt.NEW_DATA_SSL,'train')
    path_valid = join(opt.NEW_DATA_SSL,'valid')
    os.makedirs(path_train)
    os.makedirs(path_valid)

    # For data loader, need to go from index to target, for BOTH train and valid.
    loader_train_path = join(opt.NEW_DATA_SSL,'train','data_train_loader.pkl')
    loader_valid_path = join(opt.NEW_DATA_SSL,'valid','data_valid_loader.pkl')
    loader_train_dict = []
    loader_valid_dict = []
    total_train = 0
    total_valid = 0

    # Information needed for computing the normalization statistics.
    numbers_0 = []
    numbers_1 = []
    numbers_2 = []

    # There was one bad case in the second data collection.
    idx_to_skip = [(8,0)]

    # For Ryan's data it's a simple pickle file.
    with open(raw_data, 'r') as fh:
        data = pickle.load(fh)
        N = len(data)
        print("Just loaded: {}  (len: {})".format(raw_data, N))

        # ----------------------------------------------------------------------
        # Each `item` has 'image' and 'action' keys.
        # Due to the (s_t, a_t, s_{t+1}) nature of data, we should think of
        # this as iterating through actions. The actions are dicts like this:
        # {'y': 302, 'x': 475, 'length': 20, 'angle': 0}, angles: 0,90,180,270.
        # The `t` here is synced with `c_img_t.png`, fyi. We skip 0.
        # ----------------------------------------------------------------------
        NUM_EPISODES = 10
        NUM_ACTIONS = 20

        for e in range(NUM_EPISODES):
            for a in range(NUM_ACTIONS):
                if (e + 1, a) in idx_to_skip:
                    print("skipping {}-{}".format(e + 1, a))
                    continue
                s_t   = data[(e + 1, a)]['image']
                a_t   = data[(e + 1, a)]['action']
                s_tp1 = data[(e + 1, a + 1)]['image']

                # Accumulate statistics for mean and std computation across our
                # lone channel. We made values same across all three channels.
                assert s_t.shape == s_tp1.shape == (480,640,3)
                numbers_0.extend( s_t[:,:,0].flatten() )
                numbers_1.extend( s_t[:,:,1].flatten() )
                numbers_2.extend( s_t[:,:,2].flatten() )

                # Don't forget! Add info to our data loaders!! We need enough info
                # to determine a full data point, which is a pair: `(input,target)`.
                png_t   = join(opt.RAW_DATA_SSL,
                               'd_img_proc_{}_{}.png'.format(str(e+1).zfill(2), str(a).zfill(3)))
                png_tp1 = join(opt.RAW_DATA_SSL,
                               'd_img_proc_{}_{}.png'.format(str(e+1).zfill(2), str(a + 1).zfill(3)))

                # For actions just put `a_t` here and adjust in the data loader.
                if _is_validation(e + 1):
                    loader_valid_dict.append( (png_t, png_tp1, a_t) )
                    total_valid += 1
                else:
                    loader_train_dict.append( (png_t, png_tp1, a_t) )
                    total_train += 1

    assert len(loader_train_dict) == total_train
    assert len(loader_valid_dict) == total_valid

    with open(loader_train_path, 'w') as fh:
        pickle.dump(loader_train_dict, fh)
    with open(loader_valid_path, 'w') as fh:
        pickle.dump(loader_valid_dict, fh)

    print("done loading data, train {} & valid {} (total {})".format(
            total_train, total_valid, total_train+total_valid))
    numbers = np.array([numbers_0,numbers_1,numbers_2]) # Will be shape (3,D)
    print("numbers.shape: {}  (for channel mean/std)".format(numbers.shape))
    print("mean(numbers): {}".format(np.mean(numbers, axis=1)))
    print("std(numbers):  {}".format(np.std(numbers, axis=1)))
    print("\nBut, use this for actual mean/std because we want them in [0,256) ...")
    print("mean(scaled): {}".format(np.mean(numbers/255.0, axis=1)))
    print("std(scaled):  {}".format(np.std(numbers/255.0, axis=1)))


def prepare_ssldata2_with_cv():
    """Prepare Ryan's second version of the data, which is stored slightly differently.
    """
    raw_data = join(opt.RAW_DATA_SSL,'rollout.pkl')
    assert not os.path.exists(opt.NEW_DATA_SSL), \
            "target exists, please remove it:\n\t{}".format(opt.NEW_DATA_SSL)
    os.makedirs(opt.NEW_DATA_SSL)
    path_train = join(opt.NEW_DATA_SSL,'train')
    path_valid = join(opt.NEW_DATA_SSL,'valid')
    os.makedirs(path_train)
    os.makedirs(path_valid)

    # For data loader, need to go from index to target, for BOTH train and valid.
    loader_train_path = join(opt.NEW_DATA_SSL,'train','data_train_loader')
    loader_valid_path = join(opt.NEW_DATA_SSL,'valid','data_valid_loader')
    loader_train_dict = []
    loader_valid_dict = []
    total_train = 0
    total_valid = 0

    # Information needed for computing the normalization statistics.
    numbers_0 = []
    numbers_1 = []
    numbers_2 = []

    # There was one bad case in the second data collection.
    idx_to_skip = [(8,0)]

    # For Ryan's data it's a simple pickle file.
    with open(raw_data, 'r') as fh:
        data = pickle.load(fh)
        N = len(data)
        print("Just loaded: {}  (len: {})".format(raw_data, N))

        # ----------------------------------------------------------------------
        # Each `item` has 'image' and 'action' keys.
        # Due to the (s_t, a_t, s_{t+1}) nature of data, we should think of
        # this as iterating through actions. The actions are dicts like this:
        # {'y': 302, 'x': 475, 'length': 20, 'angle': 0}, angles: 0,90,180,270.
        # The `t` here is synced with `c_img_t.png`, fyi. We skip 0.
        # ----------------------------------------------------------------------
        NUM_EPISODES = 10
        NUM_ACTIONS = 20

        for split in range(NUM_EPISODES):
            loader_train_dict.append([])
            loader_valid_dict.append([])
            for e in range(NUM_EPISODES):
                for a in range(NUM_ACTIONS):
                    if (e + 1, a) in idx_to_skip:
                        if split == 0: # only print skipped values once
                            print("skipping {}-{}".format(e + 1, a))
                        continue
                    s_t   = data[(e + 1, a)]['image']
                    a_t   = data[(e + 1, a)]['action']
                    s_tp1 = data[(e + 1, a + 1)]['image']

                    # Accumulate statistics for mean and std computation across our
                    # lone channel. We made values same across all three channels.
                    assert s_t.shape == s_tp1.shape == (480,640,3)
                    if split == 0: # only compute once
                        numbers_0.extend( s_t[:,:,0].flatten() )
                        numbers_1.extend( s_t[:,:,1].flatten() )
                        numbers_2.extend( s_t[:,:,2].flatten() )

                    # Don't forget! Add info to our data loaders!! We need enough info
                    # to determine a full data point, which is a pair: `(input,target)`.
                    png_t   = join(opt.RAW_DATA_SSL,
                               'd_img_proc_{}_{}.png'.format(str(e+1).zfill(2), str(a).zfill(3)))
                    png_tp1 = join(opt.RAW_DATA_SSL,
                               'd_img_proc_{}_{}.png'.format(str(e+1).zfill(2), str(a + 1).zfill(3)))

                    # For actions just put `a_t` here and adjust in the data loader.
                    if e == split:
                        loader_valid_dict[split].append( (png_t, png_tp1, a_t) )
                    else:
                        loader_train_dict[split].append( (png_t, png_tp1, a_t) )
            with open("{}-{}.pkl".format(loader_train_path, split), 'w') as fh:
                pickle.dump(loader_train_dict[split], fh)
            with open("{}-{}.pkl".format(loader_valid_path, split), 'w') as fh:
                pickle.dump(loader_valid_dict[split], fh)

    print("done loading data for {}-fold cross validation".format(NUM_EPISODES))
    numbers = np.array([numbers_0,numbers_1,numbers_2]) # Will be shape (3,D)
    print("numbers.shape: {}  (for channel mean/std)".format(numbers.shape))
    print("mean(numbers): {}".format(np.mean(numbers, axis=1)))
    print("std(numbers):  {}".format(np.std(numbers, axis=1)))
    print("\nBut, use this for actual mean/std because we want them in [0,256) ...")
    print("mean(scaled): {}".format(np.mean(numbers/255.0, axis=1)))
    print("std(scaled):  {}".format(np.std(numbers/255.0, axis=1)))

if __name__ == "__main__":
    prepare_ssldata2_with_cv()
