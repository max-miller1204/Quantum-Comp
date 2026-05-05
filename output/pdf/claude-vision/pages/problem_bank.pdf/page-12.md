7. Consider the following state vectors. Determine the probabilities for obtaining the outcomes "0" and "1".

   (a) $\ket{\psi} = \left(\frac{1}{5} + \frac{2i}{3}\right)\ket{0} + \left(\frac{4}{15} + \frac{2i}{3}\right)\ket{1}$
   
   (b) $\ket{\psi} = \left(\frac{1}{3} + \frac{2i}{5}\right)\ket{0} + \left(\frac{8}{15} + \frac{2i}{3}\right)\ket{1}$
   
   (c) $\ket{\psi} = \left(\frac{2}{25} + \frac{8i}{75}\right)\ket{0} + \left(\frac{1}{3} + \frac{14i}{15}\right)\ket{1}$
   
   (d) $\ket{\psi} = \left(\frac{3}{25} + \frac{38i}{75}\right)\ket{0} + \left(\frac{8}{15} + \frac{2i}{3}\right)\ket{1}$

8. Two qubits are in the state given by the vector

$$\frac{i}{\sqrt{10}}\ket{0,0} + \frac{1-2i}{\sqrt{10}}\ket{0,1} + \frac{e^{i\pi/100}}{\sqrt{10}}\ket{1,0} + \frac{\sqrt{3}}{\sqrt{10}}\ket{1,1}. \tag{54}$$

   If we measure the qubits in the two-qubit $Z$-basis $\{\ket{0,0},\ket{0,1},\ket{1,0},\ket{1,1}\}$, what are the possible measurement outcomes and their associated probabilities?

9. Determine whether or not the following density matrices represent pure states. Then, write each density matrix with respect to the Pauli basis, i.e., determine the coefficients $r_X, r_Y, r_Z \in \mathbb{R}$ such that $\rho = \frac{1}{2}(\mathbb{1} + r_X X + r_Y Y + r_Z Z)$.

   (a) $\rho = \begin{pmatrix} \frac{5}{13} & \frac{3+2i}{13} \\ \frac{3-2i}{13} & \frac{8}{13} \end{pmatrix}$
   
   (b) $\rho = \begin{pmatrix} \frac{109}{225} & \frac{112}{225} + \frac{2i}{45} \\ \frac{112}{225} - \frac{2i}{45} & \frac{116}{225} \end{pmatrix}$
   
   (c) $\rho = \begin{pmatrix} \frac{377}{1125} & \frac{2422+824i}{5625} \\ \frac{2422-824i}{5625} & \frac{748}{1125} \end{pmatrix}$
   
   (d) $\rho = \begin{pmatrix} \frac{4}{225} & \frac{142-44i}{1125} \\ \frac{142+44i}{1125} & \frac{221}{225} \end{pmatrix}$

10. Prove that every Hermitian operator has real eigenvalues.

11. Prove that a linear operator $M \in \mathrm{L}(\mathbb{C}^2)$, decomposed as $M = \frac{1}{2}(c_0 \mathbb{1} + c_1 X + c_2 Y + c_3 Z)$ in the Pauli basis, is Hermitian if and only if the coefficients $c_0, c_1, c_2, c_3$ are all real-valued.

12. Let $M \in \mathrm{L}(\mathbb{C}^d)$ be an arbitrary linear operator. Prove that $M$ can be decomposed as follows:

$$M = H_1 + iH_2, \tag{55}$$

    where

$$H_1 = \frac{1}{2}(M + M^\dagger), \quad H_2 = \frac{1}{2i}(M - M^\dagger). \tag{56}$$

    Verify that $H_1$ and $H_2$ are Hermitian.

13. Let $U \in \mathrm{L}(\mathbb{C}^d)$ be a unitary operator, and let $\ket{v_1}, \ket{v_2} \in \mathbb{C}^d$ be arbitrary vectors. Prove that $\braket{Uv_1|Uv_2} = \braket{v_1|v_2}$.

12
