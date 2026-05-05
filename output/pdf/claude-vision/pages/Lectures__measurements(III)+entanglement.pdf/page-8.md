⊛ **Example:** $\rho_{AB} = \frac{1}{2}\left(\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B + \ket{1}\bra{1}_A \otimes \ket{1}\bra{1}_B\right) = \frac{1}{2}\left(\ket{0,0}\bra{0,0}_{AB} + \ket{1,1}\bra{1,1}_{AB}\right)$

This state is <u>diagonal</u> in the tensor-product basis

$$\{\ket{0}_A \otimes \ket{0}_B,\ \ket{0}_A \otimes \ket{1}_B,\ \ket{1}_A \otimes \ket{0}_B,\ \ket{1}_A \otimes \ket{1}_B\}$$

$$\rho_{AB} = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

[column labels: 00, 01, 10, 11]

⊛ **If Alice and Bob both measure in the $\{\ket{0}, \ket{1}\}$ basis, then their outcomes will be correlated!**

- If Alice gets outcome "0", then so will Bob. Same with outcome "1".

$$\text{Tr}_A\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B)\rho_{AB}\right] = \frac{1}{2}\ket{0}\bra{0}_B \rightarrow \rho_B^{(0)} = \ket{0}\bra{0}_B.\ \text{Also,}\ \rho_B^{(1)} = \ket{1}\bra{1}.$$

$$= \text{Tr}_A\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B) \cdot \frac{1}{2}\left(\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B + \ket{1}\bra{1}_A \otimes \ket{1}\bra{1}_B\right)\right]$$

$$= \frac{1}{2}\left(\text{Tr}_A\left[\ket{0}\bra{0}\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B\right] + \text{Tr}_A\left[\underbrace{\ket{0}\bra{0}\ket{1}\bra{1}}_{=\,0}{}_A \otimes \ket{1}\bra{1}_B\right]\right)$$

$$= \frac{1}{2}\text{Tr}_A\left[\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B\right]$$

$$= \frac{1}{2}\ket{0}\bra{0}_B$$
