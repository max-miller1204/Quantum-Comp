- An **entangled state** is NOT a separable state.

[Diagram: Alice (left) and Bob (right) each with an atom symbol, connected by a wavy line representing entanglement]

$$\rho_{AB} \neq \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Entangled state*

Correlations between Alice and Bob are non-local.
State of the individual systems not sufficient to describe the pair.

⊛ The **Bell states**

**Pure States:**
$$\begin{cases} \Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}, & \ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}) \\ \Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}, & \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0}) \end{cases}$$

$$\ket{\Phi^+} = \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}\!\begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Phi^-} = \begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ -\tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Psi^+} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}, \quad \ket{\Psi^-} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ -\tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$$

Observe that $\{\ket{\Phi^\pm}, \ket{\Psi^\pm}\} \longleftrightarrow \{\underbrace{(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}}_{\ket{\Phi_{z,x}}} : z, x \in \{0,1\}\}$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \begin{matrix} Z^0 = \mathbb{1}, & Z^1 = Z \\ X^0 = \mathbb{1}, & X^1 = X \end{matrix}$$

$\quad 0,0 \leftrightarrow \Phi^+$
$\quad 0,1 \leftrightarrow \Psi^+$
$\quad 1,0 \leftrightarrow \Phi^-$
$\quad 1,1 \leftrightarrow \Psi^-$

$\ket{\Phi^-} = (Z \otimes \mathbb{1})\ket{\Phi^+}$
$\ket{\Psi^+} = (X \otimes \mathbb{1})\ket{\Phi^+}$
$\ket{\Psi^-} = (ZX \otimes \mathbb{1})\ket{\Phi^+}$
