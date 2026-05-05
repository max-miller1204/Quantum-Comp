# 2. Entanglement

**※** State vectors of two qubits belong to the tensor-product space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

(a) — A **product state (vector)** has the form:

(State vector) $\quad \ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B, \quad \ket{\phi_1} \in \mathbb{C}^{d_1}, \quad \ket{\phi_2} \in \mathbb{C}^{d_2}.$

(Density operator). $\quad \rho_{AB} = \sigma_A \otimes \tau_B, \quad \sigma_A \in L(\mathbb{C}^{d_A})$ and $\tau_B \in L(\mathbb{C}^{d_B})$ are density operators.

[Diagram: Alice with her atom on the left, Bob with his atom on the right, no connection between them]

$$\rho_{AB} = \sigma_A \otimes \tau_B$$

*Product state*
Alice and Bob individually prepare their systems.

— A **separable state** has the form: $\quad \rho_{AB} = \sum_x p(x) \, \sigma_A^x \otimes \tau_B^x$

↳ Also called "classically correlated" $\qquad$ ↳ probabilities.

[Diagram: Alice with her atom on the left connected via classical communication lines (double arrows) to Bob with his atom on the right]

$$\rho_{AB} = \sum_{x \in \mathcal{X}} p(x)\, \sigma_A^x \otimes \tau_B^x$$

*Separable state*
Alice and Bob individually prepare their systems via local operations and classical communication.
