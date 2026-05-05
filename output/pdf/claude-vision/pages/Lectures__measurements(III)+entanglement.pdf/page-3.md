- Measurements of the form $\{\ket{e_k}\bra{e_k}\}_{k=1}^{d}$, for an orthonormal basis $\{\ket{e_k}\}_{k=1}^{d}$, are known as <u>projective measurements</u>, b/c $M_k \equiv \ket{e_k}\bra{e_k}$ are <u>projectors</u>.

> ✱ A <u>projector</u> is an operator/matrix satisfying $P^2 = P$.
>
> <u>Check</u>: $\big(\ket{e_k}\bra{e_k}\big)^2 = \ket{e_k}\underbrace{\braket{e_k|e_k}}_{=1}\bra{e_k} = \ket{e_k}\bra{e_k}\ \checkmark$

- A <u>general projective measurement</u> has the form $\{\Pi_x\}_{x \in X}$:

  (1) $\Pi_x \geq 0 \quad \forall x \in X$

  (2) $\Pi_x^2 = \Pi_x \quad \forall x \in X$

  (3) $\sum_{x \in X} \Pi_x = \mathbb{1}$.

- <u>Theorem</u>: Every general (POVM) measurement can be written as a projective measurement on a larger system.

  <u>Proof</u>: Consider a system $S$; we want to measure it via a probe $P$.

  [Circuit diagram: top wire labeled $\rho_S$ entering box $U$; bottom wire labeled $\ket{0}$ entering box $U$; bottom output of $U$ goes into a measurement box labeled $x$, $\{\Pi_x\}_x$ ← Projective measurement of the probe.]

  ↑ <span style="color:red">Unitary interaction of system and probe.</span>

$$\rho_S \otimes \ket{0}\bra{0}_P \;\mapsto\; U(\rho_S \otimes \ket{0}\bra{0})U^\dagger \;\mapsto\; \underline{\Pr[x] = \mathrm{Tr}\!\left[(\mathbb{1}_S \otimes \Pi_x)\, U(\rho_S \otimes \ket{0}\bra{0})U^\dagger\right]}$$

✱ We can write this in the form $\mathrm{Tr}[M_x \rho_S]$.
