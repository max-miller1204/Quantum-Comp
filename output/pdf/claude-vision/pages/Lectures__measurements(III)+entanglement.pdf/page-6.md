So for any state $\rho$:
$$\text{Tr}[M_x \rho] = \text{Tr}\left[\text{Tr}_P\left[(\mathbb{1}_S \otimes \ket{x}\bra{x}_P) VV^\dagger\right]\rho\right]$$

$$= \text{Tr}\left[(\mathbb{1}_S \otimes \ket{x}\bra{x}_P) VV^\dagger (\rho_S \otimes \mathbb{1}_P)\right]$$

$$= \text{Tr}\left[V^\dagger(\rho_S \otimes \mathbb{1}_P) V (\mathbb{1}_S \otimes \underbrace{\ket{x}\bra{x}_P})\right]$$

<span style="color:red">This defines a projective measurement b/c $\{\ket{x}\}$ is an ONB.</span>

<span style="color:red">⊛ **Fact:** for every isometry $V_{S \to SP}$, there exists a unitary $U_{SP}$ such that $V_{S \to SP} = U_{SP}(\mathbb{1}_S \otimes \ket{0}_P)$.</span>

$$= \text{Tr}\left[U^\dagger(\rho_S \otimes \ket{0}\bra{0}_P) U (\mathbb{1}_S \otimes \ket{x}\bra{x}_P)\right]$$

---

— <u>Post-measurement state after a partial measurement</u>: If we have a bipartite state $\rho_{AB}$, and we measure the A part, what is the resulting state on the B part?

- Consider measurement POVM $\{M_A^{(x)}\}_{x \in X}$.

- The probabilities are $\Pr[x] = \text{Tr}\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]$

- Conditioned on the outcome $x$, the state of B is

$$\rho_B^{(x)} = \frac{\text{Tr}_A\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]}{\text{Tr}\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]} \quad \color{red}{\} \Pr[x]}$$

⊛ Check that $\rho_B^{(x)}$ has all of the required properties of a density matrix.

$$\text{Tr}[\rho_B^{(x)}] = \frac{\text{Tr}\left[\text{Tr}_A\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]\right]}{\color{blue}{\Pr[x]}} = \frac{\text{Tr}\left[(M_A^{(x)} \otimes \mathbb{1}_B) \rho_{AB}\right]}{\color{blue}{\Pr[x]}} = 1 \checkmark$$
