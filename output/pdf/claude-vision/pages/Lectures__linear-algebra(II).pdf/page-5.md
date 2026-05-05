$\ket{1}\otimes\ket{0} = \begin{pmatrix} 0 \\ 0 \\ 1 \\ 0 \end{pmatrix}$, $\ket{1}\otimes\ket{1} = \begin{pmatrix} 0 \\ 0 \\ 0 \\ 1 \end{pmatrix}$ → This defines the vector space $\mathbb{C}^2 \otimes \mathbb{C}^2$.

✲ $\{\ket{0}\otimes\ket{0}, \ket{0}\otimes\ket{1}, \ket{1}\otimes\ket{0}, \ket{1}\otimes\ket{1}\}$ is the standard/computational basis for $\mathbb{C}^2 \otimes \mathbb{C}^2$. (Just all two-bit strings!)

✲ Probabilities: $\Pr[0,0] = |\alpha_1\alpha_2|^2$, $\Pr[0,1] = |\alpha_1\beta_2|^2$, $\Pr[1,0] = |\beta_1\alpha_2|^2$, $\Pr[1,1] = |\beta_1\beta_2|^2$.

✲ This extends to any dimension!

For $\mathbb{C}^{d_1} \otimes \mathbb{C}^{d_2}$, basis is $\{\ket{k_1}\otimes\ket{k_2} : k_1 \in \{0,1,\ldots,d_1-1\}, k_2 \in \{0,1,\ldots,d_2-1\}\}$
Dimension is $d_1 \cdot d_2$.

✲ Shorthand notation: $\ket{k_1}\otimes\ket{k_2} \equiv \ket{k_1}\ket{k_2} \equiv \ket{k_1, k_2}$.

– Tensor product of three vectors:

$$\ket{\psi_1} = \begin{pmatrix} \alpha_1 \\ \beta_1 \end{pmatrix}, \quad \ket{\psi_2} = \begin{pmatrix} \alpha_2 \\ \beta_2 \end{pmatrix}, \quad \ket{\psi_3} = \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix}$$

$$\Rightarrow \ket{\psi_1}\otimes\ket{\psi_2}\otimes\ket{\psi_3} = \big(\ket{\psi_1}\otimes\ket{\psi_2}\big)\otimes\ket{\psi_3} = \ket{\psi_1}\otimes\big(\ket{\psi_2}\otimes\ket{\psi_3}\big).$$

$$= \begin{pmatrix} \alpha_1\alpha_2 \\ \alpha_1\beta_2 \\ \beta_1\alpha_2 \\ \beta_1\beta_2 \end{pmatrix} \otimes \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} = \begin{pmatrix} \alpha_1\alpha_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \alpha_1\beta_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \beta_1\alpha_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \\ \beta_1\beta_2 \begin{pmatrix} \alpha_3 \\ \beta_3 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} \alpha_1\alpha_2\alpha_3 \\ \alpha_1\alpha_2\beta_3 \\ \alpha_1\beta_2\alpha_3 \\ \alpha_1\beta_2\beta_3 \\ \beta_1\alpha_2\alpha_3 \\ \beta_1\alpha_2\beta_3 \\ \beta_1\beta_2\alpha_3 \\ \beta_1\beta_2\beta_3 \end{pmatrix} \begin{matrix} 000 \\ 001 \\ 010 \\ 011 \\ 100 \\ 101 \\ 110 \\ 111 \end{matrix}$$

✲ The resulting vector has dimension $8 = 2 \cdot 2 \cdot 2 = 2^3$!

✲ The vector space is $\mathbb{C}^2 \otimes \mathbb{C}^2 \otimes \mathbb{C}^2$.
