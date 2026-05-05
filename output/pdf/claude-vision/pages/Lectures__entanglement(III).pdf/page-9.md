- The anti-correlation exists for <u>any</u> basis measurement!

- **Fact**: Let $U$ be an arbitrary $2 \times 2$ unitary matrix. Then
$$(U \otimes U) \ket{\Psi^-}\bra{\Psi^-} (U \otimes U)^\dagger = \ket{\Psi^-}\bra{\Psi^-}.$$

$$\ket{\Psi^-} = \tfrac{1}{\sqrt{2}}(\ket{0}\ket{1} - \ket{1}\ket{0})$$

**Proof**: First consider an arbitrary $2 \times 2$ matrix $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, $a,b,c,d \in \mathbb{C}$.

$$(M \otimes M)\ket{\Psi^-} = \tfrac{1}{\sqrt{2}}\big(M\ket{0} \otimes M\ket{1} - M\ket{1} \otimes M\ket{0}\big)$$

$\quad M\ket{0} = a\ket{0} + c\ket{1}$
$\quad M\ket{1} = b\ket{0} + d\ket{1}$

$$= \tfrac{1}{\sqrt{2}}\Big( (a\ket{0} + c\ket{1}) \otimes (b\ket{0} + d\ket{1}) - (b\ket{0} + d\ket{1}) \otimes (a\ket{0} + c\ket{1}) \Big)$$

$$= \tfrac{1}{\sqrt{2}}\Big( \cancel{ab\ket{0,0}} + ad\ket{0,1} + cb\ket{1,0} + \cancel{cd\ket{1,1}} - \cancel{ab\ket{0,0}} - cb\ket{1,0} - ad\ket{1,0}\!\!\!\!\!^{\,0,1} - \cancel{cd\ket{1,1}} \Big)$$

Wait — re-doing carefully:

$$= \tfrac{1}{\sqrt{2}}\Big( (ad - bc)\ket{0,1} - (ad - bc)\ket{1,0} \Big)$$

$$= \tfrac{1}{\sqrt{2}}(ad - bc)\big(\ket{0,1} - \ket{1,0}\big)$$

$$= (ad - bc)\,\tfrac{1}{\sqrt{2}}\big(\ket{0,1} - \ket{1,0}\big)$$

$$= \underline{\det(M)}\,\ket{\Psi^-}. \quad \to \underline{\text{determinant of } M!}$$

So for any matrix $M$: $\;(M \otimes M)\ket{\Psi^-}\bra{\Psi^-}(M \otimes M)^\dagger = |\det(M)|^2 \ket{\Psi^-}\bra{\Psi^-}.$

Determinant is product of the eigenvalues.

Let $U = \sum_{k=1}^{d} \lambda_k \ket{\gamma_k}\bra{\gamma_k}$ be the spectral decomposition of a unitary.

Then $U^\dagger = \sum_{k=1}^{d} \overline{\lambda_k} \ket{\gamma_k}\bra{\gamma_k} \;\Rightarrow\; UU^\dagger = \sum_{k=1}^{d} |\lambda_k|^2 \ket{\gamma_k}\bra{\gamma_k} = \mathbb{1}$ (by unitarity) $\quad \lambda_k = re^{i\theta}$

Also, $\sum_{k=1}^{d} \ket{\gamma_k}\bra{\gamma_k} = \mathbb{1} \;\Rightarrow\; |\lambda_k|^2 = 1 \;\forall\, k \;\Rightarrow\; \lambda_k = e^{i\theta_k} \;\Rightarrow\;$ eigenvalues of
