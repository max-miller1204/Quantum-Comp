- **Rotation Gates:**

$$R_X(\theta) = e^{-i\frac{\theta}{2}X} \quad \rightarrow \text{rotation around X-axis by angle } \theta.$$

$$R_Y(\theta) = e^{-i\frac{\theta}{2}Y} \quad \rightarrow \text{rotation around Y-axis by angle } \theta.$$

$$R_Z(\theta) = e^{-i\frac{\theta}{2}Z} \quad \rightarrow \text{rotation around Z-axis by angle } \theta.$$

[Bloch sphere diagram with axes labeled $x$, $y$, $z$; points marked $\ket{+}$ on +x axis and $\ket{+i}$ on +y axis]

$$e^M := \sum_{k=0}^{\infty} \frac{1}{k!} M^k \quad (\text{matrix exponential})$$

$$\Rightarrow \quad e^{-i\frac{\theta}{2}X} = \sum_{k=0}^{\infty} \frac{1}{k!}\left(-i\frac{\theta}{2}X\right)^k$$

$$\left(\begin{array}{l} X^2 = \mathbb{1} \\ \Rightarrow X^k = \mathbb{1},\ k \text{ even} \\ \quad\ X^k = X,\ k \text{ odd} \end{array}\right)$$

$X^3 = \underbrace{X^2}_{\mathbb{1}} \cdot X = X \qquad X^4 = \underbrace{X^2 \cdot X^2}_{} = \mathbb{1}$

$$= \sum_{k=0}^{\infty} \frac{1}{(2k)!}\left(-i\frac{\theta}{2}X\right)^{2k} + \sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\left(-i\frac{\theta}{2}X\right)^{2k+1}$$

$$\underbrace{\phantom{xxxxxxxxxxxx}}_{0,2,4,6,\ldots} \qquad \underbrace{\phantom{xxxxxxxxxxxx}}_{1,3,5,7,\ldots}$$

$$= \sum_{k=0}^{\infty} \frac{1}{(2k)!}\left(\frac{\theta}{2}\right)^{2k}(-i)^{2k}\,\mathbb{1} + \sum_{k=0}^{\infty} \frac{1}{(2k+1)!}\left(\frac{\theta}{2}\right)^{2k+1}(-i)^{2k+1} X$$

$$i \cdot i = i^2 = -1$$

$(-i)^1 = -i \quad (k=0)$

$(-i)^3 = \underbrace{-i \cdot -i}_{-1} \cdot -i = i \quad (k=1)$

$(-i)^5 = -i \qquad\qquad (k=2)$

$\vdots$

$(-i)^{2k+1} = -i(-1)^k$

$(-i)^2 = -i \cdot -i = -1 \quad (k=1)$

$(-i)^4 = ((-i)^2)^2 = 1 \quad (k=2)$

$(-i)^6 = -1 \qquad\qquad (k=3)$

$\vdots$

$(-i)^{2k} = (-1)^k$
