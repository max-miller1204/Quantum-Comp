## Expectation Value of an Observable.

**❋ Axiom of Quantum Mechanics:** Observables are described mathematically by **Hermitian operators**. $H^\dagger = H$.

- **Recall:** Hermitian operators have a *spectral/eigenvalue decomposition*:

$$H\ket{\chi_k} = \lambda_k \ket{\chi_k}$$

$$H = \sum_{k=1}^{d} \lambda_k \ket{\chi_k}\bra{\chi_k}$$

  ↑ eigenvectors.
  eigenvalues (real numbers).

**❋ Examples:** the Pauli operators!

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \ket{+}\bra{+} - \ket{-}\bra{-}$$

$$Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \ket{+i}\bra{+i} - \ket{-i}\bra{-i}$$

$$Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \ket{0}\bra{0} - \ket{1}\bra{1}.$$

- Eigenvectors are orthonormal basis ⇒ they define a measurement!

$$\sum_{k=1}^{d} \ket{\chi_k}\bra{\chi_k} = \mathbb{1}.$$

For a density operator $\rho$:
$$\Pr[k] = \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big) \to \text{The associated ``observed'' value is } \lambda_k.$$

(Example: $k \equiv$ energy level of a molecule, $\lambda_k \equiv$ the energy value).

$$\sum_{k=1}^{d} \Pr(k) = \sum_{k=1}^{d} \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big) = \mathrm{Tr}\Big(\underbrace{\Big(\sum_{k=1}^{d}\ket{\chi_k}\bra{\chi_k}\Big)}_{=\,\mathbb{1}}\rho\Big) = \mathrm{Tr}(\rho) = 1.$$

- The expected (aka "mean" or "average") value of an observable, given a state $\rho$, is

$$\sum_{k=1}^{d} \Pr(k)\cdot \lambda_k = \sum_{k=1}^{d} \mathrm{Tr}\big(\ket{\chi_k}\bra{\chi_k}\rho\big)\cdot \lambda_k$$

$$= \mathrm{Tr}\Big(\underbrace{\Big(\sum_{k=1}^{d}\lambda_k\ket{\chi_k}\bra{\chi_k}\Big)}_{H}\rho\Big) = \underline{\underline{\mathrm{Tr}(H\rho)}}$$

$$\left(\begin{array}{l}\text{❋ Recall: for a}\\ \text{random variable } X,\\ \mathbb{E}(X) = \sum_x \Pr(X=x)\cdot x\end{array}\right)$$
