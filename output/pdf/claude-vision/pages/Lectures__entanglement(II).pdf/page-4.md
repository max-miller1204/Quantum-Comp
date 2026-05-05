(b) Every $M \in L(\mathbb{C}^d)$ has a <u>Singular-value decomposition</u>:

$$M = U \Sigma V^\dagger$$

[arrows: $U$ and $V^\dagger$ labeled "unitaries"; $\Sigma$ labeled "matrix of singular values"]

In bra-ket notation: $\boxed{M = \sum_{k=1}^{r} S_k \ket{f_k}\bra{e_k}}$

[arrow to $S_k$: "singular values, $S_k > 0 \;\forall k$. (unique up to ordering)"]

rank $\equiv$ # of singular values $\to$ <u>unique</u>

$\{\ket{f_k}\}_k, \{\ket{e_k}\}_k$ are orthonormal (left and right singular vectors).

$$\Rightarrow \ket{\psi}_{AB} = \mathrm{vec}(M) = (\mathbb{1} \otimes M)\ket{\mathbb{1}_d} = \sum_{k=1}^{r} S_k \,\mathrm{vec}(\ket{f_k}\bra{e_k}) = \sum_{k=1}^{r} S_k \underbrace{\ket{\bar{e}_k}}_{A} \otimes \underbrace{\ket{f_k}}_{B}$$

$$= (\mathbb{1} \otimes \ket{f_k}\bra{e_k})\left(\sum_{i=0}^{d-1} \ket{i} \otimes \ket{i}\right) = \sum_{i=0}^{d-1} \ket{i} \otimes \ket{f_k}\bra{e_k}\ket{i}$$

$$= \underbrace{\sum_{i=0}^{d-1} \ket{i}\bra{i}\ket{\bar{e}_k} \otimes \ket{f_k}}_{\mathbb{1}} = \ket{\bar{e}_k} \otimes \ket{f_k}$$

[Right side:]
$\ket{e_k} = \sum_{i=0}^{d-1} c_i \ket{i}$

$c_i = \braket{i|e_k}$

$= \overline{\braket{i|e_k}} = \braket{i|\bar{e}_k}$ (circled)

$= \sum_{i=0}^{d-1} \bar{c}_i \ket{i}$

---

⊛ $\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{\bar{e}_k}_A \otimes \ket{f_k}_B$ is called the <u>Schmidt decomposition</u> of $\ket{\psi}_{AB}$.

⊛ $\{S_k\}_{k=1}^{r}$ are called <u>Schmidt coefficients</u>. (sometimes $\sqrt{S_k}$).
   $\;\hookrightarrow > 0$

(Normalisation: $\braket{\psi|\psi} = 1 \Rightarrow \sum_{k=1}^{r} S_k^2 = 1$)

$$1 = \braket{\psi|\psi} = \left(\sum_{k=1}^{r} S_k \bra{\bar{e}_k}_A \otimes \bra{f_k}\right)\left(\sum_{k'=1}^{r} S_{k'} \ket{\bar{e}_{k'}} \otimes \ket{f_{k'}}\right) = \sum_{k,k'=1}^{r} S_k S_{k'} \underbrace{\braket{\bar{e}_k|\bar{e}_{k'}}}_{\delta_{k,k'}} \underbrace{\braket{f_k|f_{k'}}}_{\delta_{k,k'}} = \sum_{k=1}^{r} S_k^2$$
