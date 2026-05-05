(\*) $\{\ket{\phi}\bra{\phi}, \mathbb{1}-\ket{\phi}\bra{\phi}\}$ is a measurement that tells us whether or not a given state is equal to $\ket{\phi}\bra{\phi}$.

It has two outcomes (b/c the set has two operators).

- $\ket{\phi}\bra{\phi} \equiv$ "yes, the state is $\ket{\phi}\bra{\phi}$"
- $\mathbb{1} - \ket{\phi}\bra{\phi} \equiv$ "no, the state is not $\ket{\phi}\bra{\phi}$".

(\*) For a given state $\rho$, $\Pr[\phi] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\rho\right]$  $\quad$ <span style="color:blue">Born Rule: $\{M_x\}$ POVM<br>State $\rho \to \Pr(x) = \text{Tr}(M_x \rho)$.</span>

$$\Pr[\text{not } \phi] = \text{Tr}\!\left[(\mathbb{1} - \ket{\phi}\bra{\phi})\rho\right] = \text{Tr}(\rho) - \text{Tr}\!\left[\ket{\phi}\bra{\phi}\rho\right] = 1 - \Pr[\phi].$$

- If $\rho = \ket{\phi}\bra{\phi}$ itself, then $\Pr[\phi] = \text{Tr}\!\left[\underbrace{\ket{\phi}\braket{\phi|\phi}\bra{\phi}}_{=1}\right] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\right] = \braket{\phi|\phi} = 1.$ ✓

  $\Pr[\text{not } \phi] = 1 - \Pr[\phi] = 0$

- If $\rho = \ket{\gamma}\bra{\gamma}$, then $\Pr[\phi] = \text{Tr}\!\left[\ket{\phi}\bra{\phi}\ket{\gamma}\bra{\gamma}\right] = |\braket{\phi|\gamma}|^2 \to$ fidelity!

(\*) So the swap test allows us to do the measurement $\{\ket{\phi}\bra{\phi}, \mathbb{1} - \ket{\phi}\bra{\phi}\}$ and estimate the fidelity — without even knowing what $\ket{\phi}$ is!

## ② <u>Statistical Estimation from a Quantum Computer.</u>

- When we run a quantum algorithm and do the measurement at the end, the outcomes will generally be probabilistic.

- To extract the relevant information, we have to run the algorithm many times.
