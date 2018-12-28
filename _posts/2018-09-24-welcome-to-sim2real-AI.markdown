---
layout: post
title: "Inaugural blog!"
date: 2018-09-24 13:32:20 +0300
description: Welcome blog # Add post description (optional)
img:  # Add image post (optional)
---

Welcome to our website. We are indexing the progress on simulations to real world transfer in robot perception and control. Motivated by the recent interest in learning in simulated environments and transferring the results to real world, we believe it is important to consolidate and characterise the progress now in this direction. Physics simulators like MuJoCo, Bullet, FleX, PhysX and DART, and 3D rendering engines in Unity, UnrealEngine, and Physically Based Rendering [(PBR)](https://www.pbrt.org/) engines have played a substantial role in this progress in recent times. In fact, various robotics companies like [Boston Dybamics](https://en.wikipedia.org/wiki/Boston_Dynamics), [Agility robotics](https://www.therobotreport.com/agility-cassie-bipedal-robot-simulators/), [Kuka robotics](https://www.kuka.com/en-us/products/robotics-systems/software/simulation-planning-optimization/kuka_sim), [Universal robotics](https://www.universal-robots.com/plus/software/robodk-simulation-and-offline-programming/) and [SpaceX](https://motherboard.vice.com/en_us/article/ezv79w/spacex-is-using-these-simulations-to-design-the-rocket-thatll-take-us-to-mars) rely heavily on simulations and we believe simulators will continue to be important in helping us understand the complexities of the real world and what is really needed to transfer results.

The real world is often complex and there is a huge cost involved in running experiments. Robots tend to be expensive and break often which can slow down the iteration cycle of research. Furthermore, collecting large scale real world data can be quite labourious as tasks become more complex. Simulators, on the other hand, offer appealing advantages\: 

* **Repeatability** - being able to replay the recorded trajectory with no changes/stochasticity --- resetting the states to exactly the same initial values. This is also very helpful in diagnostics and debugging.
* **Controllability** - being able to control various simulation parameters systematically and understand how they affect the simulation. 
* **Scalability** - it is a lot easier to scale a simulation experiment via distributed computing or high performance engineering infrastructure.
* **Efficiency** - simulators can often run much faster than real time. This is an extremely important characteristic and allows for fast iteration cycles in training / learning.
* **Variability** - simulators can allow for collecting large diversity of scenarios.
* **Evaluation** - providing a test bed to benchmark various algorithms.


However, simulators have their limitations too --- simulating complicated real world phenomenon still remain open research problems. Therefore, it is important to understand various critical aspects of simulations in the context of real world transfer *e.g.* 

* How good are the contact models in a physics engine and what approximations are they making?
* What level of rendering quality do we need to able to transfer results to real world? 
* What are the strengths and limitations of simulations in general? What can they faithfully simulate? 
* Which simulator might be more fitting to the user defined task and which is the fastest?
* How do the simulators implement things behind the scenes? What is the generative model they use? How can that be integrated with model-based methods?   

Keeping this in mind, we thought it might be worth consolidating, characterising, and cataloguing various things related to simulations and offer suggestions and constructive feedback on different simulators, synthetic datasets and the state of the art in simulations to real world transfer. There will be occasional tutorials on rendering, physics, robot kinematics and optimisation, and hardware.


## Acknowledgements
