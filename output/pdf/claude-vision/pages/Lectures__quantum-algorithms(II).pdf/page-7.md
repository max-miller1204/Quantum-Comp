This defines a random variable $\hat{X}_N = \frac{1}{N}\sum_{i=1}^{N} X_i$. $\hat{X}_N$ is an <u>unbiased estimator</u> of $X$:

$$\mathbb{E}[\hat{X}_N] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X_i] = \frac{1}{N}\sum_{i=1}^{N} \mathbb{E}[X] = \mathbb{E}[X].$$

$\qquad\qquad\quad = \mathbb{E}[X] \;\forall i$, b/c all samples are independent and identical.

$$\mathbb{E}[X] = \sum_x x\, \Pr[X=x]$$

$$\mathbb{E}[X] = (+1)\cdot \Pr[X=+1] + (-1)\cdot \Pr[X=-1] = \tfrac{1}{2}\left(1 + |\braket{\gamma|\phi}|^2\right) - \tfrac{1}{2}\left(1 - |\braket{\gamma|\phi}|^2\right) = |\braket{\gamma|\phi}|^2$$

- As $N \to \infty$, $\hat{X}_N \to \mathbb{E}[X] = |\braket{\gamma|\phi}|^2$  (<u>law of large numbers</u>).

⊛ So the sample average approaches the true (unknown) inner product!

```python
[89]: import numpy as np
      import matplotlib.pyplot as plt

      inner_product=0.8
      # Parameters
      p = (1/2)*(1-inner_product)        # probability of original "1"
      n_samples = 20000

      # Step 1: sample Bernoulli (0 or 1)
      samples = np.random.binomial(1, p, size=n_samples)

      # Step 2: map to +1 / -1
      mapped = 1 - 2 * samples   # 0 -> 1, 1 -> -1

      # Step 3: running average
      running_avg = np.cumsum(mapped) / np.arange(1, n_samples + 1)

      # True mean of the new variable
      true_mean = 1 - 2*p

      # Plot
      plt.figure()
      plt.plot(running_avg)#, label="Running average")
      plt.axhline(true_mean, linestyle='--', label="True inner product")

      plt.xlabel("Number of samples")
      plt.ylabel("Sample average")
      plt.title("Inner product estimation (swap test)")
      plt.legend()
      plt.show()
```

[Plot titled "Inner product estimation (swap test)". X-axis: "Number of samples" from 0 to 20000. Y-axis: "Sample average" from 0.60 to 1.00. A blue curve representing the running sample average starts with high variance near the origin (oscillating between ~0.60 and ~1.00) and quickly converges to ~0.80. A dashed horizontal line at 0.80 labeled "True inner product".]
