$M_{AB} \in L(\mathbb{C}^2 \otimes \mathbb{C}^2) \quad \to \quad M_{AB} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array} \begin{array}{c} \begin{matrix} 00 & 01 & 10 & 11 \end{matrix} \\ \begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix} \end{array}$

[The matrix entries are grouped by 2×2 blocks: green circles $a_{11}, a_{22}$; purple $a_{13}, a_{24}$; pink $a_{31}, a_{42}$; orange $a_{33}, a_{44}$.]

$$= \sum_{i,j=0}^{1} \sum_{k,\ell=0}^{1} M_{i,k;j,\ell} \, \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B.$$

$$\mathrm{Tr}_B[M_{AB}] = \sum_{i,j=0}^{1} \sum_{k,\ell=0}^{1} M_{i,k;j,\ell} \, \underbrace{\mathrm{Tr}_B\!\left[\ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B\right]}_{=\,\ket{i}\bra{j}\,\cdot\,\underbrace{\mathrm{Tr}[\ket{k}\bra{\ell}]}_{\delta_{k,\ell}}} = \sum_{i,j=0}^{1} \sum_{k=0}^{1} M_{i,k;j,k} \, \ket{i}\bra{j}_A$$

$$\mathrm{Tr}_B[M_{AB}] = \begin{array}{c} \\ 0 \\ 1 \end{array} \begin{array}{c} \begin{matrix} 0 & \quad 1 \end{matrix} \\ \begin{pmatrix} a_{11}+a_{22} & a_{13}+a_{24} \\ a_{31}+a_{42} & a_{33}+a_{44} \end{pmatrix} \end{array}$$
