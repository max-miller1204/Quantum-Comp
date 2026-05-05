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
