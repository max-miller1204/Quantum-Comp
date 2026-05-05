6. Consider the circuit below. Prove that this circuit can be used to calculate the imaginary part of the inner product $\braket{\psi|U|\psi}$, namely, $\operatorname{Im}(\braket{\psi|U|\psi})$, where $U$ is an arbitrary single-qubit gate and $\ket{\psi}$ is an arbitrary single-qubit state vector. Here, $H$ denotes the Hadamard gate and $S$ denotes the phase gate.

[Circuit diagram: top wire starts with $\ket{0}$, passes through $H$, then $S^\dagger$, then a control dot, then $H$, then a measurement. Bottom wire starts with $\ket{\psi}$, passes through $U$ (controlled by top wire).]

H on $\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})\otimes\ket{\psi}$

$\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$

$\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\otimes\ket{0} + \ket{1}\otimes\ket{1})\otimes\ket{\psi}$

$S^\dagger$ on $H\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\otimes\ket{0} + i\ket{1}\otimes\ket{1})\otimes\ket{\psi}$

$\ket{00} \rightarrow \ket{00}$

$\ket{01} \rightarrow \ket{01}$

$\ket{10} \rightarrow \ket{10}$ +

$\ket{11} \rightarrow i\ket{11}$

$\;$ [circled: $-6$]

ctrl-$U$ on $\ket{\psi}$ $\rightarrow \frac{1}{\sqrt{2}}(\ket{0}\ket{0} + i\ket{1}\ket{1})\otimes U\ket{\psi}$

H on $\ket{0}$ $\rightarrow \frac{1}{\sqrt{2}}\cdot\frac{1}{\sqrt{2}}(\ket{0}\ket{0}\otimes\ket{0} + i\ket{1}\ket{1}\otimes\ket{1})\otimes U\ket{\psi}$

by basis $\{\ket{0},\ket{1}\}$

$= \frac{1}{2}\left(\ket{0}\otimes(\ket{00}U\ket{\psi}) + \ket{1}\otimes(U_i\ket{11}\ket{\psi})\right)$

$\Pr_1 = $ squared $= \frac{1}{4}\left( \quad \right)^2$

$\Pr_2 = \frac{1}{4}\left(\text{same as this but w/ minus sign}\right)$
