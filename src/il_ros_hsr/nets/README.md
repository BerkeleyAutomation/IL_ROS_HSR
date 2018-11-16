# Training Networks

Use this for generic training of anything relevant to this project. See
`SAMPLE_RESULTS.md` for example results. It requires Python 2.7 and PyTorch
0.4.1.

Also: it is simplest for now if you run all python scripts within this
directory, so `python [script_name.py]`, not `python
il_ros_hsr/nets/[script_name].py`, etc.


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

The actual Deep Convolutional Neural Network that we use is defined in `net.py`.
It follows a Siamese design and uses pre-trained ResNet backbones.  It may also
help to run tests on the custom transformations we have, by running `python
custom_transforms.py`. This shows how we do data augmentation for training. The
validation data augmentation, of course, must be deterministic.


## Step 4: Validation

TODO

## Step 5: Deployment on Physical Robot


TODO


[1]:https://github.com/BerkeleyAutomation/IL_ROS_HSR/tree/master/scripts/ryan_data_collection
[2]:https://pytorch.org/tutorials/beginner/data_loading_tutorial.html
