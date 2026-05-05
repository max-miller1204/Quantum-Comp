$\downarrow$

$\xmapsto{H_{A'}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{0}_B - \beta \ket{1}_{A'} \ket{1}_A \ket{0}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{1}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big).$

$\xmapsto{\text{CNOT}_{AB}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{0}_B \qquad {\color{blue} Z\ket{1} = -\ket{1}}$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B - \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big). \qquad {\color{blue} Z\ket{0} = \ket{0}}$

$\xmapsto{CZ_{A'B}} \frac{1}{2} \big( \alpha \ket{0}_{A'} \ket{0}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{0}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{1}_A \ket{1}_B + \beta \ket{1}_{A'} \ket{1}_A \ket{1}_B$
$\qquad + \alpha \ket{0}_{A'} \ket{1}_A \ket{0}_B + \alpha \ket{1}_{A'} \ket{1}_A \ket{0}_B$
$\qquad + \beta \ket{0}_{A'} \ket{0}_A \ket{1}_B + \beta \ket{1}_{A'} \ket{0}_A \ket{1}_B \big).$

$= \frac{1}{2} \Big( \ket{0}_{A'} \ket{0}_A \underbrace{\big( \alpha \ket{0}_B + \beta \ket{1}_B \big)}_{\color{blue}\ket{\psi}}$
$\qquad + \ket{0}_{A'} \ket{1}_A \underbrace{\big( \alpha \ket{0}_B + \beta \ket{1}_B \big)}_{\to \ket{\psi}}$
$\qquad + \ket{1}_{A'} \ket{0}_A \big( \alpha \ket{0}_B + \beta \ket{1}_B \big)$
$\qquad + \ket{1}_{A'} \ket{1}_A \big( \alpha \ket{0}_B + \beta \ket{1}_B \big) \Big)$

$= \frac{1}{2} \big( \ket{0}_{A'} \ket{0}_A + \ket{0}_{A'} \ket{1}_A + \ket{1}_{A'} \ket{0}_A + \ket{1}_{A'} \ket{1}_A \big) \ket{\psi}_B$

$\underline{\underline{= \ket{+}_{A'} \ket{+}_A \ket{\psi}_B}}$
