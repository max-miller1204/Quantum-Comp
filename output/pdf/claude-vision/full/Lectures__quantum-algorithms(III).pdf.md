# Lectures__quantum-algorithms(III).pdf

## Page 1

① <u>Recap: Hadamard Test.</u>

Estimating $\bra{\psi}U\ket{\psi}$, where $U$ is a unitary and $\ket{\psi}$ is a state vector.

[Circuit diagram: top wire $\ket{0}$ — H — •  — H — $\pi$ (Pauli-Z measurement); bottom wire $\ket{\psi}$ — U (controlled by top wire) — ]

$$\Pr[0] = \tfrac{1}{2}\bigl(1 + \mathrm{Re}(\bra{\psi}U\ket{\psi})\bigr), \quad \Pr[1] = \tfrac{1}{2}\bigl(1 - \mathrm{Re}(\bra{\psi}U\ket{\psi})\bigr).$$

$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \;\Rightarrow\; S^\dagger = \begin{pmatrix} 1 & 0 \\ 0 & -i \end{pmatrix}$$

For the imaginary part:

[Circuit diagram: top wire $\ket{0}$ — H — $S^\dagger$ — • — H — $\pi$ ; bottom wire $\ket{\psi}$ — U (controlled) — ]

$$\Pr[0] = \tfrac{1}{2}\bigl(1 + \mathrm{Im}(\bra{\psi}U\ket{\psi})\bigr)$$

$$\Pr[1] = \tfrac{1}{2}\bigl(1 - \mathrm{Im}(\bra{\psi}U\ket{\psi})\bigr).$$

✱ In both cases, we have $\Pr[0] = \tfrac{1}{2}(1+\alpha)$, $\Pr[1] = \tfrac{1}{2}(1-\alpha)$, where $\alpha$ is unknown. To <u>estimate</u> $\alpha$, we do the following <u>procedure</u>:

For $i = 1, 2, \ldots, N$ ($N \equiv \#$ of samples / # of times we run the quantum circuit).

- Each time we get outcome "0" → record $x_i = 1$
- Each time we get outcome "1" → record $x_i = -1$

✱ This defines a random <u>variable</u> $X$:

$$\Pr[X = \pm 1] = \tfrac{1}{2}(1 \pm \alpha)$$

- Do this $N$ times, then take the <u>sample mean/average</u>: $\hat{X}_N = \tfrac{1}{N} \sum_{i=1}^{N} x_i$ ← sample mean

This defines a random variable $\hat{X}_N = \tfrac{1}{N}\sum_{i=1}^{N} X_i$. $\hat{X}_N$ is an <u>unbiased estimator</u> of $X$:

$$\mathbb{E}[\hat{X}_N] = \tfrac{1}{N}\sum_{i=1}^{N}\mathbb{E}[X_i] = \tfrac{1}{N}\sum_{i=1}^{N}\mathbb{E}[X] = \mathbb{E}[X].$$

↑ True mean

$\mathbb{E}[X_i] = \mathbb{E}[X]\;\forall i$, b/c all samples are independent and identical.

## Page 2

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

## Page 3

$$\Pr[i] = \text{Tr}\left[\ket{v_i}\bra{v_i}\rho\right] \quad \text{(Born rule)} \quad = \bra{v_i}\rho\ket{v_i}$$

The <u>expected value</u> of the observable is:

$$\langle M \rangle_\rho = \sum_{i=1}^{\hat{n}} \lambda_i \Pr[i] = \sum_{i=1}^{\hat{n}} \lambda_i \text{Tr}\left[\ket{v_i}\bra{v_i}\rho\right] = \text{Tr}\left[\underbrace{\left(\sum_{i=1}^{\hat{n}} \lambda_i \ket{v_i}\bra{v_i}\right)}_{M}\rho\right] = \text{Tr}[M\rho].$$

[Red annotation pointing to the "=" sign: "Definition of expectation value!"]

- If we don't know the eigenvectors (b/c they are hard to get for large matrices!), but we know that $M$ can be written as

$$M = \sum_{j=1}^{k} c_j \underbrace{U_j}_{\text{unitaries}}, \quad \text{then} \quad \langle M \rangle_\gamma = \text{Tr}(M\ket{\gamma}\bra{\gamma})$$

$$= \sum_{j=1}^{k} c_j \text{Tr}(U_j \ket{\gamma}\bra{\gamma})$$

$$= \sum_{j=1}^{k} c_j \underbrace{\bra{\gamma}U_j\ket{\gamma}}_{\text{Estimate using Hadamard test!}}$$

So we estimate each term individually using the Hadamard test and then add to get an overall estimate of the expectation value.

## Page 4

## ③ Quantum Fourier Transform

(a) <u>Recap</u>: discrete Fourier transform (DFT).

- Used in a lot of places!
    - Signal processing — identifying frequency components of a signal. (audio and video processing)
    - Machine learning — feature extraction
    - Scientific Computing — solving differential equations numerically.

- <u>Definition</u>: for a signal $\{x_k\}_{k=0}^{N-1}$, its DFT is

$$y_k = \frac{1}{\sqrt{N}} \sum_{k'=0}^{N-1} x_{k'}\, e^{\frac{2\pi i k' k}{N}} \qquad \left( e^{2\pi i x} = \cos(2\pi x) + i\sin(2\pi x) \right)$$

- <u>Example</u>: consider a signal of two sine waves put together:

$$x(t) = \sin(2\pi f_1 t) + \tfrac{1}{2}\sin(2\pi f_2 t)$$

with $f_1, f_2$ marked as <span style="color:purple">frequencies</span>.

- $f_1 = 5$ Hz
- $f_2 = 15$ Hz
- Sampling rate: $f_s = 100$ Hz $\Rightarrow$ 100 samples total (in 1 sec.)

[Three plots side by side:
1. "Time-Domain Signal" — continuous oscillating waveform, amplitude between -1 and 1, time 0 to 1 s.
2. "Time-Domain Signal (sampled)" — same waveform shown as discrete sample points connected by lines.
3. "Frequency-Domain Spectrum ($|y_k|$)" — magnitude vs frequency [Hz], with a tall spike of magnitude 1.0 at 5 Hz and a smaller spike of magnitude 0.5 at 15 Hz.]

## Page 5

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

## Page 6

$$\downarrow \quad \rightarrow \delta_{j,k}$$

$$= \frac{1}{d}\sum_{k'=0}^{d-1} e^{\frac{2\pi i}{d} k'(k-j)}$$

with $\underbrace{(k-j)}_{\equiv x}$

[Sketch: sine and cosine waves over $[0, 2\pi]$ on the same axis]

① If $x = 0 \rightarrow \dfrac{1}{d}\sum_{k'=0}^{d-1}(1) = 1$

② If $x \neq 0 \rightarrow \dfrac{1}{d}\sum_{k'=0}^{d-1} \omega^{k'x} \rightarrow (\omega^x)^{k'}$

$$(\omega^x)^d = e^{\frac{2\pi i}{d}\cdot d \cdot x} = e^{2\pi i x} = \underbrace{\cos(2\pi x)}_{=1\,\forall x} + i\underbrace{\sin(2\pi x)}_{=0\,\forall x}$$

$$\omega = e^{\frac{2\pi i}{d}}, \qquad \omega^x = e^{\frac{2\pi i x}{d}}, \qquad \omega^{xd} = e^{2\pi i x} = 1$$

$$= \underbrace{\frac{1}{d}\sum_{k'=0}^{d-1}(\omega^x)^{k'}}_{\text{Finite geometric series!}} = \frac{1}{d}\left(\frac{1-(\omega^x)^d}{1-\omega}\right) = 0.$$

$$\sum_{k=0}^{d-1} r^{k'} = \frac{1-r^d}{1-r}$$

③ So $\dfrac{1}{d}\sum_{k'=0}^{d-1} \omega^{k'(k-j)} = \delta_{j-k,\,0} = \delta_{j,k}$

$$\Rightarrow \;\; QQ^\dagger = \sum_{k,j=0}^{d-1} \underbrace{\left(\frac{1}{d}\sum_{k'=0}^{d-1}\omega^{k'(k-j)}\right)}_{\delta_{k,j}} \ket{k}\bra{j} = \mathbb{1} \;\checkmark$$

Similarly, $Q^\dagger Q = \mathbb{1}$.

$$Q = \frac{1}{\sqrt{d}}\begin{pmatrix} 1 & 1 & 1 & \cdots & 1 \\ 1 & \omega & \omega^2 & \cdots & \omega^{d-1} \\ 1 & \omega^2 & \omega^4 & \cdots & \omega^{2(d-1)} \\ \vdots & \vdots & & & \vdots \\ 1 & \omega^{d-1} & \omega^{2(d-1)} & \cdots & \omega^{(d-1)^2} \end{pmatrix}$$

## Page 7

<u>Note</u>: for $d=2$, $\omega = e^{\frac{2\pi i}{2}} = e^{\pi i} = -1 \;\Rightarrow\; Q = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & \omega \end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix} \to$ Hadamard!

— Let $d = 2^n$, $\omega = e^{\frac{2\pi i}{2^n}} \to$ <u>What is a circuit representation of QFT?</u>

Use the binary representation of $0, 1, 2, \ldots, 2^n - 1$

e.g., $n = 3$:

$$
\begin{aligned}
0 &\to 000 \\
1 &\to 001 \\
2 &\to 010 \\
3 &\to 011 \\
4 &\to 100 \\
5 &\to 101 \\
6 &\to 110 \\
7 &\to 111
\end{aligned}
\quad\Rightarrow\quad
\begin{array}{l}
\in \{0,1,2,\ldots,7\} \\
k \to (k_1, k_2, k_3) \\[4pt]
k = k_1 \cdot 4 + k_2 \cdot 2 + k_3 \cdot 1 \\[6pt]
\circledast \text{ In general: } k = \sum_{\ell=1}^{n} 2^{n-\ell} k_\ell
\end{array}
$$

$$Q\ket{j} = \frac{1}{\sqrt{2^n}} \sum_{k=0}^{2^n - 1} e^{\frac{2\pi i j k}{2^n}} \ket{k}$$

$$\Rightarrow Q\ket{j_1, j_2, \ldots, j_n} = \frac{1}{\sqrt{2^n}} \sum_{k_1, k_2, \ldots, k_n \in \{0,1\}} e^{\frac{2\pi i}{2^n} j (k_1 2^{n-1} + k_2 2^{n-2} + \cdots + k_n)} \ket{k_1, k_2, \ldots, k_n}$$

$$= \frac{1}{\sqrt{2^n}} \sum_{k_1 \in \{0,1\}} \sum_{k_2 \in \{0,1\}} \cdots \sum_{k_n \in \{0,1\}} e^{\frac{2\pi i}{2^n} j k_1 2^{n-1}} \, e^{\frac{2\pi i}{2^n} j k_2 2^{n-2}} \cdots e^{\frac{2\pi i}{2^n} j k_n} \ket{k_1, k_2, \ldots, k_n}$$

$$= \left( \frac{1}{\sqrt{2}} \sum_{k_1 \in \{0,1\}} e^{\frac{2\pi i}{2^n} j k_1 2^{n-1}} \ket{k_1} \right) \left( \frac{1}{\sqrt{2}} \sum_{k_2 \in \{0,1\}} e^{\frac{2\pi i}{2^n} j k_2 2^{n-2}} \ket{k_2} \right) \cdots \left( \frac{1}{\sqrt{2}} \sum_{k_n \in \{0,1\}} e^{\frac{2\pi i}{2^n} j k_n} \ket{k_n} \right)$$

$$= \left( \frac{1}{\sqrt{2}} \sum_{k_1 \in \{0,1\}} e^{2\pi i k_1 \frac{j}{2}} \ket{k_1} \right) \left( \frac{1}{\sqrt{2}} \sum_{k_2 \in \{0,1\}} e^{2\pi i k_2 \frac{j}{2^2}} \ket{k_2} \right) \cdots \left( \frac{1}{\sqrt{2}} \sum_{k_n \in \{0,1\}} e^{2\pi i k_n \frac{j}{2^n}} \ket{k_n} \right)$$

## Page 8

Consider $n=3$: $\mathcal{Q}\ket{j_1, j_2, j_3} = \left(\frac{1}{\sqrt{2}}\sum_{k_1 \in \{0,1\}} e^{2\pi i k_1 \frac{j}{2}}\ket{k_1}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_2 \in \{0,1\}} e^{2\pi i k_2 \frac{j}{2^2}}\ket{k_2}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_3 \in \{0,1\}} e^{2\pi i k_3 \frac{j}{2^3}}\ket{k_3}\right)$

$$j = 4j_1 + 2j_2 + j_3 \implies \frac{j}{2} = 2j_1 + j_2 + \frac{j_3}{2}$$

$$\frac{j}{2^2} = \frac{j}{4} = j_1 + \frac{j_2}{2} + \frac{j_3}{4}$$

$$\frac{j}{2^3} = \frac{j}{8} = \frac{j_1}{2} + \frac{j_2}{4} + \frac{j_3}{8}$$

$$\implies e^{2\pi i k_1 \frac{j}{2}} = \underbrace{e^{2\pi i k_1 (2j_1)}}_{=1} \underbrace{e^{2\pi i k_1 j_2}}_{=1} e^{2\pi i k_1 \frac{j_3}{2}} = e^{\pi i k_1 j_3} = (-1)^{k_1 j_3}$$

$$e^{2\pi i k_2 \frac{j}{4}} = \underbrace{e^{2\pi i k_2 j_1}}_{=1} \underbrace{e^{2\pi i k_2 (\frac{j_2}{2})}}_{=(-1)^{k_2 j_2}} \underbrace{e^{2\pi i k_2 (\frac{j_3}{4})}}_{= e^{\frac{2\pi i}{4} k_2 j_3}}$$

$$e^{2\pi i k_3 \frac{j}{8}} = \underbrace{e^{\frac{2\pi i}{2} k_3 j_1}}_{(-1)^{k_3 j_1}} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3}$$

Therefore: $\mathcal{Q}\ket{j_1, j_2, j_3} = \left(\frac{1}{\sqrt{2}}\sum_{k_1 \in \{0,1\}} (-1)^{k_1 j_3} \ket{k_1}\right)\left(\frac{1}{\sqrt{2}}\sum_{k_2 \in \{0,1\}} (-1)^{k_2 j_2} e^{\frac{2\pi i}{4} k_2 j_3} \ket{k_2}\right)$

$$\left(\frac{1}{\sqrt{2}}\sum_{k_3 \in \{0,1\}} (-1)^{k_3 j_1} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3} \ket{k_3}\right)$$

$$= \frac{1}{\sqrt{2^3}} \sum_{k_1, k_2, k_3 \in \{0,1\}} (-1)^{k_1 j_3} (-1)^{k_2 j_2} (-1)^{k_3 j_1} e^{\frac{2\pi i}{4} k_2 j_3} e^{\frac{2\pi i}{4} k_3 j_2} e^{\frac{2\pi i}{8} k_3 j_3} \ket{k_1, k_2, k_3}$$

$$= \widetilde{\mathcal{Q}} \ket{j_3, j_2, j_1}$$

$R_z(\theta) = e^{i\frac{\theta}{2} Z} = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{pmatrix}$ [illegible: factor]

✱ Define the rotation gate $R_k = \begin{pmatrix} 1 & 0 \\ 0 & e^{\frac{2\pi i}{2^k}} \end{pmatrix}$ $\quad R_2 = \begin{pmatrix} 1 & 0 \\ 0 & e^{\frac{2\pi i}{4}} \end{pmatrix}$

[Quantum circuit diagram enclosed in dashed purple box, labeled $\widetilde{\mathcal{Q}}$ below:
- Top wire $\ket{j_3}$: passes through control, then $R_3$ gate, then $R_2$ gate, then $H$
- Middle wire $\ket{j_2}$: $R_2$ gate, then control, then $H$, then control
- Bottom wire $\ket{j_1}$: $H$, then control, then control
]

$\begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$

$e^{\frac{\pi i}{2}} = i$

## Page 9

So $\quad U \ket{j_1, j_2, j_3} = \tilde{U} \ket{j_3, j_2, j_1} = \tilde{U} S \ket{j_1, j_2, j_3}$

$\qquad\qquad\qquad\qquad\qquad\qquad\quad \uparrow$
$\qquad\qquad\qquad\qquad\qquad$ <span style="color:purple">Permutation of the qubits!</span>

★ In general, $\tilde{U}$ is given by the following circuit:

[Quantum circuit diagram with $n$ qubit lines, top to bottom labeled $\ket{j_n}, \ket{j_{n-1}}, \ldots, \ket{j_4}, \ket{j_3}, \ket{j_2}, \ket{j_1}$.

- Bottom wire $\ket{j_1}$: starts with $H$, then acts as control for a sequence of controlled rotation gates $R_2, R_3, R_4, \ldots, R_n$ applied to wires $\ket{j_2}, \ket{j_3}, \ket{j_4}, \ldots, \ket{j_n}$ respectively.
- Next wire $\ket{j_2}$: after the $R_2$ gate from $\ket{j_1}$, has an $H$, then controls $R_2, R_3, \ldots, R_{n-1}$ on the wires above.
- Wire $\ket{j_3}$: has $R_3$ (controlled from $\ket{j_1}$), then later $R_2$ (from $\ket{j_2}$), then $H$, etc.
- Wire $\ket{j_4}$: has $R_4$ (from $\ket{j_1}$), $R_3$ (from $\ket{j_2}$), then $H$ later.
- $\vdots$
- Top wire $\ket{j_n}$: receives $R_n, R_{n-1}, \ldots, R_2$ controlled rotations, then ends with $H$.]
