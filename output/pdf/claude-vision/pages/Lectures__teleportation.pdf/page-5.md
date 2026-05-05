(2) $\text{CNOT}_{A'A}$: $\frac{1}{\sqrt{2}}(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB}$
$\qquad\qquad\qquad +\beta\underset{\color{red}1,1}{\ket{1,0,0}}_{A'AB} + \beta\underset{\color{red}1,0}{\ket{1,1,1}}_{A'AB})$

$\downarrow$

$\frac{1}{\sqrt{2}}(\alpha\ket{0,0,0}_{A'AB} + \alpha\ket{0,1,1}_{A'AB}$
$\qquad +\beta\ket{1,1,0}_{A'AB} + \beta\ket{1,0,1}_{A'AB})$

(3) Hadamard on $A'$: $\frac{1}{\sqrt{2}}(\alpha\underset{\color{red}\ket{+}}{\ket{0,0,0}}_{A'AB} + \alpha\underset{\color{red}\ket{+}}{\ket{0,1,1}}_{A'AB}$
$\qquad\qquad\qquad\qquad +\beta\underset{\color{red}\ket{-}}{\ket{1,1,0}}_{A'AB} + \beta\underset{\color{red}\ket{-}}{\ket{1,0,1}}_{A'AB})$

$\color{blue}H\ket{0} = \ket{+}$
$\color{blue}H\ket{1} = \ket{-}$

$\downarrow$

$\frac{1}{\sqrt{2}}(\alpha\ket{+,0,0}_{A'AB} + \alpha\ket{+,1,1}_{A'AB}$
$\qquad +\beta\ket{-,1,0}_{A'AB} + \beta\ket{-,0,1}_{A'AB})$

(4) Measure $A'A$ in the $Z$-basis / computational basis / $\{\ket{0},\ket{1}\}$ basis:

- **Four outcomes**: $00, 01, 10, 11 = (z,x)$

$\frac{1}{\sqrt{2}}(\alpha\ket{+,0,0}_{A'AB} + \alpha\ket{+,1,1}_{A'AB} + \beta\ket{-,1,0}_{A'AB} + \beta\ket{-,0,1}_{A'AB})$

$= \frac{1}{\sqrt{2}}\Big(\alpha\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})_{A'}\ket{0,0}_{AB} + \alpha\frac{1}{\sqrt{2}}(\ket{0}+\ket{1})_{A'}\ket{1,1}_{AB}$
$\qquad + \beta\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})_{A'}\ket{1,0}_{AB} + \beta\frac{1}{\sqrt{2}}(\ket{0}-\ket{1})_{A'}\ket{0,1}_{AB}\Big)$

$\downarrow$

$\ket{\phi}_{A'AB} = \Big(\ket{0,0}_{A'A}\frac{1}{2}(\alpha\ket{0}+\beta\ket{1})_B + \ket{0,1}_{A'A}\frac{1}{2}(\alpha\ket{1}+\beta\ket{0})_B$
$\qquad\qquad + \ket{1,0}_{A'A}\frac{1}{2}(\alpha\ket{0}-\beta\ket{1})_B + \ket{1,1}_{A'A}\frac{1}{2}(\alpha\ket{1}-\beta\ket{0})_B\Big)$
