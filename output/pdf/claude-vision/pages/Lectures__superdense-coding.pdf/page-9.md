Therefore, $\text{Tr}(Z^a X^b) = 2\, \delta_{a,0}\, \delta_{b,0}$. $\quad a, b \in \{0,1\}$

Check: $a=0, b=0 \Rightarrow \text{Tr}(\mathbb{1}) = 2$
$\phantom{Check:}\, a=0, b=1 \Rightarrow \text{Tr}(X) = 0$
$\phantom{Check:}\, a=1, b=0 \Rightarrow \text{Tr}(Z) = 0$
$\phantom{Check:}\, a=1, b=1 \Rightarrow \text{Tr}(ZX) = 0$.

Finally: $\braket{v_1 | v_2} = \frac{1}{2} \text{Tr}\bigl(X^{x \oplus x'} Z^{z' \oplus z}\bigr) = \delta_{x \oplus x', 0}\, \delta_{z' \oplus z, 0}$

[arrows above exponents labeling $a$ and $b$]

But $x \oplus x' = 0 \iff x = x'$ and $z' \oplus z = 0 \iff z' = z$

$\Rightarrow \delta_{x \oplus x', 0} = \delta_{x, x'}$ and $\delta_{z' \oplus z, 0} = \delta_{z', z}$.

So $\braket{v_1 | v_2} = \delta_{x, x'}\, \delta_{z, z'}$.

Similarly $\braket{v_2 | v_1} = \overline{\braket{v_1 | v_2}} = \delta_{x, x'}\, \delta_{z, z'}$.

So $\text{Tr}\bigl(E^{z', x'}\, E^{z, x}\bigr) = \delta_{x, x'}\, \delta_{z, z'}$. ∎

---

❋ <u>Recap</u>: Superdense coding allows Alice to send two bits to Bob using only one qubit — as long as the qubit is already entangled with Bob's qubit.

This worked b/c the 4 Bell states were used to encode the information and do the measurement — and b/c the Bell states are orthogonal, they are perfectly distinguishable.

❋ <u>Why is this interesting?</u>

With just a single (unentangled) qubit, we cannot successfully (w/ prob. 1) transmit more than one bit of information.
