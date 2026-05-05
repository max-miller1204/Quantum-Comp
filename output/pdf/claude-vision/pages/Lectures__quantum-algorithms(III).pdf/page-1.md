① <u>Recap: Hadamard Test.</u>

Estimating $\bra{\psi}U\ket{\psi}$, where $U$ is a unitary and $\ket{\psi}$ is a state vector.

[Circuit diagram: top wire $\ket{0}$ — H — •  — H — $\pi$ (Pauli-Z measurement); bottom wire $\ket{\psi}$ — U (controlled by top wire) — ]

$$\Pr[0] = \tfrac{1}{2}\bigl(1 + \mathrm{Re}(\bra{\psi}U\ket{\psi})\bigr), \quad \Pr[1] = \tfrac{1}{2}\bigl(1 - \mathrm{Re}(\bra{\psi}U\ket{\psi})\bigr).$$

$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \;\Rightarrow\; S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$$

For the imaginary part:

[Circuit diagram: top wire $\ket{0}$ — H — $S^\dagger$ — • — H — $\pi$ ; bottom wire $\ket{\psi}$ — U (controlled) — ]

$$\Pr[0] = \tfrac{1}{2}\bigl(1 + \mathrm{Im}(\bra{\psi}U\ket{\psi})\bigr)$$

$$\Pr[1] = \tfrac{1}{2}\bigl(1 - \mathrm{Im}(\bra{\psi}U\ket{\psi})\bigr).$$

✱ In both cases, we have $\Pr[0] = \tfrac{1}{2}(1+\alpha)$, $\Pr[1] = \tfrac{1}{2}(1-\alpha)$, where $\alpha$ is unknown. To <u>estimate</u> $\alpha$, we do the following <u>procedure</u>:

For $i = 1, 2, \ldots, N$ ($N \equiv \#$ of samples / # of times we run the quantum circuit).

- Each time we get outcome "0" → record $x_i = 1$
- Each time we get outcome "1" → record $x_i = -1$

✱ This defines a random <u>variable</u> $X$:

$$\Pr[X = \pm 1] = \tfrac{1}{2}(1 \pm \alpha)$$

- Do this $N$ times, then take the <u>sample mean/average</u>: $\hat{X}_N = \tfrac{1}{N} \sum_{i=1}^{N} x_i$ ← sample mean

This defines a random variable $\hat{X}_N = \tfrac{1}{N}\sum_{i=1}^{N} X_i$. $\hat{X}_N$ is an <u>unbiased estimator</u> of $X$:

$$\mathbb{E}[\hat{X}_N] = \tfrac{1}{N}\sum_{i=1}^{N}\mathbb{E}[X_i] = \tfrac{1}{N}\sum_{i=1}^{N}\mathbb{E}[X] = \mathbb{E}[X].$$

↑ True mean

$\mathbb{E}[X_i] = \mathbb{E}[X]\;\forall i$, b/c all samples are independent and identical.
