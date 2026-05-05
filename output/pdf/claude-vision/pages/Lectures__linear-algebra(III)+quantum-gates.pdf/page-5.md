- We have bases for matrices as well! $\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

Example: $d=2$, recall $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} = a\ket{0}\bra{0} + b\ket{0}\bra{1} + c\ket{1}\bra{0} + d\ket{1}\bra{1}.$

$\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} \quad \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$

The set $\{\ket{0}\bra{0}, \ket{0}\bra{1}, \ket{1}\bra{0}, \ket{1}\bra{1}\}$ is an orthonormal basis for $L(\mathbb{C}^2)$.

↳ Observe: there are $4 = 2^2$ elements! $\quad \langle B_i, B_j \rangle = \delta_{i,j}$

Check: take inner products!

$\langle \ket{0}\bra{0}, \ket{0}\bra{1} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{0})^\dagger (\ket{0}\bra{1}) \right] = \mathrm{Tr}\left[ \ket{0}\underbrace{\braket{0|0}}_{=1}\bra{1} \right] = \mathrm{Tr}\left[ \ket{0}\bra{1} \right] = \braket{1|0} = 0.$

$\langle \ket{0}\bra{1}, \ket{1}\bra{0} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{1})^\dagger \ket{1}\bra{0} \right] = \mathrm{Tr}\left[ \ket{1}\underbrace{\braket{0|1}}_{=0}\bra{0} \right] = 0.$

$\langle \ket{0}\bra{0}, \ket{0}\bra{0} \rangle = \mathrm{Tr}\left[ (\ket{0}\bra{0})^\dagger \ket{0}\bra{0} \right] = \mathrm{Tr}\left[ \ket{0}\underbrace{\braket{0|0}}_{=1}\bra{0} \right] = \mathrm{Tr}\left[ \ket{0}\bra{0} \right] = \braket{0|0} = 1$

In general: $\langle \ket{i}\bra{j}, \ket{k}\bra{\ell} \rangle = \mathrm{Tr}\left[ (\ket{i}\bra{j})^\dagger \ket{k}\bra{\ell} \right] = \mathrm{Tr}\left[ \ket{j}\underbrace{\braket{i|k}}_{=\delta_{i,k}}\bra{\ell} \right]$

$= \delta_{i,k}\, \mathrm{Tr}\left[ \ket{j}\bra{\ell} \right] = \delta_{i,k} \braket{\ell|j} = \delta_{i,k}\, \delta_{j,\ell}$

(★) Holds for arbitrary dimension! $\{\ket{i}\bra{j} : i,j \in \{0,1,\ldots,d-1\}\}$ is an orthonormal basis for $L(\mathbb{C}^d)$.

- Special basis for $d=2$: <u>Pauli Matrices</u> (aka Pauli gates).

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

$\mathrm{Tr}[X] = \mathrm{Tr}[Y] = \mathrm{Tr}[Z] = 0$

↳ <u>Bit-flip matrix</u>: $X\ket{0} = \ket{1}, \; X\ket{1} = \ket{0}.$

$X^2 = \mathbb{1}, \; Y^2 = \mathbb{1}, \; Z^2 = \mathbb{1}.$

$\mathrm{Tr}(X^\dagger X) = 2 = \mathrm{Tr}[Y^\dagger Y] = \mathrm{Tr}[Z^\dagger Z]$
