✺ These basis vectors are __orthonormal__

Two parts to this term:

1. __Orthogonal__: $\langle \vec{e}_i, \vec{e}_j \rangle = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$

   $\equiv \delta_{i,j} \rightarrow$ "Kronecker delta"

2. __Normalised__: $\|\vec{e}_k\| = \sqrt{\langle \vec{e}_k, \vec{e}_k \rangle} = 1$ for all $k$.

[Right side, in blue:]
$d = 3 \rightarrow \vec{e}_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix},\ \vec{e}_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$

$\vec{e}_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$

$\langle \vec{e}_1, \vec{e}_2 \rangle = (1\ 0\ 0) \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} = 0$

$\langle \vec{e}_1, \vec{e}_1 \rangle = (1\ 0\ 0) \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} = 1$

✺ We can extract the components of a vector in this basis using the inner product:

$$\langle \vec{e}_k, \vec{v} \rangle = \left\langle \vec{e}_k, \sum_{\ell=1}^{d} a_\ell \vec{e}_\ell \right\rangle = \sum_{\ell=1}^{d} \underbrace{\langle \vec{e}_k, \vec{e}_\ell \rangle}_{\delta_{k,\ell}} a_\ell = a_k.$$

[Right side, in blue:]
$\langle \vec{e}_1, a_1 \vec{e}_1 + a_2 \vec{e}_2 \rangle$
$= a_1 \underbrace{\langle \vec{e}_1, \vec{e}_1 \rangle}_{=1} + a_2 \underbrace{\langle \vec{e}_1, \vec{e}_2 \rangle}_{=0}$
$= a_1$

— __Bra-ket notation__: very important, used throughout quantum information and quantum computing.

$\vec{v}_1 = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_d \end{pmatrix} \rightarrow \vec{v}_1^\dagger = \begin{pmatrix} \bar{a}_1 & \bar{a}_2 & \cdots & \bar{a}_d \end{pmatrix}$

[Blue annotations:]
$|v_1\rangle$, $|v_1\rangle = \sum_{k=1}^{d} a_k |e_k\rangle$, $|e_1\rangle = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix}$

[Red annotations:]
relabel as $|v_1\rangle \rightarrow$ call it a "ket".

relabel as $\langle v_1 | \rightarrow$ call it "bra"

- Then the inner product is $\langle \vec{v}_1, \vec{v}_2 \rangle = \vec{v}_1^\dagger \vec{v}_2 = \langle v_1 | v_2 \rangle$

  [Red:] "bra-ket"

[Bottom right:] $\delta_{k,k'}$
