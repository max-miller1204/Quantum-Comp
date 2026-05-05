⊛ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{H} - \boxed{X} \models$

$$\ket{\pm i} = \tfrac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$$

[Bloch sphere with $\ket{0}$ at top (z-axis), $\ket{1}$ at bottom, $\ket{+}$ and $\ket{-}$ on x-axis, $\ket{+i}$ and $\ket{-i}$ on y-axis]

- <u>Pauli-Y measurement</u>: measure along $y$-axis; equivalent to measuring in basis $\{\ket{+i}, \ket{-i}\}$

⊛ <span style="color:red">Recall: $\ket{+i} = SH\ket{0}$, $\ket{-i} = SH\ket{1}$, $H \equiv$ Hadamard gate</span>

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

⊛ <span style="color:red">$SH$ unitary $\Rightarrow \{\ket{+i}, \ket{-i}\}$ is a basis!</span>

$S \equiv$ phase gate
$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

⊛ For a state vector $\ket{\psi}$:

$$P_r(+i) = |\braket{+i|\psi}|^2 = \braket{+i|\psi}\braket{\psi|+i} = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}]$$

$$P_r(-i) = |\braket{-i|\psi}|^2 = \braket{-i|\psi}\braket{\psi|-i} = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$$

<u>Check</u>: $P_r(+i) + P_r(-i) = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}] + \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}]$

$$= \mathrm{Tr}\big[(\ket{+i}\bra{+i} + \ket{-i}\bra{-i})\ket{\psi}\bra{\psi}\big] = \mathrm{Tr}[\ket{\psi}\bra{\psi}] = 1 \checkmark$$

<span style="color:blue">$\ket{+i} = SH\ket{0}$
$\ket{-i} = SH\ket{1}$</span>

$$= SH\ket{0}\bra{0}HS^\dagger + SH\ket{1}\bra{1}HS^\dagger = SH\ket{0}\bra{0}HS^\dagger + SH\ket{1}\bra{1}HS^\dagger$$

$$= SH\big(\ket{0}\bra{0} + \ket{1}\bra{1}\big)HS^\dagger$$
$$\quad\quad\quad\quad\quad\quad = \mathbb{1}$$
$$= SH \cdot HS^\dagger = SS^\dagger = \mathbb{1}$$
$$\quad\;\; = \mathbb{1}$$

⊛ <u>Observe</u>: $P_r(+i) = \mathrm{Tr}[\ket{+i}\bra{+i}\ket{\psi}\bra{\psi}] = \mathrm{Tr}[SH\ket{0}\bra{0}HS^\dagger \underbrace{\ket{\psi}\bra{\psi}}_{}] = \mathrm{Tr}[\ket{0}\bra{0}HS^\dagger\ket{\psi}\bra{\psi}SH]$

$P_r(-i) = \mathrm{Tr}[\ket{-i}\bra{-i}\ket{\psi}\bra{\psi}] = \mathrm{Tr}[SH\ket{1}\bra{1}HS^\dagger\ket{\psi}\bra{\psi}] = \mathrm{Tr}[\ket{1}\bra{1}\underline{HS^\dagger\ket{\psi}}\bra{\psi}SH]$

$\Rightarrow$ Apply $S^\dagger$, then $H$ gate to $\ket{\psi}$, then measure in $\{\ket{0}, \ket{1}\}$ basis!

⊛ <u>Circuit Symbol</u>: $\ket{\psi} - \boxed{S^\dagger} - \boxed{H} - \boxed{X} \models$
