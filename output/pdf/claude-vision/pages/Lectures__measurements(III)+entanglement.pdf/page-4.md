$$\text{Tr}\left[(\mathbb{1}_S \otimes \Pi_x) U (\rho_S \otimes \ket{0}\bra{0}_p) U^\dagger\right] = \text{Tr}\left[(\rho_S \otimes \ket{0}\bra{0}) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$\text{Tr}[ABC] = \text{Tr}[BCA] = \text{Tr}[CAB].$

$(X_A \otimes Y_B) = (X_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes Y_B)$

$\text{Tr}\left[(\rho_A \otimes \mathbb{1}_B) M_{AB}\right] = \text{Tr}\left[\rho_A \, \text{Tr}_B[M_{AB}]\right]$

$$= \text{Tr}\left[(\rho_S \otimes \mathbb{1}_p)(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$$= \text{Tr}\left[\rho_S \, \underbrace{\text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]}_{\equiv M_x}\right]$$

Let us show that $\{M_x\}_{x \in \mathcal{X}}$ is a POVM.

(1) Check that $M_x \geq 0.$  $\quad \langle v | M_x | v \rangle \geq 0 \;\; \forall \ket{v}$

For an arbitrary vector $\ket{v}$:

$$\langle v | M_x | v \rangle = \langle v | \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right] | v \rangle$$

$\text{Tr}[M \ket{v_1}\bra{v_2}]$
$= \langle v_2 | M | v_1 \rangle$

$$= \text{Tr}\left[(\ket{v}\bra{v}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$$= \underbrace{(\bra{v}_S \otimes \bra{0}_p) U^\dagger}_{\equiv \bra{v'}} (\mathbb{1}_S \otimes \Pi_x) \underbrace{U (\ket{v}_S \otimes \ket{0}_p)}_{\equiv \ket{v'}}$$

$$= \langle v' | (\mathbb{1}_S \otimes \Pi_x) | v' \rangle$$

$\geq 0$ b/c $\Pi_x \geq 0$ and $\mathbb{1}_S \geq 0 \Rightarrow \mathbb{1}_S \otimes \Pi_x \geq 0.$

So $M_x \geq 0 \;\checkmark\; \forall x$

(2) Check that $\sum_{x \in \mathcal{X}} M_x = \mathbb{1}.$

$$\sum_{x \in \mathcal{X}} M_x = \sum_{x \in \mathcal{X}} \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right] = \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \underbrace{\sum_{x \in \mathcal{X}} \Pi_x}_{=\mathbb{1}_p \text{ by assumption}}) U\right]$$

$$= \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) \underbrace{U^\dagger (\mathbb{1}_S \otimes \mathbb{1}_p) U}_{\mathbb{1}_S \otimes \mathbb{1}_p}\right] \quad \rightarrow U^\dagger U = \mathbb{1}$$
