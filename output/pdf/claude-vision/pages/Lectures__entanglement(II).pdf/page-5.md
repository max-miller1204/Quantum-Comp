> - If $r=1$, then $\ket{\psi} = \ket{e_1} \otimes \ket{f_1} \Rightarrow$ not entangled!
> - If $r>1$, then entangled!  $\quad r \equiv$ **Schmidt rank**.

(c) Observe: $\ket{\psi}_{AB} = \sum_{k=1}^{r} s_k \ket{\overline{e_k}}_A \otimes \ket{f_k}_B$

$$\Rightarrow \mathrm{Tr}_B[\ket{\psi}\bra{\psi}_{AB}] = \mathrm{Tr}_B\left[ \sum_{k,k'=1}^{r} s_k s_{k'} \ket{\overline{e_k}}\bra{\overline{e_{k'}}}_A \otimes \ket{f_k}\bra{f_{k'}}_B \right]$$

$$= \sum_{k,k'=1}^{r} s_k s_{k'} \ket{\overline{e_k}}\bra{\overline{e_{k'}}}_A \underbrace{\mathrm{Tr}[\ket{f_k}\bra{f_{k'}}]}_{=\,\delta_{k,k'}}$$

$$= \sum_{k=1}^{r} s_k^2 \ket{\overline{e_k}}\bra{\overline{e_k}}_A \quad \to \text{ Diagonal!}$$

Also, $\mathrm{Tr}_A[\ket{\psi}\bra{\psi}_{AB}] = \sum_{k=1}^{r} s_k^2 \ket{f_k}\bra{f_k}_B$

$\Rightarrow \mathrm{Tr}_A[\psi_{AB}]$ and $\mathrm{Tr}_B[\psi_{AB}]$ have the same (non-zero) eigenvalues!

(d) Suppose $r=d$, $s_k = \tfrac{1}{\sqrt{d}}\ \forall\ k \in \{1,2,\ldots,d\}$.

We call $\ket{\psi}$ **maximally entangled** (Note that the marginals are maximally mixed.).

(e) Observe: $\dfrac{1}{\sqrt{d}} \sum_{k=1}^{d} \ket{e_k} \otimes \ket{\overline{e_k}} = \dfrac{1}{\sqrt{d}} \sum_{k=1}^{d} \left( \sum_{j=0}^{d-1} \ket{j}\bra{j} \right) \ket{e_k} \otimes \left( \sum_{\ell=0}^{d-1} \ket{\ell}\bra{\ell} \right) \ket{\overline{e_k}}$
