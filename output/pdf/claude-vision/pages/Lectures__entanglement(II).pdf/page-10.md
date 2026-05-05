$$p_x = \text{Tr}\left[(M_A^x \otimes \mathbb{1}_B)\ket{\psi}\bra{\psi}_{AB}\right] = \text{Tr}\left[M_A^x \, \text{Tr}_B\left[\ket{\psi}\bra{\psi}_{AB}\right]\right] = \sum_{k=1}^{r} \lambda_k \text{Tr}\left[M_A^x \ket{e_k}\bra{e_k}_A\right].$$

$$= \text{Tr}_B\left[\sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}} \ket{e_k}\bra{e_{k'}}_A \otimes \ket{f_k}\bra{f_{k'}}_B\right]$$

$$= \sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}} \ket{e_k}\bra{e_{k'}}_A \underbrace{\text{Tr}\left[\ket{f_k}\bra{f_{k'}}_B\right]}_{=\delta_{k,k'}}$$

$$= \sum_{k=1}^{r} \lambda_k \ket{e_k}\bra{e_k}_A$$

$$\text{Tr}_A\left[\left(\sqrt{M_A^x} \otimes \mathbb{1}_B\right)\ket{\psi}\bra{\psi}_{AB}\left(\sqrt{M_A^x} \otimes \mathbb{1}_B\right)\right] = \text{Tr}_A\left[\sum_{k,k'=1}^{r} \sqrt{M_A^x}\ket{e_k}\bra{e_{k'}}_A\sqrt{M_A^x} \otimes \ket{f_k}\bra{f_{k'}}_B\right]$$

$$= \sum_{k,k'=1}^{r} \text{Tr}\left[\sqrt{M_A^x}\ket{e_k}\bra{e_{k'}}_A\sqrt{M_A^x}\right] \ket{f_k}\bra{f_{k'}}_B$$

$$= \sum_{k,k'=1}^{r} \text{Tr}\left[M_A^x \ket{e_k}\bra{e_{k'}}_A\right] \ket{f_k}\bra{f_{k'}}_B \quad \rightarrow \text{Not a pure state in general.}$$

3. **Entanglement with an (unknown) environment.**

   Consider a mixed state $\rho_S = \sum_{k=1}^{r} \lambda_k \ket{\psi_k}\bra{\psi_k}$ (spectral decomposition).
   
   $\uparrow$ <span style="color:red">eigenvalues</span> $\quad$ <span style="color:red">eigenvectors (orthonormal).</span>

   ⊛ <u>Note</u>: $\text{Tr}(\rho_S) = 1 \implies \text{Tr}\left[\sum_{k=1}^{r} \lambda_k \underbrace{\text{Tr}\left[\ket{\psi_k}\bra{\psi_k}\right]}_{=1}\right] = \sum_{k=1}^{r} \lambda_k = 1$ (eigenvalues sum to one).

   ⊛ <u>Note</u>: $\rho_S \geq 0 \implies \lambda_k \geq 0 \;\forall\, k. \implies 0 \leq \lambda_k \leq 1 \;\forall\, k.$
