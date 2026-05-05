# Lectures__measurements(III)+entanglement.pdf

## Page 1

# 1. Measurements

- Every orthonormal basis $\{\ket{e_k}\}_{k=1}^{d}$ in dimension $d$ defines a __measurement__: operators $\{\ket{e_k}\bra{e_k}\}_{k=1}^{d}$ such that $\sum_{k=1}^{d} \ket{e_k}\bra{e_k} = \mathbb{1}_d$.

For a state $\rho$:  $\Pr(k) = \mathrm{Tr}\big[\ket{e_k}\bra{e_k}\rho\big] = \braket{e_k|\rho|e_k}$  ("Born rule")

$$\sum_{k=1}^{d} \Pr(k) = \mathrm{Tr}\Big[\underbrace{\Big(\sum_{k=1}^{d} \ket{e_k}\bra{e_k}\Big)}_{=\,\mathbb{1}_d}\rho\Big] = \mathrm{Tr}(\rho) = 1.$$

⊛ __Example__: For the state $\rho = \frac{\mathbb{1}}{d}$ (the "maximally-mixed" state), the outcomes are completely random in every basis! (i.e., $\Pr(k) = \frac{1}{d}\ \forall\, k$).

- For a bipartite state $\rho_{AB} \rightarrow$ measuring $A$ only: $\Pr(k) = \mathrm{Tr}\big[(\ket{e_k}\bra{e_k}_A \otimes \mathbb{1}_B)\,\rho_{AB}\big]$

This is equal to $\Pr(k) = \mathrm{Tr}\big[\ket{e_k}\bra{e_k}_A\, \mathrm{Tr}_B(\rho_{AB})\big]$
$$\uparrow$$
$$\text{\underline{Partial trace}}$$

⊛ For an operator $M_{AB} = \displaystyle\sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,j;\,k,\ell}\, \ket{i}\bra{j}_A \otimes \ket{k}\bra{\ell}_B.$

$$\mathrm{Tr}_B(X_A \otimes Y_B) = X_A \cdot \mathrm{Tr}(Y_B)$$

$$\mathrm{Tr}_B(M_{AB}) = \sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,k;\,j,\ell}\, \ket{i}\bra{j}_A\, \underbrace{\mathrm{Tr}(\ket{k}\bra{\ell}_B)}_{\delta_{k,\ell}}$$

$$= \sum_{i,j=0}^{d_A-1}\Big(\sum_{k=0}^{d_B-1} M_{i,k;\,j,k}\Big)\ket{i}\bra{j}_A$$

$$\mathrm{Tr}_A(M_{AB}) = \sum_{i,j=0}^{d_A-1}\sum_{k,\ell=0}^{d_B-1} M_{i,j;\,k,\ell}\, \underbrace{\mathrm{Tr}(\ket{i}\bra{j}_A)}_{\delta_{i,j}}\ket{k}\bra{\ell}_B = \sum_{k,\ell=0}^{d_B-1}\Big(\sum_{i=0}^{d_A-1} M_{i,k;\,i,\ell}\Big)\ket{k}\bra{\ell}_B.$$

## Page 2

For a two-qubit operator: 
$$M_{AB} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{pmatrix} \overset{00}{a_{11}} & \overset{01}{a_{12}} & \overset{10}{a_{13}} & \overset{11}{a_{14}} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}$$

$$\mathrm{Tr}_B(M_{AB}) = \mathrm{Tr}_B\!\left[\begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}\right] = \begin{pmatrix} a_{11}+a_{22} & a_{13}+a_{24} \\ a_{31}+a_{42} & a_{33}+a_{44} \end{pmatrix}$$

[The 4×4 matrix is partitioned into 2×2 blocks; within each block, the diagonal entries are summed to produce the corresponding entry of the reduced 2×2 matrix. Color-coding: $a_{11},a_{22}$ (orange) → top-left; $a_{13},a_{24}$ (pink) → top-right; $a_{31},a_{42}$ (purple) → bottom-left; $a_{33},a_{44}$ (red) → bottom-right.]

$$\mathrm{Tr}_A(M_{AB}) = \mathrm{Tr}_A\!\left[\begin{pmatrix} a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34} \\ a_{41} & a_{42} & a_{43} & a_{44} \end{pmatrix}\right] = \begin{pmatrix} a_{11}+a_{33} & a_{12}+a_{34} \\ a_{21}+a_{43} & a_{22}+a_{44} \end{pmatrix}$$

[Color-coding: $a_{11},a_{33}$ (orange) → top-left; $a_{12},a_{34}$ (pink) → top-right; $a_{21},a_{43}$ (purple) → bottom-left; $a_{22},a_{44}$ (red) → bottom-right.]

— The most general form of a measurement is given by a <u>positive operator-valued measure (POVM)</u>: a (finite) set $\{M_x\}_{x \in \mathcal{X}}$ ← outcome labels.

(1) $M_x \geq 0 \quad \forall\, x \in \mathcal{X}$

(2) $\sum_x M_x = \mathbb{1}$.

- Probabilities are given by $\Pr(x) = \mathrm{Tr}(M_x \rho)$

❋ <u>Check</u>: $\sum_{x \in \mathcal{X}} \Pr(x) = \sum_{x \in \mathcal{X}} \mathrm{Tr}(M_x \rho) = \mathrm{Tr}\!\left[\underbrace{\left(\sum_x M_x\right)}_{=\mathbb{1}}\rho\right] = \mathrm{Tr}(\rho) = 1.$ ✓

## Page 3

- Measurements of the form $\{\ket{e_k}\bra{e_k}\}_{k=1}^{d}$, for an orthonormal basis $\{\ket{e_k}\}_{k=1}^{d}$, are known as <u>projective measurements</u>, b/c $M_k \equiv \ket{e_k}\bra{e_k}$ are <u>projectors</u>.

> ✱ A <u>projector</u> is an operator/matrix satisfying $P^2 = P$.
>
> <u>Check</u>: $\big(\ket{e_k}\bra{e_k}\big)^2 = \ket{e_k}\underbrace{\braket{e_k|e_k}}_{=1}\bra{e_k} = \ket{e_k}\bra{e_k}\ \checkmark$

- A <u>general projective measurement</u> has the form $\{\Pi_x\}_{x \in X}$:

  (1) $\Pi_x \geq 0 \quad \forall x \in X$

  (2) $\Pi_x^2 = \Pi_x \quad \forall x \in X$

  (3) $\sum_{x \in X} \Pi_x = \mathbb{1}$.

- <u>Theorem</u>: Every general (POVM) measurement can be written as a projective measurement on a larger system.

  <u>Proof</u>: Consider a system $S$; we want to measure it via a probe $P$.

  [Circuit diagram: top wire labeled $\rho_S$ entering box $U$; bottom wire labeled $\ket{0}$ entering box $U$; bottom output of $U$ goes into a measurement box labeled $x$, $\{\Pi_x\}_x$ ← Projective measurement of the probe.]

  ↑ <span style="color:red">Unitary interaction of system and probe.</span>

$$\rho_S \otimes \ket{0}\bra{0}_P \;\mapsto\; U(\rho_S \otimes \ket{0}\bra{0})U^\dagger \;\mapsto\; \underline{\Pr[x] = \mathrm{Tr}\!\left[(\mathbb{1}_S \otimes \Pi_x)\, U(\rho_S \otimes \ket{0}\bra{0})U^\dagger\right]}$$

✱ We can write this in the form $\mathrm{Tr}[M_x \rho_S]$.

## Page 4

$$\text{Tr}\left[(\mathbb{1}_S \otimes \Pi_x) U (\rho_S \otimes \ket{0}\bra{0}_p) U^\dagger\right] = \text{Tr}\left[(\rho_S \otimes \ket{0}\bra{0}) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$\text{Tr}[ABC] = \text{Tr}[BCA] = \text{Tr}[CAB].$

$(X_A \otimes Y_B) = (X_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes Y_B)$

$\text{Tr}\left[(\rho_A \otimes \mathbb{1}_B) M_{AB}\right] = \text{Tr}\left[\rho_A \, \text{Tr}_B[M_{AB}]\right]$

$$= \text{Tr}\left[(\rho_S \otimes \mathbb{1}_p)(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$$= \text{Tr}\left[\rho_S \, \underbrace{\text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]}_{\equiv M_x}\right]$$

Let us show that $\{M_x\}_{x \in \mathcal{X}}$ is a POVM.

(1) Check that $M_x \geq 0.$  $\quad \langle v | M_x | v \rangle \geq 0 \;\; \forall \ket{v}$

For an arbitrary vector $\ket{v}$:

$$\langle v | M_x | v \rangle = \langle v | \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right] | v \rangle$$

$\text{Tr}[M \ket{v_1}\bra{v_2}]$
$= \langle v_2 | M | v_1 \rangle$

$$= \text{Tr}\left[(\ket{v}\bra{v}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right]$$

$$= \underbrace{(\bra{v}_S \otimes \bra{0}_p) U^\dagger}_{\equiv \bra{v'}} (\mathbb{1}_S \otimes \Pi_x) \underbrace{U (\ket{v}_S \otimes \ket{0}_p)}_{\equiv \ket{v'}}$$

$$= \langle v' | (\mathbb{1}_S \otimes \Pi_x) | v' \rangle$$

$\geq 0$ b/c $\Pi_x \geq 0$ and $\mathbb{1}_S \geq 0 \Rightarrow \mathbb{1}_S \otimes \Pi_x \geq 0.$

So $M_x \geq 0 \;\checkmark\; \forall x$

(2) Check that $\sum_{x \in \mathcal{X}} M_x = \mathbb{1}.$

$$\sum_{x \in \mathcal{X}} M_x = \sum_{x \in \mathcal{X}} \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \Pi_x) U\right] = \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) U^\dagger (\mathbb{1}_S \otimes \underbrace{\sum_{x \in \mathcal{X}} \Pi_x}_{=\mathbb{1}_p \text{ by assumption}}) U\right]$$

$$= \text{Tr}_p\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_p) \underbrace{U^\dagger (\mathbb{1}_S \otimes \mathbb{1}_p) U}_{\mathbb{1}_S \otimes \mathbb{1}_p}\right] \quad \rightarrow U^\dagger U = \mathbb{1}$$

## Page 5

$$\downarrow$$
$$= \mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{0}\bra{0}_P)(\mathbb{1}_S \otimes \mathbb{1}_P)\right]$$
$$= \mathrm{Tr}_P\left[\mathbb{1}_S \otimes \ket{0}\bra{0}_P\right]$$
$$= \mathbb{1}_S. \checkmark$$

We also prove the converse: given a POVM $\{M_x\}_{x \in X}$, the measurement can be realised by a unitary b/w system and probe and measurement of the probe.

Define $V = \sum_{x \in X} \sqrt{M_x} \otimes \underbrace{\ket{x}_P}_{\text{some orthonormal vectors.}}$

$\quad\left(\circledast \underline{\text{Note}}: M_x \text{ is Hermitian, so it has spectral decomposition}\right.$
$\quad\left. M_x = \sum_{k=1}^{r} \lambda_k \ket{\varphi_k}\bra{\varphi_k}. \text{ Then the square root is } \sqrt{M_x} = \sum_{k=1}^{r} \sqrt{\lambda_k} \ket{\varphi_k}\bra{\varphi_k}.\right)$

$\circledast$ $V$ is an isometry: it satisfies
$V^\dagger V = \mathbb{1}$ (but not necessarily $VV^\dagger = \mathbb{1}$.)

$\underline{\text{Check}}: V^\dagger V = \left(\sum_x \sqrt{M_x} \otimes \bra{x}_P\right)\left(\sum_{x' \in X} \sqrt{M_{x'}} \otimes \ket{x'}_P\right)$
$$\downarrow$$
$$= \sum_{x,x' \in X} \sqrt{M_x}\sqrt{M_{x'}} \underbrace{\braket{x|x'}}_{=\delta_{x,x'}} = \sum_{x \in X} M_x = \mathbb{1} \checkmark$$

Now note that $\mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{x}\bra{x}_{P}) VV^\dagger\right] = \mathrm{Tr}_P\left[(\mathbb{1}_S \otimes \ket{x}\bra{x})\left(\sum_{x_1 \in X} \sqrt{M_{x_1}} \otimes \ket{x_1}\right)\left(\sum_{x_2 \in X} \sqrt{M_{x_2}} \otimes \bra{x_2}\right)\right]$

$$\downarrow$$
$$= \sum_{x_1, x_2 \in X} \mathrm{Tr}_P\left[\sqrt{M_{x_1}}\sqrt{M_{x_2}} \otimes \underbrace{\ket{x}\braket{x|x_1}\bra{x_2}}_{=\delta_{x,x_1}}\right]$$

$$\downarrow$$
$$= \sum_{x_1, x_2 \in X} \sqrt{M_{x_1}}\sqrt{M_{x_2}}\, \delta_{x,x_1} \underbrace{\braket{x_2|x}}_{=\delta_{x,x_2}}$$

$$\downarrow$$
$$= M_x.$$

## Page 6

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

## Page 7

# 2. Entanglement

**※** State vectors of two qubits belong to the tensor-product space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

(a) — A **product state (vector)** has the form:

(State vector) $\quad \ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B, \quad \ket{\phi_1} \in \mathbb{C}^{d_1}, \quad \ket{\phi_2} \in \mathbb{C}^{d_2}.$

(Density operator). $\quad \rho_{AB} = \sigma_A \otimes \tau_B, \quad \sigma_A \in L(\mathbb{C}^{d_A})$ and $\tau_B \in L(\mathbb{C}^{d_B})$ are density operators.

[Diagram: Alice with her atom on the left, Bob with his atom on the right, no connection between them]

$$\rho_{AB} = \sigma_A \otimes \tau_B$$

*Product state*
Alice and Bob individually prepare their systems.

— A **separable state** has the form: $\quad \rho_{AB} = \sum_x p(x) \, \sigma_A^x \otimes \tau_B^x$

↳ Also called "classically correlated" $\qquad$ ↳ probabilities.

[Diagram: Alice with her atom on the left connected via classical communication lines (double arrows) to Bob with his atom on the right]

$$\rho_{AB} = \sum_{x \in \mathcal{X}} p(x)\, \sigma_A^x \otimes \tau_B^x$$

*Separable state*
Alice and Bob individually prepare their systems via local operations and classical communication.

## Page 8

⊛ **Example:** $\rho_{AB} = \frac{1}{2}\left(\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B + \ket{1}\bra{1}_A \otimes \ket{1}\bra{1}_B\right) = \frac{1}{2}\left(\ket{0,0}\bra{0,0}_{AB} + \ket{1,1}\bra{1,1}_{AB}\right)$

This state is <u>diagonal</u> in the tensor-product basis

$$\{\ket{0}_A \otimes \ket{0}_B,\ \ket{0}_A \otimes \ket{1}_B,\ \ket{1}_A \otimes \ket{0}_B,\ \ket{1}_A \otimes \ket{1}_B\}$$

$$\rho_{AB} = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix} \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}$$

[column labels: 00, 01, 10, 11]

⊛ **If Alice and Bob both measure in the $\{\ket{0}, \ket{1}\}$ basis, then their outcomes will be correlated!**

- If Alice gets outcome "0", then so will Bob. Same with outcome "1".

$$\text{Tr}_A\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B)\rho_{AB}\right] = \frac{1}{2}\ket{0}\bra{0}_B \rightarrow \rho_B^{(0)} = \ket{0}\bra{0}_B.\ \text{Also,}\ \rho_B^{(1)} = \ket{1}\bra{1}.$$

$$= \text{Tr}_A\left[(\ket{0}\bra{0}_A \otimes \mathbb{1}_B) \cdot \frac{1}{2}\left(\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B + \ket{1}\bra{1}_A \otimes \ket{1}\bra{1}_B\right)\right]$$

$$= \frac{1}{2}\left(\text{Tr}_A\left[\ket{0}\bra{0}\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B\right] + \text{Tr}_A\left[\underbrace{\ket{0}\bra{0}\ket{1}\bra{1}}_{=\,0}{}_A \otimes \ket{1}\bra{1}_B\right]\right)$$

$$= \frac{1}{2}\text{Tr}_A\left[\ket{0}\bra{0}_A \otimes \ket{0}\bra{0}_B\right]$$

$$= \frac{1}{2}\ket{0}\bra{0}_B$$

## Page 9

- **But this is not the case for all measurements!**
  If they both measure in $\{\ket{+}, \ket{-}\}$ basis instead, then the outcomes are completely uncorrelated!
  $$\Pr(+,+) = \Pr(+,-) = \Pr(-,+) = \Pr(-,-) = \tfrac{1}{4}.$$

  If Alice gets outcome "+" (happens with probability $\tfrac{1}{2}$), then Bob's state is
  $$\rho_B^{(+)} = \tfrac{1}{1/2} \operatorname{Tr}_A\!\left[(\ket{+}\!\bra{+}_A \otimes \mathbb{1}_B)\rho_{AB}\right] = \tfrac{\mathbb{1}}{2} \rightarrow \text{completely random for Bob!}$$

- So, in this case, the correlations depend on the basis choice!

✱ **Aside**: All states of two probabilistic bits can be expressed as diagonal density matrices in the computational basis.

$$\rho_{AB} = \begin{array}{c} {\scriptstyle 00} \\ {\scriptstyle 01} \\ {\scriptstyle 10} \\ {\scriptstyle 11} \end{array}\!\!\begin{pmatrix} p_{00} & & & 0 \\ & p_{01} & & \\ & & p_{10} & \\ 0 & & & p_{11} \end{pmatrix}$$
$$\quad\quad\,\,\,{\scriptstyle 00\;\;01\;\;10\;\;11}$$

✱ Even one bit!
$$\rho = \begin{pmatrix} p_1 & \\ & p_2 \end{pmatrix} = \tfrac{1}{2}\left(p_1 \ket{0}\!\bra{0} + p_2 \ket{1}\!\bra{1}\right)$$
describes an arbitrary state of one bit!

## Page 10

- An <mark>entangled state</mark> is NOT a separable state.

[Diagram: Alice (left) and Bob (right) each holding a box containing an atom, connected by a wavy line representing entanglement]

$$\rho_{AB} \neq \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Entangled state*

Correlations between Alice and Bob are non-local.
State of the individual systems not sufficient to describe the pair.

$Z\ket{0} = \ket{0}$
$Z\ket{1} = -\ket{1}$

(b) <u>Examples</u>:

1. The <mark>Bell states</mark>

$$\ket{\Phi_{0,0}} = \ket{\Phi^+}, \quad (Z \otimes \mathbb{1})\ket{\Phi^+} = \tfrac{1}{\sqrt{2}}(Z\ket{0}\ket{0} + Z\ket{1}\ket{1})$$
$$= \tfrac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1}) \quad\quad = \tfrac{1}{\sqrt{2}}(\ket{0,0} - \ket{1,1})$$
$$= \ket{\Phi^-}$$

$$\Phi^{\pm} = \ket{\Phi^{\pm}}\bra{\Phi^{\pm}}, \quad \ket{\Phi^{\pm}} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1})$$

$$\Psi^{\pm} = \ket{\Psi^{\pm}}\bra{\Psi^{\pm}}, \quad \ket{\Psi^{\pm}} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0})$$

Observe that $\{\ket{\Phi^{\pm}}, \ket{\Psi^{\pm}}\} \longleftrightarrow \{\underbrace{(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}}_{\ket{\Phi_{z,x}}} : z, x \in \{0,1\}\}$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad Z^0 = \mathbb{1},\ Z^1 = Z$$
$$X^0 = \mathbb{1},\ X^1 = X$$

$0,0 \leftrightarrow \Phi^+$
$0,1 \leftrightarrow \Psi^+$
$1,0 \leftrightarrow \Phi^-$
$1,1 \leftrightarrow \Psi^-$

→ <u>In $d$ dimensions</u>: $\ket{\Phi_d^+} := \tfrac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k,k} \quad (d=3) \ \tfrac{1}{\sqrt{3}}(\ket{0}\ket{0} + \ket{1}\ket{1} + \ket{2}\ket{2})$

(See later for the other $d$-dimensional Bell states.)

$$\ket{\Phi^+} = \begin{pmatrix} 00 \\ 01 \\ 10 \\ 11 \end{pmatrix}\!\!\begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Phi^-} = \begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ -\tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Psi^+} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}, \quad \ket{\Psi^-} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ -\tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$$

## Page 11

$$(X \otimes I)\ket{\Phi^+} = \frac{1}{\sqrt{2}}\left(\underbrace{X\ket{0}}_{\ket{1}}\ket{0} + \underbrace{X\ket{1}}_{\ket{0}}\ket{1}\right) = \frac{1}{\sqrt{2}}\left(\ket{1}\ket{0} + \ket{0}\ket{1}\right) = \ket{\Psi^+}$$

$$(ZX \otimes I)\ket{\Phi^+} = \frac{1}{\sqrt{2}}\left(ZX\ket{0}\ket{0} + ZX\ket{1}\ket{1}\right) = \frac{1}{\sqrt{2}}\left(-\ket{1}\ket{0} + \ket{0}\ket{1}\right) = \ket{\Psi^-}$$

$$\begin{aligned} Z\ket{1} &= -\ket{1} & Z\ket{0} &= \ket{0} \end{aligned}$$

## Page 12

✳️ $\ket{\psi_1} = \alpha_1 \ket{0} + \beta_1 \ket{1}, \quad \ket{\psi_2} = \alpha_2 \ket{0} + \beta_2 \ket{1}$

$\ket{\psi_1} \otimes \ket{\psi_2} = \alpha_1 \alpha_2 \ket{0,0} + \alpha_1 \beta_2 \ket{0,1} + \beta_1 \alpha_2 \ket{1,0} + \beta_1 \beta_2 \ket{1,1} \neq \tfrac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1})$

There does not exist values of $\alpha_1, \alpha_2, \beta_1, \beta_2$ such that $\ket{\psi_1} \otimes \ket{\psi_2} = \ket{\Phi^+}$.

---

✳️ $\{\ket{\Phi_{z,x}} : z, x \in \{0,1\}\}$ is an ONB for $\mathbb{C}^2 \otimes \mathbb{C}^2$

$$\underbrace{U \ket{z, x}}_{} = \ket{\Phi_{z,x}}$$

↳ $U$ is a **unitary matrix**: $U^\dagger U = \mathbb{1} = U U^\dagger \iff U^\dagger = U^{-1}$
   (change-of-basis matrix)

$\Rightarrow \{\ket{\Phi_{z,x}}\bra{\Phi_{z',x'}} : z, x, z', x' \in \{0,1\}\}$ is an ONB for $L(\mathbb{C}^2 \otimes \mathbb{C}^2)$

$\Rightarrow \rho_{AB} = \displaystyle\sum_{\substack{z,x \in \{0,1\} \\ z',x' \in \{0,1\}}} \underbrace{C_{z,x,z',x'}}_{\in \mathbb{C}} \, \ket{\Phi_{z,x}}\bra{\Phi_{z',x'}}_{AB}$

---

✳️ $\displaystyle\sum_{z,x \in \{0,1\}} \mathbb{P}^{z,x}_{AB} = \mathbb{1}_{AB} \longrightarrow$ Bell states form a **measurement** (POVM)

   ↳ Important ingredient in teleportation.
