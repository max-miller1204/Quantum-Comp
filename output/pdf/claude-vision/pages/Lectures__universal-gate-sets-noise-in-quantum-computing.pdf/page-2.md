$$R_z(\theta) = \begin{pmatrix} \cos(\frac{\theta}{2}) & 0 \\ 0 & \cos(\frac{\theta}{2}) \end{pmatrix} - i \begin{pmatrix} \sin(\frac{\theta}{2}) & 0 \\ 0 & -\sin(\frac{\theta}{2}) \end{pmatrix} \qquad e^{i\varphi} = \cos(\varphi) + i\sin(\varphi)$$

$$= \begin{pmatrix} \cos(\frac{\theta}{2}) - i\sin(\frac{\theta}{2}) & 0 \\ 0 & \cos(\frac{\theta}{2}) + i\sin(\frac{\theta}{2}) \end{pmatrix}$$

$$= \begin{pmatrix} e^{-i\frac{\theta}{2}} & 0 \\ 0 & e^{i\frac{\theta}{2}} \end{pmatrix}$$

★ So every single-qubit gate can be decomposed into rotation gates:

$$U = R_z(\alpha)\, R_y(\theta)\, R_z(\beta), \quad \text{for appropriate angles } \alpha, \beta, \theta.$$

> *Lemma 5.1.* For a unitary $2\times 2$ matrix $W$, a $\wedge_1(W)$ gate can be simulated by a network of the form
>
> [Circuit diagram: controlled-$W$ gate equals a circuit with control line passing through CNOTs interleaved with single-qubit gates $A$, $B$, $C$ on the target line: $-A-\oplus-B-\oplus-C-$, with controls on the top wire.]
>
> where $A$, $B$, and $C \in SU(2)$ if and only if $W \in SU(2)$.

(b) <u>Approximate case</u>: Arises when the # of gates in the set is finite

(B/c the set of unitaries is uncountably infinite, while the set of sequences of gates from a finite set will be countably infinite.)

★ <mark>Theorem:</mark> <u>Clifford gates</u> + <u>one single-qubit non-Clifford gate</u> is universal!

$$\hookrightarrow T \text{ gate!} \quad T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$$

– Recall Pauli operators on $n$ qubits: $\mathcal{P}_n = \{I, X, Y, Z\}^{\otimes n} \to P = I \otimes X \otimes Y \otimes X \otimes Z$
$$\hookrightarrow 4^n$$

$\to$ Let $\mathcal{P}_n^* = \mathcal{P}_n \setminus \{I^{\otimes n}\}$
$\hookrightarrow$ exclude the identity gate.
