(a) Key ingredient: the two-qubit __Bell measurement__

- POVM is $\{\Phi^+, \Phi^-, \Psi^+, \Psi^-\}$, $\quad \Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}$, $\Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}$.

$$\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{0} \pm \ket{1}\ket{1}\right)$$
$$\ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}\left(\ket{0}\ket{1} \pm \ket{1}\ket{0}\right)$$

- Circuit description of the measurement:

[Circuit diagram: Two wires labeled $A'$ (top, source) and $A$ (bottom, target). A CNOT gate with control on $A'$ and target on $A$, followed by a Hadamard gate $H$ on the $A'$ wire, then $z$-basis measurements ($\ket{x}$ boxes) on both wires.]

Hadamard gate: $H\ket{0} = \ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0}+\ket{1})$
$H\ket{1} = \ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0}-\ket{1})$

$$H = \tfrac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

$z$-basis measurement.

CNOT gate (source $\to$ target):
$$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

$\text{CNOT}\ket{0,0} = \ket{0,0}$
$\text{CNOT}\ket{0,1} = \ket{0,1}$
$\text{CNOT}\ket{1,0} = \ket{1,1}$
$\text{CNOT}\ket{1,1} = \ket{1,0}$

---

(b) __Protocol analysis__

$\ket{\psi}_{A'} = \alpha \ket{0}_{A'} + \beta \ket{1}_{A'} \quad \to$ State Alice wants to send to Bob. $\quad (|\alpha|^2 + |\beta|^2 = 1)$

$\ket{\Phi^+}_{AB} = \tfrac{1}{\sqrt{2}}\left(\ket{0,0}_{AB} + \ket{1,1}_{AB}\right) \to$ Shared entanglement.

(1) Joint initial state: 
$$\ket{\psi}_{A'} \otimes \ket{\Phi^+}_{AB} = \left(\alpha\ket{0}_{A'} + \beta\ket{1}_{A'}\right) \otimes \tfrac{1}{\sqrt{2}}\left(\ket{0,0}_{AB} + \ket{1,1}_{AB}\right)$$
$$= \tfrac{1}{\sqrt{2}}\Big(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB} + \beta\ket{1,0,0}_{A'AB} + \beta\ket{1,1,1}_{A'AB}\Big)$$
