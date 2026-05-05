# Quantum mechanics

1. Draw a Bloch sphere and label the following locations:
    (a) Where a qubit is exactly $\ket{0}$.
    (b) Where a qubit is exactly $\ket{1}$.
    (c) Where a qubit is half $\ket{0}$ and half $\ket{1}$.
    (d) Where a qubit is more $\ket{0}$ than $\ket{1}$.
    (e) Where a qubit is more $\ket{1}$ then $\ket{0}$.

2. Prove that the Pauli operators are orthogonal to each other; specifically, $\mathrm{Tr}[XY] = 0$, $\mathrm{Tr}[XZ] = 0$, and $\mathrm{Tr}[YZ] = 0$, where we recall that the Pauli operators are
$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -\mathrm{i} \\ \mathrm{i} & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}. \tag{47}$$

3. Define the Bell state vector
$$\ket{\Phi} = \frac{1}{\sqrt{2}}\big(\ket{0,0} + \ket{1,1}\big) = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \frac{1}{\sqrt{2}} \end{pmatrix}. \tag{48}$$

    Prove that
$$\frac{1}{4}\big(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X - Y \otimes Y + Z \otimes Z\big) = \ket{\Phi}\bra{\Phi} = \begin{pmatrix} \tfrac{1}{2} & 0 & 0 & \tfrac{1}{2} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ \tfrac{1}{2} & 0 & 0 & \tfrac{1}{2} \end{pmatrix}. \tag{49}$$

4. Prove that
$$\frac{1}{2}\big(\mathbb{1}_2 \otimes \mathbb{1}_2 + X \otimes X + Y \otimes Y + Z \otimes Z\big) = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}. \tag{50}$$

5. Consider an operator $M \in \mathrm{L}(\mathbb{C}^2)$ decomposed in the Pauli basis as $M = \tfrac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$.

    (a) Verify that
$$c_0 = \mathrm{Tr}[M], \quad c_1 = \mathrm{Tr}[XM], \quad c_2 = \mathrm{Tr}[YM], \quad c_3 = \mathrm{Tr}[ZM]. \tag{51}$$

    (b) Verify that the Hilbert–Schmidt norm of $M$ is $\|M\|_{\mathrm{HS}} = \sqrt{\tfrac{1}{2}\big(|c_0|^2 + |c_1|^2 + |c_2|^2 + |c_3|^2\big)}$.

6. Consider an arbitrary $2 \times 2$ matrix as follows:
$$M = \begin{pmatrix} p & q \\ r & s \end{pmatrix}, \quad p, q, r, s \in \mathbb{C}. \tag{52}$$

    Show that
$$\mathrm{Tr}[M] = p + s, \quad \mathrm{Tr}[XM] = q + r, \quad \mathrm{Tr}[YM] = \mathrm{i}(q - r), \quad \mathrm{Tr}[ZM] = p - s. \tag{53}$$

11
