① <u>Recap: Quantum Gates</u>

- Quantum gates describe how the states of qubits evolve — Similar to classical logic gates like AND, OR, NOT.

- Composing gates leads to <u>circuits</u>, which are used to describe quantum computations.

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left, passing through 3 layers of gates (1st layer, 2nd layer, 3rd layer) separated by dashed vertical lines, ending in measurement read-outs $D \rightsquigarrow x_1', x_2', x_3', x_4', x_5', x_6'$ on the right. Below: $(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$. Arrow labeled "time" pointing right. The measurements are labeled "Measurement/read-out".]

- Mathematically, quantum gates are described by <u>unitary matrices/operators</u> $U^\dagger U = U U^\dagger = \mathbb{1}$. They are <u>norm and trace preserving</u>. They describe <u>basis changes</u>.

  $\ket{\psi} \to U\ket{\psi} \to \|U\ket{\psi}\| = \|\ket{\psi}\|$  $\quad \{U\ket{k}\}_{k=0}^{d-1}$

  $\rho \to U\rho U^\dagger \to \mathrm{Tr}(U\rho U^\dagger) = \mathrm{Tr}(\rho)$.

- <u>Examples</u>:

  - <u>Pauli gates</u>:
  
    $-\boxed{X}- \quad \to \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \quad \left( X\ket{0} = \ket{1},\ X\ket{1} = \ket{0} \right)$

    $-\boxed{Y}- \quad \to \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} \quad \left( Y\ket{0} = i\ket{1},\ Y\ket{1} = -i\ket{0} \right)$

    $-\boxed{Z}- \quad \to \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \quad \left( Z\ket{0} = \ket{0},\ Z\ket{1} = -\ket{1} \right)$
