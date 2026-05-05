23. Define the $n$-qubit GHZ state vector as follows:

$$|\text{GHZ}_n\rangle := \frac{1}{\sqrt{2}}(|0\rangle^{\otimes n} + |1\rangle^{\otimes n}), \tag{67}$$

for $n \in \{1, 2, \ldots\}$. Then, define

$$|\text{GHZ}_{z,\vec{x}}\rangle := (Z^z \otimes X^{\vec{x}})|\text{GHZ}_n\rangle, \tag{68}$$

for $z \in \{0,1\}$ and $\vec{x} \in \{0,1\}^{n-1}$. Prove that the set $\{|\text{GHZ}_{z,\vec{x}}\rangle\}_{z\in\{0,1\},\,\vec{x}\in\{0,1\}^{n-1}}$ is an orthonormal basis for $(\mathbb{C}^2)^{\otimes n}$, and thereby conclude that the set $\{|\text{GHZ}_{z,\vec{x}}\rangle\langle\text{GHZ}_{z,\vec{x}}|\}_{z\in\{0,1\},\,\vec{x}\in\{0,1\}^{n-1}}$ is a POVM.

24. ★ *Fusing two GHZ state vectors.* Consider a GHZ state of three qubits and a GHZ state of four qubits. We can merge these to create a larger GHZ state of six qubits using the following protocol, which is similar to the teleportation protocol.

   Step 1 Apply the CNOT gate to the third qubit of the first GHZ state (which is the control qubit) and the first qubit of the second GHZ state (which is the target qubit).

   Step 2 Then, measure the target qubit in the $\{|0\rangle, |1\rangle\}$ basis.

   Step 3 If the measurement outcome is "0", do nothing; if the outcome is "1", then apply the Pauli-$X$ gate to all of the remaining qubits of the second GHZ state.

   Prove that, with probability one, this procedure results in the larger GHZ state of six qubits.

25. ★ Let $\rho$ and $\sigma$ be quantum states. Consider a very simple hypothesis testing strategy for guessing whether a given quantum system is in state $\rho$ or $\sigma$: Bob discards the state of the system and guesses "$\rho$" with probability $q$ and "$\sigma$" with probability $1 - q$.

   (a) What is the POVM corresponding to this strategy?
   (b) Evaluate the type-I and type-II error probabilities for this strategy.
   (c) If, in the symmetric setting, the prior probability for being given the state $\rho$ is $p \in [0,1]$, then evaluate the expected error probability for this strategy.

26. ★ Consider states $\rho$ and $\sigma$ along with a POVM $\{M_0, M_1\}$ representing a strategy for hypothesis testing of a single copy of the quantum system, where the outcome "0" corresponds to $\rho$ and the outcome "1" corresponds to $\sigma$. Let $p \in [0,1]$ be the prior probability of being given $\rho$, and let $n \in \{2, 3, \ldots\}$. Construct the POVM $\{M_\rho^{(n)}, M_\sigma^{(n)}\}$ and evaluate the type-I and type-II error probabilities for the following two strategies for hypothesis testing of $n$ copies of the quantum system.

   (a) The *majority-vote* strategy: (1) Measure each system according to the POVM $\{M_0, M_1\}$, and let $N_x$ be the number of times the outcome $x \in \{0, 1\}$ occurs; (2) If $N_0 > N_1$, guess "$\rho$", and if $N_1 > N_0$, guess "$\sigma$". If $n$ is even and $N_0 = N_1$, then guess "$\rho$" with probability $q \in [0,1]$ and "$\sigma$" with probability $1 - q$.

   (b) The *unanimous-vote* strategy: (1) Measure each system according to the POVM $\{M_0, M_1\}$, and let $N_x$ be the number of times the outcome $x \in \{0,1\}$ occurs. (2) If $N_0 = n$, then guess "$\rho$"; otherwise, guess "$\sigma$".

15
