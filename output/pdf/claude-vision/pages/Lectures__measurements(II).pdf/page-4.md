② <u>Partial Measurements: Measuring Only Some Qubits</u>

[Circuit diagram: 6 input qubits $\ket{x_1}, \ket{x_2}, \ket{x_3}, \ket{x_4}, \ket{x_5}, \ket{x_6}$ enter from the left. Three layers of two-qubit gates (boxes) are applied. After the 3rd layer, the 1st, 3rd, and 5th qubits are measured (shown as red measurement boxes outputting $x$). Dashed vertical lines separate 1st layer, 2nd layer, 3rd layer. Time axis points to the right.]

$(x_1, x_3, x_4, x_5, x_6) \in \{0,1\}^6$

✺ Suppose we only measure the 1st, 3rd, and 5th qubits.

— To get the measurement outcome probabilities, we apply the measurement operators only on the relevant qubits.

✺ <u>Notation</u>: States and operators for multiple qubits and qudits.

- For two qubits, the standard basis is $\{\ket{0}\otimes\ket{0}, \ket{0}\otimes\ket{1}, \ket{1}\otimes\ket{0}, \ket{1}\otimes\ket{1}\}$
  
  $\equiv \ket{0,0}, \equiv \ket{0,1}, \equiv \ket{1,0}, \equiv \ket{1,1}$
  
  [arrows pointing to first factor: "1st qubit"; second factor: "2nd qubit"]

  We often <u>label</u> the qubits by $A, B, C, \dots$

  So we write $\ket{0,0}_{AB} \equiv \ket{0}_A \otimes \ket{0}_B$.
  
  ["qubit A", "qubit B"]
  
  $\rightarrow$ For state vector $\ket{\psi}_{AB} \in \mathbb{C}^2 \otimes \mathbb{C}^2$
  
  [arrows: "qubit A", "qubit B"]

  $\ket{\psi}_{AB} = a\ket{0,0}_{AB} + b\ket{0,1}_{AB} + c\ket{1,0}_{AB} + d\ket{1,1}_{AB}$.

- Similar for three or more qubits: $\ket{\psi}_{ABC} = \sum_{\vec{x} \in \{0,1\}^3} c_{\vec{x}} \ket{\vec{x}}_{ABC}$
  
  $\ket{\vec{x}}_{ABC} \equiv \ket{x_1, x_2, x_3}_{ABC}$
