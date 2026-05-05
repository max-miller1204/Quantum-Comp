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
