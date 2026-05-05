⊛ <u>Observe</u>: If $\ket{\psi} = \ket{0}$, then $\Pr(0) = 1$, $\Pr(1) = 0$.
If $\ket{\psi} = \ket{1}$, then $\Pr(0) = 0$, $\Pr(1) = 1$.

— We can measure with respect to other Pauli operators too!

[Bloch sphere diagram with $\ket{0}$ at top (+z), $\ket{1}$ at bottom, $\ket{+}$ on +x axis, $\ket{-}$ on −x, $\ket{+i}$ on +y, $\ket{-i}$ on −y]

- <u>Pauli-X measurement</u>: measure along x-axis; equivalent to measuring in basis $\{\ket{+}, \ket{-}\}$

⊛ Recall: $\ket{+} = H\ket{0}$, $\ket{-} = H\ket{1}$, $H \equiv$ Hadamard gate
$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

⊛ $H$ unitary $\Rightarrow \{\ket{+}, \ket{-}\}$ is a basis!

⊛ For a state vector $\ket{\psi}$:
$$\Pr(+) = |\braket{+|\psi}|^2 = \braket{+|\psi}\braket{\psi|+} = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big]$$
$$\Pr(-) = |\braket{-|\psi}|^2 = \braket{-|\psi}\braket{\psi|-} = \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big]$$

$\ket{+} = H\ket{0}$
$\ket{-} = H\ket{1}$

<u>Check</u>: $\Pr(+) + \Pr(-) = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big] + \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big]$

$$= \mathrm{Tr}\Big[\underbrace{\big(\ket{+}\bra{+} + \ket{-}\bra{-}\big)}_{\downarrow}\ket{\psi}\bra{\psi}\Big] = \mathrm{Tr}\big[\ket{\psi}\bra{\psi}\big] = 1 \;\checkmark$$

$$= H\ket{0}\bra{0}H^\dagger + H\ket{1}\bra{1}H^\dagger = H\ket{0}\bra{0}H + H\ket{1}\bra{1}H$$
$$= H\underbrace{\big(\ket{0}\bra{0} + \ket{1}\bra{1}\big)}_{=\,\mathbb{1}}H$$
$$= HH = \mathbb{1}$$

⊛ <u>Observe</u>: $\Pr(+) = \mathrm{Tr}\big[\ket{+}\bra{+}\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[H\ket{0}\bra{0}H\,\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[\ket{0}\bra{0}\,\underline{H\ket{\psi}\bra{\psi}H}\big]$

$\quad\;\; \Pr(-) = \mathrm{Tr}\big[\ket{-}\bra{-}\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[H\ket{1}\bra{1}H\,\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}\big[\ket{1}\bra{1}\,\underline{H\ket{\psi}\bra{\psi}H}\big]$

[with $\ket{\psi'}$ labeled above $H\ket{\psi}\bra{\psi}H$]

$\Rightarrow$ Apply $H$ gate to $\ket{\psi}$, then measure in $\{\ket{0}, \ket{1}\}$ basis!

$X\ket{+} = \ket{+},\; X\ket{-} = -\ket{-}$
