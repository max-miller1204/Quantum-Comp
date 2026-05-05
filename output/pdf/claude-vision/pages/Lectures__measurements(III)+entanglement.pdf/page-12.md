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
