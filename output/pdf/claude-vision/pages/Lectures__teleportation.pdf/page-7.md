⇒ State of Bob conditioned on Alice's outcome is $X\ket{\psi}$.

- <u>Outcome (1,0)</u>: $\Pr(1,0) = \text{Tr}\Big[ \big(\bra{1,0}_{A'A} \otimes \mathbb{I}_B\big) \ket{\phi}\bra{\phi}_{A'AB} \big(\ket{1,0}_{A'A} \otimes \mathbb{I}_B\big) \Big]$

$$\ket{\phi}_{A'AB} = \tfrac{1}{2}\Big( \ket{0,0}_{A'A}\big(\alpha\ket{0}+\beta\ket{1}\big)_B + \ket{0,1}_{A'A}\big(\alpha\ket{1}+\beta\ket{0}\big)_B$$
$$+ \ket{1,0}_{A'A}\big(\alpha\ket{0}-\beta\ket{1}\big)_B + \ket{1,1}_{A'A}\big(\alpha\ket{1}-\beta\ket{0}\big)_B \Big)$$

$\ket{\psi} = \alpha\ket{0}+\beta\ket{1}$
$Z\ket{\psi} = \alpha Z\ket{0} + \beta Z\ket{1}$, $\quad Z\ket{1}=-\ket{1}$
$\quad\quad = \alpha\ket{0} - \beta\ket{1}$.

$\big(\bra{1,0}_{A'A} \otimes \mathbb{I}_B\big)\ket{\phi}_{A'AB} = \tfrac{1}{2}\big(\alpha\ket{0}-\beta\ket{1}\big) = \tfrac{1}{2} Z\ket{\psi}$ → Pauli $Z$

$$\text{Tr}\big[\tfrac{1}{2} Z\ket{\psi}\bra{\psi} Z \tfrac{1}{2}\big] = \tfrac{1}{4}\text{Tr}\big[Z\ket{\psi}\bra{\psi} Z\big] = \tfrac{1}{4}\text{Tr}\big[\ket{\psi}\bra{\psi}\big] = \tfrac{1}{4}.$$

$Z^2 = \mathbb{I}$

$\Rightarrow \Pr(1,0) = \tfrac{1}{4}$

⇒ State of Bob conditioned on Alice's outcome is $Z\ket{\psi}$.

- <u>Outcome (1,1)</u>: $\Pr(1,1) = \text{Tr}\Big[ \big(\bra{1,1}_{A'A} \otimes \mathbb{I}_B\big) \ket{\phi}\bra{\phi}_{A'AB} \big(\ket{1,1}_{A'A} \otimes \mathbb{I}_B\big) \Big]$

$$\ket{\phi}_{A'AB} = \tfrac{1}{2}\Big( \ket{0,0}_{A'A}\big(\alpha\ket{0}+\beta\ket{1}\big)_B + \ket{0,1}_{A'A}\big(\alpha\ket{1}+\beta\ket{0}\big)_B$$
$$+ \ket{1,0}_{A'A}\big(\alpha\ket{0}-\beta\ket{1}\big)_B + \ket{1,1}_{A'A}\big(\alpha\ket{1}-\beta\ket{0}\big)_B \Big)$$

$\big(\bra{1,1}_{A'A} \otimes \mathbb{I}_B\big)\ket{\phi}_{A'AB} = \tfrac{1}{2}\big(\alpha\ket{1}-\beta\ket{0}\big) = \tfrac{1}{2} XZ\ket{\psi}_B$

$$\text{Tr}\big[\tfrac{1}{2} XZ\ket{\psi}\bra{\psi} ZX \tfrac{1}{2}\big] = \tfrac{1}{4}\text{Tr}\big[ZX\ket{\psi}\bra{\psi} XZ\big] = \tfrac{1}{4}\text{Tr}\big[\ket{\psi}\bra{\psi}\big] = \tfrac{1}{4}.$$

$\Rightarrow \Pr(1,1) = \tfrac{1}{4}$

$Z^2 = \mathbb{I},\ X^2 = \mathbb{I}$

⇒ State of Bob conditioned on Alice's outcome is $XZ\ket{\psi}$.
