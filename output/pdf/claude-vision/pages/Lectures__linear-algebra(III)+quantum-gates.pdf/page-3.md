**Proof:** Just use the definition!

$$\mathrm{Tr}(\ket{v}\bra{v}) = \sum_{k=0}^{d-1} \bra{k}\ket{v}\bra{v}\ket{k} = \sum_{k=0}^{d-1} \braket{v|k}\braket{k|v} = \bra{v}\left(\sum_{k=0}^{d-1} \ket{k}\bra{k}\right)\ket{v} = \braket{v|v}. \blacksquare$$

[annotation: $\bra{v}\mathbb{1}\ket{v}$, with $\sum_{k=0}^{d-1}\ket{k}\bra{k} = \mathbb{1}$]

**Similarly:** $\mathrm{Tr}\big[M\ket{v_1}\bra{v_2}\big] = \braket{v_2|M|v_1}$ for all $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$, $M \in L(\mathbb{C}^d)$.

**Proof:** 
$$\mathrm{Tr}\big[M\ket{v_1}\bra{v_2}\big] = \sum_{k=0}^{d-1}\bra{k}M\ket{v_1}\braket{v_2|k} = \sum_{k=0}^{d-1}\braket{v_2|k}\bra{k}M\ket{v_1} = \bra{v_2}\left(\sum_{k=0}^{d-1}\ket{k}\bra{k}\right)M\ket{v_1}$$

$$= \braket{v_2|M|v_1}. \blacksquare \qquad\qquad = \bra{v_2}\underbrace{\mathbb{1}\cdot M}_{=M}\ket{v_1}$$

[annotation: $\mathbb{1}\ket{v} = \ket{v}$, $\mathbb{1}\cdot M = M$]

---

- **Transpose of a matrix:** flip the rows and columns.

- $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \;\rightarrow\; M^T = \begin{pmatrix} a & c \\ b & d \end{pmatrix}$

- ⊛ **Note:** $\big(\ket{i}\bra{j}\big)^T = \ket{j}\bra{i}.$ $\qquad \underline{(M_1 + M_2)^T = M_1^T + M_2^T}$

- **In general:** $M = \sum_{i,j=0}^{d-1} m_{i,j}\ket{i}\bra{j} \;\Rightarrow\; M^T = \sum_{i,j=0}^{d-1} m_{i,j}\ket{j}\bra{i}$

$$M^T = \left(\sum_{i,j=0}^{d-1} m_{i,j}\ket{i}\bra{j}\right)^T = \sum_{i,j=0}^{d-1} m_{i,j}\big(\ket{i}\bra{j}\big)^T$$

- ⊛ A matrix $M$ is called **symmetric** if $M^T = M$.

$$M^T = M \;\rightarrow\; m_{i,j} = m_{j,i}$$
