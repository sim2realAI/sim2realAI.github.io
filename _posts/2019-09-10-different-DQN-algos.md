---
title: Different DQN variations
---

Over the years, different variations of the classic DQN have appeared each with their own attempt at reducing the amount of data needed to learn _i.e._ data efficiency and increasing the overall performance racked against humans at the ATARI benchmarks. These variations are listed below.

**Classic DQN**

$$\mathcal{L} = (R_{t+1} + \gamma_{t} \max_{a'} Q_{\bar{\theta}}  (S_{t+1}, a') - Q_{\theta}(S_{t}, A_{t}))^2$$

**Double DQN**

$$\mathcal{L} = (R_{t+1} + \gamma_{t} Q_{\bar{\theta}}(S_{t+1}, \underset{a'}{\operatorname{argmax}} Q_{\theta}  (S_{t+1}, a')) - Q_{\theta}(S_{t}, A_{t}))^2$$

**Prioritised Replay**

$$p_t  \propto |R_{t+1} + \gamma_{t} \max_{a'} Q_{\bar{\theta}}  (S_{t+1}, a') - Q_{\theta}(S_{t}, A_{t})|^{\omega}$$

**Dueling Networks** 

$$Q_{\theta}(s, a) = V_{\eta}(f_{\xi}(s)) + A_{\phi}(f_{\xi}(s), a) - \frac{\sum_{a'} A_{\phi}(f_{\xi}(s), a')}{N_{actions}}$$

where $$V$$ is the value function and $$A$$ is the advantage function.

**Multi-step Returns**

$$R_{t}^{(n)} = \sum_{k=0}^{n-1} \gamma_{t}^{(k)} R_{t+k+1}$$

$$\mathcal{L} =  (R_{t}^{(n)} + \gamma_{t}^{(n)} \max_{a'} Q_{\bar{\theta}}  (S_{t+n}, a') - Q_{\theta}(S_{t}, A_{t}))^2$$

**Distributional RL**

$$z^{i} = v_{min} + (i-1) \frac{v_{max}-v_{min}}{N_{atoms}-1}$$

$$d_{t} = (\textbf{z}, p_{\theta}(S_t, A_t))$$

$$d^{'}_{t} = (R_{t+1} + \gamma_{t+1}\textbf{z}, p_{\bar{\theta}}(S_{t+1}, a^{*}_{t+1}))$$

$$\mathcal{L} = D_{KL}(\Phi_{z}d^{'}_{t} || d_{t})$$

where $$\Phi_{z}$$ is the projection operator as explained in the original distributional RL paper. The cross entropy $$D_{KL}$$ is minimised here instead of $$L_{2}^{2}$$ loss function as in classic DQN.

Important to remember that $$\gamma$$ is usually fixed in these algorithms but it can be learnt however for each different time-step. For a fixed gamma the time-horizon can be computed as 

$$1 + \gamma + \gamma^2 + \gamma^3 + ... = \frac{1}{1-\gamma}$$

Therefore, the effective time-horizon for $$\gamma=0.99$$ is 100 time-steps.