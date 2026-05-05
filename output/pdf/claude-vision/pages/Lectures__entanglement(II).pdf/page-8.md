(b) How do mixed states arise in nature?

1. Lack of knowledge of state preparation.

[Diagram: A box labeled "Source" with arrows pointing to:
- $\ket{\psi_1}$ w/ prob. $p_1$
- $\ket{\psi_2}$ w/ prob. $p_2$
- $\vdots$
- $\ket{\psi_N}$ w/ prob. $p_N$]

✸ Now someone uses the source to prepare a state, but they don't tell you which one it is. How do you describe your knowledge of the system?
$\hookrightarrow$ (They don't mention the label.)

$\rho_{XS}^\dagger = \rho_{XS}$

$\rho_{XS} \geq 0$

$\text{Tr}[\rho_{XS}] = 1$

$$\rho_{XS} = \sum_{k=1}^{N} p_k \underbrace{\ket{k}\bra{k}_X}_{\text{ONB}} \otimes \ket{\psi_k}\bra{\psi_k}_S \qquad \left(\text{This is a } \underline{\text{classical-quantum state}}\right)$$

[Red annotation pointing to $\ket{k}\bra{k}_X$: classical variable/register. ("which state is it"?)]

✸ To figure out what state the system is prepared in, we measure the "classical register" $X$.
(w.r.t. POVM $\{\ket{k}\bra{k}\}_{k=1}^{N}$)

$$\text{Tr}\left[(\ket{k}\bra{k}_X \otimes \mathbb{1}_S)\rho_{XS}\right] = \text{Tr}\left[(\ket{k}\bra{k}_X \otimes \mathbb{1}_S)\underbrace{\sum_{k'=1}^{N} p_{k'} \ket{k'}\bra{k'}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S}_{\rho_{XS}}\right]$$

$$= \sum_{k'=1}^{N} \text{Tr}\left[p_{k'} \underbrace{\ket{k}\braket{k|k'}\bra{k'}_X}_{\delta_{k,k'}} \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right]$$

$$= p_k \checkmark \quad (\text{as expected!})$$

[Brace below: State conditioned on outcome $k$] (i.e., you know what the label is).
