$r$: Schmidt rank.

(3) $\ket{\psi}_{AB}$ is entangled if and only if $\underline{r > 1}$.

- Entanglement of mixed states is more complicated!

  A mixed state (density operator) $\rho_{AB}$ is entangled it $\underline{\text{cannot}}$ be written as

  $$\rho_{AB} = \sum_{x \in \mathcal{X}} \underbrace{p(x)}_{\text{probabilities}} \tau_A^{(x)} \otimes \omega_B^{(x)} \rightarrow \text{This is } \underline{\text{Separable}}.$$

- ✱ If A & B are qubits, then $\rho_{AB}$ is separable if and only if $\rho_{AB}^{T_B} \geq 0$. $\quad$ <span style="color:red">↙ partial transpose</span>

## ② Teleportation

- A method to transfer the state of a qubit from Alice to Bob using entanglement and classical communication only.

- <u>Given</u>: (1) State vector that Alice wants to send to Bob.
  (2) Shared entangled state b/w Alice and Bob.

- <u>Goal</u>: Transfer the state of qubit $A'$ to Bob's qubit.

[Teleportation circuit diagram: Alice has qubit $\ket{\psi}_{A'}$ which together with her half of $\ket{\Phi^+}_{AB}$ goes into a Bell Measurement, producing classical bits $x \in \{0,1\}$ and $z \in \{0,1\}$. Bob's qubit (the other half of $\ket{\Phi^+}_{AB}$) has $X^x$ then $Z^z$ applied conditioned on the classical bits, yielding $\ket{\psi}_B$.]

- If $x=0$, do nothing. If $x=1$, apply $X$.
- If $z=0$, do nothing. If $z=1$, apply $Z$.
