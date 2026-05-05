# Lectures__entanglement(II).pdf

## Page 1

# ① Recap: Entanglement

❋ State vectors of two qubits belong to the tensor-product space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

(a) — A **product state (vector)** has the form:

(State vector) $\ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B$, $\ket{\phi_1} \in \mathbb{C}^{d_1}$, $\ket{\phi_2} \in \mathbb{C}^{d_2}$.

(Density operator). $\rho_{AB} = \sigma_A \otimes \tau_B$, $\sigma_A \in L(\mathbb{C}^{d_A})$ and $\tau_B \in L(\mathbb{C}^{d_B})$ are density operators.

[Diagram: Alice and Bob each with their own atom/system, separated]

$$\rho_{AB} = \sigma_A \otimes \tau_B$$

*Product state*
Alice and Bob individually prepare their systems.

— A **separable state** has the form: $\rho_{AB} = \sum_x p(x)\, \sigma_A^x \otimes \tau_B^x$

↳ Also called "classically correlated"   ↳ probabilities.

[Diagram: Alice and Bob each with their own atom/system, connected by a classical communication channel (double arrows between them)]

$$\rho_{AB} = \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Separable state*
Alice and Bob individually prepare their systems via local operations and classical communication.

## Page 2

- An **entangled state** is NOT a separable state.

[Diagram: Alice (left) and Bob (right) each with an atom symbol, connected by a wavy line representing entanglement]

$$\rho_{AB} \neq \sum_{x \in \mathcal{X}} p(x) \sigma_A^x \otimes \tau_B^x$$

*Entangled state*

Correlations between Alice and Bob are non-local.
State of the individual systems not sufficient to describe the pair.

⊛ The **Bell states**

**Pure States:**
$$\begin{cases} \Phi^\pm = \ket{\Phi^\pm}\bra{\Phi^\pm}, & \ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}) \\ \Psi^\pm = \ket{\Psi^\pm}\bra{\Psi^\pm}, & \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0}) \end{cases}$$

$$\ket{\Phi^+} = \begin{matrix} 00 \\ 01 \\ 10 \\ 11 \end{matrix}\!\begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ \tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Phi^-} = \begin{pmatrix} \tfrac{1}{\sqrt{2}} \\ 0 \\ 0 \\ -\tfrac{1}{\sqrt{2}} \end{pmatrix}, \quad \ket{\Psi^+} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ \tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}, \quad \ket{\Psi^-} = \begin{pmatrix} 0 \\ \tfrac{1}{\sqrt{2}} \\ -\tfrac{1}{\sqrt{2}} \\ 0 \end{pmatrix}$$

Observe that $\{\ket{\Phi^\pm}, \ket{\Psi^\pm}\} \longleftrightarrow \{\underbrace{(Z^z X^x \otimes \mathbb{1})\ket{\Phi^+}}_{\ket{\Phi_{z,x}}} : z, x \in \{0,1\}\}$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \quad X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \begin{matrix} Z^0 = \mathbb{1}, & Z^1 = Z \\ X^0 = \mathbb{1}, & X^1 = X \end{matrix}$$

$\quad 0,0 \leftrightarrow \Phi^+$
$\quad 0,1 \leftrightarrow \Psi^+$
$\quad 1,0 \leftrightarrow \Phi^-$
$\quad 1,1 \leftrightarrow \Psi^-$

$\ket{\Phi^-} = (Z \otimes \mathbb{1})\ket{\Phi^+}$
$\ket{\Psi^+} = (X \otimes \mathbb{1})\ket{\Phi^+}$
$\ket{\Psi^-} = (ZX \otimes \mathbb{1})\ket{\Phi^+}$

## Page 3

## ② Determining Entanglement.

✱ Given a state vector $\ket{\psi}$, how to determine if it is entangled or not?

Precisely: $\exists\, \ket{\phi_1}, \ket{\phi_2}$ s.t. $\ket{\psi} = \ket{\phi_1} \otimes \ket{\phi_2}$ ?

(a) $\ket{\psi}_{AB} \in \mathbb{C}^d \otimes \mathbb{C}^d \;\to\; \ket{\psi}_{AB} = \sum_{i,j=0}^{d-1} M_{i,j} \ket{i}_A \otimes \ket{j}_B$

$$\begin{pmatrix} a \\ b \\ c \\ d \end{pmatrix} \to \begin{pmatrix} a & c \\ b & d \end{pmatrix}$$

[arrow indicating that the two-index quantity ↔ matrix!]

Let $M = \sum_{i,j=0}^{d-1} M_{i,j} \ket{j}\bra{i} \in L(\mathbb{C}^d)$.

$M\ket{i} = \sum_{j=0}^{d-1} M_{i,j}\ket{j}$

**Lemma:** $\ket{\psi}_{AB} = (\mathbb{1} \otimes M)\ket{\Gamma_d}$, $\quad \ket{\Gamma_d} = \sum_{i=0}^{d-1} \ket{i} \otimes \ket{i}$.

$\left\{ d=2: \ket{\Gamma_2} = \ket{0}\ket{0} + \ket{1}\ket{1} = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix} \right.$

**Proof:** $(\mathbb{1} \otimes M)\ket{\Gamma_d} = (\mathbb{1} \otimes M)\left(\sum_{i=0}^{d-1} \ket{i} \otimes \ket{i}\right) = \sum_{i=0}^{d-1} \ket{i} \otimes M\ket{i} = \sum_{i,j=0}^{d-1} M_{i,j}\ket{i} \otimes \ket{j} = \ket{\psi}_{AB}$. ∎

$\mathrm{vec}(M) := (\mathbb{1} \otimes M)\ket{\Gamma_d} \equiv \ket{M}\rangle \;\Rightarrow\;$ Stacking the **columns** into a vector!

**Example:** $d=2$, $M = \begin{matrix} & {\scriptstyle 0} & {\scriptstyle 1} \\ {\scriptstyle 0} & \begin{pmatrix} a & b \\ c & d \end{pmatrix} \end{matrix}$

[colored boxes grouping entries: green box around column 0 $(a,c)$, orange box around column 1 $(b,d)$, with arrows showing them stacked into the vector below]

$\Rightarrow \quad (\mathbb{1} \otimes M)\ket{\Gamma_2} = a\ket{0,0} + c\ket{0,1} + b\ket{1,0} + d\ket{1,1}$

$$= \begin{pmatrix} a \\ c \\ b \\ d \end{pmatrix}$$

✱ For every $\ket{\psi} \in \mathbb{C}^d \otimes \mathbb{C}^d$, $\exists\, M \in L(\mathbb{C}^d)$ such that $\ket{\psi} = \mathrm{vec}(M) = (\mathbb{1} \otimes M)\ket{\Gamma}$.

## Page 4

(b) Every $M \in L(\mathbb{C}^d)$ has a <u>Singular-value decomposition</u>:

$$M = U \Sigma V^\dagger$$

[arrows: $U$ and $V^\dagger$ labeled "unitaries"; $\Sigma$ labeled "matrix of singular values"]

In bra-ket notation: $\boxed{M = \sum_{k=1}^{r} S_k \ket{f_k}\bra{e_k}}$

[arrow to $S_k$: "singular values, $S_k > 0 \;\forall k$. (unique up to ordering)"]

rank $\equiv$ # of singular values $\to$ <u>unique</u>

$\{\ket{f_k}\}_k, \{\ket{e_k}\}_k$ are orthonormal (left and right singular vectors).

$$\Rightarrow \ket{\psi}_{AB} = \mathrm{vec}(M) = (\mathbb{1} \otimes M)\ket{\mathbb{1}_d} = \sum_{k=1}^{r} S_k \,\mathrm{vec}(\ket{f_k}\bra{e_k}) = \sum_{k=1}^{r} S_k \underbrace{\ket{\bar{e}_k}}_{A} \otimes \underbrace{\ket{f_k}}_{B}$$

$$= (\mathbb{1} \otimes \ket{f_k}\bra{e_k})\left(\sum_{i=0}^{d-1} \ket{i} \otimes \ket{i}\right) = \sum_{i=0}^{d-1} \ket{i} \otimes \ket{f_k}\bra{e_k}\ket{i}$$

$$= \underbrace{\sum_{i=0}^{d-1} \ket{i}\bra{i}\ket{\bar{e}_k} \otimes \ket{f_k}}_{\mathbb{1}} = \ket{\bar{e}_k} \otimes \ket{f_k}$$

[Right side:]
$\ket{e_k} = \sum_{i=0}^{d-1} c_i \ket{i}$

$c_i = \braket{i|e_k}$

$= \overline{\braket{i|e_k}} = \braket{i|\bar{e}_k}$ (circled)

$= \sum_{i=0}^{d-1} \bar{c}_i \ket{i}$

---

⊛ $\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{\bar{e}_k}_A \otimes \ket{f_k}_B$ is called the <u>Schmidt decomposition</u> of $\ket{\psi}_{AB}$.

⊛ $\{S_k\}_{k=1}^{r}$ are called <u>Schmidt coefficients</u>. (sometimes $\sqrt{S_k}$).
   $\;\hookrightarrow > 0$

(Normalisation: $\braket{\psi|\psi} = 1 \Rightarrow \sum_{k=1}^{r} S_k^2 = 1$)

$$1 = \braket{\psi|\psi} = \left(\sum_{k=1}^{r} S_k \bra{\bar{e}_k}_A \otimes \bra{f_k}\right)\left(\sum_{k'=1}^{r} S_{k'} \ket{\bar{e}_{k'}} \otimes \ket{f_{k'}}\right) = \sum_{k,k'=1}^{r} S_k S_{k'} \underbrace{\braket{\bar{e}_k|\bar{e}_{k'}}}_{\delta_{k,k'}} \underbrace{\braket{f_k|f_{k'}}}_{\delta_{k,k'}} = \sum_{k=1}^{r} S_k^2$$

## Page 5

> - If $r=1$, then $\ket{\psi} = \ket{e_1} \otimes \ket{f_1} \Rightarrow$ not entangled!
> - If $r>1$, then entangled!  $\quad r \equiv$ **Schmidt rank**.

(c) Observe: $\ket{\psi}_{AB} = \sum_{k=1}^{r} s_k \ket{\overline{e_k}}_A \otimes \ket{f_k}_B$

$$\Rightarrow \mathrm{Tr}_B[\ket{\psi}\bra{\psi}_{AB}] = \mathrm{Tr}_B\left[ \sum_{k,k'=1}^{r} s_k s_{k'} \ket{\overline{e_k}}\bra{\overline{e_{k'}}}_A \otimes \ket{f_k}\bra{f_{k'}}_B \right]$$

$$= \sum_{k,k'=1}^{r} s_k s_{k'} \ket{\overline{e_k}}\bra{\overline{e_{k'}}}_A \underbrace{\mathrm{Tr}[\ket{f_k}\bra{f_{k'}}]}_{=\,\delta_{k,k'}}$$

$$= \sum_{k=1}^{r} s_k^2 \ket{\overline{e_k}}\bra{\overline{e_k}}_A \quad \to \text{ Diagonal!}$$

Also, $\mathrm{Tr}_A[\ket{\psi}\bra{\psi}_{AB}] = \sum_{k=1}^{r} s_k^2 \ket{f_k}\bra{f_k}_B$

$\Rightarrow \mathrm{Tr}_A[\psi_{AB}]$ and $\mathrm{Tr}_B[\psi_{AB}]$ have the same (non-zero) eigenvalues!

(d) Suppose $r=d$, $s_k = \tfrac{1}{\sqrt{d}}\ \forall\ k \in \{1,2,\ldots,d\}$.

We call $\ket{\psi}$ **maximally entangled** (Note that the marginals are maximally mixed.).

(e) Observe: $\dfrac{1}{\sqrt{d}} \sum_{k=1}^{d} \ket{e_k} \otimes \ket{\overline{e_k}} = \dfrac{1}{\sqrt{d}} \sum_{k=1}^{d} \left( \sum_{j=0}^{d-1} \ket{j}\bra{j} \right) \ket{e_k} \otimes \left( \sum_{\ell=0}^{d-1} \ket{\ell}\bra{\ell} \right) \ket{\overline{e_k}}$

## Page 6

$$= \ket{\Phi_d^+}$$

$$= \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k,k}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{k=1}^{d} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \braket{j | e_k} \braket{\ell | \bar{e}_k} \qquad \overline{\braket{e_k|\ell}} = \braket{e_k|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{k=1}^{d} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \braket{j|e_k}\braket{e_k|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j,\ell=0}^{d-1} \ket{j} \otimes \ket{\ell} \bra{j} \underbrace{\left( \sum_{k=1}^{d} \ket{e_k}\bra{e_k} \right)}_{= \mathbb{1}_d \text{ b/c } \{\ket{e_k}\} \text{ is ONB!}} \ket{\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j,\ell=0}^{d-1} \ket{j,\ell} \braket{j|\ell}$$

$$\downarrow$$
$$= \frac{1}{\sqrt{d}} \sum_{j=0}^{d-1} \ket{j,j}$$

$$\downarrow$$
$$= \ket{\Phi_d^+}. \qquad \underline{\underline{\quad}}$$

---

$$\frac{1}{\sqrt{2}}(\ket{0,0} + \ket{1,1})$$

$$\frac{1}{\sqrt{2}}(\underbrace{\ket{0}}_{\ket{e_1}}\underbrace{\ket{1}}_{\ket{f_1}} + \underbrace{\ket{1}}_{\ket{e_2}}\underbrace{\ket{0}}_{\ket{f_2}})$$

---

**(f) Vectorized unitaries are maximally entangled**

$$\ket{\gamma}_{AB} = (\mathbb{1} \otimes U)\ket{\Phi_d^+} = \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \underbrace{\ket{k}}_{\equiv \ket{e_k}} \otimes \underbrace{U\ket{k}}_{\equiv \ket{f_k}}$$

(↑ unitary)

Also, 
$$\mathrm{Tr}_A\!\left[\ket{\gamma}\bra{\gamma}_{AB}\right] = \mathrm{Tr}_A\!\left[(\mathbb{1}_A \otimes U_B) \overbrace{\Phi^+_{AB}}^{\ket{\Phi_d^+}\bra{\Phi_d^+}_{AB}} (\mathbb{1}_A \otimes U_B^\dagger)\right]$$

$$\downarrow$$
$$= U\, \mathrm{Tr}_A\!\left[\Phi^+_{AB}\right] U^\dagger \quad (*)$$
$$\qquad \searrow = \frac{\mathbb{1}_B}{d}$$

$$\downarrow$$
$$= \frac{1}{d} U U^\dagger$$

$$\downarrow$$
$$= \frac{1}{d} \mathbb{1}_B \qquad \left(\text{Similar for } \mathrm{Tr}_A[\ket{\gamma}\bra{\gamma}_{AB}]\right).$$

$(M \otimes \mathbb{1})(\mathbb{1} \otimes N)$
$\quad = (\mathbb{1} \otimes N)(M \otimes \mathbb{1})$

$(*):$
$$= \sum_{k=0}^{d-1} (\bra{k}_A \otimes \mathbb{1}_B)(\mathbb{1}_A \otimes U_B)\Phi^+(\mathbb{1}_A \otimes U_B^\dagger)(\ket{k}_A \otimes \mathbb{1})$$

$$= \sum_{k=0}^{d-1} U_B \bra{k}_A \Phi^+_{AB} \ket{k}_A U_B^\dagger = U_B\, \mathrm{Tr}_A[\Phi^+_{AB}]\, U_B^\dagger$$

## Page 7

<u>Proof of (\*)</u>: $\text{Tr}_A[\Phi^+_{AB}] = \frac{1}{d}\text{Tr}_A\left[\left(\sum_{k=0}^{d-1} \ket{k}_A\ket{k}_B\right)\left(\sum_{k'=0}^{d-1}\bra{k'}_A\bra{k'}_B\right)\right]$

$\ket{\Phi^+}_{AB} = \frac{1}{\sqrt{d}}\sum_{k=0}^{d-1}\ket{k}\ket{k}$

$$= \frac{1}{d}\sum_{k,k'=0}^{d-1}\underbrace{\text{Tr}_A\left[\ket{k}\bra{k'}_A \otimes \ket{k}\bra{k'}_B\right]}_{}$$

$$= \text{Tr}[\ket{k}\bra{k'}_A]\,\ket{k}\bra{k'}_B$$

$$= \delta_{k,k'}\,\ket{k}\bra{k'}_B$$

$$= \frac{1}{d}\sum_{k=0}^{d-1}\ket{k}\bra{k}_B$$

$$= \frac{1}{d}\mathbb{1}_B. \;\blacksquare$$

(g) Mixed-state entanglement is much harder to characterize! (More on this later...).

③ <u>Purification of mixed states</u>

(a) <u>Recall</u>: For qubits, pure states are on the surface of the Bloch sphere; mixed states are inside.

[Bloch sphere diagram with axes $x, y, z$; $\ket{0}$ at top (+z), $\ket{1}$ at bottom (−z), $\ket{+}$ on +x, $\ket{-}$ on −x (shown rotated), $\ket{+i}$ on +y, $\ket{-i}$ on −y]

$\ket{\psi} = \alpha\ket{0} + \beta\ket{1},$
$\alpha, \beta \in \mathbb{C},$
$|\alpha|^2 + |\beta|^2 = 1$

$\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} \pm \ket{1})$
$\ket{\pm i} = \frac{1}{\sqrt{2}}(\ket{0} \pm i\ket{1})$

Qubit
$\ket{0}$ or $\ket{1}$;
or *superposition*

General mixed states have the form $\rho = \sum_{k=1}^{N} p_k \underbrace{\ket{\psi_k}\bra{\psi_k}}_{\text{pure states}}$.

$p_k \rightarrow$ probabilities.

## Page 8

(b) How do mixed states arise in nature?

1. Lack of knowledge of state preparation.

[Diagram: A box labeled "Source" with arrows pointing to:
- $\ket{\psi_1}$ w/ prob. $p_1$
- $\ket{\psi_2}$ w/ prob. $p_2$
- $\vdots$
- $\ket{\psi_N}$ w/ prob. $p_N$]

✸ Now someone uses the source to prepare a state, but they don't tell you which one it is. How do you describe your knowledge of the system?
$\hookrightarrow$ (They don't mention the label.)

$\rho_{XS}^\dagger = \rho_{XS}$

$\rho_{XS} \geq 0$

$\text{Tr}[\rho_{XS}] = 1$

$$\rho_{XS} = \sum_{k=1}^{N} p_k \underbrace{\ket{k}\bra{k}_X}_{\text{ONB}} \otimes \ket{\psi_k}\bra{\psi_k}_S \qquad \left(\text{This is a } \underline{\text{classical-quantum state}}\right)$$

[Red annotation pointing to $\ket{k}\bra{k}_X$: classical variable/register. ("which state is it"?)]

✸ To figure out what state the system is prepared in, we measure the "classical register" $X$.
(w.r.t. POVM $\{\ket{k}\bra{k}\}_{k=1}^{N}$)

$$\text{Tr}\left[(\ket{k}\bra{k}_X \otimes \mathbb{1}_S)\rho_{XS}\right] = \text{Tr}\left[(\ket{k}\bra{k}_X \otimes \mathbb{1}_S)\underbrace{\sum_{k'=1}^{N} p_{k'} \ket{k'}\bra{k'}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S}_{\rho_{XS}}\right]$$

$$= \sum_{k'=1}^{N} \text{Tr}\left[p_{k'} \underbrace{\ket{k}\braket{k|k'}\bra{k'}_X}_{\delta_{k,k'}} \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right]$$

$$= p_k \checkmark \quad (\text{as expected!})$$

[Brace below: State conditioned on outcome $k$] (i.e., you know what the label is).

## Page 9

$$\frac{\text{Tr}_X\left[\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\rho_{XS}\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\right]}{p_k}$$

$$= \frac{1}{p_k}\sum_{k'=1}^{N} \text{Tr}_X\left[\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\left(p_{k'}\ket{k'}\bra{k'}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right)\left(\ket{k}\bra{k}_X \otimes \mathbb{1}_S\right)\right]$$

$$\downarrow$$

$$= \frac{1}{p_k}\sum_{k'=1}^{N} p_{k'}\, \underbrace{\text{Tr}_X\left[\ket{k}\braket{k|k'}\braket{k'|k}\bra{k}_X \otimes \ket{\psi_{k'}}\bra{\psi_{k'}}_S\right]}_{=\,\delta_{k',k}\,\ket{\psi_{k'}}\bra{\psi_{k'}}}$$

$$\downarrow$$

$$= \frac{1}{p_k}\, p_k \ket{\psi_k}\bra{\psi_k}$$

$$= \ket{\psi_k}\bra{\psi_k} \quad \checkmark \quad (\text{as expected!})$$

✱ But if you don't know the outcome/label? $\rightarrow$ <u>Trace out the register X!</u>

$$\text{Tr}_X(\rho_{XS}) = \text{Tr}_X\left[\sum_{k=1}^{N} p_k \ket{k}\bra{k}_X \otimes \ket{\psi_k}\bra{\psi_k}_S\right]$$

$$\downarrow$$

$$= \sum_{k=1}^{N} p_k\, \underbrace{\text{Tr}_X\left[\ket{k}\bra{k}_X \otimes \ket{\psi_k}\bra{\psi_k}_S\right]}_{=\,\underbrace{\text{Tr}[\ket{k}\bra{k}]}_{=1}\,\ket{\psi_k}\bra{\psi_k}}$$

$$\downarrow$$

$$= \underline{\underline{\sum_{k=1}^{N} p_k \ket{\psi_k}\bra{\psi_k}.}}$$

**2. Measurement on one part of a pure state.**

$$\ket{\psi}_{AB} = \sum_{k=1}^{r} \sqrt{\lambda_k}\,\ket{e_k}_A \otimes \ket{f_k}_B \quad \rightarrow \text{ Measure } A \text{ wrt POVM } \{M_A^x\}_{x \in \mathcal{X}}$$

Conditioned on outcome $x$, state on $B$ is $\quad \dfrac{1}{p_x}\,\text{Tr}_A\left[\left(\sqrt{M_A^x}\otimes \mathbb{1}_B\right)\ket{\psi}\bra{\psi}_{AB}\left(\sqrt{M_A^x}\otimes \mathbb{1}_B\right)\right]$

## Page 10

$$p_x = \text{Tr}\left[(M_A^x \otimes \mathbb{1}_B)\ket{\psi}\bra{\psi}_{AB}\right] = \text{Tr}\left[M_A^x \, \text{Tr}_B\left[\ket{\psi}\bra{\psi}_{AB}\right]\right] = \sum_{k=1}^{r} \lambda_k \text{Tr}\left[M_A^x \ket{e_k}\bra{e_k}_A\right].$$

$$= \text{Tr}_B\left[\sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}} \ket{e_k}\bra{e_{k'}}_A \otimes \ket{f_k}\bra{f_{k'}}_B\right]$$

$$= \sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}} \ket{e_k}\bra{e_{k'}}_A \underbrace{\text{Tr}\left[\ket{f_k}\bra{f_{k'}}_B\right]}_{=\delta_{k,k'}}$$

$$= \sum_{k=1}^{r} \lambda_k \ket{e_k}\bra{e_k}_A$$

$$\text{Tr}_A\left[\left(\sqrt{M_A^x} \otimes \mathbb{1}_B\right)\ket{\psi}\bra{\psi}_{AB}\left(\sqrt{M_A^x} \otimes \mathbb{1}_B\right)\right] = \text{Tr}_A\left[\sum_{k,k'=1}^{r} \sqrt{M_A^x}\ket{e_k}\bra{e_{k'}}_A\sqrt{M_A^x} \otimes \ket{f_k}\bra{f_{k'}}_B\right]$$

$$= \sum_{k,k'=1}^{r} \text{Tr}\left[\sqrt{M_A^x}\ket{e_k}\bra{e_{k'}}_A\sqrt{M_A^x}\right] \ket{f_k}\bra{f_{k'}}_B$$

$$= \sum_{k,k'=1}^{r} \text{Tr}\left[M_A^x \ket{e_k}\bra{e_{k'}}_A\right] \ket{f_k}\bra{f_{k'}}_B \quad \rightarrow \text{Not a pure state in general.}$$

3. **Entanglement with an (unknown) environment.**

   Consider a mixed state $\rho_S = \sum_{k=1}^{r} \lambda_k \ket{\psi_k}\bra{\psi_k}$ (spectral decomposition).
   
   $\uparrow$ <span style="color:red">eigenvalues</span> $\quad$ <span style="color:red">eigenvectors (orthonormal).</span>

   ⊛ <u>Note</u>: $\text{Tr}(\rho_S) = 1 \implies \text{Tr}\left[\sum_{k=1}^{r} \lambda_k \underbrace{\text{Tr}\left[\ket{\psi_k}\bra{\psi_k}\right]}_{=1}\right] = \sum_{k=1}^{r} \lambda_k = 1$ (eigenvalues sum to one).

   ⊛ <u>Note</u>: $\rho_S \geq 0 \implies \lambda_k \geq 0 \;\forall\, k. \implies 0 \leq \lambda_k \leq 1 \;\forall\, k.$

## Page 11

$\circledast$ There exists a pure state $\ket{\psi}_{ES}$ such that $\mathrm{Tr}_E[\ket{\psi}\bra{\psi}_{ES}] = \rho_S$.

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}\underset{\text{\color{red}environment}}{\color{red}\uparrow}$

Proof: (by explicit construction) Consider $\sqrt{\rho_S} = \sum_{k=1}^{r} \sqrt{\lambda_k}\, \ket{\gamma_k}\bra{\gamma_k}$

Then $\ket{\psi}_{ES} = (\mathbb{1}_E \otimes \sqrt{\rho_S})\ket{\Gamma} = \left(\mathbb{1}_E \otimes \sum_{k=1}^{r}\sqrt{\lambda_k}\,\ket{\gamma_k}\bra{\gamma_k}_S\right)\ket{\Gamma}$

$\phantom{xxxxxx}\underset{\color{red}\dim(\mathcal{H}_E) \geq r}{\color{red}\uparrow} \phantom{xxxx} \underset{\color{red}\ket{\Gamma} = \sum_{k=0}^{d-1}\ket{k,k}}{\color{red}\uparrow}$

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}{\color{blue}\underline{\mathrm{vec}(\ket{e_k}\bra{f_k}) = \overline{\ket{f_k}} \otimes \ket{e_k}}}$

$\phantom{xx}= \sum_{k=1}^{r} \sqrt{\lambda_k}\, \underbrace{(\mathbb{1}_E \otimes \ket{\gamma_k}\bra{\gamma_k}_S)\ket{k,k}_{ES}}_{\color{red}\overline{\ket{\gamma_k}}_E \otimes \ket{\gamma_k}_S} = \sum_{k=1}^{r}\sqrt{\lambda_k}\,\overline{\ket{\gamma_k}}_E \otimes \ket{\gamma_k}_S$

- This is a state vector: $\braket{\psi|\psi} = \left(\sum_{k=1}^{r}\sqrt{\lambda_k}\,\bra{\overline{\gamma_k}}_E \otimes \bra{\gamma_k}_S\right)\left(\sum_{k'=1}^{r}\sqrt{\lambda_{k'}}\,\overline{\ket{\gamma_{k'}}}_E \otimes \ket{\gamma_{k'}}_S\right)$

$\phantom{xxxxxxxxxxxxxxxxx} = \sum_{k,k'=1}^{r} \sqrt{\lambda_k \lambda_{k'}}\, \underbrace{\braket{\overline{\gamma_k}|\overline{\gamma_{k'}}}}_{\delta_{k,k'}} \underbrace{\braket{\gamma_k|\gamma_{k'}}}_{\delta_{k,k'}}$

$\phantom{xxxxxxxxxxxxxxxxx} = \sum_{k=1}^{r} \lambda_k$

$\phantom{xxxxxxxxxxxxxxxxx} = 1 \quad \checkmark$

- $\mathrm{Tr}_E[\ket{\psi}\bra{\psi}_{ES}] = \mathrm{Tr}_E\left[(\mathbb{1}_E \otimes \sqrt{\rho_S})\ket{\Gamma}\bra{\Gamma}_{ES}(\mathbb{1}_E \otimes \sqrt{\rho_S})\right]$

$\phantom{xxxxxxxxxxxxxxx} = \sqrt{\rho_S}\, \underbrace{\mathrm{Tr}_E[\ket{\Gamma}\bra{\Gamma}_{ES}]}_{}\, \sqrt{\rho_S}$

$\phantom{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx} {\color{blue}\ket{\Gamma} = \sum_{k=0}^{d-1}\ket{k,k}}$

## Page 12

$$= \sum_{k,k'=0}^{d-1} \mathrm{Tr}_E\left[\ket{k}\bra{k'}_E \otimes \ket{k}\bra{k'}_S\right]$$

$$= \sum_{k,k'=0}^{d-1} \delta_{k,k'} \ket{k}\bra{k'}_S$$

$$= \sum_{k=0}^{d-1} \ket{k}\bra{k}_S = \mathbb{1}_S.$$

$$= \rho_S \checkmark$$

$$\sqrt{\rho_S}\, \mathbb{1}\, \sqrt{\rho_S} = \rho_S$$
