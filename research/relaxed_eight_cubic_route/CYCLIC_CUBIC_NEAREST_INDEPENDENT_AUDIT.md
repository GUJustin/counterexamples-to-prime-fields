# Independent audit of the F17 cyclic-cubic gate

**PASS with the stated coefficient-field restriction.** On the full forty-eight-node pullback Y=T³ of the original F17 sixteen-node received word, every degree-at-most-nine polynomial with coefficients in F17 that is not a polynomial in T³ has at most seventeen matches. No algebraic-closure or characteristic-zero exclusion follows from this gate alone.

Write uniquely Q(T)=E(Y)+T O(Y)+T²V(Y), with degrees at most 3,2,2. For every nonzero y in F17 there is one rational cube root t=y^11 and a conjugate pair t omega,t omega² in F289. Since 17 is −1 modulo3, Frobenius interchanges that pair. An F17-coefficient polynomial matches one member of the pair if and only if it matches both. The two linear conditions for this pair are

    O(y)=t V(y),    E(y)−t² V(y)=w(y),

obtained using omega²=−1−omega. The rational root contributes the separate equation E(y)+t O(y)+t²V(y)=w(y). Thus the exact match count is s+2d, including full fibers in both terms.

For a non-descended candidate (O,V not both zero), the polynomial O(Y)³−Y V(Y)³ is nonzero: an identity would require 3 ord_0 O=1+3 ord_0 V, unless both vanish identically. Its degree is at most seven. Every conjugate-pair match supplies a distinct root, so d≤7. Eighteen matches also force d≥1 because s≤16.

For each possible actual set of d double-match fibers, impose its 2d linear equations. If the resulting affine space has dimension h, a target candidate must satisfy at least m=18−2d of the sixteen single-root equations. Among the first 16−m+h such equations it satisfies at least h. Enumerating all h-subsets of that prefix therefore includes a set satisfied by the candidate. The code retains every consistent positive-dimensional refined space as unresolved instead of discarding it. In the audited run all such spaces are absent, so the unique solutions and explicit match counts form an exhaustive search. This justification does not assume the selected h equations are automatically independent.

`verify_cyclic_cubic_nearest.py` independently reconstructs the equations in reversed V/O/E coefficient order and uses FLINT modular row reduction in place of the original handwritten solver. It reproduces 97,992 refined systems and consistent double-subset counts

    d=1,...,7: 16,120,560,1820,4368,80,8.

There are no hits and no unresolved families at target eighteen. This implies the nineteen- and twenty-match non-descended exclusions without replaying those weaker thresholds. Runtime was 4.36 seconds, peak RSS 29,280 KiB. The receipt is `cyclic_cubic_nearest_gate.verified.json`.

Descended polynomials are deliberately excluded from this conclusion. Some residue cubics can have six base matches and therefore eighteen pulled-back matches. The original eight have twenty-one. For thresholds nineteen through twenty-one, the source cubic census and this gate imply that the eight inherited polynomials are the complete list **among F17-coefficient candidates**. A candidate over F289 or the algebraic closure need not match the conjugate pair together, and its interpolation coefficients need not reduce into F17. Consequently a direct characteristic-zero completeness transfer is not justified by this receipt.

The same verifier independently recomputes J=E²−C from all final padded-source exact norm records in sqrt(17)/sqrt(39) bases. All forty-eight ten-source J and all sixty-one eleven-source J are nonzero. Together with the previously audited parity calculation, the proposition may accurately describe them as nonzero scalar squares over the algebraic closure, rather than including a possible zero case.

## Stronger target-seventeen replay

The independent verifier was subsequently run at target seventeen, with m=17−2d and the same proof. It reproduces all 150,760 refined systems, no hits, and no unresolved families. Therefore the sharper audited bound is **at most sixteen matches** for non-descended F17-coefficient degree-nine candidates. Receipt: `cyclic_cubic_nearest_gate_17.verified.json`; 5.95 seconds, 29,408 KiB. All field-scope limitations above remain unchanged.
