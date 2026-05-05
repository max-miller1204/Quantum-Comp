So $\quad U \ket{j_1, j_2, j_3} = \tilde{U} \ket{j_3, j_2, j_1} = \tilde{U} S \ket{j_1, j_2, j_3}$

$\qquad\qquad\qquad\qquad\qquad\qquad\quad \uparrow$
$\qquad\qquad\qquad\qquad\qquad$ <span style="color:purple">Permutation of the qubits!</span>

★ In general, $\tilde{U}$ is given by the following circuit:

[Quantum circuit diagram with $n$ qubit lines, top to bottom labeled $\ket{j_n}, \ket{j_{n-1}}, \ldots, \ket{j_4}, \ket{j_3}, \ket{j_2}, \ket{j_1}$.

- Bottom wire $\ket{j_1}$: starts with $H$, then acts as control for a sequence of controlled rotation gates $R_2, R_3, R_4, \ldots, R_n$ applied to wires $\ket{j_2}, \ket{j_3}, \ket{j_4}, \ldots, \ket{j_n}$ respectively.
- Next wire $\ket{j_2}$: after the $R_2$ gate from $\ket{j_1}$, has an $H$, then controls $R_2, R_3, \ldots, R_{n-1}$ on the wires above.
- Wire $\ket{j_3}$: has $R_3$ (controlled from $\ket{j_1}$), then later $R_2$ (from $\ket{j_2}$), then $H$, etc.
- Wire $\ket{j_4}$: has $R_4$ (from $\ket{j_1}$), $R_3$ (from $\ket{j_2}$), then $H$ later.
- $\vdots$
- Top wire $\ket{j_n}$: receives $R_n, R_{n-1}, \ldots, R_2$ controlled rotations, then ends with $H$.]
