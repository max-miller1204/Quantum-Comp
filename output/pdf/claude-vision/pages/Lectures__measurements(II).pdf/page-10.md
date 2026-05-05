Compare with the full trace:

$$\mathrm{Tr}(\rho_{AB}) = \sum_{k=0}^{d_A-1} \sum_{\ell=0}^{d_B-1} \left(\bra{k}_A \otimes \bra{\ell}_B\right) \rho_{AB} \left(\ket{k}_A \otimes \ket{\ell}_B\right).$$

$$= \mathrm{Tr}\left[\ket{x}\bra{x}_A \underbrace{\mathrm{Tr}_B(\rho_{AB})}_{=\rho_A}\right]$$

For measurement of $B$ instead: $\Pr(x) = \mathrm{Tr}\left[\left(\mathbb{1}_A \otimes \ket{x}\bra{x}_B\right)\rho_{AB}\right] = \mathrm{Tr}\left[\ket{x}\bra{x}_B \underbrace{\mathrm{Tr}_A(\rho_{AB})}_{=\rho_B}\right].$
