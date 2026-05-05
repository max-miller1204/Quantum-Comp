$$= \underbrace{\sum_{k=0}^{\infty} \frac{1}{(2k)!} \left(\frac{\theta}{2}\right)^{2k} (-1)^k}_{\cos(\frac{\theta}{2})} \mathbb{1} \;-\; i \underbrace{\sum_{k=0}^{\infty} \frac{1}{(2k+1)!} \left(\frac{\theta}{2}\right)^{2k+1} (-1)^k}_{\sin(\frac{\theta}{2})} X$$

$$= \cos\left(\tfrac{\theta}{2}\right) \mathbb{1} - i \sin\left(\tfrac{\theta}{2}\right) X$$

(✱) Similar argument to show $R_y(\theta) = e^{-i\frac{\theta}{2} Y} = \cos(\tfrac{\theta}{2}) \mathbb{1} - i \sin(\tfrac{\theta}{2}) Y$

$$R_z(\theta) = e^{-i\frac{\theta}{2} Z} = \cos(\tfrac{\theta}{2}) \mathbb{1} - i \sin(\tfrac{\theta}{2}) Z$$

- **Important properties of Unitaries.**

  - <u>Unitaries preserve norm</u>: For $U \in L(\mathbb{C}^d)$ unitary, $\ket{v} \in \mathbb{C}^d$ arbitrary,

  $$\ket{\tilde{v}} = U\ket{v} \;\rightarrow\; \| \ket{\tilde{v}} \|^2 = \braket{\tilde{v}|\tilde{v}} = \braket{v | \underbrace{U^\dagger U}_{=\mathbb{1}} | v} = \braket{v|v}$$

  $$\left( (M_1 M_2)^\dagger = M_2^\dagger M_1^\dagger \right)$$

  $$\bra{\tilde{v}} = (\ket{\tilde{v}})^\dagger = (U\ket{v})^\dagger = \bra{v} U^\dagger$$

  - <u>Unitaries preserve states</u>: let $\rho$ be a density operator representing a mixed quantum state. Then the transformed state is given by

  $$\tilde{\rho} = U \rho U^\dagger \;\rightarrow\; \text{This is still a density matrix!}$$

  Check: (1) $\tilde{\rho}^\dagger = (U \rho U^\dagger)^\dagger = (U^\dagger)^\dagger \rho^\dagger U^\dagger = U \rho U^\dagger$ ✓
  
  $\;\;\;\;\underbrace{\;\;\;}_{\tilde{\rho}} \quad \underbrace{\;\;\;}_{=U} \underbrace{\;\;\;}_{=\rho} \underbrace{\;\;\;}_{\tilde{\rho}}$

  $$\left( (M_1 M_2 M_3)^\dagger = M_3^\dagger M_2^\dagger M_1^\dagger \right)$$

  (2) $\text{Tr}[\tilde{\rho}] = \text{Tr}[U \rho U^\dagger] = \text{Tr}[U^\dagger U \rho] = \text{Tr}[\rho] = 1$ ✓

  $$\left( \text{(✱) Cyclicity of trace: } \text{Tr}[M_1 M_2 M_3] = \text{Tr}[M_2 M_3 M_1] = \text{Tr}[M_3 M_2 M_1] \right)$$
