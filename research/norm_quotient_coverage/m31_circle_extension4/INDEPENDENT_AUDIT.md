# Independent M31 circle-character and compiler audit

2026-09-18. **PASS** for the stated ordinary-RS selected-domain theorem. Read README.md and verify.py; independently recomputed the exact seed sum and all six outward-rounded recurrence steps, matching the producer's exact numerators. Receipt: `independent_arithmetic.json`.

## Character lemma, all native characters

The map a(t)=(t−i)/(t+i) gives the claimed bijection P1(F_p)→T; finite t never has denominator zero because i∉F_p, and infinity maps to1. For b∈F_(p^4)\F_(p^2), the fractional transform z=−i(b+1)/(b−1) also lies outside F_(p^2). Since every proper subfield of F_(p^4) lies in F_(p^2), z has degree four. Its conjugates are distinct and disjoint from±i.

For any extension η of ψ from T to K*, the identity a(t)=(t+i)^(p−1) proves

    χ(b−a(t))ψ(a(t))=χ(b−1)χ(t−z)κ(t+i),
    κ=η^(p−1)(χ|K*)^(-1).

This identity includes the required denominator character. On diagonal F_p*, χκ=1, since η^(p−1)=1 there. Changing η by a character trivial on T changes neither η^(p−1) nor κ.

Apply the Katz rank-one construction to E×K and regular element(z,−i). The four z-punctures have nontrivial inertia for EVERY χ≠1; descending through either field norm does not change this conclusion. The two i-punctures contribute only if κ is nontrivial. Infinity has trivial inertia and trace1, because both linear factors have leading coefficient1 and their diagonal character is trivial. The actual circle term at infinity is correspondingly χ(b−1), which is exactly the constant prefactor in the displayed formula.

Extend across infinity and any removable finite punctures. The open curve then has at most six punctures. Geometric nontriviality at z makes Hc2 vanish, nonproperness makes Hc0 vanish, and tame Euler characteristic gives dim Hc1≤4. Weight≤1 yields the claimed4sqrt(p) projective-sum bound. If κ is trivial there are only four punctures and the improved2sqrt(p) follows. No norm-descended or restriction-trivial characters need exclusion. This is a derivation from Katz's proof, not his unrefined affine theorem as printed.

Averaging all twists of T/H and removing reserved tag1 therefore gives exactly the normalized population bound used in the recurrence. The independent rational replay agrees with its seed and final exact integer decision; no decimal estimate is used for validity.

## Exact RS interpretation

The map X↦X^1024 on T has1024-point fibers because1024 divides p+1. The reserved polynomial R=(X^1024−1)/(X−1) has precisely the other1023 roots of the identity fiber. Coefficients and competitors lie in E, and the evaluation domain lies in K; the ordinary polynomial root bounds work unchanged. The source witnesses displayed in the note have degree≤131071, attain132095 common matches, and the independent source upper bounds match. The monic cleared residual bounds every interior witness by133119 and the product coverage attains it.

This is ordinary univariate RS over E, not a proof for a base-field-restricted Circle-STARK space, a special circle basis, a prescribed domain, or a protocol state. The note maintains these distinctions correctly.

## Does the circle increase the margin?

For fixed n,J,m, the compiler's margins are entirely determined by m; the circle produces NO additional degree or agreement gain. Its character bias has the same square-root scale as the corresponding degree-four base-line bound, and its population size(p+1)/m differs negligibly from(p−1)/m asymptotically. The useful change is available divisibility and field size.

At the SAME M31 characteristic and power-of-two length n262144, a base-F_p multiplicative-fiber construction has m dividing both n and p−1, hence only m≤2. The circle has order p+1=2^31 and supports m1024. Thus it materially enlarges the accessible margin compared with that same-base-field route. At the already proved Goldilocks/base-field m1024 instance, it instead gives exactly the SAME margins with a smaller native alphabet (about124 rather than192 bits), at the cost of changing the evaluation domain from the base field to its quadratic extension.

For this exact all-label subset compiler and native alphabet p^4, increasing m to2048 at the same n gives s127,r65,w2047. Exact arithmetic shows binom(127,65)<p^4−1, so all native labels are impossible by counting. Larger power-of-two m only reduce the available total subsets further. Thus1024 is already the largest possible fiber size for full coverage in this fixed ledger. The circle route does not by itself offer a still larger capacity margin at these matched parameters; new witness/cardinality structure would be required.
