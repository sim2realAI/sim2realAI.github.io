---
layout: post
title: "DREAM: Camera Calibration through Sim2Real Keypoint Detection"
date: 2020-06-07 00:00:00 +0000 #13:32:20 +0100  -- date TBD
description: description TBD # Add post description (optional)
img:  # Add image post (optional)
---

*Preamble TBD*. This post describes an approach to camera calibration without fiducial markers that combines deep-learning-based keypoint detection with a principled, geometric algorithm to provide a camera-to-robot pose estimate from a single RGB image. Our approach is facilitated by sim2real transfer: we train the keypoint detector using only synthetic images. Our approach, which is detailed further in our [paper](https://arxiv.org/abs/1911.09231) published at ICRA 2020, is called **DREAM:** **D**eep **R**obot-to-camera **E**xtrinsics for **A**rticulated **M**anipulators.

# DREAM: Camera Calibration without Fiducial Markers



<!-- <img align="right" src="/assets/img/2019-02-28/Tobin_etal_2018--sim2real.jpg" width="42%" hspace="20px"> -->

# Keypoint Detection

TBD

## Training Images

TBD

## Images

TBD

# Lessons Learned

TBD

# Open Questions

How many images are enough?

# Code and Documentation

Our code is available here: [TBD](TBD). We have released pre-trained models for the Franka Emika Panda, KUKA iiwa7, and Rethink Robotics Baxter. These models and the datasets we used to quantify our results are available at the [NVIDIA project site](TBD).

We encourage you to try our approach the next time you need to calibrate your RGB camera for your manipulation experiments.

# Authors

[Tim Lee](http://timlee.ai), Ph.D. in Robotics researcher with the [Intelligent Autonomous Manipulation Lab](https://labs.ri.cmu.edu/iam/) at Carnegie Mellon University. Tim completed this research as an intern with NVIDIA's Seattle Robotics Lab in 2019.

# Acknowledgements

We'd like to thanks Ankur Handa, *TBD*, and *TBD* for their help with editing and proofreading this post.

# Credits / Bibliography

TBD
