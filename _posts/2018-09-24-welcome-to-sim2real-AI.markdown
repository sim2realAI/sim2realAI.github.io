---
layout: post
title: "Inaugural blog!"
date: 2018-09-24 13:32:20 +0300
description: Welcome blog # Add post description (optional)
img:  # Add image post (optional)
---

Welcome to our website. We are indexing the progress on simulations to real world transfer in robot perception and control. The past few years have seen a huge interest in learning via simulations and transferring the results to real world. This is largely due to the availability of popular simulators *e.g.* physics simulators like MuJoCo, Bullet, and DART, and 3D rendering engines in Unity, UnrealEngine, and Physically Based Rendering engines.

The real world is often complex and there is a huge cost involved in running experiments. Moreover, collecting large scale real world data can be quite labourious. On the other hand, simulations offer various advantages: 

* Repeatability - being able to replay the trajectory with no changes/stochasticity.
* Controllability - being able to control various simulation parameters systematically and understand how they affect the simulation. 
* Efficiency - simulators can often run much faster than real time. 
* Variability - simulators can allow for collecting large diversity of scenarios.
* Evaluation - providing a test bed to benchmark various algorithms.


We believe simulators will continue to play a key role in helping us understand what is needed to transfer results to real world. While there is huge excitement about transferrability, it is important to critically evaluate various important aspects of simulations *e.g.* how good are the contact models in a physics engines and what approximations are they making, how good is the rendering quality for visual perception and how can we be sure that it will transfer, what are the strengths and limitations of simulations and which simulator might be more fitting to the task and which is the fastest, to name a few.

Keeping this in mind, we thought it might be worth putting this all together on a website that can catalogue various things related to simulations and offer suggestions on different simulators, synthetic datasets and the state of the art in simulations to real world transfer. There will be occasional tutorials on rendering, physics, robotics, hardware, and SLAM.



<!--{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

-->