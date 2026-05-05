- **Classical logic circuits:**

  [Circuit diagram: input $x_1$ goes into a NOT gate; inputs $x_2, x_3$ go into an OR gate; the NOT output and OR output feed into an AND gate; the AND output and another signal feed into a final OR gate.]

  - For every logic gate, we have a truth table (how 0 + 1 are transformed by the gate.)

  [Gate symbols shown: OR, AND, XOR, NOR, NAND, NOT]

  | A | NOT A |
  |---|-------|
  | 0 | 1     |
  | 1 | 0     |

  | A | B | A AND B |
  |---|---|---------|
  | 0 | 0 | 0       |
  | 0 | 1 | 0       |
  | 1 | 0 | 0       |
  | 1 | 1 | 1       |

  | A | B | A OR B |
  |---|---|--------|
  | 0 | 0 | 0      |
  | 0 | 1 | 1      |
  | 1 | 0 | 1      |
  | 1 | 1 | 1      |

  | A | B | A XOR B |
  |---|---|---------|
  | 0 | 0 | 0       |
  | 0 | 1 | 1       |
  | 1 | 0 | 1       |
  | 1 | 1 | 0       |

  | A (control bit) | B (target bit) | A CNOT B |
  |-----------------|----------------|----------|
  | 0               | 0              | 0  0     |
  | 0               | 1              | 0  1     |
  | 1               | 0              | 1  1     |
  | 1               | 1              | 1  0     |

  ⊛ Reversible version of XOR gate.

  $$A, B \mapsto A,\; A \oplus B. \quad \oplus$$

  - For a given circuit, we use these truth tables, combining them to get the truth table of the whole circuit.
