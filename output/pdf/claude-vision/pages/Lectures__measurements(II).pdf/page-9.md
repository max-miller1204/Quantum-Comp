- Recall: for a computational-basis measurement on qubit $A$ of two-qudit system $AB$ in state $\rho_{AB}$: $\Pr[x] = \text{Tr}\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B) \rho_{AB} \big)$

  $\{\ket{k,\ell}: k \in \{0,1,\ldots,d_A-1\},\ \ell \in \{0,1,\ldots,d_B-1\}\}$ is a basis

  $\quad \xrightarrow{\ \ } \underline{= \text{Tr}\big[ \ket{x}\bra{x}_A \,\text{Tr}_B(\rho_{AB}) \big]}.$

$$\Rightarrow \text{Tr}\big[ (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big] = \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \bra{k,\ell}_{AB}\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big)\ket{k,\ell}_{AB}.$$

(This is a sum over the diagonal elements.)

$$= \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} (\bra{k}_A \otimes \bra{\ell}_B)\big( (\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB} \big)(\ket{k}_A \otimes \ket{\ell}_B).$$

$\left( \circledast \text{ Property of tensor product:} \atop (M_1 \otimes M_2)(N_1 \otimes N_2) = M_1 N_1 \otimes M_2 N_2 \right)$

$$= \bra{k}_A (\mathbb{1}_A \otimes \bra{\ell}_B)(\ket{x}\bra{x}_A \otimes \mathbb{1}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$\left( \circledast\ (\mathbb{1}_A \otimes M_B)(N_A \otimes \mathbb{1}_B) \atop = N_A \otimes M_B \atop = (N_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes M_B). \right)$

$$= \bra{k}_A \ket{x}\bra{x}_A (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$$= \sum_{k=0}^{d_A-1}\sum_{\ell=0}^{d_B-1} \bra{k}_A \ket{x}\bra{x}_A (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)\ket{k}_A$$

$$= \sum_{k=0}^{d_A-1} \bra{k}_A \ket{x}\bra{x}_A \left( \underbrace{\sum_{\ell=0}^{d_B-1} (\mathbb{1}_A \otimes \bra{\ell}_B)\rho_{AB}(\mathbb{1}_A \otimes \ket{\ell}_B)}_{\equiv\, \text{Tr}_B(\rho_{AB})\ \to\ \text{the partial trace!}} \right) \ket{k}_A$$
