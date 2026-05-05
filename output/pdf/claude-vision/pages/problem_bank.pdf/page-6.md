(b) Let
$$\ket{\phi_j} := S^{-\frac{1}{2}}\ket{\psi_j} \tag{25}$$
for all $j \in \{0, 1, \ldots, d-1\}$. Prove that $\{\ket{\phi_j}\}_{j=0}^{d-1}$ is an orthonormal basis for $\mathbb{C}^d$. Also, prove that $\braket{\phi_i|\psi_j} = \bra{i} G^{\frac{1}{2}} \ket{j}$ for all $i, j \in \{0, 1, \ldots, d-1\}$, where $G := T^\dagger T$ and $T := \sum_{j=0}^{d-1} \ket{\psi_j}\bra{j}$.

(c) Let us now show that the vectors defined in (25) are optimal with respect to the Euclidean norm, in the following sense:
$$\inf_Q \left\{ \sum_{j=0}^{d-1} \| \ket{\psi_j} - \ket{\phi_j} \|_2^2 : \ket{\phi_j} = Q\ket{\psi_j},\ \braket{\phi_i|\phi_j} = \delta_{i,j}\ \forall j \in \{0, 1, \ldots, d-1\} \right\} \tag{26}$$
$$= \sum_{j=0}^{d-1} \| \ket{\psi_j} - S^{-\frac{1}{2}} \ket{\psi_j} \|_2^2, \tag{27}$$

where the optimization in (26) is with respect to every invertible linear operator $Q$.

  i. Prove that solving the optimization problem given by (26) can be reduced to solving the optimization problem given by
$$\sup_Q \left\{ \mathrm{Tr}[(Q + Q^\dagger)S] : QSQ^\dagger = \mathbb{1}_d \right\}. \tag{28}$$

  ii. Prove that the constraint $QSQ^\dagger = \mathbb{1}_d$ in (28) implies that $Q = US^{-\frac{1}{2}}$, where $U$ is a unitary operator. (*Hint*: Consider a polar decomposition of $Q$.)
  Hence, show that the optimization problem given by (28) is equivalent to
$$\sup_U \mathrm{Re}\left( \mathrm{Tr}[U S^{\frac{1}{2}}] \right), \tag{29}$$
where the optimization is with respect to unitary operators $U$ acting on $\mathbb{C}^d$.

  iii. Prove that the solution to the optimization problem given by (29) is $U = \mathbb{1}_d$, implying that the optimal $Q$ in (26) is indeed $S^{-\frac{1}{2}}$.

18. Prove that the trace norm can be calculated as $\|M\|_1 = \mathrm{Tr}[\sqrt{M^\dagger M}]$. (*Hint*: Start by writing $M$ in terms of its singular-value decomposition. Then recall how we define the square root of Hermitian operators.)

19. Prove that $\|P\|_1 = \mathrm{Tr}[P]$ for every (Hermitian) positive semi-definite operator $P$.

20. ★ Let $\ket{u}, \ket{v} \in \mathbb{C}^d$, with $d \in \{2, 3, \ldots\}$, be arbitrary vectors (not necessarily unit/state vectors). Prove that
$$\| \ket{u}\bra{u} - \ket{v}\bra{v} \|_1^2 = (\braket{u|u} + \braket{v|v})^2 - 4|\braket{u|v}|^2. \tag{30}$$

21. Let $\ket{\psi} \in \mathbb{C}^d$ be a state vector, with $d \in \{2, 3, \ldots\}$. Prove that
$$\frac{1}{2} \left\| \ket{\psi}\bra{\psi} - \frac{\mathbb{1}_d}{d} \right\|_1 = 1 - \frac{1}{d}. \tag{31}$$

In other words, every pure state is the same trace distance away from the maximally-mixed state.

6
