- **Example:** $n=2 \to \{\ket{0,0}, \ket{0,1}, \ket{1,0}, \ket{1,1}\}$

  $n=3 \to \{\ket{0,0,0}, \ket{0,0,1}, \ket{0,1,0}, \ket{0,1,1}, \ket{1,0,0}, \ket{1,0,1}, \ket{1,1,0}, \ket{1,1,1}\}.$

- Tensor product and inner product.

  By definition: $(\bra{v_1} \otimes \bra{v_2})(\ket{u_1} \otimes \ket{u_2}) = \braket{v_1|u_1} \cdot \braket{v_2|u_2}.$

  $$\braket{0,1,0|1,1,0} = \underbrace{\braket{0|1}}_{=0}\underbrace{\braket{1|1}}_{=1}\underbrace{\braket{0|0}}_{=1}$$

- **Example:** for basis vectors,
  $$\braket{0,1,0|1,0,1} = \underbrace{\braket{0|1}}_{=0} \cdot \underbrace{\braket{1|0}}_{=0} \cdot \underbrace{\braket{0|1}}_{=0} = 0.$$

  In general: for basis vectors $\ket{\vec{x}}, \ket{\vec{y}}$, $\vec{x} = (x_1, x_2, \ldots, x_n) \in \{0,1\}^n$
  $$\vec{y} = (y_1, y_2, \ldots, y_n) \in \{0,1\}^n$$

  $$\braket{\vec{x}|\vec{y}} = \delta_{\vec{x},\vec{y}} = \delta_{x_1,y_1}\,\delta_{x_2,y_2}\cdots \delta_{x_n,y_n}$$

- Probabilities: For a state of $n$ qubits given by

  $$\ket{\psi} = \sum_{\vec{x} \in \{0,1\}^n} c_{\vec{x}} \ket{\vec{x}} \to \text{Normalization condition is } \sum_{\vec{x} \in \{0,1\}^n} |c_{\vec{x}}|^2 = 1.$$

  Probabilities are: $\Pr[\vec{x}] = |c_{\vec{x}}|^2 = \braket{\vec{x}|\psi}$

## ③ Matrices: Linear Transformations of Vectors

(✱) Matrices will be used to define and describe states inside the Bloch sphere (i.e., mixed states) and the gates we can apply to qubits on a quantum computer.
