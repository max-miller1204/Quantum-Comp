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
