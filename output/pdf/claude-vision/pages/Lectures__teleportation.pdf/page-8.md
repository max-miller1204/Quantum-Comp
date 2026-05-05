**Summary:**
- $\Pr(0,0) = \tfrac{1}{4} \to$ State $\ket{\psi}$ for Bob.
- $\Pr(0,1) = \tfrac{1}{4} \to$ State $X\ket{\psi}$ for Bob.
- $\Pr(1,0) = \tfrac{1}{4} \to$ State $Z\ket{\psi}$ for Bob.
- $\Pr(1,1) = \tfrac{1}{4} \to$ State $XZ\ket{\psi}$ for Bob.

(5) After the measurement, Alice communicates the outcomes to Bob.

(6) Depending on the outcome, Bob applies a __correction__:

[column labels in red: $z\ \ x$]

$0,0 \to$ No correction

$0,1 \to$ Apply Pauli-$X$  $\quad X(X\ket{\psi}) = \underbrace{X^2}_{=\mathbb{1}}\ket{\psi} = \ket{\psi}$

$1,0 \to$ Apply Pauli-$Z$  $\quad Z(Z\ket{\psi}) = \underbrace{Z^2}_{=\mathbb{1}}\ket{\psi} = \ket{\psi}$

$1,1 \to$ Apply Pauli-$X$, then Pauli-$Z$

Then Bob recovers Alice's state!

⊛ Teleportation is __not__ instantaneous / faster than light — it only works if Bob gets Alice's measurement outcomes ⤳ this takes time!

⊛ The teleported state can also be a mixed state.
