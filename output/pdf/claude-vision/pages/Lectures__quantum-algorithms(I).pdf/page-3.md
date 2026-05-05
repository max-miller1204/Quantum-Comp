(a) From the swap test, we know that $\Pr(0) = \frac{1}{2}(1+\alpha)$, $\quad \alpha = |\braket{\psi|\phi}|^2$.

$$\Pr(1) = \frac{1}{2}(1-\alpha)$$

Running this many times will give us a bunch of "0"s and "1"s.

How do we use the "0"s and "1"s to estimate $\alpha$?

(b) <u>Procedure</u>: For $i = 1, 2, \ldots, N$ ($N \equiv$ number of samples)

- Each time we get outcome "0" $\to$ record $x_i = 1$
- Each time we get outcome "1" $\to$ record $x_i = -1$

$\circledast$ This defines a <u>random variable</u> $X$:

$$\Pr[X = \pm 1] = \frac{1}{2}(1 \pm \alpha)$$

- Do this $N$ times, then take the <u>sample mean/average</u>: $\hat{x}_N = \frac{1}{N} \sum_{i=1}^{N} x_i$

This defines a random variable $\hat{X}_N = \frac{1}{N}\sum_{i=1}^{N} X_i$. $\hat{X}_N$ is an <u>unbiased estimator</u> of $X$:

$$\mathbb{E}[\hat{X}_N] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X_i] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X] = \mathbb{E}[X].$$

$\quad = \mathbb{E}[X]\ \forall i$, b/c all samples are independent and identical.

$$\mathbb{E}[X] = (+1)\cdot \Pr[X = +1] + (-1)\cdot \Pr[X = -1] = \frac{1}{2}(1+\alpha) - \frac{1}{2}(1-\alpha) = \alpha.$$

- As $N \to \infty$, $\hat{X}_N \to \mathbb{E}[X] = |\braket{\psi|\phi}|^2$ (<u>law of large numbers</u>).

$\circledast$ So the sample average approaches the true (unknown) value of $\alpha$!
