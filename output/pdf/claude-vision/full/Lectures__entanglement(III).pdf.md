# Lectures__entanglement(III).pdf

## Page 1

# ① Determining Entanglement.

(a) Given a state vector $\ket{\psi}_{AB}$, how to determine if it is entangled or not?
Precisely: $\exists\, \ket{\phi_1}_A, \ket{\phi_2}_B$ s.t. $\ket{\psi}_{AB} = \ket{\phi_1}_A \otimes \ket{\phi_2}_B$ ?

✸ **Theorem (Schmidt Decomposition):** Every state vector $\ket{\psi}_{AB}$ can be written as

$$\ket{\psi}_{AB} = \sum_{k=1}^{r} S_k \ket{e_k}_A \otimes \ket{f_k}_B. \qquad \left(\ket{\psi}_{AB} = \sum_{i,j=0}^{d-1} c_{i,j} \ket{i}_A \otimes \ket{j}_B\right)$$

- $r$: Schmidt rank
- $\{S_k\}_{k=1}^{r}$: Schmidt coefficients $S_k > 0\ \forall k$
- $\{\ket{e_k}_A\}_{k=1}^{r}$ and $\{\ket{f_k}_B\}_{k=1}^{r}$ are orthonormal vectors.

(**Proof** (recall): Write the vector $\ket{\psi}_{AB}$ as a matrix, then do the singular value decomposition of the matrix.)

- The Schmidt rank is **unique** — so we get the following criterion:

$$\boxed{\begin{array}{l} \bullet \text{ If } r = 1, \text{ then } \ket{\psi} = \ket{e_1} \otimes \ket{f_1} \Rightarrow \text{not entangled!} \\[4pt] \bullet \text{ If } r > 1, \text{ then entangled!} \qquad \ket{\mathcal{E}^+} = \tfrac{1}{\sqrt{d}} \sum_{k=0}^{d-1} \ket{k}_A \ket{k}_B \end{array}}$$

(b) What about mixed states? More complicated!

- **Example:** convex mixtures of Bell states. $\left(\ket{\Phi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,0} \pm \ket{1,1}),\ \ket{\Psi^\pm} = \tfrac{1}{\sqrt{2}}(\ket{0,1} \pm \ket{1,0})\right)$

$$\rho_{AB} = p_1 \Phi^+_{AB} + p_2 \Phi^-_{AB} + p_3 \Psi^+_{AB} + p_4 \Psi^-_{AB}, \quad \text{probabilities } p_1, p_2, p_3, p_4 \in [0,1]$$

$$\Phi^\pm_{AB} = \ket{\Phi^\pm}\bra{\Phi^\pm}_{AB},\quad \Psi^\pm_{AB} = \ket{\Psi^\pm}\bra{\Psi^\pm}_{AB}. \qquad p_1 + p_2 + p_3 + p_4 = 1$$

## Page 2

- $p_1 = 1, p_2 = p_3 = p_4 = 0 \implies \rho_{AB} = \Phi^+_{AB} \implies$ entangled!

- $p_1 = 0, p_2 = 1, p_3 = p_4 = 0 \implies \rho_{AB} = \Phi^-_{AB} \implies$ entangled!

- $p_1 = p_2 = 0, p_3 = 1, p_4 = 0 \implies \rho_{AB} = \Psi^+_{AB} \implies$ entangled!

- $p_1 = p_2 = p_3 = 0, p_4 = 1 \implies \rho_{AB} = \Psi^-_{AB} \implies$ entangled!

- <u>But</u>: $p_1 = p_2 = p_3 = p_4 = \frac{1}{4} \implies \rho_{AB} = \frac{1}{4}\Phi^+_{AB} + \frac{1}{4}\Phi^-_{AB} + \frac{1}{4}\Psi^+_{AB} + \frac{1}{4}\Psi^-_{AB} = \frac{1}{4}\mathbb{1}_A \otimes \mathbb{1}_B$

  $\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad$ B/c Bell states form ONB.

  $\implies$ <u>not</u> entangled!

- General criterion: <u>Positive Partial Transpose (PPT) criterion</u>

<u>Recall</u>: Transpose of a matrix (flip rows and columns).

$\quad$ In Bra-ket notation: $\quad M = \sum_{i,j=0}^{d-1} m_{i,j} \ket{i}\bra{j}$

$\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad M^T = \sum_{i,j=0}^{d-1} m_{i,j} \ket{j}\bra{i} \quad \rightsquigarrow (M^T)^T = M.$

$\quad$ For $M_{AB} \in L(\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B})$: $\quad M_{AB} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i}\bra{i'}_A \otimes \ket{j}\bra{j'}_B.$

$\quad$ <u>Partial transpose on A</u>: $\quad M_{AB}^{T_A} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i'}\bra{i}_A \otimes \ket{j}\bra{j'}_B.$

$\quad$ <u>Partial transpose on B</u>: $\quad M_{AB}^{T_B} = \sum_{i,i'=0}^{d_A-1} \sum_{j,j'=0}^{d_B-1} m_{\substack{i,j \\ i',j'}} \ket{i}\bra{i'}_A \otimes \ket{j'}\bra{j}_B.$

$\quad$ <u>Full transpose</u>: $M_{AB}^T = M_{AB}^{T_A T_B} \implies M_{AB}^{T_A} = (M_{AB}^{T_B})^T$

$\quad\quad (M_{AB}^{T_A})^{T_A} = M_{AB} \quad\quad (M_{AB}^{T_B})^T = (M_{AB}^{T_B})^{T_A T_B} = M_{AB}^{T_A}$

## Page 3

For $M_{AB} = $

$$\begin{array}{c} \phantom{00}\;\;00\;\;\;\;\;01\;\;\;\;\;10\;\;\;\;\;11 \\ \begin{array}{c}00\\01\\10\\11\end{array}\!\!\left(\begin{array}{cccc} m_1 & m_2 & m_3 & m_4 \\ m_5 & m_6 & m_7 & m_8 \\ m_9 & m_{10} & m_{11} & m_{12} \\ m_{13} & m_{14} & m_{15} & m_{16} \end{array}\right) \end{array}$$

[Purple ovals/arrows indicate swapping pairs: $(m_2 \leftrightarrow m_5)$, $(m_4 \leftrightarrow m_7)$, $(m_{10} \leftrightarrow m_{13})$, $(m_{12} \leftrightarrow m_{15})$]

$$M_{AB}^{T_B} = \begin{array}{c} \phantom{00}\;\;00\;\;\;\;\;01\;\;\;\;\;10\;\;\;\;\;11 \\ \begin{array}{c}00\\01\\10\\11\end{array}\!\!\left(\begin{array}{cccc} m_1 & m_5 & m_3 & m_7 \\ m_2 & m_6 & m_4 & m_8 \\ m_9 & m_{13} & m_{11} & m_{15} \\ m_{10} & m_{14} & m_{12} & m_{16} \end{array}\right) \end{array}$$

---

[Reproductions of two journal article headers:]

**PHYSICAL REVIEW LETTERS**, Volume 77, 19 August 1996, Number 8 — "Separability Criterion for Density Matrices", Asher Peres, Department of Physics, Technion–Israel Institute of Technology, 32 000, Haifa, Israel (Received 8 April 1996)

**PHYSICS LETTERS A** 223 (1996) 1–8, 25 November 1996 — "Separability of mixed states: necessary and sufficient conditions", Michał Horodecki, Paweł Horodecki, Ryszard Horodecki (University of Gdańsk / Technical University of Gdańsk)

---

✸ **Theorem (PPT Criterion):** $\rho_{AB}$ separable $\Rightarrow \rho_{AB}^{T_A} \geq 0,\; \rho_{AB}^{T_B} \geq 0.$

$X \Rightarrow Y$
$\neg Y \Rightarrow \neg X$

✸ **Contrapositive:** $\rho_{AB}^{T_{A/B}} \not\geq 0 \;\Rightarrow\; \rho_{AB}$ entangled

$\Rightarrow$ Just check if $\rho_{AB}^{T_{A/B}}$ has a negative eigenvalue!

✸ **Converse:** $\rho_{AB}^{T_{A/B}} \geq 0 \;\xcancel{\Rightarrow}\; \rho_{AB}\text{ separable}$ $\;\longrightarrow$ NOT true in general!

(There are entangled states w/ positive partial transpose.)

(Example in this paper.)

## Page 4

[Header: Elsevier Physics Letters A 232 (1997) 333–339, "Separability criterion and inseparable mixed states with positive partial transposition" by Paweł Horodecki, 4 August 1997]

**Proof:** $\rho_{AB}$ separable $\Rightarrow \rho_{AB} = \sum_x p(x)\, \tau_A^x \otimes \omega_B^x$

$$\Rightarrow \rho_{AB}^{T_B} = \sum_x p(x)\, \underbrace{\tau_A^x}_{\geq 0} \otimes \underbrace{(\omega_B^x)^T}_{\geq 0} \geq 0$$

$M \geq 0 \Rightarrow M^T \geq 0$ (full transpose does not change eigenvalues.)

$\Rightarrow \rho_{AB}^{T_B} \geq 0. \quad \rho_{AB}^{T_A} = (\rho_{AB}^{T_B})^T \;\;$ ↪ Full transpose. $\;\Rightarrow \rho_{AB}^{T_A} \geq 0.$ ∎

---

[highlighted box:]
※ Converse **is** true for $2\otimes 2$ and $2\otimes 3$!

↳ $\rho_{AB}$ separable $\iff \rho_{AB}^{T_{A/B}} \geq 0.$

---

- **Examples of the PPT criterion:** $\quad \ket{\Phi^+} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{0} + \ket{1}\ket{1}).$

$$-\;\rho_{AB} = \Phi_{AB}^+ = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 1 & 0 & 0 & 1 \end{pmatrix} \Rightarrow \rho_{AB}^{T_B} = \frac{1}{2}\begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

$\underbrace{\hphantom{XXXXXXXXXXXXX}}_{\mathbb{F}_{AB} \;\to\; \text{swap operator.}}$

※ Eigenvalues of $\mathbb{F}_{AB}$ are $\pm 1.$

※ $\mathbb{F}_{AB} = \sum_{i,j=0}^{d-1} \ket{j,i}\bra{i,j} \quad (\mathbb{F}_{AB}\ket{i,j} = \ket{j,i})$

$\ket{j,i}\bra{i,j} \equiv \ket{j}\bra{i}\otimes\ket{i}\bra{j}$

$\mathbb{F}_{AB}\ket{0}\ket{0} = \ket{0}\ket{0}$
$\mathbb{F}_{AB}\ket{0}\ket{1} = \ket{1}\ket{0}$
$\mathbb{F}_{AB}\ket{1}\ket{0} = \ket{0}\ket{1}$
$\mathbb{F}_{AB}\ket{1}\ket{1} = \ket{1}\ket{1}$

## Page 5

(\*) $F_{AB}\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right) = \ket{\chi_2}_A \otimes \ket{\chi_1}_B.$

<u>Proof</u>: $F_{AB}\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right) = \left(\sum_{i,j=0}^{d-1} \ket{j}\bra{i}_A \otimes \ket{i}\bra{j}_B\right)\left(\ket{\chi_1}_A \otimes \ket{\chi_2}_B\right)$

$$= \sum_{i,j=0}^{d-1} \ket{j}\braket{i|\chi_1} \otimes \ket{i}\braket{j|\chi_2}$$

$$= \sum_{i,j=0}^{d-1} \ket{j}\braket{j|\chi_2} \otimes \ket{i}\braket{i|\chi_1}$$

$$= \underbrace{\left(\sum_{j=0}^{d-1} \ket{j}\bra{j}_A\right)}_{=\mathbb{1}_A}\ket{\chi_2}_A \otimes \underbrace{\left(\sum_{i=0}^{d-1} \ket{i}\bra{i}_B\right)}_{=\mathbb{1}_B}\ket{\chi_1}_B$$

$$= \ket{\chi_2}_A \otimes \ket{\chi_1}_B.$$

$p_1 = 1-p$
$p_2 = p_3 = p_4 = \frac{p}{3}.$

– <u>Isotropic state</u>: $\rho_{AB}^{(p)} = (1-p)\,\Phi_{AB}^+ + \frac{p}{3}\left(\Phi_{AB}^- + \Psi_{AB}^+ + \Psi_{AB}^-\right),\quad p \in [0,1].$

$$\rho_{AB}^{(p)} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{array}{cccc} 00 & 01 & 10 & 11 \end{array} \\ \left(\begin{array}{cccc} \frac{1-p}{2}+\frac{p}{6} & 0 & 0 & \frac{1-p}{2}-\frac{p}{6} \\ 0 & \frac{p}{3} & 0 & 0 \\ 0 & 0 & \frac{p}{3} & 0 \\ \frac{1-p}{2}-\frac{p}{6} & 0 & 0 & \frac{1-p}{2}+\frac{p}{6} \end{array}\right)$$

[Purple ovals/arrows indicate swapping the (00,11) anti-diagonal block with the (01,10) block under partial transpose]

$$\left(\rho_{AB}^{(p)}\right)^{T_B} = \begin{array}{c} \\ 00 \\ 01 \\ 10 \\ 11 \end{array}\!\!\begin{array}{cccc} 00 & 01 & 10 & 11 \end{array} \\ \left(\begin{array}{cccc} \frac{1-p}{2}+\frac{p}{6} & 0 & 0 & 0 \\ 0 & \frac{p}{3} & \frac{1-p}{2}-\frac{p}{6} & 0 \\ 0 & \frac{1-p}{2}-\frac{p}{6} & \frac{p}{3} & 0 \\ 0 & 0 & 0 & \frac{1-p}{2}+\frac{p}{6} \end{array}\right)$$

## Page 6

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

## Page 7

- <u>Recall example from before</u>: $\rho_{AB} = \frac{1}{2}\left(\ket{0}\bra{0}_A \otimes \ket{1}\bra{1}_B + \ket{1}\bra{1}_A \otimes \ket{0}\bra{0}_B\right)$

  - This state is separable (not entangled).
  - If Alice and Bob both measure in $\{\ket{0}, \ket{1}\}$ basis, then:
    - They both get "0" and "1" w/ probability $\frac{1}{2}$.
      (i.e., locally, it looks completely random, b/c $\rho_A = \text{Tr}_B[\rho_{AB}] = \frac{1}{2}\mathbb{1}_A$ and $\rho_B = \text{Tr}_A[\rho_{AB}] = \frac{1}{2}\mathbb{1}_B$.)
    - But if they compare their measurement outcomes, they will always be the opposite! (Whenever Alice got a "0" or "1", Bob got "1" or "0".) So their outcomes are perfectly <u>anti-correlated</u>.

- But the same thing happens with the maximally-entangled state!

  $\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}(\ket{0}_A\ket{1}_B - \ket{1}_A\ket{0}_B)$ — in the $\{\ket{0}, \ket{1}\}$ basis, the outcomes are
  
  $\quad\quad\quad\quad\quad\;\; \underbrace{\;\;}_{\ket{e_1}}\;\underbrace{\;\;}_{\ket{f_1}}\;\;\underbrace{\;\;}_{\ket{e_2}}\;\underbrace{\;\;}_{\ket{f_2}}$
  
  perfectly anti-correlated!

- So how to distinguish the two? What makes the entangled state special?

- To see the difference, measure in a different basis! Say in the $\{\ket{+}, \ket{-}\}$ basis.

  - For $\rho_{AB} = \frac{1}{2}(\ket{0}\bra{0}_A \otimes \ket{1}\bra{1}_B + \ket{1}\bra{1}_A \otimes \ket{0}\bra{0}_B)$:

    $\Pr[+,+] = \text{Tr}\left[\left(\ket{+}\bra{+}_A \otimes \ket{+}\bra{+}_B\right)\rho_{AB}\right] = \frac{1}{2}\left(\underbrace{\braket{+|0}\braket{0|+}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{+|1}\braket{1|+}}_{\frac{1}{\sqrt{2}}} + \underbrace{\braket{+|1}\braket{1|+}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{+|0}\braket{0|+}}_{\frac{1}{\sqrt{2}}}\right)$

    $\left[\ket{\pm} = \frac{1}{\sqrt{2}}(\ket{0} + \ket{1})\right]$
    
    $\quad\quad\quad\quad\quad\quad\quad\quad = \frac{1}{2}\left(\frac{1}{4} + \frac{1}{4}\right) = \frac{1}{4}.$

  Similarly: $\Pr[+,-] = \Pr[-,+] = \Pr[-,-] = \frac{1}{4}$.

  So the outcomes are completely <u>uncorrelated</u>!

  Why? B/c the joint distribution is a product of the marginal distributions.

## Page 8

- Marginal distributions are given by the partial trace:
  - Marginal for Alice: $\rho_A = \frac{1}{2}\mathbb{1}_A \Rightarrow \Pr_A[+] = \Pr_A[-] = \frac{1}{2}$
  - Marginal for Bob: $\rho_B = \frac{1}{2}\mathbb{1}_B \Rightarrow \Pr_B[+] = \Pr_B[-] = \frac{1}{2}$
  - Product of the marginals: $\Pr_A[+]\cdot\Pr_B[+] = \frac{1}{4}$, $\Pr_A[+]\cdot\Pr_B[-] = \frac{1}{4}$
  
  $P_{XY} = P_X \cdot P_Y$
  
  $$\Pr_A[-]\cdot\Pr_B[+] = \frac{1}{4}, \quad \Pr_A[-]\cdot\Pr_B[-] = \frac{1}{4}.$$

  This is the same as the joint distribution calculated above!
  So Alice and Bob's random variables are independent $\Rightarrow$ no correlation.

- But for $\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}(\ket{0}_A\ket{1}_B - \ket{1}_A\ket{0}_B)$, the outcomes are still perfectly anti-correlated!

  - $(\bra{+}_A \otimes \bra{+}_B)\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}\big(\underbrace{\braket{+|0}}_{=\frac{1}{\sqrt{2}}}\underbrace{\braket{+|1}}_{\frac{1}{\sqrt{2}}} - \braket{+|1}\braket{+|0}\big) = 0 \Rightarrow \underline{\Pr[+,+] = 0}$
  
  - $(\bra{+}_A \otimes \bra{-}_B)\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}\big(\underbrace{\braket{+|0}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{-|1}}_{-\frac{1}{\sqrt{2}}} - \underbrace{\braket{+|1}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{-|0}}_{\frac{1}{\sqrt{2}}}\big) = \frac{1}{\sqrt{2}}\left(-\frac{1}{2}-\frac{1}{2}\right) = -\frac{1}{\sqrt{2}}$
  
  $$\Rightarrow \underline{\Pr[+,-] = \big|(\bra{+}_A \otimes \bra{-}_B)\ket{\Psi^-}_{AB}\big|^2 = \frac{1}{2}}$
  
  - $(\bra{-}_A \otimes \bra{+}_B)\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}\big(\underbrace{\braket{-|0}}_{\frac{1}{\sqrt{2}}}\underbrace{\braket{+|1}}_{\frac{1}{\sqrt{2}}} - \underbrace{\braket{-|1}}_{-\frac{1}{\sqrt{2}}}\underbrace{\braket{+|0}}_{\frac{1}{\sqrt{2}}}\big) = \frac{1}{\sqrt{2}}\left(\frac{1}{2}+\frac{1}{2}\right) = \frac{1}{\sqrt{2}}$
  
  $$\Rightarrow \underline{\Pr[-,+] = \big|(\bra{-}_A \otimes \bra{+}_B)\ket{\Psi^-}_{AB}\big|^2 = \frac{1}{2}}$
  
  - $(\bra{-}_A \otimes \bra{-}_B)\ket{\Psi^-}_{AB} = \frac{1}{\sqrt{2}}\big(\underbrace{\braket{-|0}}_{=\frac{1}{\sqrt{2}}}\underbrace{\braket{-|1}}_{-\frac{1}{\sqrt{2}}} - \underbrace{\braket{-|1}}_{-\frac{1}{\sqrt{2}}}\underbrace{\braket{-|0}}_{\frac{1}{\sqrt{2}}}\big) = 0 \Rightarrow \underline{\Pr[-,-] = 0}.$

## Page 9

- The anti-correlation exists for <u>any</u> basis measurement!

- **Fact**: Let $U$ be an arbitrary $2 \times 2$ unitary matrix. Then
$$(U \otimes U) \ket{\Psi^-}\bra{\Psi^-} (U \otimes U)^\dagger = \ket{\Psi^-}\bra{\Psi^-}.$$

$$\ket{\Psi^-} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{1} - \ket{1}\ket{0})$$

**Proof**: First consider an arbitrary $2 \times 2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $a,b,c,d \in \mathbb{C}$.

$$(M \otimes M)\ket{\Psi^-} = \tfrac{1}{\sqrt{2}}\big(M\ket{0} \otimes M\ket{1} - M\ket{1} \otimes M\ket{0}\big)$$

$\quad M\ket{0} = a\ket{0} + c\ket{1}$
$\quad M\ket{1} = b\ket{0} + d\ket{1}$

$$= \tfrac{1}{\sqrt{2}}\Big( (a\ket{0} + c\ket{1}) \otimes (b\ket{0} + d\ket{1}) - (b\ket{0} + d\ket{1}) \otimes (a\ket{0} + c\ket{1}) \Big)$$

$$= \tfrac{1}{\sqrt{2}}\Big( \cancel{ab\ket{0,0}} + ad\ket{0,1} + cb\ket{1,0} + \cancel{cd\ket{1,1}} - \cancel{ab\ket{0,0}} - cb\ket{1,0} - ad\ket{1,0}\!\!\!\!\!^{\,0,1} - \cancel{cd\ket{1,1}} \Big)$$

Wait — re-doing carefully:

$$= \tfrac{1}{\sqrt{2}}\Big( (ad - bc)\ket{0,1} - (ad - bc)\ket{1,0} \Big)$$

$$= \tfrac{1}{\sqrt{2}}(ad - bc)\big(\ket{0,1} - \ket{1,0}\big)$$

$$= (ad - bc)\,\tfrac{1}{\sqrt{2}}\big(\ket{0,1} - \ket{1,0}\big)$$

$$= \underline{\det(M)}\,\ket{\Psi^-}. \quad \to \underline{\text{determinant of } M!}$$

So for any matrix $M$: $\;(M \otimes M)\ket{\Psi^-}\bra{\Psi^-}(M \otimes M)^\dagger = |\det(M)|^2 \ket{\Psi^-}\bra{\Psi^-}.$

Determinant is product of the eigenvalues.

Let $U = \sum_{k=1}^{d} \lambda_k \ket{\gamma_k}\bra{\gamma_k}$ be the spectral decomposition of a unitary.

Then $U^\dagger = \sum_{k=1}^{d} \overline{\lambda_k} \ket{\gamma_k}\bra{\gamma_k} \;\Rightarrow\; UU^\dagger = \sum_{k=1}^{d} |\lambda_k|^2 \ket{\gamma_k}\bra{\gamma_k} = \mathbb{1}$ (by unitarity) $\quad \lambda_k = re^{i\theta}$

Also, $\sum_{k=1}^{d} \ket{\gamma_k}\bra{\gamma_k} = \mathbb{1} \;\Rightarrow\; |\lambda_k|^2 = 1 \;\forall\, k \;\Rightarrow\; \lambda_k = e^{i\theta_k} \;\Rightarrow\;$ eigenvalues of

## Page 10

a unitary are complex numbers with unit modulus.

$\Rightarrow \det(u) = \lambda_1 \lambda_2 \cdots \lambda_d$ is a complex number with unit modulus.

$\Rightarrow |\det(u)|^2 = 1.$

$\Rightarrow (u \otimes u) \ket{\Psi^-}\bra{\Psi^-} (u \otimes u)^\dagger = |\det(u)|^2 \ket{\Psi^-}\bra{\Psi^-} = \ket{\Psi^-}\bra{\Psi^-}.$ ∎

- The vectors $\{u^\dagger \ket{0}, u^\dagger \ket{1}\}$ define a measurement, with measurement operators $M_0 = u^\dagger \ket{0}\bra{0} u$, $M_1 = u^\dagger \ket{1}\bra{1} u$.

$$M_0 + M_1 = u^\dagger \ket{0}\bra{0} u + u^\dagger \ket{1}\bra{1} u = u^\dagger \underbrace{(\ket{0}\bra{0} + \ket{1}\bra{1})}_{=\mathbb{1}} u = u^\dagger u = \mathbb{1}. \checkmark$$

Probability distribution is:

$$\Pr(i,j) = \mathrm{Tr}\big[ (M_i \otimes M_j) \ket{\Psi^-}\bra{\Psi^-}_{AB} \big] = \mathrm{Tr}\big[ (u^\dagger \ket{i}\bra{i} u \otimes u^\dagger \ket{j}\bra{j} u) \ket{\Psi^-}\bra{\Psi^-}_{AB} \big]$$

$\textcolor{blue}{(X_1 \otimes Y_1)(X_2 \otimes Y_2) = X_1 X_2 \otimes Y_1 Y_2}$

$$= \mathrm{Tr}\big[ (u^\dagger \otimes u^\dagger) \ket{i,j}\bra{i,j} (u \otimes u) \ket{\Psi^-}\bra{\Psi^-}_{AB} \big]$$

$$= \mathrm{Tr}\big[ \ket{i,j}\bra{i,j} \underbrace{(u \otimes u) \ket{\Psi^-}\bra{\Psi^-} (u \otimes u)^\dagger}_{= \ket{\Psi^-}\bra{\Psi^-} \text{ (from above)}} \big]$$

$$= \mathrm{Tr}\big[ \ket{i,j}\bra{i,j} \ket{\Psi^-}\bra{\Psi^-} \big]$$

$\Rightarrow$ Same distribution as the $\{\ket{0}, \ket{1}\}$ basis! So still anti-correlated!

$\textcolor{red}{\circledast \text{ We can formalize this idea into an } \underline{\text{experimental test}} \text{ for entanglement.}}$
