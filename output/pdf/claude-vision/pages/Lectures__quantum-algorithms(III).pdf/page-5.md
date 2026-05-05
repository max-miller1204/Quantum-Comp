(b) <u>The Quantum Version!</u>   (Quantum Fourier Transform $\equiv$ QFT).

- $Y_k = \frac{1}{\sqrt{N}} \sum_{k'=0}^{N-1} x_{k'} \, e^{\frac{2\pi i k' k}{N}} \quad \longrightarrow \quad Q\ket{k} = \frac{1}{\sqrt{d}} \sum_{k'=0}^{d-1} e^{\frac{2\pi i k k'}{d}} \ket{k'}$   (action on basis vectors).

$$\underbrace{\phantom{Q\ket{k}}}_{\text{QFT matrix}}$$

$\ket{x} = \sum_{k=0}^{d-1} x_k \ket{k} \quad \Longrightarrow \quad Q\ket{x} = \sum_{k=0}^{d-1} x_k \, Q\ket{k} = \sum_{k=0}^{d-1} x_k \, \frac{1}{\sqrt{d}} \sum_{k'=0}^{d-1} e^{\frac{2\pi i k k'}{d}} \ket{k'}$

$$= \sum_{k'=0}^{d-1} \underbrace{\left( \frac{1}{\sqrt{d}} \sum_{k=0}^{d-1} x_k \, e^{\frac{2\pi i k k'}{d}} \right)}_{\equiv\, Y_{k'}} \ket{k'} = \ket{\tilde{x}}$$

- The QFT matrix is unitary! Let $\omega = e^{\frac{2\pi i}{d}}, \quad \overline{\omega} = e^{-\frac{2\pi i}{d}} = \omega^{-1}$  $\quad d = 2^n$

$$\cos\!\left(\tfrac{2\pi}{d}\right) + i\sin\!\left(\tfrac{2\pi}{d}\right)$$

$$Q = \frac{1}{\sqrt{d}} \sum_{k,k'=0}^{d-1} \omega^{k k'} \ket{k}\bra{k'}$$

$\omega = e^{\frac{2\pi i}{d}} = \cos\!\left(\tfrac{2\pi}{d}\right) + i\sin\!\left(\tfrac{2\pi}{d}\right)$

$\overline{\omega} = \cos\!\left(\tfrac{2\pi}{d}\right) - i\sin\!\left(\tfrac{2\pi}{d}\right)$

$\quad = e^{-\frac{2\pi i}{d}}$

$\quad = \omega^{-1}$

$$Q Q^\dagger = \left( \frac{1}{\sqrt{d}} \sum_{k,k'=0}^{d-1} \omega^{k k'} \ket{k}\bra{k'} \right) \left( \frac{1}{\sqrt{d}} \sum_{j,j'=0}^{d-1} \omega^{-j j'} \ket{j'}\bra{j} \right)$$

$$= \frac{1}{d} \sum_{k,k'=0}^{d-1} \sum_{j,j'=0}^{d-1} \omega^{k k'} \, \omega^{-j j'} \ket{k} \underbrace{\braket{k'|j'}}_{=\,\delta_{j',k'}} \bra{j}$$

$$= \frac{1}{d} \sum_{k,k'=0}^{d-1} \sum_{j=0}^{d-1} \omega^{k k'} \, \omega^{-j k'} \ket{k}\bra{j}$$

$$= \sum_{k,j=0}^{d-1} \underbrace{\left( \frac{1}{d} \sum_{k'=0}^{d-1} \omega^{k'(k-j)} \right)}_{\phantom{xxx}} \ket{k}\bra{j}$$
