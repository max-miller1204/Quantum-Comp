# CS 4134 Exam 2 Study Guide

**Date:** Thursday, March 5, 2026 | **Problems:** 8 | **Time:** 75 minutes

**Grading:** Start at 100%. Lose 2 pts per missed/unclear step (max -10 per problem). Unattempted = -10.

**Given on exam:** Pauli matrices (X, Y, Z), Bell state vectors, Swap operator F.

---

## CHEAT SHEET: Everything You Need to Know

### 1. Linear Algebra Fundamentals

**Complex numbers:**
- Conjugate: if z = a + bi, then z̄ = a - bi
- |z|² = zz̄ = a² + b²
- Conjugate distributes over addition: conj(z₁ + z₂) = z̄₁ + z̄₂

**Dirac notation:**
- |v⟩ = column vector, ⟨v| = conjugate transpose (row vector)
- ⟨0|v⟩ = first component of |v⟩, ⟨1|v⟩ = second component
- Inner product: ⟨v₁|v₂⟩ = conj(⟨v₂|v₁⟩)
- |v⟩ is normalized if ⟨v|v⟩ = 1
- To normalize: |v⟩/√(⟨v|v⟩)

**Key bases:**
- Z-basis (computational): |0⟩ = (1,0)ᵀ, |1⟩ = (0,1)ᵀ
- X-basis: |+⟩ = (|0⟩+|1⟩)/√2, |−⟩ = (|0⟩−|1⟩)/√2
- Y-basis: |+i⟩ = (|0⟩+i|1⟩)/√2, |−i⟩ = (|0⟩−i|1⟩)/√2

**Outer products:**
- |v⟩⟨w| is a matrix (rank-1 operator)
- Completeness: if {|eₖ⟩} is an ONB, then Σ|eₖ⟩⟨eₖ| = 𝟙

**Orthonormality:**
- ⟨eᵢ|eⱼ⟩ = δᵢⱼ (1 if i=j, 0 otherwise)
- To prove ONB: show orthonormality + completeness (Σ|eₖ⟩⟨eₖ| = 𝟙)

**Unitary operators:**
- U†U = UU† = 𝟙
- Preserve inner products: ⟨Uv₁|Uv₂⟩ = ⟨v₁|v₂⟩
- If {|eₖ⟩} and {|fₖ⟩} are ONBs, then U = Σ|eₖ⟩⟨fₖ| is unitary
- To verify: check U†U = 𝟙

**Hermitian operators:**
- M† = M (self-adjoint)
- General 2×2: M = ((a, b+ci),(b-ci, d)) with a,d real
- Always have real eigenvalues
- Proof: if M|λ⟩ = λ|λ⟩, then λ = ⟨λ|M|λ⟩/⟨λ|λ⟩ which is real since ⟨v|M|v⟩ is real for Hermitian M

**Conjugate transpose identity:**
- ⟨v₂|Mv₁⟩ = ⟨M†v₂|v₁⟩

**Eigenvalues/eigenvectors:**
- M|v⟩ = λ|v⟩
- To find: solve det(M - λ𝟙) = 0

### 2. Tensor Products & Multi-Qubit Systems

**Tensor product basics:**
- |v⟩ ⊗ |w⟩ = |v,w⟩ (shorthand)
- (A ⊗ B)(|v⟩ ⊗ |w⟩) = (A|v⟩) ⊗ (B|w⟩)
- Two-qubit computational basis: |0,0⟩, |0,1⟩, |1,0⟩, |1,1⟩

**Matrix form of tensor product (Kronecker product):**
- If A is m×n and B is p×q, then A⊗B is mp×nq
- Each entry aᵢⱼ of A is replaced by aᵢⱼ·B

**Bell states (MEMORIZE — given on exam but know their properties):**
- |Φ⁺⟩ = (|00⟩+|11⟩)/√2
- |Φ⁻⟩ = (|00⟩−|11⟩)/√2
- |Ψ⁺⟩ = (|01⟩+|10⟩)/√2
- |Ψ⁻⟩ = (|01⟩−|10⟩)/√2
- They form an ONB for C²⊗C²
- All are maximally entangled

**Product vs Entangled states:**
- Product state: |ψ⟩_AB = |a⟩_A ⊗ |b⟩_B (can be factored)
- Entangled: CANNOT be written as a product
- Test: write coefficient matrix and check if rank 1 (product) or rank > 1 (entangled)
- Example proof: |Φ⁺⟩ is entangled because (α₁|0⟩+β₁|1⟩)⊗(α₂|0⟩+β₂|1⟩) requires α₁α₂ = β₁β₂ = 1/√2 and α₁β₂ = β₁α₂ = 0, which is impossible

### 3. Quantum Mechanics / States

**Density operators (3-part definition):**
1. ρ is Hermitian: ρ† = ρ
2. ρ is positive semi-definite: ⟨v|ρ|v⟩ ≥ 0 for all |v⟩ (equivalently, all eigenvalues ≥ 0)
3. Tr[ρ] = 1

**Pure vs Mixed states:**
- Pure: ρ = |ψ⟩⟨ψ| (rank 1), purity Tr[ρ²] = 1
- Mixed: ρ = Σpᵢ|ψᵢ⟩⟨ψᵢ|, purity Tr[ρ²] < 1
- Maximally mixed: ρ = 𝟙/d, purity = 1/d

**Bloch sphere representation (single qubit):**
- ρ = ½(𝟙 + rₓX + r_yY + r_zZ) where (rₓ,r_y,r_z) is the Bloch vector
- Pure states: |r⃗| = 1 (on the sphere surface)
- Mixed states: |r⃗| < 1 (inside the sphere)
- |0⟩ → north pole (0,0,1), |1⟩ → south pole (0,0,-1)
- |+⟩ → (1,0,0), |−⟩ → (-1,0,0)
- |+i⟩ → (0,1,0), |−i⟩ → (0,-1,0)

**Pauli decomposition of 2×2 operators:**
- Any M ∈ L(C²): M = ½(c₀𝟙 + c₁X + c₂Y + c₃Z)
- c₀ = Tr[M], c₁ = Tr[XM], c₂ = Tr[YM], c₃ = Tr[ZM]
- M is Hermitian iff c₀,c₁,c₂,c₃ are all real
- For a density matrix: c₀ = 1 (since Tr[ρ]=1), and rₓ=c₁, r_y=c₂, r_z=c₃

**For a general 2×2 matrix M = ((p,q),(r,s)):**
- Tr[M] = p+s, Tr[XM] = q+r, Tr[YM] = i(q-r), Tr[ZM] = p-s

### 4. Measurements

**Projective measurement:**
- A measurement is a set of projectors {Πₖ} with ΣΠₖ = 𝟙
- Probability of outcome k: Pr[k] = ⟨ψ|Πₖ|ψ⟩ = Tr[Πₖ|ψ⟩⟨ψ|]
- Post-measurement state: Πₖ|ψ⟩/√Pr[k]

**Measuring in Z-basis {|0⟩⟨0|, |1⟩⟨1|}:**
- If |ψ⟩ = α|0⟩ + β|1⟩, Pr[0] = |α|², Pr[1] = |β|²

**Two-qubit Z-basis measurement:**
- Basis: {|00⟩, |01⟩, |10⟩, |11⟩}
- Pr[outcome] = |amplitude|²

**POVM (Positive Operator-Valued Measure):**
- Set {Mₖ} where each Mₖ ≥ 0 and ΣMₖ = 𝟙
- Pr[k] = Tr[Mₖρ]
- More general than projective measurements

### 5. Partial Trace

**Definition:** TrB[|i⟩⟨j|_A ⊗ |k⟩⟨l|_B] = |i⟩⟨j|_A · Tr[|k⟩⟨l|_B] = |i⟩⟨j|_A · ⟨l|k⟩

**Key identities:**
- TrA[PA ⊗ MB] = Tr[PA] · MB
- TrB[PA ⊗ MB] = Tr[MB] · PA
- TrA[(𝟙_A ⊗ MB)HAB(𝟙_A ⊗ NB)] = MB · TrA[HAB] · NB

**For 2-qubit state with 4×4 matrix:** TrB partitions into 2×2 blocks and traces each block.

### 6. Entanglement

**Schmidt decomposition:**
- Any bipartite state |ψ⟩_AB = Σᵢ λᵢ|aᵢ⟩|bᵢ⟩ (λᵢ ≥ 0, called Schmidt coefficients)
- Schmidt rank = number of nonzero λᵢ
- Product state ↔ Schmidt rank 1
- Entangled ↔ Schmidt rank > 1

**To compute Schmidt decomposition:**
1. Write the coefficient matrix C where |ψ⟩ = Σcᵢⱼ|i⟩|j⟩
2. Compute SVD: C = UDV†
3. Schmidt coefficients are the singular values

**Purification:**
- For density operator ρ = Σλₖ|ψₖ⟩⟨ψₖ|
- Purification: |ψ_ρ⟩ = Σ√λₖ |ψₖ⟩⊗|ψₖ⟩
- Equivalently: |ψ_ρ⟩ = (𝟙⊗√ρ)|Γ⟩ where |Γ⟩ = Σ|k⟩⊗|k⟩

**Entanglement properties of Bell states:**
- |Ψ⁻⟩ is invariant under (U⊗U): (U⊗U)|Ψ⁻⟩⟨Ψ⁻|(U⊗U)† = |Ψ⁻⟩⟨Ψ⁻|
- Measuring entangled states: outcomes are correlated
- For |Φ⁺⟩ in Z-basis: always get same outcome (00 or 11)
- For |Ψ⁻⟩ in Z-basis: always get opposite outcomes (01 or 10)
- Correlations persist in ANY basis for |Ψ⁻⟩

**Classical correlation vs Entanglement:**
- ρ = ½(|00⟩⟨00| + |11⟩⟨11|) is classically correlated (NOT entangled)
- Correlated in Z-basis but uncorrelated in X-basis
- Entangled states (like |Ψ⁻⟩) are correlated in EVERY basis

### 7. Pauli Matrices (given on exam, but know properties)

```
X = (0 1; 1 0)    Y = (0 -i; i 0)    Z = (1 0; 0 -1)
```

**Actions:**
- X|0⟩ = |1⟩, X|1⟩ = |0⟩ (bit flip)
- Z|0⟩ = |0⟩, Z|1⟩ = −|1⟩ (phase flip)
- Y = iXZ

**Properties:**
- All are Hermitian (P† = P) and Unitary (P² = 𝟙)
- Tr[XY] = Tr[XZ] = Tr[YZ] = 0 (mutually orthogonal under trace)
- {𝟙, X, Y, Z} form a basis for L(C²)

**Pauli tensor product identities:**
- ¼(𝟙⊗𝟙 + X⊗X − Y⊗Y + Z⊗Z) = |Φ⁺⟩⟨Φ⁺|
- ½(𝟙⊗𝟙 + X⊗X + Y⊗Y + Z⊗Z) = F (swap operator)

### 8. Quantum Gates & Circuits

**Single-qubit gates:**
- Hadamard: H = (1/√2)((1,1),(1,-1))
  - H|0⟩ = |+⟩, H|1⟩ = |−⟩, H|+⟩ = |0⟩, H|−⟩ = |1⟩
- S gate: S = ((1,0),(0,i)) — quarter turn on Bloch sphere
- T gate: T = ((1,0),(0,e^{iπ/4}))
- Phase gate: Rz(θ)

**Two-qubit gates:**
- CNOT: |c,t⟩ → |c, c⊕t⟩ (flips target if control=1)
  - CNOT = |0⟩⟨0|⊗𝟙 + |1⟩⟨1|⊗X
  - Matrix: ((1,0,0,0),(0,1,0,0),(0,0,0,1),(0,0,1,0))
- Controlled-Z: CZ = |0⟩⟨0|⊗𝟙 + |1⟩⟨1|⊗Z
  - CZ = (H⊗𝟙)·CNOT·(H⊗𝟙) ... actually: put H on target before and after CNOT

**Circuit identities (know these!):**
- SWAP = three CNOTs
- CZ = H-on-target → CNOT → H-on-target
- Flipping CNOT direction: H⊗H → CNOT(reversed) → H⊗H
- CNOT(X⊗𝟙) = (X⊗X)CNOT
- CNOT(𝟙⊗X) = (𝟙⊗X)CNOT
- CNOT(Z⊗𝟙) = (Z⊗𝟙)CNOT
- CNOT(𝟙⊗Z) = (Z⊗Z)CNOT
- XZXZ = -𝟙 and ZXZX = -𝟙

**Verifying a valid quantum gate:** Show U†U = 𝟙 (unitary).

### 9. Vectorization & Trace Identities

**vec(M) ≡ |M⟩⟩ := (𝟙⊗M)|Γ_d⟩** where |Γ_d⟩ = Σ|k⟩⊗|k⟩

- vec(|v₁⟩⟨v₂|) = conj(|v₂⟩) ⊗ |v₁⟩
- (𝟙⊗M)|Γ_d⟩ = (Mᵀ⊗𝟙)|Γ_d⟩
- Tr[M] = ⟨Γ_d|(𝟙⊗M)|Γ_d⟩

### 10. Probability Review

- Joint PMF, marginal PMF (sum over other variables)
- Conditional probability: Pr[A|B] = Pr[A∩B]/Pr[B]
- Covariance: Cov(X,Y) = E[XY] - E[X]E[Y]
- Independence: Pr[X,Y] = Pr[X]·Pr[Y]

---

## LIKELY EXAM PROBLEMS (by topic)

### From Problem Bank (in scope):

**Linear Algebra (1-13):**
| # | Topic | Difficulty | Likely? |
|---|-------|-----------|---------|
| 3 | Vector in C², inner products, normalization | Easy | HIGH |
| 5 | Inner products with |+⟩,|−⟩ basis | Medium | HIGH |
| 7 | Trace identities: Tr[|v₁⟩⟨v₂|], Tr[M|v₁⟩⟨v₂|] | Medium | HIGH |
| 8 | Orthonormality, completeness, change of basis | Medium | HIGH |
| 9 | Orthogonality condition, normalization | Medium | HIGH |
| 10 | Eigenvectors/eigenvalues, verify unitary | Medium | HIGH |
| 11 | Prove ⟨v₂|Mv₁⟩ = ⟨M†v₂|v₁⟩ | Medium | MEDIUM |
| 12 | Vectorization, vec identities | Hard | MEDIUM |
| 13 | Prove M†M is positive semi-definite | Medium | MEDIUM |

**Quantum Mechanics (1-21):**
| # | Topic | Difficulty | Likely? |
|---|-------|-----------|---------|
| 1 | Bloch sphere labeling | Easy | HIGH |
| 2 | Pauli orthogonality (Tr[XY]=0 etc.) | Easy | HIGH |
| 3 | Prove |Φ⟩⟨Φ| via Pauli decomposition | Medium | HIGH |
| 5 | Pauli decomposition coefficients via trace | Medium | HIGH |
| 6 | Trace formulas for 2×2 matrix | Medium | HIGH |
| 7 | Measurement probabilities for state vectors | Medium | HIGH |
| 8 | Two-qubit Z-basis measurement | Medium | HIGH |
| 9 | Density matrix: pure/mixed + Pauli decomposition | Medium | VERY HIGH |
| 10 | Prove Hermitian → real eigenvalues | Medium | HIGH |
| 11 | Hermitian ↔ real Pauli coefficients | Medium | MEDIUM |
| 12 | Decompose M = H₁ + iH₂ (Hermitian parts) | Medium | MEDIUM |
| 13 | Unitaries preserve inner products | Medium | HIGH |
| 14 | Completeness relation proof | Medium | HIGH |
| 15 | ONB change → unitary operator | Medium | HIGH |
| 16 | Verify unitary matrices | Easy | HIGH |
| 17 | Partial trace calculations | Medium-Hard | VERY HIGH |
| 18 | Three-qubit partial traces | Hard | MEDIUM |
| 20 | Bell state measurement probabilities | Medium | HIGH |
| 21 | Verify POVM | Medium | MEDIUM |

**Entanglement (1-5):**
| # | Topic | Difficulty | Likely? |
|---|-------|-----------|---------|
| 1 | Product vs entangled state identification | Medium | VERY HIGH |
| 2 | (U⊗Ū)|Φ_d⟩ = |Φ_d⟩ | Medium | HIGH |
| 3 | |Ψ⁻⟩ invariance under (U⊗U) | Medium | HIGH |
| 4 | X gate on Bell states (transformations) | Medium | HIGH |
| 5 | Schmidt decomposition | Medium-Hard | VERY HIGH |

### From Assignments (high-probability exam material):

**Assignment 1:** Inner products, normalization, change of basis (|+⟩,|−⟩)
**Assignment 2:** Hermitian definition, Bloch sphere, density operator definition, purity
**Assignment 3:** Two-qubit measurement (Z and X basis), orthonormality proofs, completeness, change-of-basis measurement, covariance, completeness relation, unitary from ONBs, quantum circuit analysis, partial trace identities
**Assignment 4:** Correlated measurements on mixed states, proving entanglement (|Φ⁺⟩ cannot be factored), spectral decomposition & purification, Pauli tensor product identities (|Φ⁺⟩⟨Φ⁺| and SWAP), Bell state measurements, |Ψ⁻⟩ invariance under (U⊗U)

---

## TOP 8 PREDICTED EXAM QUESTIONS

Based on 8 problems, 75 minutes, and the scope (LA 1-13, QM 1-21, Ent 1-5, plus assignments):

**Q1 (Warm-up Linear Algebra):** Given a state vector with complex amplitudes, compute inner products, check normalization, normalize it. *(PB LA #3/#4, HW1 #2/#3)*

**Q2 (Bloch Sphere / Pauli Decomposition):** Given a 2×2 density matrix, determine if pure/mixed, find the Bloch vector (rₓ,r_y,r_z). *(PB QM #9, HW2 #2/#3)*

**Q3 (Measurement Probabilities):** Given a state vector (1 or 2 qubits), compute measurement probabilities in Z-basis and/or X-basis. *(PB QM #7/#8, HW3 #1)*

**Q4 (Orthonormality / Completeness / Change of Basis):** Prove two vectors are orthonormal, show completeness, express a third vector in that basis, compute measurement probabilities in that basis. *(PB LA #8, HW3 #2)*

**Q5 (Partial Trace):** Compute partial trace of a two-qubit (or three-qubit) operator. May involve diagonal or off-diagonal 4×4 matrices. *(PB QM #17, HW3 #8/#9)*

**Q6 (Entanglement / Bell States):** Either prove a state is entangled (cannot factor), compute Schmidt decomposition, OR work with Bell state properties and Pauli decomposition. *(PB Ent #1/#5, HW4 #2/#4)*

**Q7 (Unitary / Gate Verification):** Verify a matrix is unitary, compute eigenvectors/eigenvalues, or express a gate in bra-ket notation. *(PB LA #10, PB QM #16, HW3 #7)*

**Q8 (Correlations / Measurement on Entangled States):** Given a bipartite state (pure or mixed), compute measurement correlations. May involve Bell state mixture. Show outcomes are correlated/uncorrelated depending on the basis. *(PB QM #20, HW4 #1/#5/#6)*

---

## QUICK-REFERENCE FORMULAS

```
Pauli matrices:
X = (0,1;1,0)  Y = (0,-i;i,0)  Z = (1,0;0,-1)

Bell states:
|Φ±⟩ = (|00⟩ ± |11⟩)/√2    |Ψ±⟩ = (|01⟩ ± |10⟩)/√2

Swap: F = 𝟙⊗𝟙 + all permutation terms
½(𝟙⊗𝟙 + X⊗X + Y⊗Y + Z⊗Z) = F

Density operator:  ρ† = ρ,  ρ ≥ 0,  Tr[ρ] = 1
Purity: Tr[ρ²],  pure ↔ Tr[ρ²]=1

Measurement: Pr[k] = Tr[Πₖρ] = |⟨k|ψ⟩|²

Partial trace: TrB[A⊗B] = A·Tr[B]

Pauli decomposition: ρ = ½(𝟙 + rₓX + r_yY + r_zZ)
  rₓ = Tr[Xρ], r_y = Tr[Yρ], r_z = Tr[Zρ]
```

---

## COMMON MISTAKES TO AVOID

1. **Forgetting to conjugate** when computing ⟨v| from |v⟩
2. **Not showing all steps** — grading docks 2 pts per skipped step
3. **Tensor product order matters** — |0⟩⊗|1⟩ ≠ |1⟩⊗|0⟩
4. **Partial trace:** make sure you trace out the correct subsystem
5. **Normalization:** after computing, always verify your answer sums to 1
6. **Probabilities = |amplitude|²**, not amplitude²  (need modulus squared for complex)
7. **Hermitian conjugate of a product:** (AB)† = B†A† (reverses order)
8. **Don't forget the 1/√2 in Bell states** when expanding
