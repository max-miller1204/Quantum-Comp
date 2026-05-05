$$\ket{1}\bra{0} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad \ket{1}\bra{1} = \begin{pmatrix} 0 \\ 1 \end{pmatrix}\begin{pmatrix} 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

Then $\;M = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}\quad$ $\begin{aligned} a &= \braket{0|M|0}, & c &= \braket{1|M|0} \\ b &= \braket{0|M|1}, & d &= \braket{1|M|1} \end{aligned}$

This makes multiplication easier! (No need to remember matrix multiplication rules).

$$M\ket{v} = \big(a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}\big)\big(v_1\ket{0} + v_2\ket{1}\big)$$

$$= av_1\underbrace{\ket{0}\braket{0|0}}_{1} + av_2\ket{0}\underbrace{\braket{0|1}}_{0} + bv_1\ket{0}\underbrace{\braket{1|0}}_{0} + bv_2\underbrace{\ket{0}\braket{1|1}}_{1}$$

$$\quad + cv_1\underbrace{\ket{1}\braket{0|0}}_{1} + cv_2\ket{1}\underbrace{\braket{0|1}}_{0} + dv_1\ket{1}\underbrace{\braket{1|0}}_{0} + dv_2\underbrace{\ket{1}\braket{1|1}}_{1}$$

$$= (av_1 + bv_2)\ket{0} + (cv_1 + dv_2)\ket{1}$$

$$= \begin{pmatrix} av_1 + bv_2 \\ cv_1 + dv_2 \end{pmatrix} \checkmark \quad (\text{just as before!})$$

- **Arbitrary $d \times d$ matrices:**

$$M = \sum_{i,j=0}^{d-1} M_{i,j}\,\ket{i}\bra{j}$$

$\uparrow$ entry in the $i^{\text{th}}$ row and $j^{\text{th}}$ column. (complex number)

$$\braket{k|M|\ell} = \bra{k}\left(\sum_{i,j=0}^{d-1} M_{i,j}\,\ket{i}\bra{j}\right)\ket{\ell}$$

$$= \sum_{i,j=0}^{d-1} M_{i,j}\,\underbrace{\braket{k|i}}_{\delta_{k,i}}\underbrace{\braket{j|\ell}}_{\delta_{j,\ell}} = M_{k,\ell}$$

$$M_1 = \sum_{i,j=0}^{d-1} M^{(1)}_{i,j}\,\ket{i}\bra{j} \qquad M_2 = \sum_{i,j=0}^{d-1} M^{(2)}_{i,j}\,\ket{i}\bra{j}$$

$$M_1 \cdot M_2 = \left(\sum_{i_1,j_1=0}^{d-1} M^{(1)}_{i_1,j_1}\,\ket{i_1}\bra{j_1}\right)\left(\sum_{i_2,j_2=0}^{d-1} M^{(2)}_{i_2,j_2}\,\ket{i_2}\bra{j_2}\right)$$

$$= \sum_{i_1,j_1=0}^{d-1}\sum_{i_2,j_2=0}^{d-1} M^{(1)}_{i_1,j_1} M^{(2)}_{i_2,j_2}\,\ket{i_1}\underbrace{\braket{j_1|i_2}}_{\delta_{j_1,i_2}}\bra{j_2} = \sum_{i_1,j_2=0}^{d-1}\left(\sum_{j_1=0}^{d-1} M^{(1)}_{i_1,j_1} M^{(2)}_{j_1,j_2}\right)\ket{i_1}\bra{j_2}$$
