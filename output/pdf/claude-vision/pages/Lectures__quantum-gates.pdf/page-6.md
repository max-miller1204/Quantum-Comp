- From calculating $U\ket{\vec{x}}$ for all $\vec{x}$, we get something like the "truth table" of the quantum circuit.

✱ Elementary quantum gates (building blocks of larger circuits).

- **Pauli gates:** $-\boxed{X}-\ \rightarrow\ X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}\ \left(X\ket{0}=\ket{1},\ X\ket{1}=\ket{0}\right)$

  $X^\dagger = X$,
  $X^\dagger X = X^2 = \mathbb{1}$

  $\quad\quad\quad\quad\quad\quad\ \  -\boxed{Y}-\ \rightarrow\ Y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}\ \left(Y\ket{0}=i\ket{1},\ Y\ket{1}=-i\ket{0}\right)$

  $\quad\quad\quad\quad\quad\quad\ \  -\boxed{Z}-\ \rightarrow\ Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\ \left(Z\ket{0}=\ket{0},\ Z\ket{1}=-\ket{1}\right)$

- **Hadamard gate:** $-\boxed{H}-\ \rightarrow\ H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

  $H^\dagger = H \rightarrow H^2 = \mathbb{1}$.

  $H\ket{0} = \ket{+} = \frac{1}{\sqrt{2}}(\ket{0}+\ket{1})$
  $H\ket{1} = \ket{-} = \frac{1}{\sqrt{2}}(\ket{0}-\ket{1})$.

- **Phase gate:** $-\boxed{S}-\ \rightarrow\ S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \rightarrow S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$

- **T-gate:** $-\boxed{T}-\ \rightarrow\ T = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}$

  $\underbrace{\phantom{e^{i\pi/4}}}_{\downarrow}$

  $e^{i\pi/4} = \cos\left(\frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{4}\right)$
  $\quad\quad = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}}i$
