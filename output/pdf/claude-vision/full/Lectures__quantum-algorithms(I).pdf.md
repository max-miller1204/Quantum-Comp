# Lectures__quantum-algorithms(I).pdf

## Page 1

# ① Recap: Swap test

- **Goal:** given two pure states given by $\ket{\psi}$ and $\ket{\phi}$, find out how close they are.

[Circuit diagram: top wire starts in $\ket{0}$, applies $H$, then control to SWAP gate, then $H$, then Pauli-Z measurement (denoted by $X$ box). Middle wire is $\ket{\psi}$ entering SWAP. Bottom wire is $\ket{\phi}$ entering SWAP. Annotation: "Pauli-Z measurement $\{\ket{0}\bra{0}, \ket{1}\bra{1}\}$".]

$$\Pr[0] = \tfrac{1}{2}\left(1 + |\braket{\psi|\phi}|^2\right)$$

$$\Pr[1] = \tfrac{1}{2}\left(1 - |\braket{\psi|\phi}|^2\right)$$

$H\ket{0} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1}) = \ket{+}$

$H\ket{1} = \tfrac{1}{\sqrt{2}}(\ket{0}-\ket{1}) = \ket{-}$

$$\begin{aligned}
\ket{0}\ket{0} &\mapsto \ket{0}\ket{0} \\
\ket{0}\ket{1} &\mapsto \ket{1}\ket{0} \\
\ket{1}\ket{0} &\mapsto \ket{0}\ket{1} \\
\ket{1}\ket{1} &\mapsto \ket{1}\ket{1}
\end{aligned}$$

$\to$ This means that $\text{SWAP}(\ket{\psi}\ket{\phi}) = \ket{\phi}\ket{\psi}$

- The quantity $|\braket{\psi|\phi}|^2$ quantifies the closeness of $\ket{\psi}$ and $\ket{\phi}$ — it is called the **fidelity** of $\ket{\psi}$ and $\ket{\phi}$.

$$\{M_x\}_x,\quad M_x \geq 0,\quad \sum_x M_x = \mathbb{1}.$$

(★) Observe that $\{\ket{\phi}\bra{\phi},\ \mathbb{1} - \ket{\phi}\bra{\phi}\}$ is a measurement (POVM).

**Check:** $\braket{v|\phi}\braket{\phi|v} = |\braket{v|\phi}|^2 \geq 0$ ✓

Also, from the Cauchy–Schwarz inequality: $|\braket{v|\phi}|^2 \leq \braket{v|v} \cdot \underbrace{\braket{\phi|\phi}}_{=1}$

$\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad = \braket{v|v} = \||v\rangle\|^2$

Therefore, $\braket{v|(\mathbb{1} - \ket{\phi}\bra{\phi})|v} = \braket{v|v} - \underbrace{|\braket{v|\phi}|^2}_{\leq \braket{v|v}} \geq 0$ ✓

Finally, $\ket{\phi}\bra{\phi} + \mathbb{1} - \ket{\phi}\bra{\phi} = \mathbb{1}$ ✓

So $\{\ket{\phi}\bra{\phi},\ \mathbb{1} - \ket{\phi}\bra{\phi}\}$ satisfies the definition of a quantum measurement (POVM).

## Page 2

(\*) $\{\ket{\phi}\bra{\phi}, \mathbb{1}-\ket{\phi}\bra{\phi}\}$ is a measurement that tells us whether or not a given state is equal to $\ket{\phi}\bra{\phi}$.

It has two outcomes (b/c the set has two operators).

- $\ket{\phi}\bra{\phi} \equiv$ "yes, the state is $\ket{\phi}\bra{\phi}$"
- $\mathbb{1} - \ket{\phi}\bra{\phi} \equiv$ "no, the state is not $\ket{\phi}\bra{\phi}$".

(\*) For a given state $\rho$, $\Pr[\phi] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\rho\right]$  $\quad$ <span style="color:blue">Born Rule: $\{M_x\}$ POVM<br>State $\rho \to \Pr(x) = \text{Tr}(M_x \rho)$.</span>

$$\Pr[\text{not } \phi] = \text{Tr}\!\left[(\mathbb{1} - \ket{\phi}\bra{\phi})\rho\right] = \text{Tr}(\rho) - \text{Tr}\!\left[\ket{\phi}\bra{\phi}\rho\right] = 1 - \Pr[\phi].$$

- If $\rho = \ket{\phi}\bra{\phi}$ itself, then $\Pr[\phi] = \text{Tr}\!\left[\underbrace{\ket{\phi}\braket{\phi|\phi}\bra{\phi}}_{=1}\right] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\right] = \braket{\phi|\phi} = 1.$ ✓

  $\Pr[\text{not } \phi] = 1 - \Pr[\phi] = 0$

- If $\rho = \ket{\gamma}\bra{\gamma}$, then $\Pr[\phi] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\ket{\gamma}\bra{\gamma}\right] = |\braket{\phi|\gamma}|^2 \to$ fidelity!

(\*) So the swap test allows us to do the measurement $\{\ket{\phi}\bra{\phi}, \mathbb{1} - \ket{\phi}\bra{\phi}\}$ and estimate the fidelity — without even knowing what $\ket{\phi}$ is!

## ② <u>Statistical Estimation from a Quantum Computer.</u>

- When we run a quantum algorithm and do the measurement at the end, the outcomes will generally be probabilistic.

- To extract the relevant information, we have to run the algorithm many times.

## Page 3

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

## Page 4

③ <u>Hadamard Test</u>: Estimating $\braket{\psi|U|\psi}$, where $U$ is a unitary and $\ket{\psi}$ is a state vector.

[Circuit diagram: top wire $\ket{0}$ — H — •(control) — H — measurement (Pauli-Z); bottom wire $\ket{\psi}$ — U(target) —. The measurement is annotated "Pauli-Z measurement".]

$\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$

$$\ket{\psi_{init}} = \ket{0}\ket{\psi} \mapsto \ket{+}\ket{\psi} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{\psi} + \ket{1}\ket{\psi}\big) \mapsto \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{\psi} + \ket{1}U\ket{\psi}\big)$$

$$\mapsto \tfrac{1}{2}\big(\ket{+}\ket{\psi} + \ket{-}U\ket{\psi}\big) = \tfrac{1}{\sqrt{2}}\Big(\ket{0}\tfrac{1}{\sqrt{2}}(\ket{\psi}+U\ket{\psi}) + \ket{1}\tfrac{1}{\sqrt{2}}(\ket{\psi} - U\ket{\psi})\Big) = \ket{\psi_{final}}$$

$$\Pr[0] = \mathrm{Tr}\Big[\big(\ket{0}\bra{0} \otimes \mathbb{1}\big)\ket{\psi_{final}}\bra{\psi_{final}}\Big] \qquad \tfrac{1}{2}(\ket{\psi}+U\ket{\psi})^{\dagger} = \tfrac{1}{2}(\bra{\psi} + \bra{\psi}U^{\dagger})$$

$$= \tfrac{1}{4}\Big(\big(\bra{\psi} + \bra{\psi}U^{\dagger}\big)\big(\ket{\psi} + U\ket{\psi}\big)\Big)$$

$$= \tfrac{1}{4}\Big(\underbrace{\braket{\psi|\psi}}_{=\braket{\psi|\psi}=1} + \braket{\psi|U|\psi} + \underbrace{\braket{\psi|U^{\dagger}|\psi}}_{= \overline{\braket{\psi|U|\psi}}} + \underbrace{\braket{\psi|U^{\dagger}U|\psi}}_{=\mathbb{1}}\Big) \qquad \begin{matrix} z = x+yi \\ \bar{z} = x-yi \end{matrix} \Bigg\} \to z + \bar z = 2x$$

$$\hspace{8cm} x = \mathrm{Re}(z).$$

$$= \tfrac{1}{2}\Big(1 + \mathrm{Re}\big(\braket{\psi|U|\psi}\big)\Big)$$
$$\hspace{2cm}\underbrace{\phantom{\mathrm{Re}\braket{\psi|U|\psi}}}_{\alpha}$$

$$\Pr[1] = \tfrac{1}{2}\Big(1 - \underbrace{\mathrm{Re}\big(\braket{\psi|U|\psi}\big)}_{\alpha}\Big)$$

$\to$ Then same procedure as above to estimate $\alpha$!
$\Pr[0] = \tfrac{1}{2}(1+\alpha), \quad \Pr[1] = \tfrac{1}{2}(1-\alpha).$

✱ For the imaginary part → include the S gate!

[Circuit diagram: top wire $\ket{0}$ — H — S† — •(control) — H — measurement (Pauli-Z); bottom wire $\ket{\psi}$ — U(target) —.]

$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \implies S^{\dagger} = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$$

$S^{\dagger}\ket{0} = \ket{0}$
$S^{\dagger}\ket{1} = -i\ket{1}$

$$\ket{0}\ket{\psi} \mapsto \ket{+}\ket{\psi} = \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{\psi} + \ket{1}\ket{\psi}\big) \mapsto \tfrac{1}{\sqrt{2}}\big(\underbrace{\ket{0}}_{S^{\dagger}\ket{0}}\ket{\psi} - i\underbrace{\ket{1}}_{S^{\dagger}\ket{1}}\ket{\psi}\big)$$

$$\mapsto \tfrac{1}{\sqrt{2}}\big(\ket{0}\ket{\psi} - i\ket{1}U\ket{\psi}\big) \mapsto \tfrac{1}{\sqrt{2}}\big(\ket{+}\ket{\psi} - i\ket{-}U\ket{\psi}\big)$$

[curly brace gathering the final lines]

## Page 5

$$= \frac{1}{\sqrt{2}}\left(\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})\ket{\psi} - i\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})U\ket{\psi}\right)$$

$$= \frac{1}{2}\left(\ket{0}\ket{\psi} + \ket{1}\ket{\psi} - i\ket{0}U\ket{\psi} + i\ket{1}U\ket{\psi}\right)$$

$$= \frac{1}{2}\left(\ket{0}(\ket{\psi}-iU\ket{\psi}) + \ket{1}(\ket{\psi}+iU\ket{\psi})\right) \longrightarrow (\ket{\psi}-iU\ket{\psi})^\dagger = \bra{\psi} + i\bra{\psi}U^\dagger$$

$$\Rightarrow \Pr[0] = \frac{1}{4}\left(\bra{\psi}+i\bra{\psi}U^\dagger\right)\left(\ket{\psi}-iU\ket{\psi}\right) = \frac{1}{4}\Big(\underbrace{\braket{\psi|\psi}}_{=1} - i\braket{\psi|U|\psi} + i\braket{\psi|U^\dagger|\psi}$$

$$+ \underbrace{\braket{\psi|U^\dagger U|\psi}}_{\substack{=\mathbb{1}\\=1}}\Big)$$

$$= \frac{1}{4}\Big(1 - i\underbrace{\braket{\psi|U|\psi}}_{z} + i\underbrace{\overline{\braket{\psi|U|\psi}}}_{\bar z} + 1\Big) \qquad \left(z - \bar z = x+iy - x+iy = 2iy\right)$$

$$= \frac{1}{4}\left(2 - i\underbrace{\left(\braket{\psi|U|\psi} - \overline{\braket{\psi|U|\psi}}\right)}_{= 2i\,\mathrm{Im}(\braket{\psi|U|\psi})}\right)$$

$$= \frac{1}{2}\Big(1 + \underbrace{\mathrm{Im}(\braket{\psi|U|\psi})}_{\alpha}\Big)$$

$$\Pr[1] = \frac{1}{2}\Big(1 - \underbrace{\mathrm{Im}(\braket{\psi|U|\psi})}_{\alpha}\Big)$$

$\rightarrow$ Then same procedure as above to estimate $\alpha$!
$$\Pr[0] = \tfrac{1}{2}(1+\alpha), \quad \Pr[1] = \tfrac{1}{2}(1-\alpha).$$
