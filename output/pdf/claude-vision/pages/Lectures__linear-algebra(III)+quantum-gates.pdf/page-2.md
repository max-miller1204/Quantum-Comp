⊛ <u>Notation</u>: $L(\mathbb{C}^d) \equiv$ set of all matrices/linear operators acting on $\mathbb{C}^d$ (i.e., $d \times d$ matrices) (dimension is $d^2$.)

- For any vector $\ket{v} \in \mathbb{C}^d$, $\ket{v}\bra{v} \in L(\mathbb{C}^d)$ is a $d \times d$ matrix.

$$\ket{v} = \sum_{k=0}^{d-1} v_k \ket{k} \implies \ket{v}\bra{v} = \left(\sum_{k=0}^{d-1} v_k \ket{k}\right)\left(\sum_{k'=0}^{d-1} \overline{v_{k'}} \bra{k'}\right) = \sum_{k,k'=0}^{d-1} v_k \overline{v_{k'}} \ket{k}\bra{k'}.$$

- <u>Identity matrix</u>: $\mathbb{1} \to \mathbb{1}\ket{v} = \ket{v}$ for all $\ket{v} \in \mathbb{C}^d$.

$$\mathbb{1} = \begin{pmatrix} 1 & & 0 \\ & 1 & \\ & & \ddots \\ 0 & & & 1 \end{pmatrix} = \sum_{k=0}^{d-1} \ket{k}\bra{k} \quad \overset{M_{ij} = \delta_{ij}}{\to} \quad \text{For any orthonormal basis } \{\ket{e_k}\}_{k=1}^d : \mathbb{1} = \sum_{k=1}^d \ket{e_k}\bra{e_k}.$$

- <u>Trace of a Matrix</u>: Sum of the diagonal elements.

$$M = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \to \text{Tr}[M] = a + d = \bra{0}M\ket{0} + \bra{1}M\ket{1}.$$

In general: $M = \sum_{i,j=0}^{d-1} M_{ij} \ket{i}\bra{j} \implies \text{Tr}[M] = \sum_{i=0}^{d-1} M_{i,i} = \sum_{i=0}^{d-1} \bra{i}M\ket{i}.$

⊛ Consider a state vector $\ket{\psi} = \alpha\ket{0} + \beta\ket{1} \implies \bra{\psi} = \overline{\alpha}\bra{0} + \overline{\beta}\bra{1}$, $|\alpha|^2 + |\beta|^2 = 1$.

$$\implies \ket{\psi}\bra{\psi} = (\alpha\ket{0} + \beta\ket{1})(\overline{\alpha}\bra{0} + \overline{\beta}\bra{1}) = \alpha\overline{\alpha}\ket{0}\bra{0} + \alpha\overline{\beta}\ket{0}\bra{1} + \beta\overline{\alpha}\ket{1}\bra{0} + \beta\overline{\beta}\ket{1}\bra{1}$$

$$= |\alpha|^2 \ket{0}\bra{0} + \alpha\overline{\beta}\ket{0}\bra{1} + \beta\overline{\alpha}\ket{1}\bra{0} + |\beta|^2 \ket{1}\bra{1} = \begin{pmatrix} |\alpha|^2 & \alpha\overline{\beta} \\ \beta\overline{\alpha} & |\beta|^2 \end{pmatrix}$$

$\hookrightarrow |\alpha|^2 = \Pr[0]$
$\quad\;\; |\beta|^2 = \Pr[1]$

Now take the trace: $\text{Tr}[\ket{\psi}\bra{\psi}] = |\alpha|^2 + |\beta|^2 = 1.$

In general: $\text{Tr}[\ket{v}\bra{v}] = \braket{v|v}$ for all $\ket{v} \in \mathbb{C}^d$.
