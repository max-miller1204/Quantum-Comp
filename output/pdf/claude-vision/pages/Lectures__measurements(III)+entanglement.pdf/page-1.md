# 1. Measurements

- Every orthonormal basis $\{\ket{e_k}\}_{k=1}^{d}$ in dimension $d$ defines a __measurement__: operators $\{\ket{e_k}\bra{e_k}\}_{k=1}^{d}$ such that $\sum_{k=1}^{d} \ket{e_k}\bra{e_k} = \mathbb{1}_d$.

For a state $\rho$:  $\Pr(k) = \mathrm{Tr}\big[\ket{e_k}\bra{e_k}\rho\big] = \braket{e_k|\rho|e_k}$  ("Born rule")

$$\sum_{k=1}^{d} \Pr(k) = \mathrm{Tr}\Big[\underbrace{\Big(\sum_{k=1}^{d} \ket{e_k}\bra{e_k}\Big)}_{=\,\mathbb{1}_d}\rho\Big] = \mathrm{Tr}(\rho) = 1.$$

⊛ __Example__: For the state $\rho = \frac{\mathbb{1}}{d}$ (the "maximally-mixed" state), the outcomes are completely random in every basis! (i.e., $\Pr(k) = \frac{1}{d}\ \forall\, k$).

- For a bipartite state $\rho_{AB} \rightarrow$ measuring $A$ only: $\Pr(k) = \mathrm{Tr}\big[(\ket{e_k}\bra{e_k}_A \otimes \mathbb{1}_B)\,\rho_{AB}\big]$

This is equal to $\Pr(k) = \mathrm{Tr}\big[\ket{e_k}\bra{e_k}_A\, \mathrm{Tr}_B(\rho_{AB})\big]$
$$\uparrow$$
$$\text{\underline{Partial trace}}$$

⊛ For an operator $M_{AB} = \displaystyle\sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,j;\,k,\ell}\, \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B.$

$$\mathrm{Tr}_B(X_A \otimes Y_B) = X_A \cdot \mathrm{Tr}(Y_B)$$

$$\mathrm{Tr}_B(M_{AB}) = \sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,k;\,j,\ell}\, \ket{i}\bra{j}_A\, \underbrace{\mathrm{Tr}(\ket{k}\bra{\ell}_B)}_{\delta_{k,\ell}}$$

$$= \sum_{i,j=0}^{d_A-1}\Big(\sum_{k=0}^{d_B-1} M_{i,k;\,j,k}\Big)\ket{i}\bra{j}_A$$

$$\mathrm{Tr}_A(M_{AB}) = \sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,j;\,k,\ell}\, \underbrace{\mathrm{Tr}(\ket{i}\bra{j}_A)}_{\delta_{i,j}}\ket{k}\bra{\ell}_B = \sum_{k,\ell=0}^{d_B-1}\Big(\sum_{i=0}^{d_A-1} M_{i,k;\,i,\ell}\Big)\ket{k}\bra{\ell}_B.$$
