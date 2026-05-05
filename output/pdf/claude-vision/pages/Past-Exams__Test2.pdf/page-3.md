**TOTAL: [40]**

3. (a) Given any orthonormal basis $\{\ket{e_k}\}_{k=1}^d$ for $\mathbb{C}^d$, prove that $\mathbb{1}_d = \sum_{k=1}^d \ket{e_k}\bra{e_k}$.

   (b) Let $\{\ket{e_k}\}_{k=1}^d$ and $\{\ket{f_k}\}_{k=1}^d$ be two orthonormal bases for $\mathbb{C}^d$. Prove that $U = \sum_{k=1}^d \ket{e_k}\bra{f_k}$ is a unitary operator.

[-10]

a) orthogonal: $\braket{V_1 | V_2} = 0$

   normal: $\braket{V_1 | V_1} = 1$ OR $\braket{V_2 | V_2} = 1$

   $\braket{0|1} = \begin{pmatrix} 1 & 0 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = 0$

   $\braket{1|1} = \begin{pmatrix} 0 & 1 \end{pmatrix}\begin{pmatrix} 0 \\ 1 \end{pmatrix} = 1$

   $I_d = \sum_{k=1}^d \ket{e_k}\bra{e_k}$

   $I^2 = \bra{e_k} \sum_{k=1}^d \ket{e_k}$

   $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} =$

b) $U^\dagger U = I$

   $U^\dagger = \sum_{k=1}^d \overline{f_k}\ket{e_k}$ \qquad $U = \sum_{k=1}^d \ket{e_k}\bra{f_k}$

   $\sum_{k=1}^d \sum_{k=1}^d \overline{f_k}\ket{f_k} \, \bra{e_k}\ket{e_k} = 1 \cdot I = I$
   
   $\qquad\qquad\qquad\downarrow \qquad\qquad \downarrow$
   $\qquad\qquad\quad = I \qquad\quad = 1$

4
