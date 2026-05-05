Eigenvalues of $\left(\rho_{AB}^{(p)}\right)^{T_B}$:  $\quad \lambda_1 = \frac{1}{6}(3-2p) \quad$ (multiplicity 3)

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad \lambda_2 = \frac{1}{2}(-1+2p) \quad$ (multiplicity 1).

$\left(\text{\textcolor{purple}{\textasteriskcentered\ We need a negative eigenvalue for entanglement!}}\right)$

[Plot: x-axis labeled $p$ from 0 to 1.0, y-axis from $-0.4$ to $0.4$. Blue line: $\frac{1}{6}(3-2p)$, decreasing from $0.5$ at $p=0$ to about $0.17$ at $p=1$. Orange line: $\frac{1}{2}(-1+2p)$, increasing from $-0.5$ at $p=0$ through $0$ at $p=0.5$ to $0.5$ at $p=1$. Red dashed vertical line at $p=0.5$ marking the boundary. Region $p < 0.5$ labeled "Entangled", region $p > 0.5$ labeled "Separable".]

$$\rho_{AB}^{(p)} = (1-p)\,\Phi_{AB}^{+} + \frac{p}{3}\left(\Phi_{AB}^{-} + \Psi_{AB}^{+} + \Psi_{AB}^{-}\right)$$

\textcolor{red}{\textasteriskcentered\ Observe:} $\operatorname{Tr}\!\left[\rho_{AB}^{(p)}\,\Phi_{AB}^{+}\right] = \bra{\Phi^+}\rho_{AB}^{(p)}\ket{\Phi^+}$

$$= (1-p)\bra{\Phi^+}\Phi_{AB}^{+}\ket{\Phi^+} + \frac{p}{3}\left(\underbrace{\bra{\Phi^+}\Phi_{AB}^{-}\ket{\Phi^+}}_{0} + \underbrace{\bra{\Phi^+}\Psi_{AB}^{+}\ket{\Phi^+}}_{0} + \underbrace{\bra{\Phi^+}\Psi_{AB}^{-}\ket{\Phi^+}}_{0}\right)$$

$$= 1-p \quad\Rightarrow\quad p = 1 - \bra{\Phi^+}\rho_{AB}^{(p)}\ket{\Phi^+}.$$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\hookrightarrow$ This is called the \textbf{\underline{fidelity}}.

\textcolor{red}{\textasteriskcentered\ So $\rho_{AB}^{(p)}$ is entangled if and only if $\quad \bra{\Phi^+}\rho_{AB}^{(p)}\ket{\Phi^+} > \frac{1}{2}$}

---

② **Classical vs. Quantum Correlations: Bell/CHSH Inequality**

- The above criteria for detecting entanglement are purely mathematical.
- In practice, we need to do \underline{measurements} to determine whether or not qubits are entangled.
