---
layout: post
title: "Inaugural blog!"
date: 2018-09-24 13:32:20 +0300
description: Welcome blog # Add post description (optional)
img:  # Add image post (optional)
---

Welcome to our website. We are indexing the progress on simulations to real world transfer in robot perception and control. Motivated by the recent interest in learning via simulations and transferring the results to real world, we believe it is important to consolidate and characterise the progress now in this direction. Physics simulators like MuJoCo, Bullet, and DART, and 3D rendering engines in Unity, UnrealEngine, and Physically Based Rendering engines have played a substantial role in this progress and we believe simulators will continue to be important in helping us understand what is needed to transfer results to real world

The real world is often complex and there is a huge cost involved in running experiments. Robots are expensive and break often which can slow down the iteration cycle of research. Furthermore, collecting large scale real world data can be quite labourious. While this is not to say that real world experiments are close to impossible but simulators are appealing due to the following advantages\: 

* Repeatability - being able to replay the recorded trajectory with no changes/stochasticity --- resetting the states to exactly the same initial conditions. This is also very helpful in diagnostics and debugging.
* Controllability - being able to control various simulation parameters systematically and understand how they affect the simulation. 
* Scalability - it is a lot easier to scale a simulation experiment via distributed computing or high performance engineering infrastructure.
* Efficiency - simulators can often run much faster than real time. This is an extremely important characteristic and allows for fast iteration cycles in training / learning.
* Variability - simulators can allow for collecting large diversity of scenarios.
* Evaluation - providing a test bed to benchmark various algorithms.


While there is huge excitement about transferrability, it is important to understand various important aspects of simulations *e.g.* how good are the contact models in a physics engines and what approximations are they making, how good is the rendering quality for visual perception and how can we be sure that it will transfer, what are the strengths and limitations of simulations and which simulator might be more fitting to the task and which is the fastest, to name a few.

Keeping this in mind, we thought it might be worth putting this all together on a website that can catalogue various things related to simulations and offer suggestions on different simulators, synthetic datasets and the state of the art in simulations to real world transfer. There will be occasional tutorials on rendering, physics, robotics, hardware, and SLAM.



<!--{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

-->
