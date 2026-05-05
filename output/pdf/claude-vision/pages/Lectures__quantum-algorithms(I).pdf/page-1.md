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
