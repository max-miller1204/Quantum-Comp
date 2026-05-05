## ④ Observables

- In quantum mechanics, measurement outcomes are not deterministic — they occur with some probability.

- What is the *expected* outcome of a measurement?

- Recall: For a probability mass function $p_X(x)$, $\quad \left( \begin{array}{l} p_X(x) \in [0,1] \;\; \forall x \in \mathcal{X} \\ \sum_{x \in \mathcal{X}} p_X(x) = 1 \end{array} \right)$

  [Red annotation: $X$ is a Random variable $\to \Pr(X = x) = p_X(x)$.]

  the expected value is

$$\mathbb{E}(X) = \sum_x p_X(x) \cdot x$$

- We can measure w.r.t. any orthonormal basis — consider basis $\{\ket{e_k}\}_{k=1}^{d}$.

  Outcomes are labeled by $k$
  Outcome $k$ is associated with value $\lambda_k$. $\leftrightarrow$ random variable $X$

  For a state vector $\ket{\psi} \in \mathbb{C}^d$, the probability distribution is

$$\Pr(k) = |\braket{e_k|\psi}|^2 \equiv \Pr(X = \lambda_k)$$

  The expected value of $X$ is:

  [Blue annotation: $\braket{v_1 | M | v_2} = \mathrm{Tr}\left[ M \ket{v_2}\bra{v_1} \right]$.]

$$\mathbb{E}(X) = \sum_{k=1}^{d} \Pr(X = \lambda_k) \cdot \lambda_k = \sum_{k=1}^{d} |\braket{e_k|\psi}|^2 \cdot \lambda_k = \sum_{k=1}^{d} \braket{e_k | \psi}\braket{\psi | e_k} \cdot \lambda_k$$

$$= \sum_{k=1}^{d} \mathrm{Tr}\!\left( \ket{e_k}\bra{e_k} \psi \rangle\langle \psi \right) \cdot \lambda_k = \mathrm{Tr}\!\left[ \left( \sum_{k=1}^{d} \lambda_k \ket{e_k}\bra{e_k} \right) \ket{\psi}\bra{\psi} \right] = \mathrm{Tr}\!\left[ H \ket{\psi}\bra{\psi} \right].$$

$$H \ket{e_{k'}} = \sum_{k=1}^{d} \lambda_k \ket{e_k}\underbrace{\braket{e_k|e_{k'}}}_{\delta_{k,k'}} = \lambda_{k'} \ket{e_{k'}}$$

[Red annotation: $H \to$ Hermitian operator.]
