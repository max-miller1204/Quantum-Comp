# ① Universal Gate Sets

- We want to use a set of elementary gates to execute <u>arbitrary</u> unitaries on $n$ qubits.

[Diagram: a quantum circuit on 4 wires showing several single-qubit boxes and two-qubit boxes spanning adjacent wires arranged in columns, illustrating decomposition of an arbitrary unitary into elementary gates.]

- <u>Two versions</u>: 
  - Exact  ↓ Requires (uncountably) infinite # of gates in the set.
  - Approximate. → we can allow for some error/deviation in the implementation. → Relevant when we want the set to be finite.

(a) <u>Exact case</u>: CNOT + all single-qubit gates are universal! ( ✱ This set <u>is not finite</u>.)

> **Lemma 4.1.** Every unitary $2\times 2$ matrix can be expressed as
> $$\begin{pmatrix} e^{i\delta} & 0 \\ 0 & e^{i\delta} \end{pmatrix} \begin{pmatrix} e^{i\alpha/2} & 0 \\ 0 & e^{-i\alpha/2} \end{pmatrix} \begin{pmatrix} \cos\theta/2 & \sin\theta/2 \\ -\sin\theta/2 & \cos\theta/2 \end{pmatrix}$$
> $$\times \begin{pmatrix} e^{i\beta/2} & 0 \\ 0 & e^{-i\beta/2} \end{pmatrix},$$
> where $\delta, \alpha, \theta,$ and $\beta$ are real valued. Moreover, any special unitary $2\times 2$ matrix (i.e., with unity determinant) can be expressed as
> $$\begin{pmatrix} e^{i\alpha/2} & 0 \\ 0 & e^{-i\alpha/2} \end{pmatrix} \begin{pmatrix} \cos\theta/2 & \sin\theta/2 \\ -\sin\theta/2 & \cos\theta/2 \end{pmatrix} \begin{pmatrix} e^{i\beta/2} & 0 \\ 0 & e^{-i\beta/2} \end{pmatrix}.$$

✱ Recall the rotation gates!

$$R_x(\theta) = e^{-i\frac{\theta}{2}X} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)X$$

$$R_y(\theta) = e^{-i\frac{\theta}{2}Y} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Y$$

$$R_z(\theta) = e^{-i\frac{\theta}{2}Z} = \cos\!\left(\tfrac{\theta}{2}\right)\mathbb{1} - i\sin\!\left(\tfrac{\theta}{2}\right)Z$$

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\quad Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix},\quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

<u>Observe</u>: 
$$R_y(\theta) = \begin{pmatrix} \cos(\tfrac{\theta}{2}) & 0 \\ 0 & \cos(\tfrac{\theta}{2}) \end{pmatrix} - i\begin{pmatrix} 0 & -i\sin(\tfrac{\theta}{2}) \\ i\sin(\tfrac{\theta}{2}) & 0 \end{pmatrix} = \begin{pmatrix} \cos(\tfrac{\theta}{2}) & -\sin(\tfrac{\theta}{2}) \\ \sin(\tfrac{\theta}{2}) & \cos(\tfrac{\theta}{2}) \end{pmatrix}$$
