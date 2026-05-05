# ① Recap: Entanglement

❋ State vectors of two qubits belong to the tensor-product space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

(a) — A **product state (vector)** has the form:

(State vector) $\ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B$, $\ket{\phi_1} \in \mathbb{C}^{d_1}$, $\ket{\phi_2} \in \mathbb{C}^{d_2}$.

(Density operator). $\rho_{AB} = \sigma_A \otimes \tau_B$, $\sigma_A \in L(\mathbb{C}^{d_A})$ and $\tau_B \in L(\mathbb{C}^{d_B})$ are density operators.

[Diagram: Alice and Bob each with their own atom/system, separated]

$$\rho_{AB} = \sigma_A \otimes \tau_B$$

*Product state*
Alice and Bob individually prepare their systems.

— A **separable state** has the form: $\rho_{AB} = \sum_x p(x)\, \sigma_A^x \otimes \tau_B^x$

↳ Also called "classically correlated"   ↳ probabilities.

[Diagram: Alice and Bob each with their own atom/system, connected by a classical communication channel (double arrows between them)]

$$\rho_{AB} = \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Separable state*
Alice and Bob individually prepare their systems via local operations and classical communication.
