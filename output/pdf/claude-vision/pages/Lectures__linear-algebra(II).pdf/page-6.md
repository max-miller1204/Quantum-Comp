✻ **Abstract notation:** $\ket{\psi_1} = \alpha_1\ket{0} + \beta_1\ket{1}$, $\ket{\psi_2} = \alpha_2\ket{0} + \beta_2\ket{1}$, $\ket{\psi_3} = \alpha_3\ket{0} + \beta_3\ket{1}$

$$\Rightarrow \ket{\psi_1} \otimes \ket{\psi_2} \otimes \ket{\psi_3} = \big(\alpha_1\ket{0} + \beta_1\ket{1}\big) \otimes \big(\alpha_2\ket{0} + \beta_2\ket{1}\big) \otimes \big(\alpha_3\ket{0} + \beta_3\ket{1}\big)$$

$$= \big(\alpha_1\alpha_2\ket{0,0} + \alpha_1\beta_2\ket{0,1} + \beta_1\alpha_2\ket{1,0} + \beta_1\beta_2\ket{1,1}\big) \otimes \big(\alpha_3\ket{0} + \beta_3\ket{1}\big)$$

$$= \alpha_1\alpha_2\alpha_3\ket{0,0,0} + \alpha_1\alpha_2\beta_3\ket{0,0,1} + \alpha_1\beta_2\alpha_3\ket{0,1,0} + \alpha_1\beta_2\beta_3\ket{0,1,1}$$
$$+ \beta_1\alpha_2\alpha_3\ket{1,0,0} + \beta_1\alpha_2\beta_3\ket{1,0,1} + \beta_1\beta_2\alpha_3\ket{1,1,0} + \beta_1\beta_2\beta_3\ket{1,1,1}$$

— **Arbitrary number of tensor products:**

$$\ket{\psi_j} = \sum_{k=0}^{1} C_{j,k}\ket{k} = C_{j,0}\ket{0} + C_{j,1}\ket{1}$$

$$\rightarrow \underbrace{\ket{\psi_1} \otimes \ket{\psi_2} \otimes \cdots \otimes \ket{\psi_n}}_{\text{vector in } (\mathbb{C}^2)^{\otimes n}} = \bigotimes_{j=1}^{n}\ket{\psi_j} = \sum_{k_1,k_2,\ldots,k_n=0}^{1} C_{1,k_1} C_{2,k_2} \cdots C_{n,k_n} \ket{k_1, k_2, \ldots, k_n}$$

✻ **Generalizes to arbitrary dimension!** $\ket{\psi_j} = \sum_{k=0}^{d_j-1} C_{j,k}\ket{k}$

$$\Rightarrow \underbrace{\bigotimes_{j=1}^{n} \ket{\psi_j}}_{\text{Vector in } \mathbb{C}^{d_1} \otimes \mathbb{C}^{d_2} \otimes \cdots \otimes \mathbb{C}^{d_n}} = \sum_{k_1=0}^{d_1-1} \sum_{k_2=0}^{d_2-1} \cdots \sum_{k_n=0}^{d_n-1} C_{1,k_1} C_{2,k_2} \cdots C_{n,k_n} \ket{k_1, k_2, \ldots, k_n}$$

— **Basis of $n$-qubit space $(\mathbb{C}^2)^{\otimes n}$ is labeled by all $n$-bit strings.**

$$(\mathbb{C}^2)^{\otimes n} = \mathrm{span}\big\{\ket{\vec{x}} : \underbrace{\vec{x} \in \{0,1\}^n}_{\text{Set of all $n$-bit strings.}}\big\}$$

**Notation:** $\vec{x} \in \{0,1\}^n \Rightarrow \vec{x} = (x_1, x_2, \ldots, x_n)$, $x_i \in \{0,1\}$

$$\ket{\vec{x}} = \ket{x_1, x_2, \ldots, x_n} \equiv \ket{x_1} \otimes \ket{x_2} \otimes \cdots \otimes \ket{x_n}$$
