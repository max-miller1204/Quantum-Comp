$$\downarrow$$
$$= \mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_P)(\mathbb{1}_S \otimes \mathbb{1}_P)\right]$$
$$= \mathrm{Tr}_P\left[\mathbb{1}_S \otimes \ket{0}\bra{0}_P\right]$$
$$= \mathbb{1}_S. \checkmark$$

We also prove the converse: given a POVM $\{M_x\}_{x \in X}$, the measurement can be realised by a unitary b/w system and probe and measurement of the probe.

Define $V = \sum_{x \in X} \sqrt{M_x} \otimes \underbrace{\ket{x}_P}_{\text{some orthonormal vectors.}}$

$\quad\left(\circledast \underline{\text{Note}}: M_x \text{ is Hermitian, so it has spectral decomposition}\right.$
$\quad\left. M_x = \sum_{k=1}^{r} \lambda_k \ket{\varphi_k}\bra{\varphi_k}. \text{ Then the square root is } \sqrt{M_x} = \sum_{k=1}^{r} \sqrt{\lambda_k} \ket{\varphi_k}\bra{\varphi_k}.\right)$

$\circledast$ $V$ is an isometry: it satisfies
$V^\dagger V = \mathbb{1}$ (but not necessarily $VV^\dagger = \mathbb{1}$.)

$\underline{\text{Check}}: V^\dagger V = \left(\sum_x \sqrt{M_x} \otimes \bra{x}_P\right)\left(\sum_{x' \in X} \sqrt{M_{x'}} \otimes \ket{x'}_P\right)$
$$\downarrow$$
$$= \sum_{x,x' \in X} \sqrt{M_x}\sqrt{M_{x'}} \underbrace{\braket{x|x'}}_{=\delta_{x,x'}} = \sum_{x \in X} M_x = \mathbb{1} \checkmark$$

Now note that $\mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{x}\bra{x}_{P}) VV^\dagger\right] = \mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{x}\bra{x})\left(\sum_{x_1 \in X} \sqrt{M_{x_1}} \otimes \ket{x_1}\right)\left(\sum_{x_2 \in X} \sqrt{M_{x_2}} \otimes \bra{x_2}\right)\right]$

$$\downarrow$$
$$= \sum_{x_1, x_2 \in X} \mathrm{Tr}_P\left[\sqrt{M_{x_1}}\sqrt{M_{x_2}} \otimes \underbrace{\ket{x}\braket{x|x_1}\bra{x_2}}_{=\delta_{x,x_1}}\right]$$

$$\downarrow$$
$$= \sum_{x_1, x_2 \in X} \sqrt{M_{x_1}}\sqrt{M_{x_2}}\, \delta_{x,x_1} \underbrace{\braket{x_2|x}}_{=\delta_{x,x_2}}$$

$$\downarrow$$
$$= M_x.$$
