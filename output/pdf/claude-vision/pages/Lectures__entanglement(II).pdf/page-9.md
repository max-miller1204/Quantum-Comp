$$\frac{\text{Tr}_X\left[\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\rho_{XS}\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\right]}{p_k}$$

$$= \frac{1}{p_k}\sum_{k'=1}^{N} \text{Tr}_X\left[\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\left(p_{k'}\ket{k'}\bra{k'}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right)\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\right]$$

$$\downarrow$$

$$= \frac{1}{p_k}\sum_{k'=1}^{N} p_{k'}\, \underbrace{\text{Tr}_X\left[\ket{k}\braket{k|k'}\braket{k'|k}\bra{k}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right]}_{=\,\delta_{k',k}\,\ket{\psi_{k'}}\bra{\psi_{k'}}}$$

$$\downarrow$$

$$= \frac{1}{p_k}\, p_k \ket{\psi_k}\bra{\psi_k}$$

$$= \ket{\psi_k}\bra{\psi_k} \quad \checkmark \quad (\text{as expected!})$$

✱ But if you don't know the outcome/label? $\rightarrow$ <u>Trace out the register X!</u>

$$\text{Tr}_X(\rho_{XS}) = \text{Tr}_X\left[\sum_{k=1}^{N} p_k \ket{k}\bra{k}_X \otimes \ket{\psi_k}\bra{\psi_k}_S\right]$$

$$\downarrow$$

$$= \sum_{k=1}^{N} p_k\, \underbrace{\text{Tr}_X\left[\ket{k}\bra{k}_X \otimes \ket{\psi_k}\bra{\psi_k}_S\right]}_{=\,\underbrace{\text{Tr}[\ket{k}\bra{k}]}_{=1}\,\ket{\psi_k}\bra{\psi_k}}$$

$$\downarrow$$

$$= \underline{\underline{\sum_{k=1}^{N} p_k \ket{\psi_k}\bra{\psi_k}.}}$$

**2. Measurement on one part of a pure state.**

$$\ket{\psi}_{AB} = \sum_{k=1}^{r} \sqrt{\lambda_k}\,\ket{e_k}_A \otimes \ket{f_k}_B \quad \rightarrow \text{ Measure } A \text{ wrt POVM } \{M_A^x\}_{x \in \mathcal{X}}$$

Conditioned on outcome $x$, state on $B$ is $\quad \dfrac{1}{p_x}\,\text{Tr}_A\left[\left(\sqrt{M_A^x}\otimes \mathbb{1}_B\right)\ket{\psi}\bra{\psi}_{AB}\left(\sqrt{M_A^x}\otimes \mathbb{1}_B\right)\right]$
