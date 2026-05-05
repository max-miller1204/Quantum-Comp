- <u>Conjugate Transpose of a Matrix:</u>

  - Recall for vectors: $\ket{v} = \begin{pmatrix} v_0 \\ v_1 \\ \vdots \\ v_{d-1} \end{pmatrix} \;\Rightarrow\; \bra{v} = \begin{pmatrix} \bar{v}_0 & \bar{v}_1 & \cdots & \bar{v}_{d-1} \end{pmatrix}$

    OR: $\ket{v} = \sum_{k=0}^{d-1} v_k \ket{k} \;\Rightarrow\; \bra{v} = \sum_{k=0}^{d-1} \bar{v}_k \bra{k}$.

  - Similar for matrices! $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \;\Rightarrow\; M^{\dagger} = \begin{pmatrix} \bar{a} & \bar{c} \\ \bar{b} & \bar{d} \end{pmatrix}$.   ($\dagger$ = "dagger")

  - In general: $M = \sum_{i,j=0}^{d-1} M_{i,j} \ket{i}\bra{j} \;\Rightarrow\; M^{\dagger} = \sum_{i,j=0}^{d-1} \overline{M_{i,j}} \ket{j}\bra{i}$

  $\circledast$ <u>Note:</u> $\big( \ket{i}\bra{j} \big)^{\dagger} = \ket{j}\bra{i}$.

  $\circledast$ A matrix $M$ is called <mark>Hermitian</mark> if $M^{\dagger} = M$.   $\;\to\; M_{i,j} = \overline{M_{j,i}}$

  $\quad M = \begin{pmatrix} a & b \\ \bar{b} & d \end{pmatrix}$, $\;\bar{a} = a,\; \bar{d} = d \;\;(a, d \in \mathbb{R})$

- <u>Inner Product and Orthonormal Bases of Matrices.</u>

  - Recall vector inner product: $\ket{u} = \sum_{k=0}^{d-1} u_k \ket{k}, \;\; \ket{v} = \sum_{k=0}^{d-1} v_k \ket{k}$

    $\Rightarrow \;\braket{u|v} = \Big( \sum_{k=0}^{d-1} \bar{u}_k \bra{k} \Big) \Big( \sum_{k=0}^{d-1} v_k \ket{k} \Big) = \sum_{k=0}^{d-1} \bar{u}_k v_k$

  - Matrix inner product: $\langle M_1, M_2 \rangle = \mathrm{Tr}\big[ M_1^{\dagger} M_2 \big]$, $\;\; \langle M_2, M_1 \rangle = \overline{\langle M_1, M_2 \rangle}$

    From this, we define a <u>norm for matrices</u>: $\| M \|_2 = \sqrt{\langle M, M \rangle} = \sqrt{\mathrm{Tr}[ M^{\dagger} M ]}$

  - Matrices $M_1, M_2$ are <u>orthogonal</u> if $\langle M_1, M_2 \rangle = 0$.
