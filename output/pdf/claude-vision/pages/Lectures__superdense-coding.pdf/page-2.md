[Circuit diagram: Input $\rho_{AB}$ on two qubits A (top) and B (bottom). A CNOT gate with A as control and B as target, then a Hadamard H on qubit A, then Pauli-Z measurement boxes (labeled X) on both qubits.]

$\rho_{AB} \mapsto U\rho_{AB}U^\dagger \mapsto (H\otimes \mathbb{1})U\rho_{AB}U^\dagger(H^\dagger \otimes \mathbb{1})$

↑ Pauli-Z measurement.   ↓ State just before measurement.

Now do a Pauli-Z measurement on each qubit.

The POVM is $\{|0,0\rangle\langle 0,0|, |0,1\rangle\langle 0,1|, |1,0\rangle\langle 1,0|, |1,1\rangle\langle 1,1|\}$.

Outcome probabilities:

$\Pr(z,x) = \mathrm{Tr}\big[|z,x\rangle\langle z,x|_{AB}\,(H\otimes\mathbb{1})\,U\rho_{AB}U^\dagger\,(H^\dagger\otimes\mathbb{1})\big]$

$\qquad \mathrm{Tr}\big[|z,x\rangle\langle z,x|\,\sigma\big]$

$\mathrm{Tr}[ABC] = \mathrm{Tr}[CAB] = \mathrm{Tr}[BCA]$

$= \mathrm{Tr}\big[(H^\dagger\otimes\mathbb{1})|z,x\rangle\langle z,x|_{AB}(H\otimes\mathbb{1})\,U\rho_{AB}U^\dagger\big]$  (cyclicity of trace)

$= \mathrm{Tr}\big[\underbrace{U^\dagger(H^\dagger\otimes\mathbb{1})|z,x\rangle\langle z,x|_{AB}(H\otimes\mathbb{1})U}_{M_{z,x}}\,\rho_{AB}\big]$  (cyclicity of trace again).

$U^\dagger = U$ (b/c CNOT is Hermitian)

$H^\dagger = H$ (b/c Hadamard is also Hermitian). $\Rightarrow M_{z,x} = U(H\otimes\mathbb{1})|z,x\rangle\langle z,x|(H\otimes\mathbb{1})U$

(1) $U(H\otimes\mathbb{1})|0,0\rangle = \mathrm{CNOT}|+,0\rangle = \mathrm{CNOT}\tfrac{1}{\sqrt{2}}(|0\rangle|0\rangle + |1\rangle|0\rangle)$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(\mathrm{CNOT}|0\rangle|0\rangle + \underbrace{\mathrm{CNOT}|1\rangle|0\rangle}_{=|1\rangle|1\rangle})$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(|0\rangle|0\rangle + |1\rangle|1\rangle)$

$\qquad\qquad = |\Phi^+\rangle$

$\Rightarrow M_{0,0} = \Phi^+$

$|+\rangle = \tfrac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$

(2) $U(H\otimes\mathbb{1})|0,1\rangle = \mathrm{CNOT}|+,1\rangle = \mathrm{CNOT}\tfrac{1}{\sqrt{2}}(|0\rangle|1\rangle + |1\rangle|1\rangle)$

$\qquad\qquad = \tfrac{1}{\sqrt{2}}(\mathrm{CNOT}|0\rangle|1\rangle + \mathrm{CNOT}|1\rangle|1\rangle)$
