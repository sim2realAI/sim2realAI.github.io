---
layout: post
title: "DREAM: Camera Calibration without Fiducial Markers through Sim2Real Keypoint Detection"
date: 2020-06-07 00:00:00 +0000 #13:32:20 +0100  -- date TBD
description: description TBD # Add post description (optional)
img:  # Add image post (optional)
---

*Preamble TBD*. This post describes an approach to camera calibration without fiducial markers that combines deep-learning-based keypoint detection with a principled, geometric algorithm to provide a camera-to-robot pose estimate from a single RGB image. Our approach is facilitated by sim2real transfer: we train the keypoint detector using only synthetic images. Our approach, which is detailed further in our [paper](https://arxiv.org/abs/1911.09231) published at ICRA 2020, is called **DREAM:** **D**eep **R**obot-to-camera **E**xtrinsics for **A**rticulated **M**anipulators. Code, datasets, and pre-trained models for DREAM are [publically released](https://github.com/NVlabs/DREAM).

<!-- # DREAM: Camera Calibration without Fiducial Markers -->

### A DREAM of Better Camera Calibration

DREAM is a two-stage pipeline. The first stage detects keypoints of a manipulator in an input RGB image. The second stages uses the detected keypoints along with the camera intrinsics and robot proprioception to estimate the camera's pose with respect to the manipulator. It can be seen that the first stage involes two-dimensional inference, whereas the second involves three-dimensional inference. 

<img align="center" src="/assets/img/2020-06-10/Lee_etal_2020_DREAM_pipeline.png" width="100%" hspace="20px">

DREAM is a great example of an approach that is enabled by deep learning, while still leveraging classical algorithms. Although one could regress directly to pose, geometric algorithms, such as PnP, provide a principled method for obtaining pose once keypoints are detected. Therefore, we need not apply deep learning to the entire pipeline and regress directly to pose, which ``bakes in'' the camera intrinsics. As our approach is intended to be used on a variety of cameras, we utilize deep learning for what it's very good at --- image detection --- and the rest of the problem is thereafter solved with perspective-n-point.

This post will focus on the first stage, and how we transfer keypoint detection from sim2real with only synthetic data.

### Stage 1: Keypoint Detection (TBD name, diff from below)

The output is the $$k$$ keypoints, where $$N_k$$ is the number of keypoints used.

### Stage 2: Pose Estimation from PnP

The output is $$T$$. This output is suitable for camera calibration, or other uses (?). We utilize the TBD implementation of PnP available in OpenCV (cite).

# Fantastic Keypoints and Where To Find Them

DREAM requires specification of keypoints to detect based on the canonical frame of the robot. In our work, we chose the keypoints at the positions of the joints based on the robot URDF (Unified Robot Description Format) model. In principle, these keypoints can exist anywhere on the robot --- including ``inside'' the robot, as was the case for the DREAM models trained for ICRA. More keypoints will probably provide better results in terms of both accuracy (with diminishing returns) and robustness. Particularly in this case, more keypoints would help provide a more stable solution when keypoints are occluded or otherwise not all detected.

Other approaches include defining the keypoints at the bounding box vertices (as in DOPE). However, from robot proprioception, we know where the keypoints are, so defining them on the robot is probably best so the network can use RGB cues to learn where they are.

# Synthetic Data Generation

Deep learning requires data --- _lots_ of data. Fortunately, synthetic data samples are cheap, relatively speaking. To transfer our keypoint detector to reality, we needed to provide sufficient training data with enough variation so that the network learns the salient signal within the input images to detect keypoints. We employ two common approaches (cite?) for facilitating learning are two techniques: domain randomization and image augmentation.

We utilize Unreal Engine 4 as our renderer along with a developmental version of [NDDS](https://github.com/NVIDIA/Dataset_Synthesizer), the NVIDIA Deep learning Dataset Synthesizer, that provides the above randomizations. In particular, this version of NDDS provides the capability for robot control during data capture. We captured images at 640x480 resolution. Our data generation pipline also captured depth images and object segmentation masks; however, we only train our network using the RGB images.

## Domain Randomization

Broadly speaking, domain randomization refers to changing the _content_ of an image (Image-level changes are covered through image augmentation) to provide a diversity of examples to facilitate generalization (cite?). For example, if the network were to only see examples of the keypoints at the same robot joint configuration, we wouldn't be certain whether it could extrapolate to other joint configurations. To that end, we aimed to provide domain randomizations in factors that could reasonably change in real settings:
- Camera pose is randomly chosen within a hemispherical shell with the robot at the center. The camera view is slightly perturbed so that the robot is not always at the center of the image.
- Robot joint configuration is randomly chosen. Specifically, each joint angle is chosen from a uniform angle distribution that is chosen independently for each joint. This, along with perturbing the camera view, means that some images will not have every keypoint in the field of view.
- The lighting of the scene is varied in their position, intensity, and color. (Note that we do not use ray tracing for rendering these images.)
- Variation in scene background. We randomly choose a pattern or an image from the COCO dataset (cite).
- Addition of distractor objects from the YCB dataset (cite).
- The color of the robot mesh was randomly chosen.

## Image Augmentation

Image augmentation provides image-level noise to provide richer examples and increases network robustness (cite?). We use [albumentations](https://github.com/albumentations-team/albumentations) for our image augmentation. Specifically, the following augmentations are applied to the training images:
- Gaussian white (zero-mean) noise for each pixel.
- Random adjustment to image brightness and contrast.
- Random translation, rotation and scaling.

## Example Training Images

Below are some training image examples.

...

# Training the Network

## Network details

## Example Keypoint Detection



# Conclusions

## Limitations and Future Work

- Only designed for one manipulator, but multiple manipulators can be deconflicted a la DOPE (cite)
- Keypoint jitter - heuristic for peak finding. Might be improved by end-to-end learning something for part.
- Not all keypoints are equally useful for PNP. Therefore, some robot joint configurations may be more ``informative'' than others. Degenerate cases can occur, such as all keypoints along a line.

## Lessons Learned

Transferring robot perception to reality from only synthetic images is not trivial. Through this work, we provide the following lessons learned for other researchers seeking to transfer robot perception algorithms to reality from only synthetic images.

1. **Photorealistic textures help.** *TBD*

2. **Judicious restriction of domain randomization will help.** *Mention Baxter camera angles, etc*

3. **Interpretability of belief maps.** Originally, we explored the idea of not training belief maps directly, and instead, let the network learn what representation would be best. For this, we added a softmax layer at the end of the network, and used the keypoint position itself as the training label (instead of the belief map). 

## Open Questions

- How many images are enough? In the work of Deep Object Pose Estimation (DOPE), work that DREAM was strongly influenced by, Tremblay et al. study variation in the size of the dataset. Empirically we found that about 20,000 images worked for a robot at a fixed joint configuration, so more was needed when we needed to vary the joint configuration. It is possible that similar gains could be achieved with less data, although perhaps there is some correlation with the expressivity of the network being used.

- How do you know when the network is ``good enough''? Train vs validation


<!-- # Open Questions

How many images are enough? -->

# Code and Documentation

The DREAM code is available on [GitHub](https://github.com/NVlabs/DREAM). We have also released pre-trained models for the Franka Emika Panda, KUKA iiwa7, and Rethink Robotics Baxter. These models and the datasets we used to quantify our results are available through the [NVIDIA project site](https://research.nvidia.com/publication/2020-03_DREAM).

We encourage roboticists to lose the fiducial marker and try our approach the next time you need to calibrate your camera for your manipulation tasks.

# Authors

[Tim Lee](http://timlee.ai), Ph.D. in Robotics researcher with the [Intelligent Autonomous Manipulation Lab](https://labs.ri.cmu.edu/iam/) at Carnegie Mellon University. Tim completed this research as an intern with NVIDIA's Seattle Robotics Lab in 2019.

# Acknowledgements

We'd like to thanks Ankur Handa, *TBD*, and *TBD* for their help with editing and proofreading this post.

# Credits / Bibliography

TBD
