---
layout: post
title: "DREAM: Camera Calibration through Sim2Real Keypoint Detection"
date: 2020-06-07 00:00:00 +0000 #13:32:20 +0100  -- date TBD
description: description TBD # Add post description (optional)
img:  # Add image post (optional)
---

*Preamble TBD*. This post describes an approach to camera calibration without fiducial markers that combines deep-learning-based keypoint detection with a principled, geometric algorithm to provide a camera-to-robot pose estimate from a single RGB image. Our approach is facilitated by sim2real transfer: we train the keypoint detector using only synthetic images. Our approach, which is detailed further in our [paper](https://arxiv.org/abs/1911.09231) published at ICRA 2020, is called **DREAM:** **D**eep **R**obot-to-camera **E**xtrinsics for **A**rticulated **M**anipulators.

# DREAM: Camera Calibration without Fiducial Markers

DREAM is a two-stage pipeline. The first stage detects keypoints of a manipulator in an input RGB image. The second stages uses the detected keypoints along with the camera intrinsics and robot proprioception to estimate the camera's pose with respect to the manipulator. Interestingly, the first stage involes two-dimensional inference, whereas the second involves three-dimensional inference. 

<!-- <img align="right" src="/assets/img/2019-02-28/Tobin_etal_2018--sim2real.jpg" width="42%" hspace="20px"> -->

### Stage 1: Keypoint Detection (TBD name, diff from below)

The output is the $$k$$ keypoints, where $$N_k$$ is the number of keypoints used.

### Stage 2: Pose Estimation from PnP

The output is $$T$$. This output is suitable for camera calibration, or other uses (?).



# Keypoint Detection

This post will focus on the first stage, and how we transfer keypoint detection from sim2real with only synthetic data.

TBD

## Synthetic Data Generation

Mention 

### Training Image Examples

Labels - mention training directly

## Domain Randomization

-> what types of domain randomization we used

## Image Augmentation

Adding domain randomization to the scene...

## Images

TBD

## Limitations and Future Work

- Only designed for one manipulator, but multiple-manipulators can be deconflicted a la DOPE (cite)
- Keypoint jitter
- Not all keypoints are equally useful for PNP

# Lessons Learned

Transferring robot perception to reality from only synthetic images is not trivial. Through this work, we provide the following lessons learned for other researchers seeking to transfer robot perception algorithms to reality from only synthetic images.

1. **Photorealistic textures help.** *TBD*

2. **Judicious restriction of data will help.** *Mention Baxter camera angles, etc*

3. **Interpretability of belief maps.** Originally, we explored the idea of not training belief maps directly, and instead, let the network learn what representation would be best. For this, we added a softmax layer at the end of the network, and used the keypoint position itself as the training label (instead of the belief map). 

<!-- # Open Questions

How many images are enough? -->

# Code and Documentation

The DREAM code is available here: [TBD](TBD). We have also released pre-trained models for the Franka Emika Panda, KUKA iiwa7, and Rethink Robotics Baxter. These models and the datasets we used to quantify our results are available at the [NVIDIA project site](TBD).

We encourage roboticists to lose the fiducial marker and try our approach the next time you need to calibrate your camera for your manipulation tasks.

# Authors

[Tim Lee](http://timlee.ai), Ph.D. in Robotics researcher with the [Intelligent Autonomous Manipulation Lab](https://labs.ri.cmu.edu/iam/) at Carnegie Mellon University. Tim completed this research as an intern with NVIDIA's Seattle Robotics Lab in 2019.

# Acknowledgements

We'd like to thanks Ankur Handa, *TBD*, and *TBD* for their help with editing and proofreading this post.

# Credits / Bibliography

TBD
