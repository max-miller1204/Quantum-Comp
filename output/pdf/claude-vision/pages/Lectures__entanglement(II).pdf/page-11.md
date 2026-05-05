$\circledast$ There exists a pure state $\ket{\psi}_{ES}$ such that $\mathrm{Tr}_E[\ket{\psi}\bra{\psi}_{ES}] = \rho_S$.

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}\underset{\text{\color{red}environment}}{\color{red}\uparrow}$

Proof: (by explicit construction) Consider $\sqrt{\rho_S} = \sum_{k=1}^{r} \sqrt{\lambda_k}\, \ket{\gamma_k}\bra{\gamma_k}$

Then $\ket{\psi}_{ES} = (\mathbb{1}_E \otimes \sqrt{\rho_S})\ket{\Gamma} = \left(\mathbb{1}_E \otimes \sum_{k=1}^{r}\sqrt{\lambda_k}\,\ket{\gamma_k}\bra{\gamma_k}_S\right)\ket{\Gamma}$

$\phantom{xxxxxx}\underset{\color{red}\dim(\mathcal{H}_E) \geq r}{\color{red}\uparrow} \phantom{xxxx} \underset{\color{red}\ket{\Gamma} = \sum_{k=0}^{d-1}\ket{k,k}}{\color{red}\uparrow}$

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}{\color{blue}\underline{\mathrm{vec}(\ket{e_k}\bra{f_k}) = \overline{\ket{f_k}} \otimes \ket{e_k}}}$

$\phantom{xx}= \sum_{k=1}^{r} \sqrt{\lambda_k}\, \underbrace{(\mathbb{1}_E \otimes \ket{\gamma_k}\bra{\gamma_k}_S)\ket{k,k}_{ES}}_{\color{red}\overline{\ket{\gamma_k}}_E \otimes \ket{\gamma_k}_S} = \sum_{k=1}^{r}\sqrt{\lambda_k}\,\overline{\ket{\gamma_k}}_E \otimes \ket{\gamma_k}_S$

- This is a state vector: $\braket{\psi|\psi} = \left(\sum_{k=1}^{r}\sqrt{\lambda_k}\,\bra{\overline{\gamma_k}}_E \otimes \bra{\gamma_k}_S\right)\left(\sum_{k'=1}^{r}\sqrt{\lambda_{k'}}\,\overline{\ket{\gamma_{k'}}}_E \otimes \ket{\gamma_{k'}}_S\right)$

$\phantom{xxxxxxxxxxxxxxxxx} = \sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}}\, \underbrace{\braket{\overline{\gamma_k}|\overline{\gamma_{k'}}}}_{\delta_{k,k'}} \underbrace{\braket{\gamma_k|\gamma_{k'}}}_{\delta_{k,k'}}$

$\phantom{xxxxxxxxxxxxxxxxx} = \sum_{k=1}^{r} \lambda_k$

$\phantom{xxxxxxxxxxxxxxxxx} = 1 \quad \checkmark$

- $\mathrm{Tr}_E[\ket{\psi}\bra{\psi}_{ES}] = \mathrm{Tr}_E\left[(\mathbb{1}_E \otimes \sqrt{\rho_S})\ket{\Gamma}\bra{\Gamma}_{ES}(\mathbb{1}_E \otimes \sqrt{\rho_S})\right]$

$\phantom{xxxxxxxxxxxxxxx} = \sqrt{\rho_S}\, \underbrace{\mathrm{Tr}_E[\ket{\Gamma}\bra{\Gamma}_{ES}]}_{}\, \sqrt{\rho_S}$

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx} {\color{blue}\ket{\Gamma} = \sum_{k=0}^{d-1}\ket{k,k}}$
