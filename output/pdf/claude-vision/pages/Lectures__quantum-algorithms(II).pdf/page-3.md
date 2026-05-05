- **Example: Teleportation**

[Diagram: Alice (top) holds $\ket{\psi}_{A'}$ and one half of $\ket{\Phi^+}_{AB}$. She performs a Bell measurement, obtaining classical bits $z, x$ which are sent to Bob. Bob applies $X^x$ then $Z^z$ to his half of the entangled pair, recovering $\ket{\psi}_B$.]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1}.$

(✱) **If Alice and Bob are not spatially separated, then the algorithm can be modified as follows:**

[Circuit diagram: Three wires labeled $\ket{\psi}_{A'}$, $\ket{0}_A$, $\ket{0}_B$. The red box on left contains: $H$ on $\ket{0}_A$, then CNOT from $A$ (control) to $B$ (target) — this prepares $\ket{\Phi^+}_{AB}$. Then CNOT with $A'$ as control and $A$ as target, $H$ on $A'$. Blue box on right: CNOT from $A$ to $B$ ($X$ correction), then controlled-$Z$ from $A'$ to $B$, output $\ket{\psi}_B$.]

$\ket{+} = \tfrac{1}{\sqrt{2}}(\ket{0} + \ket{1})$

$$\ket{0}_A\ket{0}_B \mapsto \ket{+}_A\ket{0}_B = \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{0}_B) \mapsto \tfrac{1}{\sqrt{2}}(\ket{0}_A\ket{0}_B + \ket{1}_A\ket{1}_B) = \ket{\Phi^+}$$

$$\ket{\psi}_{A'}\ket{0}_A\ket{0}_B \mapsto \ket{\psi}_{A'} \otimes \ket{\Phi^+}_{AB} = \tfrac{1}{\sqrt{2}}\big(\ket{\psi}_{A'}\ket{0}_A\ket{0}_B + \ket{\psi}_{A'}\ket{1}_A\ket{1}_B\big)$$

$\ket{\psi}_{A'} = \alpha\ket{0} + \beta\ket{1}$

$$= \tfrac{1}{\sqrt{2}}\big(\alpha\ket{0}_{A'}\ket{0}_A\ket{0}_B + \beta\ket{1}_{A'}\ket{0}_A\ket{0}_B$$
$$+ \alpha\ket{0}_{A'}\ket{1}_A\ket{1}_B + \beta\ket{1}_{A'}\ket{1}_A\ket{1}_B\big).$$

$$\xmapsto{\text{CNOT}_{A'A}} \tfrac{1}{\sqrt{2}}\big(\alpha\ket{0}_{A'}\ket{0}_A\ket{0}_B + \beta\ket{1}_{A'}\ket{1}_A\ket{0}_B$$
$$+ \alpha\ket{0}_{A'}\ket{1}_A\ket{1}_B + \beta\ket{1}_{A'}\ket{0}_A\ket{1}_B\big).$$
