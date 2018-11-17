# Training Networks

Use this for generic training of anything relevant to this project. See
`SAMPLE_RESULTS.md` for example results. It requires Python 2.7 and PyTorch
0.4.1.

Also: it is simplest for now if you run all python scripts within this
directory, so `python [script_name.py]`, not `python
il_ros_hsr/nets/[script_name].py`, etc. The script will sometimes make temporary
directories, prefixed with `tmp`, for visualization purposes. These can be
removed.


## Step 1: Data Generation

[See this directory][1].


## Step 2: Data Preparation

- There is data on our shared data storage, but it is best for speed purposes
  that the data be copied into a local directory on the computer one is using,
  for faster loading.

- Depending on the dataset type, choose the method in `prepare_data.py` and then
  run `python prepare_data.py`. This should generate a pickle file for the
  validation and testing set, with references to the full image paths (which,
  again, should be stored in a local directory for speed). Look at the [PyTorch
  data loading and processing tutorial][2].

- To *inspect* the data, run `python custom_transforms.py`. This will run a set
  of transformations that we use for data augmentation. It will save as `.png`
  files, as long as the transforms involving normalization and converting to
  tensors are not used. 

Notes:

- `ryanhoque/ssldata` has only RGB images.

- `ryanhoque/ssldata2` has RGB and depth images.

The above names should be synced with the method names in `prepare_data.py`.

**BEFORE PROCEEDING TO TRAINING**: make sure that the `MEAN` and `STD` values
from `prepare_data.py` are used and copied into the neural net options,
`options.py`. This is necessary in order to have correct data normalization (and
then un-normalization for visualizations later). Also, did you inspect via
`python custom_transforms.py`?


## Step 3: Training

Run `python train_action_predictor.py`. But before doing so:

- Check the output directory for where the predictions are saved, so you can
  plot the *quantitative* results and visualize the *qualitative* results.
  
- There are command line arguments. Test and see which ones work.

- The actual Deep Convolutional Neural Network that we use is defined in
  `net.py`.  It follows a Siamese design and uses pre-trained ResNet backbones.

- The models and statistics are saved in a particular directory. To make it easy
  to remember what we ran, the args are stored there. Additionally, the date is
  included in the name, e.g.,: `resnet18_2018-11-16-14-20_000` means we started
  running the script on Nov (i.e., represented by the number 11) 16 at 14:20
  (2:20pm).


Additionally, inside the model directory, we save the args, PyTorch model (with
the usual `.pt` extension), and the statistics encountered during training.
Here is a possible output:

```
$ ls -lh resnet18_2018-11-16-16-53_000
total 44M
-rw-rw-r-- 1 nobody nogroup  44M Nov 16 16:54 act_predictor.pt
-rw-rw-r-- 1 nobody nogroup  112 Nov 16 16:53 args.json
-rw-rw-r-- 1 nobody nogroup 1007 Nov 16 16:54 stats_train.pkl
-rw-rw-r-- 1 nobody nogroup 1007 Nov 16 16:54 stats_valid.pkl
```


## Step 4: Validation and Data Inspection

By default, the training script will save validation set information in
`stats_valid.pkl` as you can see above. In addition, it will save images in a
temporary validation set directory for qualitative inspections.

Use `stats_train.pkl` and `stats_valid.pkl` for plotting. For an example, see
`plot_example.py`.


## Step 5: Deployment on Physical Robot

Before testing on the physical robot, please test in `deploy_test.py` on sample
images.

Pick the path to the model that you want to use. Then, write a script
elsewhere that loads the model in a similar manner as `deploy_test.py` here. In
order to use it in the real robot, the images should be roughly seen from
similar angles, and the data must be processed similarly. Then, call the
network, get the action, and "de-process" the action towards normal image-space.
Then we convert that to robot space.

TODO


[1]:https://github.com/BerkeleyAutomation/IL_ROS_HSR/tree/master/scripts/ryan_data_collection
[2]:https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
