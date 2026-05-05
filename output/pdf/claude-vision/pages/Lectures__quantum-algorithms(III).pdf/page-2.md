$$\mathbb{E}[X] = (+1) \cdot \Pr[X=+1] + (-1) \cdot \Pr[X=-1] = \tfrac{1}{2}(1+\alpha) - \tfrac{1}{2}(1-\alpha) = \alpha.$$

- As $N \to \infty$, $\hat{X}_N \to \mathbb{E}[X] = \alpha$  $\quad$ (law of large numbers).

✱ So the sample average approaches the true (unknown) value of $\alpha$!

② <u>Motivation: Expectation values</u>

- Why do we care about quantities of the form $\braket{\psi|U|\psi}$?

  B/c they can be used to compute <u>expectation values</u> of <u>observables</u>.

- <u>Observable</u>: Any Hermitian operator ( <u>recall</u>: $M$ Hermitian $\iff M^\dagger = M$ )

  ✱ <u>Fact from linear algebra</u>: Every Hermitian operator can be <u>diagonalized</u>.

  $$M = \sum_{i=1}^{d} \lambda_i \ket{v_i}\bra{v_i}, \quad \text{where:} \quad \lambda_i : \text{eigenvalues (real numbers)}. \quad Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$
  $$\boxed{\sum_{i=1}^{d} \ket{v_i}\bra{v_i} = \mathbb{1}} \qquad \ket{v_i}: \text{orthonormal eigenvectors.} \quad = \ket{0}\bra{0} - \ket{1}\bra{1}$$

  ✱ <u>Axiom of quantum mechanics</u>: every physical quantity corresponds to a Hermitian operator. (e.g., position, momentum, energy...).

  The eigenvalues are the possible values of the quantity.

  We get the value of the quantity through measurement.

- For an observable / Hermitian operator $M$, the corresponding measurement is given by the eigenvectors. ($\{\ket{v_i}\bra{v_i}\}$ is the POVM.)

- For a state $\rho$, the probability that it has value $\lambda_i$ is
