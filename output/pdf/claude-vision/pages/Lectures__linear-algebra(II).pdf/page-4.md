$$= \frac{1}{\||v\rangle\|^2} \underbrace{\sum_{k=0}^{d-1} |a_k|^2}_{= \||v\rangle\|^2}$$

$$= \frac{1}{\||v\rangle\|^2} \cdot \||v\rangle\|^2$$

$$= 1 \checkmark$$

- **Tensor product of vectors**: Used to describe the state of multiple qubits. (and entanglement!).

  - One qubit: 2-dimensional vector: $|\psi\rangle = \begin{pmatrix} \alpha \\ \beta \end{pmatrix}$.

  - If qubit 1 has state $|\psi_1\rangle$ and qubit 2 has state $|\psi_2\rangle$, then the **joint state** is given by

$$|\psi_1\rangle \otimes |\psi_2\rangle = \underbrace{\begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}}_{|\psi_1\rangle} \otimes \underbrace{\begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix}}_{|\psi_2\rangle} = \begin{pmatrix} \alpha_1 \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix} \\ \beta_1 \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} \alpha_1 \alpha_2 \\ \alpha_1 \beta_2 \\ \beta_1 \alpha_2 \\ \beta_1 \beta_2 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

(4-dimensional vector!)

$\underset{\color{red}\text{tensor/Kronecker product}}{\color{red}\uparrow}$

⊛ **Abstract notation**: $|\psi_1\rangle = \alpha_1|0\rangle + \beta_1|1\rangle,\ |\psi_2\rangle = \alpha_2|0\rangle + \beta_2|1\rangle$

$$\Rightarrow |\psi_1\rangle \otimes |\psi_2\rangle = \big(\alpha_1|0\rangle + \beta_1|1\rangle\big) \otimes \big(\alpha_2|0\rangle + \beta_2|1\rangle\big)$$

[red arrows indicate distributing the tensor product across all four cross-terms]

$$= \alpha_1\alpha_2 |0\rangle\otimes|0\rangle + \alpha_1\beta_2 |0\rangle\otimes|1\rangle + \beta_1\alpha_2 |1\rangle\otimes|0\rangle + \beta_1\beta_2 |1\rangle\otimes|1\rangle$$

**Recall:** $|0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix},\ |1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} \Rightarrow \underline{|0\rangle\otimes|0\rangle} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix};\ \underline{|0\rangle\otimes|1\rangle} = \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix}$
