(3) For arbitrary $\ket{v} \in \mathbb{C}^d$, $\bra{v} \tilde{\rho} \ket{v} = \underbrace{\bra{v} U}_{\bra{\tilde{v}}} \rho \underbrace{U^\dagger \ket{v}}_{\ket{\tilde{v}}}$

$$= \bra{\tilde{v}} \rho \ket{\tilde{v}} \geq 0 \quad \text{b/c } \rho \geq 0 \text{ by assumption}$$

$\Rightarrow$ So $\tilde{\rho} \geq 0$ ✓

---

— **Product of unitaries is a unitary:** if $U_1, U_2$ are unitaries, then $U = U_1 U_2$ is also a unitary.

Check: $U^\dagger U = (U_1 U_2)^\dagger U_1 U_2 = U_2^\dagger \underbrace{U_1^\dagger U_1}_{= \mathbb{1}} U_2 = U_2^\dagger U_2 = \mathbb{1}$ ✓

$U U^\dagger = (U_1 U_2)(U_1 U_2)^\dagger = U_1 \underbrace{U_2 U_2^\dagger}_{= \mathbb{1}} U_1^\dagger = U_1 U_1^\dagger = \mathbb{1}$ ✓
