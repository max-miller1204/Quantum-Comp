⊛ We also call matrices <u>linear operators / transformations</u>.

– <u>2×2 matrices</u>:  $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $a,b,c,d \in \mathbb{C}$.

- Multiplying a matrix with a vector: $\ket{v} = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}$

$$M\ket{v} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} av_1 + bv_2 \\ cv_1 + dv_2 \end{pmatrix}$$

- Matrices act linearly as follows:  $M(\alpha \ket{v_1} + \beta \ket{v_2}) = \underline{\alpha M \ket{v_1} + \beta M \ket{v_2}}$

$$= \begin{pmatrix} \alpha a & \alpha b \\ \alpha c & \alpha d \end{pmatrix}$$

- Matrix multiplication: $M_1 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix}$, $M_2 = \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix}$

$$M_1 \cdot M_2 = \begin{pmatrix} a_1 & b_1 \\ c_1 & d_1 \end{pmatrix} \begin{pmatrix} a_2 & b_2 \\ c_2 & d_2 \end{pmatrix} = \begin{pmatrix} a_1 a_2 + b_1 c_2 & a_1 b_2 + b_1 d_2 \\ c_1 a_2 + d_1 c_2 & c_1 b_2 + d_1 d_2 \end{pmatrix}$$

- Abstract notation from vectors extends to matrices!

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + b\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} + c\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} + d\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

⊛ <u>Recall</u>:  $\ket{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $\ket{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$ → $\bra{0} = (1\ 0)$, $\bra{1} = (0\ 1)$

⊛ <u>Observe</u>: $\ket{0}\bra{0} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}(1\ 0) = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $\ket{0}\bra{1} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}(0\ 1) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$

$\underbrace{\phantom{xx}}_{2\times 1}\underbrace{\phantom{xx}}_{1\times 2}$
