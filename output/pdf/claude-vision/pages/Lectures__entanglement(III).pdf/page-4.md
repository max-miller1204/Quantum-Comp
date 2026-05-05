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
