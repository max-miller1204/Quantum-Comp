- **Quantum Circuits and Gates**: very similar! But the gates act on the complex vector space $(\mathbb{C}^2)^{\otimes n}$ of $n$ qubits ⟶ they are represented by <mark>unitary matrices</mark>. ⟶ matrix $U \in L(\mathbb{C}^d)$ satisfying $U^\dagger U = U U^\dagger = \mathbb{1}$.

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ on the left, passing through 3 layers of gate boxes (1st layer, 2nd layer, 3rd layer separated by dashed vertical lines), with measurement/read-out on the right giving outputs $\sim x_1', x_2', x_3', x_4', x_5', x_6'$. Time flows left to right. Inputs satisfy $(x_1, x_2, x_3, x_4, x_5, x_6) \in \{0,1\}^6$.]

- ✸ Each box represents a gate / unitary matrix.
- ✸ Multiply the gates to get a unitary matrix for the full circuit.

✸ Why unitary matrix? Comes from quantum physics (Schrödinger equation).

✸ To understand what the circuit does, we just have to know how it acts on basis vectors!

<u>Recall</u>: any state vector of $n$ qubits can be represented as

$$\ket{\psi} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}}, \quad c_{\vec{x}} \in \mathbb{C}, \quad \sum_{\vec{x} \in \{0,1\}^n} |c_{\vec{x}}|^2 = 1.$$

$$\left( \begin{array}{l} \vec{x} \equiv (x_1, x_2, \ldots, x_n), \; x_i \in \{0,1\} \\ \ket{\vec{x}} \equiv \ket{x_1, x_2, \ldots, x_n} \\ \quad\quad = \ket{x_1} \otimes \ket{x_2} \otimes \cdots \otimes \ket{x_n} \end{array} \right)$$

↳ input state of the quantum circuit.

$$\Rightarrow U \ket{\psi} = U \left( \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}} \right) = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \, \underline{U \ket{\vec{x}}}.$$

$\left( \text{✸ Linearity of matrices: } M(\alpha \ket{v_1} + \beta \ket{v_2}) = \alpha M \ket{v_1} + \beta M \ket{v_2} \right).$
