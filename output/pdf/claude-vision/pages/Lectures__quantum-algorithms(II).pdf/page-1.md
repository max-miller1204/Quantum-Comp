① <u>Recap</u>: Quantum Circuits

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left. 

1st layer: $U_1$ acts on qubits 1,2; $U_2$ acts on qubits 3,4; $U_3$ acts on qubits 5,6.
2nd layer: $U_4$ acts on qubits 2,3; $U_5$ acts on qubits 4,5.
3rd layer: $U_6$ on qubits 1,2; $U_7$ on qubits 3,4; $U_8$ on qubits 5,6.

Each output line ends with a measurement (D) producing $x_1', x_2', x_3', x_4', x_5', x_6'$.]

$(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

1st layer | 2nd layer | 3rd layer  →  time

(✱) The circuit elements/gates are <u>unitaries</u>.
$$\left( U : U^\dagger U = U U^\dagger = \mathbb{1} \right)$$

Measurement / read-out:
$$\{\ket{0}\bra{0}, \ket{1}\bra{1}\} \rightarrow \begin{array}{l} \text{Pauli-}Z \\ \text{Computational} \\ \text{Basis.} \end{array}$$

---

(a) <u>Pauli gates</u>:

$-\boxed{X}- \quad \rightarrow \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \left( X\ket{0} = \ket{1},\ X\ket{1} = \ket{0} \right)$

$-\boxed{Y}- \quad \rightarrow \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \left( Y\ket{0} = i\ket{1},\ Y\ket{1} = -i\ket{0} \right)$

$-\boxed{Z}- \quad \rightarrow \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \quad \left( Z\ket{0} = \ket{0},\ Z\ket{1} = -\ket{1} \right)$

(b) <u>Hadamard gate</u>:

$-\boxed{H}- \quad \rightarrow \quad H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

$$H\ket{0} = \ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0} + \ket{1})$$
$$H\ket{1} = \ket{-} = \tfrac{1}{\sqrt{2}}(\ket{0} - \ket{1}).$$
