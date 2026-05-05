$$= \tfrac{1}{\sqrt{2}}\underbrace{\big(\bra{0}\bra{0}+\bra{1}\bra{1}\big)}_{\sum_{k=0}^{1}\bra{k}\bra{k}} \big(X^{x'}Z^{z'}Z^{z}X^{x}\otimes \mathbb{1}\big) \tfrac{1}{\sqrt{2}}\underbrace{\big(\ket{0}\ket{0}+\ket{1}\ket{1}\big)}_{\sum_{k'=0}^{1}\ket{k'}\ket{k'}}$$

$$= \tfrac{1}{2}\sum_{k,k'=0}^{1} \bra{k}\bra{k}\big(X^{x'}Z^{z'}Z^{z}X^{x}\otimes \mathbb{1}\big)\ket{k'}\ket{k'}$$

$$= \tfrac{1}{2}\sum_{k,k'=0}^{1} \bra{k}X^{x'}Z^{z'}Z^{z}X^{x}\ket{k'}\underbrace{\braket{k|k'}}_{=\delta_{k,k'}} \qquad \color{blue}{\bra{k}\bra{k}(M_1\otimes M_2)\ket{k'}\ket{k'}}$$
$$\color{blue}{= \bra{k}M_1\ket{k'}\bra{k}M_2\ket{k'}}$$

$$= \tfrac{1}{2}\sum_{k=0}^{1}\bra{k}X^{x'}Z^{z'}Z^{z}X^{x}\ket{k} \qquad \color{blue}{\sum_{k}\bra{k}M\ket{k}=\mathrm{Tr}(M)}$$

$$= \tfrac{1}{2}\mathrm{Tr}\!\left[X^{x'}Z^{z'}Z^{z}X^{x}\right] = \tfrac{1}{2}\mathrm{Tr}\!\left[X^{x}X^{x'}Z^{z'}Z^{z}\right] = \underline{\underline{\tfrac{1}{2}\mathrm{Tr}\!\left[X^{x\oplus x'}Z^{z'\oplus z}\right]}}.$$

$\color{blue}{X^{0}=\mathbb{1}}$
$\color{blue}{X^{1}=X}$

$\color{red}{\to x=0,\,x'=0 \;\Rightarrow\; X^{0}X^{0}=\mathbb{1}}$
$\color{red}{\;\;\;\; x=0,\,x'=1 \;\Rightarrow\; X^{0}X^{1}=X}$
$\color{red}{\;\;\;\; x=1,\,x'=0 \;\Rightarrow\; X^{1}X^{0}=X}$
$\color{red}{\;\;\;\; x=1,\,x'=1 \;\Rightarrow\; X^{1}X^{1}=X^{2}=\mathbb{1}}$

$\Rightarrow X^{x}X^{x'} = X^{\underline{\underline{x\oplus x'}}} \quad \oplus$

$\uparrow$ XOR!

$$\begin{pmatrix} 0\oplus 0 = 0 \\ 0\oplus 1 = 1 \\ 1\oplus 0 = 1 \\ 1\oplus 1 = 0 \end{pmatrix}$$

$\color{red}{\text{Same for } Z^{z'}Z^{z}:\; z'=0,\,z=0 \Rightarrow \mathbb{1}}$
$\color{red}{\;\;\;\; z'=0,\,z=1 \Rightarrow Z}$
$\color{red}{\;\;\;\; z'=1,\,z=0 \Rightarrow Z} \;\;\Rightarrow\; Z^{z'}Z^{z} = Z^{z'\oplus z}$
$\color{red}{\;\;\;\; z'=1,\,z=1 \Rightarrow \mathbb{1}}$

Now, we use the fact that $Z$ and $X$ are orthogonal:

$$Z=\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix},\quad X=\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix} \;\Rightarrow\; \mathrm{Tr}[X]=\mathrm{Tr}[Z]=0,\text{ and}$$

$$\mathrm{Tr}[ZX] = \mathrm{Tr}\!\left[\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}\right] = \mathrm{Tr}\!\left[\begin{pmatrix}0 & 1\\ -1 & 0\end{pmatrix}\right] = 0.$$
