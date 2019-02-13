---
layout: post
title: "UnrealROX"
date: 2019-02-13 13:32:20 +0100
description: Tools for synthetic data generation # Add post description (optional)
img:  # Add image post (optional)
---

<!--<center><img src="/assets/img/2019-02-13/header.jpg" width="100%" style="margin-right:10px; margin-left:10px"></center>-->
<!--<center><img src="/assets/img/2019-02-13/header.jpg" width="100%"></center>-->

In this post, we will focus on a simulator named [UnrealROX](https://arxiv.org/abs/1810.06936). The content of this post is mainly sourced from the two publicly available works related to this tool. The whole UnrealROX system is described with all details in the corresponding arXiv paper. A proof of concept for such tool was published at IROS2018, where it was used to generate a large-scale photorealistic indoor dataset for robotic tasks named [The RobotriX](https://arxiv.org/abs/1901.06514).

UnrealROX is an environment built over Unreal Engine 4 which aims to reduce that reality gap by leveraging hyperrealistic indoor scenes that are explored by robot agents which also interact with objects in a visually realistic manner in that simulated world. Photorealistic scenes and robots are rendered by Unreal Engine into a virtual reality headset which captures gaze so that a human operator can move the robot and use controllers for the robotic hands; scene information is dumped on a per-frame basis so that it can be reproduced offline to generate raw data and ground truth annotations. This virtual reality environment enables robotic vision researchers to generate realistic and visually plausible data with full ground truth for a wide variety of problems such as class and instance semantic segmentation, object detection, depth estimation, visual grasping, and navigation to name a few.


# Architecture

While most tools for generating synthetic data opt for a client-server architecture so that different commands, e.g., to position objects, cameras, or to generate frames, are issued by a client API and captured by a server running in the simulation environment, UnrealROX somewhat differs in this aspect. UnrealROX architecture is a record and playback one where the whole sequence is recorded and its information is dumped on a per-frame basis so that it can be later reproduced to generate the required data anytime and in any conditions.

<center><img src="/assets/img/2019-02-13/diagram.jpg" width="80%"></center>

UnrealROX decouples the recording and data generation processes so that we can achieve high framerate when gathering data in virtual without decreasing performance due to extra processing tasks such as changing rendering modes, cameras, and writing images to disk. When in record mode, it gathers and dumps, on a per-frame basis, all the information that will be needed to replay and reconstruct the whole sequence, its data, and its ground truth. That information will be later used as input for the playback subsystem to reproduce the sequence and generate all the requested data.

The information is dumped in raw text format for efficiency. After the sequence is fully recorded, the raw text file is processed and converted into a more structured and readable JSON file so that it can be easily interpreted by the playback system. This also allows for easy modifications that can be introduced in the JSON file to produce different output sequences without recording them, for instance, by changing the initial position of static objects.

Once the scene has been recorded, the operator can take advantage of the user interface in UE4 to provide the needed data for the playback mode: the sequence description file in JSON format and an output directory as well as other secondary parameters (e.g., frame start, frame skipping for reducing the output frame rate, resolution, or raw data to generate to name a few options). This mode disables any physics simulation and interactions and then interprets the sequence file to generate all the raw data from it: RGB images, depth maps, instance segmentation masks, and normals. For each frame, the playback mode moves every object and every robot joint to the previously recorded position and sets their rotations accordingly. Once everything is positioned, it loops through each camera. For each one of them, the aforementioned rendering modes (RGB, depth, instance maps, and normals) are switched and the corresponding images are generated.

> This architecture decision is not perfect though and neither are the most common ones. Both of them excel at certain aspects while do not perform that well at others. For instance, client-server ones allow for a simplified API access through common scripting languages (such as Python) so that one can position objects and generate frames more dynamically. On the other hand, record-playback architectures require the user to generate sequences so that all the entities can be positioned and no API access is provided. However, record-playback architectures generate realistic trajectories that do not need to be synthetically generated and they are usually much more efficient when generating the data since they do not need to pay for the overhead that client-server communication requires.

# Engine

The rendering engine chosen to generate photorealistic RGB images and immerse the agent in VR was Unreal Engine 4 (UE4). The reasons for this choice were the following ones: 
- it is arguably one of the best game engines able to produce extremely realistic renderings, 
- beyond gaming, it has become widely adopted by Virtual Reality developers and indoor/architectural visualization experts so a whole lot of tools, examples, documentation, and assets are available; 
- due to its impact across various communities, many hardware solutions offer plugins for UE4 that make them work out-of-the-box; and 
- Epic Games provides the full C++ source code and updates to it so the full suite can be used and easily modified for free.

Arguably, the most attractive feature of UE4 is its capability to render photorealistic scenes. Some UE4 features that enable this realism are: physically-based materials, pre-calculated bounce light via Lightmass, stationary lights, post-processing, and reflections. It is also important to remark that UnrealROX has strict real-time constraints for rendering since the operator must be immersed in virtual reality, i.e., it requires extremely realistic and complex scenes rendered at very high framerates (usually more than 80 FPS). By design, UE4 is engineered for virtual reality so it provides a specific rendering solution for it named Forward Renderer. That renderer is able to generate images that meet UnrealROX’s quality standard at 90 FPS thanks to high-quality lighting features, Multi-Sample Anti-Aliasing (MSAA), and instanced stereo rendering.

<center><img src="/assets/img/2019-02-13/wooden.gif" width="49%">
<img src="/assets/img/2019-02-13/modern.gif" width="49%"></center>

The whole system was built over UE4 taking advantage of various existing features, extending certain ones with to suit their specific needs, and implementing others from scratch to devise a more efficient and cleaner project that abides to software design principles.

# Features

UnrealROX features various characteristics that make it appealing for generating synthetic data for robotic problems. In the following lines, we will review the most significant ones.

## Robot Models

One of the most important parts of the system is the representation of the robots in the virtual environment. Robots are represented by the mesh that models them, the control and movement logic, the animations that it triggers, and the grasping system. Those robotic entities are encapsulated in a class that contains all the common behavior that any robot would have within UnrealROX, which can then be extended by child classes that implement specific differences such as the mesh behavior or the configuration of the fingers for the grasping system.  The user itself must create a pawn for each robot that model that has to be imported into the tool. In such class, a 3D mesh and textures must be provided to represent the robot. Furthermore, cinematic constraints must be manually specified for the robot.

## Control in Virtual Reality

Seamlessly integrating robots in a scene and making them controllable in VR by a human agent to record sequences requires three issues to be solved: (1) gaze and head movement with first person Point of View (PoV), (2) inverse kinematics to be able to move them with motion controllers and reach for objects, and (3) locomotion to move the robot in the scene

The first issue is solved by using the VR headset to control the robot’s head movement and render its first person PoV to the user. Inverse kinematics for the virtual robot are manually implemented with Forward And Backward Reaching Inverse Kinematics (FABRIK), a built-in inverse kinematics solver in UE4 that works on a chain of bones of arbitrary length. Locomotion is handled by thumbsticks on the VR controllers.

UnrealROX decouples the movement logic (in the robot pawn) and the control one (in its own controller class). The controller class handles all the control-related events, and those events can be generated by keyboard, gamepads or virtual reality controllers. This means that the robot can be transparently controlled by several input devices, including Oculus Rift and HTC Vive headsets.

<center><img src="/assets/img/2019-02-13/embodiment.jpg" width="80%"></center>

## Visually Realistic Grasping

The grasping subsystem is one of the core features of UnrealROX to produce visually realistic results. UnrealROX focuses on providing realistic object interaction from two perspectives:  (1) the way the robot grasp an object and (2) the movements it makes. To simulate a real robot behaviour when grasping an object, smooth and plausible movements are needed. The grasping action is fully controlled by the user through the VR controllers, whose movements are limited to those of the human hands. In this way, we achieve a good representation of a humanoid robot interacting in a realistic home environment. In contrast with common VR approaches which are animation-driven or based on predefined movements (thus limiting the interaction to a reduced set of objects), UnrealROX makes robot agents able to manipulate and interact with any object whose physics are being simulated by Unreal Engine, regardless of its geometry and pose. In this way, the user can freely decide which object to interact with without any restrictions. The robot can manipulate an object with each hand, and change an object from one hand to the other. It can also manipulate two different objects at the same time.

<!--<center><img src="/assets/img/2019-02-13/interact1.gif" width="49%">
<img src="/assets/img/2019-02-13/interact2.gif" width="49%"></center>-->

<center><img src="/assets/img/2019-02-13/interact3.gif" width="49%">
<img src="/assets/img/2019-02-13/interact4.gif" width="49%"></center>

<center><img src="/assets/img/2019-02-13/interact5.gif" width="49%">
<img src="/assets/img/2019-02-13/interact6.gif" width="49%"></center>

At the implementation level, this system makes of UE4’s trigger volumes placed on each one of the finger phalanges. These triggers act as sensors that will determine collisions with the object. Using the VR controllers, the user is able to close robot’s hands around the object and the animation of each finger is driven by the collisions of such triggers to wrap around the object. This way, finger positions change smoothly in order to replicate a real robot hand behaviour and to avoid exaggerated object clipping.

## Multi-camera Recording

Most robots in the public market integrate multiple cameras in different parts of their bodies. In addition, external cameras are usually added to the system to provide data from different points of view, e.g., ambient assisted living environments tend to feature various camera feeds for different rooms to provide the robot with information that it is not able to perceive directly. UnrealROX allows the addition of multiple cameras in a synthetic environment with the goal in mind of having the same or more amount of data that we would have in a real environment.

To simulate those situations in a synthetic scenario, UnrealROX gives the user the ability to place cameras attached to sockets in the robot’s body, e.g., the wrist itself or the end-effector (eye-in-hand). Furthermore, it also provides the functionality to add static cameras in the scene.

<center><img src="/assets/img/2019-02-13/rgb_fp.jpg" width="33%">
<img src="/assets/img/2019-02-13/rgb_lh.jpg" width="33%">
<img src="/assets/img/2019-02-13/rgb_mr.jpg" width="33%"></center>

## Camera Parameters and Stereo Cameras

Apart from handling attached and static cameras, UnrealROX exposes the most demanded camera settings through its interface (projection mode, Field of View (FoV), color grading, tone mapping, lens, and various rendering effects), as well as providing additional features such as creating stereo-vision setups.

Creating a stereo setup is as simple as marking it in the user interface and specifying the baseline for the cameras. This can be done either in the recording phase or even during the playback one. A sequence that was not recorded with stereo cameras can easily be adapted to feature such cameras by indicating their parameters and the system will transparently handle it.

## Ground Truth

UnrealROX records for each sequence all the 6D poses for cameras, objects and robot joints so that the sequence can be reproduced to generate a set of raw data consisting of (by default):

- RGB images at 1920x1080 resolution in 24-bit JPG(95%) format.
- Depth maps at 1920x1080 resolution in 16-bit grayscale PNG format.
- 2D instance masks at 1920x1080 resolution in RGB 24-bit PNG format.
- Normal maps at 1920x1080 resolution in RGB PNG format.

That raw data, together with the information in the sequence file, can be processed with generator scripts to produce all other derived ground truth data:

- 2D class masks at 1920x1080 resolution in RGB 24-bit PNG format.
- 2D/3D object instance bounding boxes in XML format.
- 3D point clouds in PLY format with RGB color.
- 3D instance/class masks in PLY format with RGB color.

<center><img src="/assets/img/2019-02-13/data.gif" width="49%">
<img src="/assets/img/2019-02-13/bboxes.jpg" width="49%"></center>

# Applications

The UnrealROX environment has multiple potential application scenarios to generate data for various robotic vision tasks. Traditional algorithms for solving such tasks can take advantage of the data but the main purpose of this environment is providing the ability to generate large-scale datasets. Having the possibility of generating vast amounts of high-quality annotated data, data-driven algorithms such as deep learning models can especially benefit from it to increase their performance, in terms of accuracy, and improve their generalization capabilities in unseen situations during training. The set of tasks and problems that can be addressed using such data ranges from low to high-level ones, covering the whole spectrum of indoor robotics.

By using UnrealROX, authors were able to generate **The RobotriX** a dataset of 38 semantic classes totaling 8M stills recorded at +60 frames per second with full HD resolution. Thanks to the high quality and quantity of both raw information and annotations, The RobotriX might serve as a new milestone for investigating 2D and 3D robotic vision tasks with large-scale data-driven techniques.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/CiRc5tCtCak" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>

> More details about the project can be consulted at the original paper or the GitHub repository [3dperceptionlab/therobotrix](https://github.com/3dperceptionlab/therobotrix).


# Limitations

UnrealROX is a useful tool which great potential as an offline large-scale synthetic data generator. However, it is still limited by various factors that restrict its application to certain domains:

- The lack of a client-server API limits the usefulness of the system being at the same time its strength and its weakness. The chosen architecture is more efficient and can be encapsulated inside Unreal Engine’s interface itself but then it cannot be used dynamically for instance to train reinforcement learning agents. UnrealROX is better suited for offline learning.
- Another important short-coming is the absence of tactile information when grasping objects. Although the system is able to indicate whether the hand is colliding with the object or not, there is no force or pressure simulation at all.
- Robot models have to be imported manually. This means that all their constraints and inverse kinematics must be defined within Unreal Engine’s editor by hand. This fact makes it harder to import and get any robot to work properly in a reasonable time frame.
- The system does not support the simulation of fluids or non-rigid objects and their deformations when grasping such kind of objects.

All of these limitations are currently being addressed by the creators with priority on the reinforcement learning API and the simulation of tactile sensors.

# Code and Documentation

The whole UnrealROX project is available for download as open-source code in GitHub [3dperceptionlab/unrealrox](https://github.com/3dperceptionlab/unrealrox). Furthermore, extensive documentation describing the configuration and usage processes is also provided in [ReadTheDocs](https://unrealrox.readthedocs.io/en/latest/).

# Contact

UnrealROX was developed by the 3D Perception Lab at the University of Alicante, Spain. The current maintainers of the tool are:

- Pablo Martinez-Gonzalez [Design, UE4 Backend, Lead Programmer] (pmartinez@dtic.ua.es)
- Sergiu Oprea [Grasping, Data Generation] (soprea@dtic.ua.es)
- Alberto Garcia-Garcia [Design, Prototyping, Data Generation, Project Lead] (agarcia@dtic.ua.es)
- Alvaro Jover-Alvarez [UE4 Expert, Support Programmer] (ajover@dtic.ua.es)
- Sergio Orts-Escolano [Design, Technical Advice] (sorts@ua.es)
- Jose Garcia-Rodriguez [Technical Advice] (jgarcia@dtic.ua.es)

# Authors

Alberto Garcia-Garcia (agarcia@dtic.ua.es) 

# Acknowledgements 

We would like to thank Ankur Handa for proofreading and editing this post. 

# Credits

- Assets (scenes and objects) for The RobotriX were originated from two sources: [UE4Arch](https://ue4arch.com/) and [Unreal Engine Marketplace](https://www.unrealengine.com/marketplace/store). They can be acquired from there to fully reproduce the dataset.
- This work was inspired by [UnrealCV](https://github.com/unrealcv/unrealcv) by Weichao Qiu et al. Weichao was specially kind when answering questions for the first prototypes.
- This project was possible thanks to a generous hardware donation by NVIDIA Corporation (Titan X, Titan Xp, and Titan V).
- Epic Games and in particular the Unreal Community support was invaluable through the development of this project.

<!--<center><img src="/assets/img/2019-02-13/dab.gif" width="50%"></center>-->
