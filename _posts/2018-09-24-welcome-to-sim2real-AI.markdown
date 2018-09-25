---
layout: post
title: "Inaugural blog!"
date: 2018-09-24 13:32:20 +0300
description: Welcome blog # Add post description (optional)
img:  # Add image post (optional)
---

Welcome to our website. We are indexing the progress on simulations to real world transfer in robot perception and control. Past few years have seen a huge interest in learning via simulations and transferring the results to real world. This is largely due to the availability of popular simulators *e.g.* physics simulators like MuJoCo, Bullet, and DART, and 3D rendering engines in Unity, UnrealEngine, and Physically Based Rendering engines.

Real world is often complex and there is a huge cost involved in running experiments. Moreover, collecting large scale real world data can be quite labourious. On the other hand, simulations offer various advantages

* Repeatability - being able to replay the trajectory with no changes/stochasticity.
* Controllability - being able to control various simulations parameters systematically and understand how they affec the simulation. 
* Efficiency - simulators can often run much faster than real time. 
* Variability - simulators can allow for collecting large diversity of scenarios.
* Evaluation - provide a test bed to benchmark various algorithms.


We believe simulators will continue to play a key role in helping us understand what it needs to transfer results to real world. While there is huge excitement on transferrability, it is important to critically evaluate various important aspects of simualtions *e.g.* how good are the contact models in a physics engines and what approximations are they making, how good is the rendering quality for visual perception and how can we be sure that it will transfer, what are the strengths and limitations of the simulations and which simulator might be more fitting to the task, which simulator is the fastest, to name a few.

Keeping this in mind, we thought it might be worth putting it all together on a website that can catalogue various things related to simulations and offer any suggestions on various simulators, synthetic datasets and state of the art in simulations to real world transfer. There will be occasional tutorials on rendering, physics, robotics, hardware, and SLAM.



<!--{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

-->