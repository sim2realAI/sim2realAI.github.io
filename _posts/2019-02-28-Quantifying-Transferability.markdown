---
layout: post
title: "Quantifying the Transferability of Sim-2-Real Control Policies"
date: 2019-02-21 12:00:00 +0100
description: On the simulation optimization bias and the optimality gap in the context of reinforcement learning # Add post description (optional)
img:  # Add image post (optional)
---

We start by framing reinforcement learning problem as a _stochastic program_, i.e., maximizing the expectation of estimated discounted return $$J(\theta)$$ over the domain parameters $$\xi \sim p(\xi; \psi)$$, where $$\psi$$ are the parameters of the distribution

$$
    J(\theta^{\star}) = \max_{\theta \in \Theta} \mathbb{E}_\xi \left[J(\theta, \xi) \right].
$$

Since it is intractable to compute the expectation over all domains, we approximate the stochastic program using $n$ samples

$$
    \hat{J}_n(\theta^{\star}_n) = \max_{\theta \in \Theta} \frac{1}{n}\sum_{i=1}^{n} J(\theta, \xi_i).
$$

It has been shown under mild assumptions, which are fulfilled in the reinforcement leaning setting, that [sample-based optimization is optimistically biased](https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/WR025i002p00152), i.e., the solution is guaranteed to degrade in terms of performance when transformed to the real system.
This loss in performance can be expressed by the _Simulation Optimization Bias_ (SOB)

$$
    \mathrm{b}\left[ \hat{J}_n(\theta^{\star}_n) \right] =
    \underbrace{
        \mathbb{E}_\xi \left[ \max_{\hat{\theta} \in \Theta} \frac{1}{n}\sum_{i=1}^{n} J(\hat{\theta}, \xi_i) \right]
    }_{\text{optimal value for samples}}
    -
    \underbrace{
        \max_{\theta \in \Theta} \mathbb{E}_\xi \left[ J(\theta, \xi) \right]
    }_{\text{true optimal value}}
    \ge 0.
$$

The figure below qualitatively displays the SOB between the true optimum $J(\theta^\star)$ and the sample-based optimum $\hat{J}_n(\theta_n^\star)$. The shaded region visualizes the variance arising when approximating $J(\theta)$ with $n$ domains.

<center>
<img src="/assets/img/2019-02-28/SOB_sketch.png" width="50%">
</center>

Unfortunately, this quantity can not be used right away as an objective function, because we can not compute the expectation in the minuend, and we do not know the optimal policy parameters for the real system $\theta^\star$ in the subtrahend.  
Inspired by the work of [Mak et al.](https://ac.els-cdn.com/S0167637798000546/1-s2.0-S0167637798000546-main.pdf?_tid=8f5399ae-fda8-41f9-b499-5991d943237c&acdnat=1550665775_b5dfa73c82228c19975ebbc882d775a7) on assessing the solution quality of convex stochastic problems, we employ the _Optimality Gap_ (OG) at the candidate solution $\theta^c$

$$
    G(\theta^c) =
    \underbrace{\max_{\theta \in \Theta} \mathbb{E}_\xi \left[J(\theta, \xi) \right]}_{\text{best solution's value}} -
    \underbrace{\mathbb{E}_\xi \left[J(\theta^c, \xi) \right]}_{\text{candidate solution's value}}
    \ge 0
$$

to quantify how much our solution $\theta^c$, e.g. yielded by a policy search algorithm, is worse than the best solution the algorithm could have found. In general, this measure is agnostic to the fact if we are evaluating the policies in simulation or reality. Since we are discussing the sim-2-real setting, think of OG as a quantification of our solutions suboptimality in simulation.  
However, computing $G(\theta^c)$ also includes an expectation over all domains. Thus, we have to approximate it from samples. Using $n$ domains, the estimated OG at our candidate solution is

$$
    \hat{G}_n(\theta^c) = \max_{\theta\in\Theta} \hat{J}_n(\theta) - \hat{J}_n(\theta^c) \ge G(\theta^c).
$$

In SPOTA, an upper confidence bound on $\hat{G}_n(\theta^c)$ is used to give a probabilistic guarantee on the transferability of the policy learned in simulation. So, the results is a policy that with probability $(1-\alpha)$ does not lose more than $\beta$ in terms of return when transferred from one domain to a different domain of the same source distribution $p(\xi; \psi)$.  
Essentially, SPOTA increases the number of domains for every iteration until the policy's upper confidence bound on the estimated OG is lower than the desired threshold $\beta$.  

Let's assume everything worked out fine and we trained a policy from randomized simulations such that the upper confidence bound on $\hat{G}_n(\theta^c)$ was reduced below the desired threshold.
Now, the key question is if this property actually contributes to our goal of obtaining a low Simulation Optimization Bias (SOB).  
The relation between the OG and and the SOB can be written as

$$
    \mathrm{b}\left[ \hat{J}_n(\theta^{\star}_n) \right] = \mathbb{E}_\xi \left[ \hat{G}_n(\theta^c) \right]- G(\theta^c)
$$

where in this case the evaluation is performed in the real world.<!-- where in this case $G(\theta^c)$ is evaluated in the real world. -->
Therefore, lowering the upper confidence bound on the estimated OG $\hat{G}_n(\theta^c)$ contributes to lowering the SOB $\mathrm{b}\left[ \hat{J}_n(\theta^{\star}_n) \right]$.

> Please note, that the terminology used in this post deviates sightly from the one used in [Muratore et al.](https://www.ias.informatik.tu-darmstadt.de/uploads/Team/FabioMuratore/Muratore_Treede_Gienger_Peters--SPOTA_CoRL2018.pdf).

### SPOTA &mdash; Sim-2-Sim Results

Preceding results on transferring policies trained with SPOTA from one simulation to another have been reported in [Muratore et al.](https://www.ias.informatik.tu-darmstadt.de/uploads/Team/FabioMuratore/Muratore_Treede_Gienger_Peters--SPOTA_CoRL2018.pdf). The videos below show the performance in example scenarios side-by-side with **3 baselines**:

* **EPOpt** by [Rajeswaran et al.](https://arxiv.org/pdf/1610.01283.pdf) which is a domain ranomization algorithm that maximizes the [conditional value at risk](https://en.wikipedia.org/wiki/Expected_shortfall) of the expected discounted return
* **TRPO** without domain randomization (implementation from [Duan et al.](https://arxiv.org/pdf/1604.06778.pdf))
* **LQR** applying optimal control for the system linearized around the goal state (an equilibrium)

<center>
<iframe width="603" height="452" src="https://www.youtube.com/embed/RQ7zq_bcv_k" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="603" height="452" src="https://www.youtube.com/embed/ORi9sjhs_tw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</center>

### SPOTA &mdash; Sim-2-Real Results

Finally, I want to share some _early_  results acquired on the [2 DoF Ball Balancer from Quanser](https://www.quanser.com/products/2-dof-ball-balancer/). Here, the task is to stabilize a ball at the center of the plate. The device receives voltage commands for the two motors and yields measurements of the ball position (2D relative to the plate) as well as the motors' shaft angular positions (relative to their initial position). Including the velocities derived from the position signals, the system has a 2-dim continuous action space and a 8-dim continuous observation space.

Assume we obtained an analytical model of the dynamics and determined the parameters with some imperfections (e.g., the characteristics of the servo motors from the data sheet do not match the reality).

In the first experiment, we investigate what happens if we train control policies on a slightly faulty simulator using a model-free reinforcement learning algorithm called Proximal Policy Optimization (PPO).  
**Left video**: a policy learned with PPO on a simulator with larger ball and larger plate&mdash; tested on the nominal system.  
**Right video**: another policy learned with PPO on a simulator with higher motor as well as gear box efficiency&mdash; tested on the nominal system.  
<center>
<video width="301" src="/assets/vid/2019-02-28/HC_trn_domain1_stabilizing.mov" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen muted loop controls></video>

<video width="301" src="/assets/vid/2019-02-28/HC_trn_domain2_stabilizing.mov" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen muted loop controls></video>
</center>

<br>
In the second experiment, we test policies trained using SPOTA, i.e., applying domain randomization.  
**Left video**: a policy learned with SPOTA&mdash; tested on the nominal system.  
**Right video**: the same policy learned with SPOTA&mdash; tested with a modified ball (the ball was cut open and filled with paper, the remaining glue makes the ball roll unevenly).
<center>
<video width="301" src="/assets/vid/2019-02-28/SPOTA_nominal_stabilizing.mov" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen muted loop controls></video>

<video width="301" src="/assets/vid/2019-02-28/SPOTA_heavier_ball_stablilizing.mov" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen muted loop controls></video>
</center>

> Disclaimer: despite a dead band in the servo motors' voltage commands, noisy velocity signals from the ball detection, and (minor) nonlinearities in the dynamics this stabilizing task can also be solved by tuning the gains of a PD-controller while executing real-world trials.  
Furthermore, after a careful parameter estimation, we are able to learn this task for the nominal system in simulation using PPO. However, the resulting policy is sensitive to model uncertainties (e.g., testing with a different ball).

---

## Author

[Fabio Muratore](https://www.ias.informatik.tu-darmstadt.de/Team/FabioMuratore) &mdash; Intelligent Autonomous Systems Group (TU Darmstadt) and Honda Research Institute Europe

## Acknowledgements

I want to thank Ankur Handa editing, and Michael Gienger for proofreading this post.

## Credits

First figure with permission from Josh Tobin [(source)](https://arxiv.org/pdf/1703.06907.pdf)  
Second figure with permission from Yevgen Chebotar [(source)](https://arxiv.org/pdf/1810.05687.pdf)
