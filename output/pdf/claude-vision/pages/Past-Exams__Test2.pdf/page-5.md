TOTAL: [-2]

5. (a) Two qubits are in the state given by the vector

$$\frac{i}{\sqrt{10}}\ket{0,0} + \frac{1-2i}{\sqrt{10}}\ket{0,1} + \frac{e^{i\pi/100}}{\sqrt{10}}\ket{1,0} + \frac{\sqrt{3}}{\sqrt{10}}\ket{1,1}.$$

If we measure the qubits in the two-qubit Z-basis $\{\ket{0,0}, \ket{0,1}, \ket{1,0}, \ket{1,1}\}$, what are the possible measurement outcomes and their associated probabilities? What are the possible measurement outcomes and their associated probabilities if instead we measure in the two-qubit X-basis $\{\ket{+,+}, \ket{+,-}, \ket{-,+}, \ket{-,-}\}$?

(b) Consider the following two state vectors:

$$\ket{v_1} = \frac{\sqrt{3}}{2}\ket{0} + \frac{i}{2}\ket{1}, \quad \ket{v_2} = \frac{i}{2}\ket{0} + \frac{\sqrt{3}}{2}\ket{1}$$

i. Prove that $\ket{v_1}$ and $\ket{v_2}$ are orthonormal, and thus that they define a measurement.

ii. Consider a qubit in the state given by

$$\ket{u} = \frac{1}{2}\ket{0} - \frac{\sqrt{3}}{2}\ket{1}.$$

If we measure the state given by $\ket{u}$ with respect to the measurement defined by $\{\ket{v_1}\bra{v_1}, \ket{v_2}\bra{v_2}\}$, then what are the possible outcomes and their associated probabilities?

---

a) $\quad a\ket{0,0} + b\ket{0,1} + c\ket{1,0} + d\ket{1,1}$

$P_A = |a|^2 = \left|\frac{i}{\sqrt{10}}\right|^2 = \boxed{\frac{1}{10}}$

$P_B = |b|^2 = \left|\frac{(1-2i)}{\sqrt{10}}\right|^2 = \frac{1^2}{10} + \frac{-2i^2}{10} = \frac{1}{10} + \frac{4}{10} = \boxed{\frac{5}{10}}$

$P_C = |c|^2 = \left|\frac{e^{i\pi/100}}{\sqrt{10}}\right|^2 = \frac{10}{10} - \frac{9}{10} = \boxed{\frac{1}{10}}$

$P_D = |d|^2 = \left|\frac{\sqrt{3}}{\sqrt{10}}\right|^2 = \boxed{\frac{3}{10}}$

If X-basis → have to factor in $\frac{1}{\sqrt{2}}$ \quad Need more [-2]

b) Orthonormal → orthogonal: $\braket{v_1|v_2} = 0$ \quad i) first orthogonal → $\begin{pmatrix} \frac{\sqrt{3}}{2} & -\frac{i}{2} \end{pmatrix} \begin{pmatrix} \frac{i}{2} \\ \frac{\sqrt{3}}{2} \end{pmatrix}$

Normal: $\braket{v_1|v_1} = 1$
$\braket{v_2|v_2} = 1$ \qquad $= 0$

ii) $\ket{u} = a\ket{0} + b\ket{1}$ \qquad Normal → $\|\ket{v_1}\| = \sqrt{\left(\frac{\sqrt{3}}{2}\right)^2 + \left(\frac{i}{2}\right)^2} = \sqrt{\frac{3}{4} + \frac{1}{4}} = 1$

$P_a = \left|\frac{1}{2}\right|^2 = \frac{1}{4}$ \quad [-2]

$P_b = \left|-\frac{\sqrt{3}}{2}\right|^2 = \frac{3}{4}$ \qquad $\|\ket{v_2}\| = \sqrt{\left(\frac{i}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2} = \sqrt{\frac{1}{4} + \frac{3}{4}} = 1$

6
