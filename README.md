# IL_ROS_HSR 

The goal of this package is to support various learning-based robotics tasks
involving the HSR and the Fetch robots.

Right now, it supports the HSR and bed-making (as suggested by the package
name), but we will eventually add more tasks and seamless support for the Fetch.


## Installation

Requirements: Ubuntu 16.04, ROS Kinetic, HSR package libraries.


- Make a Python 2.7 virtualenv. We use `--system-site-packages` because we have
  ROS installed system-wide.

  ```
  virtualenv --system-site-packages --python=python2  <path_to_env_name>
  ```

- Install [HSR_CORE][3].

- Install this package by running `python setup.py develop`, which ensures that
  your changes in this code are immediately reflected (i.e., no re-installation
  is required).


## Code Structure

Use `main/` for any scripts to run for your experiments.

Use `scripts/` for supporting scripts, such as for plotting results.

Within `src/il_ros_hsr`, there are three main sub-packages:

- `core`: Contains core utilities across multiple projects. **This will
  gradually be phased out in favor of `HSR_CORE`**; it is only left here for
  backwards compatibility.
- `p_pi`: Use for different application tasks, such as bed-making, each in their 
  own sub-directories.
- `nets`: For developing any Deep Learning code.


## TODO

- Get a `requirements.txt` file.
- Phase out `il_ros_hsr.core` in favor of `hsr_core`.
- Extend support for the Fetch robot and make package robot-agnostic.


## History

This code was used for, among other things, the [bed-making project][1], so some
of the scripts and READMEs reflect that code usage. To get the exact code
snapshot that was used for the paper, [clone this other GitHub repository
instead][2] and set it up in your own virtualenv. That repository will not be
updated further.


[1]:https://arxiv.org/abs/1809.09810
[2]:https://github.com/DanielTakeshi/IL_ROS_HSR
[3]:https://github.com/BerkeleyAutomation/HSR_CORE
