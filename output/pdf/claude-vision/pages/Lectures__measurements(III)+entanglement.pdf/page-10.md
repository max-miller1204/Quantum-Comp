- An <mark>entangled state</mark> is NOT a separable state.

[Diagram: Alice (left) and Bob (right) each holding a box containing an atom, connected by a wavy line representing entanglement]

$$\rho_{AB} \neq \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Entangled state*

Correlations between Alice and Bob are non-local.
State of the individual systems not sufficient to describe the pair.

$Z\ket{0} = \ket{0}$
$Z\ket{1} = -\ket{1}$

(b) <u>Examples</u>:

1. The <mark>Bell states</mark>

$$\ket{\Phi_{0,0}} = \ket{\Phi^+}, \quad (Z \otimes \mathbb{1})\ket{\Phi^+} = \tfrac{1}{\sqrt{2}}(Z\ket{0}\ket{0} + Z\ket{1}\ket{1})$$
$$= \tfrac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1}) \quad\quad = \tfrac{1}{\sqrt{2}}(\ket{0,0} - \ket{1,1})$$
$$= \ket{\Phi^-}$$

$$\Phi^{\pm} = \ket{\Phi^{\pm}}\bra{\Phi^{\pm}}, \quad \ket{\Phi^{\pm}} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1})$$

$$\Psi^{\pm} = \ket{\Psi^{\pm}}\bra{\Psi^{\pm}}, \quad \ket{\Psi^{\pm}} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0})$$

Observe that $\{\ket{\Phi^{\pm}}, \ket{\Psi^{\pm}}\} \longleftrightarrow \{\underbrace{(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}}_{\ket{\Phi_{z,x}}} : z, x \in \{0,1\}\}$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Z^0 = \mathbb{1},\ Z^1 = Z$$
$$X^0 = \mathbb{1},\ X^1 = X$$

$0,0 \leftrightarrow \Phi^+$
$0,1 \leftrightarrow \Psi^+$
$1,0 \leftrightarrow \Phi^-$
$1,1 \leftrightarrow \Psi^-$

→ <u>In $d$ dimensions</u>: $\ket{\Phi_d^+} := \tfrac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k,k} \quad (d=3) \ \tfrac{1}{\sqrt{3}}(\ket{0}\ket{0} + \ket{1}\ket{1} + \ket{2}\ket{2})$

(See later for the other $d$-dimensional Bell states.)

$$\ket{\Phi^+} = \begin{pmatrix} 00 \\ 01 \\ 10 \\ 11 \end{pmatrix}\!\!\begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Phi^-} = \begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ -\tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Psi^+} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}, \quad \ket{\Psi^-} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ -\tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$$
