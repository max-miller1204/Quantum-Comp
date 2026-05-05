12. Let $M \in \mathrm{L}(\mathbb{C}^d)$ be an arbitrary linear operator. Define the vector $|M\rangle\!\rangle$ as follows:
$$|M\rangle\!\rangle \equiv \mathrm{vec}(M) := (\mathbb{1}_d \otimes M)|\Gamma_d\rangle, \tag{12}$$

where
$$|\Gamma_d\rangle := \sum_{k=0}^{d-1} |k\rangle \otimes |k\rangle. \tag{13}$$

(a) Prove that
$$\mathrm{vec}(|v_1\rangle\langle v_2|) = \overline{|v_2\rangle} \otimes |v_1\rangle, \tag{14}$$
where $|v_1\rangle, |v_2\rangle \in \mathbb{C}^d$ are arbitrary and $\overline{|v_2\rangle}$ denotes the complex conjugate of $|v_2\rangle$ with respect to the basis $\{|k\rangle\}_{k=0}^{d-1}$.

(b) If $M \in \mathrm{L}(\mathbb{C}^2)$ is the $2 \times 2$ matrix given by
$$M = \begin{pmatrix} p & q \\ r & s \end{pmatrix}, \quad p, q, r, s \in \mathbb{C}, \tag{15}$$
then show that $|M\rangle\!\rangle$ is the column vector defined by stacking the columns of $M$:
$$|M\rangle\!\rangle = \begin{pmatrix} p \\ r \\ q \\ s \end{pmatrix}. \tag{16}$$

(c) For $M \in \mathrm{L}(\mathbb{C}^d)$ prove that
$$(\mathbb{1}_d \otimes M)|\Gamma_d\rangle = (M^{\mathsf{T}} \otimes \mathbb{1}_d)|\Gamma_d\rangle, \tag{17}$$
where $M^{\mathsf{T}}$ is the transpose of $M$.

(d) For $M \in \mathrm{L}(\mathbb{C}^d)$, prove that
$$\mathrm{Tr}[M] = \langle \Gamma_d|(\mathbb{1}_d \otimes M)|\Gamma_d\rangle. \tag{18}$$

(e) For $K, M, L \in \mathrm{L}(\mathbb{C}^d)$, prove that
$$\mathrm{vec}(KML^\dagger) = (\overline{L} \otimes K)\mathrm{vec}(M). \tag{19}$$

13. Let $M \in \mathrm{L}(\mathbb{C}^d)$ be an arbitrary linear operator. Prove that $M^\dagger M$ is positive semi-definite.

14. ★ Prove that a linear operator $M \in \mathrm{L}(\mathbb{C}^d)$, with $d \in \{1, 2, \dots\}$, is injective if and only if it is surjective.

15. ★ Let $\{|\psi_j\rangle\}_{j=0}^{d-1}$ be a set of $d$ linearly independent vectors in $\mathbb{C}^d$, with $d \in \{2, 3, \dots\}$. By definition, this means that, for all $c_0, c_1, \dots, c_{d-1} \in \mathbb{C}$, the equation $c_0|\psi_0\rangle + c_1|\psi_1\rangle + \cdots + c_{d-1}|\psi_{d-1}\rangle = 0$ implies $c_0 = c_1 = \cdots = c_{d-1} = 0$.

   (a) Let
$$T := \sum_{j=0}^{d-1} |\psi_j\rangle\langle j|. \tag{20}$$

   The operator $T$ can be thought of as a $d \times d$ matrix whose columns are given by the vectors $|\psi_j\rangle$. Prove that $T$ is invertible. (*Hint*: First prove that $T$ is injective, by showing that its kernel contains only the zero vector. Then use the result of the previous problem.)

4
