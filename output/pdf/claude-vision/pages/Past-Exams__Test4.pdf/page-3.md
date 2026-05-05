3. Consider the following two state vectors, $\ket{v_1} = \frac{\sqrt{3}}{2}\ket{0} + \frac{i}{2}\ket{1}$ and $\ket{v_2} = \frac{i}{2}\ket{0} + \frac{\sqrt{3}}{2}\ket{1}$.

   (a) Prove that $\ket{v_1}$ and $\ket{v_2}$ are orthonormal.
   (b) Show that $\ket{v_1}\bra{v_1} + \ket{v_2}\bra{v_2} = \mathbb{1}$.
   (c) Consider a qubit in the state given by $\ket{u} = \frac{1}{2}\ket{0} - \frac{\sqrt{3}}{2}\ket{1}$. If we measure this state with respect to the measurement $\{\ket{v_1}\bra{v_1}, \ket{v_2}\bra{v_2}\}$, then what are the possible outcomes and their associated probabilities?

---

orthonormal = orthogonal & normal

a) $\braket{v_1|v_2} = \left| \frac{\sqrt{3}}{2} \cdot \frac{\sqrt{3}}{2} \braket{0|1} + \frac{i}{2} \cdot \frac{i}{2} \braket{1|0} \right| = \frac{3}{4} + \frac{i^2}{4} = 1\;?$

[marked $-5$ in red]

$\braket{v_1|v_1} = \left| \left(\frac{\sqrt{3}}{2}\right)^2 + \left(\frac{i}{2}\right)^2 \right| = \frac{3}{4} + \frac{1}{4} = \frac{4}{4} = 1$

$\braket{v_2|v_2} = \left| \left(\frac{i}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2 \right| = \frac{1}{4} + \frac{3}{4} = \frac{4}{4} = 1$

b) $\ket{v_1}\bra{v_1} = \begin{pmatrix} \frac{\sqrt{3}}{2} \\ \frac{i}{2} \end{pmatrix} \begin{pmatrix} \frac{\sqrt{3}}{2} & -\frac{i}{2} \end{pmatrix} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix}$

[marked $-3$ in blue circle, ✓]

$\ket{v_2}\bra{v_2} = \begin{pmatrix} \frac{i}{2} \\ \frac{\sqrt{3}}{2} \end{pmatrix} \begin{pmatrix} -\frac{i}{2} & \frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix}$

$\ket{v_1}\bra{v_1} + \ket{v_2}\bra{v_2} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix} + \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = I$

c) $\ket{v_1}\bra{v_1}\ket{u} = \begin{pmatrix} \frac{3}{4} & 0 \\ 0 & \frac{1}{4} \end{pmatrix} \begin{pmatrix} \frac{1}{2} \\ -\frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{3}{8} \\ -\frac{\sqrt{3}}{8} \end{pmatrix}$

[marked $-2$]

$\ket{v_2}\bra{v_2}\ket{u} = \begin{pmatrix} \frac{1}{4} & 0 \\ 0 & \frac{3}{4} \end{pmatrix} \begin{pmatrix} \frac{1}{2} \\ -\frac{\sqrt{3}}{2} \end{pmatrix} = \begin{pmatrix} \frac{1}{8} \\ -\frac{3\sqrt{3}}{8} \end{pmatrix}$
