(d) $\text{CNOT}(\mathbb{1} \otimes Z) = (Z \otimes Z)\text{CNOT}$.

$$
\begin{array}{c}
[\text{Circuit: top wire is control (dot), bottom wire has } Z \text{ then target } \oplus] \quad = \quad [\text{Circuit: top wire is control (dot) then } Z; \text{ bottom wire is target } \oplus \text{ then } Z]
\end{array}
\tag{86}
$$

13. Consider the following circuit:

$$
\begin{array}{c}
\ket{0} - H - \bullet - \times - \measuredangle \\
\ket{0} - S - H - \times - \measuredangle
\end{array}
\tag{87}
$$

[Two-qubit circuit: top qubit $\ket{0}$, then $H$, then control of a CZ (vertical line connecting both wires), then SWAP (×), then measurement. Bottom qubit $\ket{0}$, then $S$, then $H$ (after the CZ control acts on top, the controlled gate target is on bottom — actually the vertical line connects the dot on top to bottom wire after $S$), then $H$, then SWAP, then measurement.]

The final measurement is in the Pauli-$Z$ basis. What is the probability of obtaining each outcome?

14. Consider the following circuit:

$$
\begin{array}{c}
\ket{0} - H - \bullet - \bullet - H - \measuredangle \\
\ket{0} - H - \bullet - \bullet - H - \measuredangle \\
\ket{\psi} - \oplus - S - \oplus -
\end{array}
\tag{88}
$$

[Three-qubit circuit. Top qubit: $\ket{0}$, $H$, control, control, $H$, measurement. Middle qubit: $\ket{0}$, $H$, control, control, $H$, measurement. Bottom qubit: $\ket{\psi}$, target $\oplus$ (controlled by both top qubits via Toffoli), $S$, target $\oplus$ (Toffoli again).]

The final measurement is in the Pauli-$Z$ basis.

(a) Show that the probability of both measurement outcomes being 0 is $\frac{5}{8}$.

(b) Show that the circuit applies the gate $R_z(\theta)$ to the third qubit if the measurement outcomes are both 0, where $\theta$ is given by $\cos(\theta) = \frac{3}{5}$; otherwise, the circuit applies $Z$ to the third qubit.

15. Recall the following circuit for the Hadamard test:

$$
\begin{array}{c}
\ket{0} - H - \bullet - H - \measuredangle \\
\ket{\psi} - U -
\end{array}
\tag{89}
$$

Here, $U$ is an arbitrary unitary and can act on an arbitrary number of qubits. Using this circuit, it is possible to determine the real part of $\braket{\psi|U|\psi}$, i.e., $\text{Re}(\braket{\psi|U|\psi})$.

Now, show that by adding the $S$ gate as follows, it is possible to also calculate the imaginary part of the inner product, namely, $\text{Im}(\braket{\psi|U|\psi})$.

$$
\begin{array}{c}
\ket{0} - H - S - \bullet - H - \measuredangle \\
\ket{\psi} - U -
\end{array}
\tag{90}
$$

20
