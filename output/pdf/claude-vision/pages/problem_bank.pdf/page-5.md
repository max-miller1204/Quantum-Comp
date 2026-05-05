(b) Using (a), prove that $\{\ket{\psi_j}\}_{j=1}^d$ is a basis for $\mathbb{C}^d$. In other words, prove that every vector $\ket{\phi} \in \mathbb{C}^d$ can be written as a unique linear combination of the vectors $\ket{\psi_j}$. We thus have that every set of $d$ linearly independent vectors in $\mathbb{C}^d$ is a basis for $\mathbb{C}^d$.

(c) Prove that if $\sum_{j=1}^d \ket{\psi_j}\bra{\psi_j} = \mathbb{1}_d$, then $\{\ket{\psi}_j\}_{j=1}^d$ is an orthonormal basis for $\mathbb{C}^d$.

By combining this result with (57), we have that a linearly independent set $\{\ket{\psi_j}\}_{j=1}^d$ of vectors in $\mathbb{C}^d$ is an orthonormal basis if and only if $\sum_{j=1}^d \ket{\psi_j}\bra{\psi_j} = \mathbb{1}_d$.

16. ★ Let $\{B_j\}_{j=1}^{d^2}$ be an orthonormal basis for $\mathrm{L}(\mathbb{C}^d)$, with $d \in \{2, 3, \dots\}$.

   (a) Prove that
   $$\sum_{j=1}^{d^2} \overline{B_j} \otimes B_j = \Gamma_d, \tag{21}$$
   where $\Gamma_d = \ket{\Gamma_d}\bra{\Gamma_d} = \sum_{i,j=0}^{d-1} \ket{i,i}\bra{j,j}$. Similarly, prove that
   $$\sum_{j=1}^{d^2} B_j^\dagger \otimes B_j = F, \tag{22}$$
   where $F = \sum_{i,j=0}^{d-1} \ket{i,j}\bra{j,i}$.

   (*Hint*: Start by verifying that $\{\overline{B_j}\}_{j=1}^{d^2}$ is an orthonormal basis for $\mathrm{L}(\mathbb{C}^d)$. Then, use the fact that every linear operator $Z \in \mathrm{L}(\mathbb{C}^d \otimes \mathbb{C}^d)$ can be written as $Z = \sum_{j,k=1}^{d^2} c_{j,k} \overline{B_j} \otimes B_k$ for some coefficients $c_{j,k} \in \mathbb{C}$.)

   (b) Prove that for $M \in \mathrm{L}(\mathbb{C}^d)$,
   $$\sum_{j=1}^{d^2} B_j M B_j^\dagger = \mathrm{Tr}[M] \mathbb{1}_d. \tag{23}$$
   (*Hint*: Use (18), (19), and (21).)

   (c) Prove that $\{\ket{B_j}\!\rangle\}_{j=1}^{d^2}$ is an orthonormal basis for $\mathbb{C}^d \otimes \mathbb{C}^d$.

17. ★ Let $\{\ket{\psi_j}\}_{j=0}^{d-1}$ be a set of linearly independent, normalized, but non-orthogonal vectors in $\mathbb{C}^d$, with $d \in \{2, 3, \dots\}$. We would like to transform these vectors into a new set $\{\ket{\phi_j}\}_{j=0}^{d-1}$ of orthonormal vectors via an invertible linear operator $Q$, such that $\ket{\phi_j} = Q\ket{\psi_j}$ for all $j \in \{0, 1, \dots, d-1\}$.

   (a) Prove that the operator $S$ defined as
   $$S := \sum_{j=0}^{d-1} \ket{\psi_j}\bra{\psi_j} \tag{24}$$
   is invertible and positive definite. (*Hint*: Write $S$ in terms of the operator $T$ defined in (20).)

5
