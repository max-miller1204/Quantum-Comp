<u>Recall</u>: $\ket{V_1} = \begin{pmatrix} a_1 \\ b_1 \end{pmatrix}$, $\ket{V_2} = \begin{pmatrix} a_2 \\ b_2 \end{pmatrix}$ $\Rightarrow$ $\ket{V_1} \otimes \ket{V_2} = \begin{pmatrix} a_1 a_2 \\ a_1 b_2 \\ b_1 a_2 \\ b_1 b_2 \end{pmatrix} = \begin{pmatrix} a_1 \begin{pmatrix} a_2 \\ b_2 \end{pmatrix} \\ b_1 \begin{pmatrix} a_2 \\ b_2 \end{pmatrix} \end{pmatrix}$

$M_1 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix}$, $M_2 = \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix}$ $\Rightarrow$ $M_1 \otimes M_2 = \begin{pmatrix} a_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} & b_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} \\ c_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} & d_1 \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} \end{pmatrix}$

$= \begin{pmatrix} a_1 a_2 & a_1 b_2 & b_1 a_2 & b_1 b_2 \\ a_1 c_2 & a_1 d_2 & b_1 c_2 & b_1 d_2 \\ c_1 a_2 & c_1 b_2 & d_1 a_2 & d_1 b_2 \\ c_1 c_2 & c_1 d_2 & d_1 c_2 & d_1 d_2 \end{pmatrix}$

$\text{Tr}[M \otimes N] = \text{Tr}[N]\,\text{Tr}[M].$

$\langle M_1 \otimes M_2,\, N_1 \otimes N_2 \rangle = \langle M_1, N_1 \rangle \langle M_2, N_2 \rangle$

$\langle M, N \rangle = \text{Tr}(M^\dagger N).$

[Circuit diagram: three parallel wires labeled 1, 2, 3, each passing through a single-qubit gate $U_1$, $U_2$, $U_3$ respectively]  $\longleftrightarrow$  $U_1 \otimes U_2 \otimes U_3.$

[Circuit diagram: three input states $\ket{\psi_1}$, $\ket{\psi_2}$, $\ket{\psi_3}$ each entering gates $U_1$, $U_2$, $U_3$ respectively]  $\longleftrightarrow$  $(U_1 \otimes U_2 \otimes U_3)(\ket{\psi_1} \otimes \ket{\psi_2} \otimes \ket{\psi_3})$

$\qquad\qquad = U_1\ket{\psi_1} \otimes U_2\ket{\psi_2} \otimes U_3\ket{\psi_3}.$
