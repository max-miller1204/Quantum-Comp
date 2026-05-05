- Define the $n$-qubit Clifford group as

$$\mathcal{C}_n := \left\{ U : P \in \pm \mathcal{P}_n^* \Rightarrow UPU^\dagger \in \pm \mathcal{P}_n^* \right\} / U(1) \quad \rightarrow \text{mod out global phase}$$

$\rightarrow$ Transforms Paulis to Paulis (up to sign)

$H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \rightarrow HXH = Z, \; HZH = X$

⊛ <u>Theorem</u>: $\mathcal{C}_n = \langle H_i, S_i, \text{CNOT}_{i,j} \;:\; i,j \in \{1,2,\ldots,n\} \rangle / U(1)$

  ⊛ $H, S, \text{CNOT}$ are <u>generators</u> of the Clifford group!

  ⊛ (Take all possible products of $H, S, \text{CNOT}$, and ignore global phase.)

⊛ <mark><u>Corollary</u>:</mark> $\{H, S, \text{CNOT}, T\}$ is universal $\rightarrow \{H, \text{CNOT}, T\}$ is universal. $(S = T^2)$.

---

② <u>Noise and Errors in Quantum Computing</u>

⊛ In quantum computing, we care about <u>precise control</u> of qubits — but they inevitably <u>interact with their environment</u>! This evolution is unitary.

(<u>ideal case</u>).

[Circuit: $\ket{0} \longrightarrow \boxed{G} \longrightarrow G\ket{0}$]

  $\underbrace{\phantom{\boxed{G}}}_{\text{Unitary gate.}}$

(<u>reality</u>) $\rightarrow$ gate noise.

[Circuit:
- System: $\ket{0} \longrightarrow$ [box $\mathcal{N}$] $\longrightarrow \mathcal{N}(\ket{0}\bra{0}) \rightarrow$ "quantum channel"
- Environment: $\ket{0} \longrightarrow$ [into box, traced out]
]
