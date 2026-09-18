# Independent opposite-pair collision-ceiling audit

2026-09-18. **PASS**, with the stated collision-class scope. Read README.md, verify.py, and verified.json; independently recomputed both integer sums using factorial binomials and a separately filtered h-range. All values and strict inequalities agree; receipt `independent_verified.json`.

## Algebra and combinatorial counting

A support's partial pattern records which singleton of each opposite pair is present, while empty/full pairs share the neutral partial state. Two supports in the same pattern differ by disjoint sets A,B of full pairs of equal cardinality h. Their common roots C are uniquely their intersection. In the punctured domain the tag1 pair is unavailable for a full-pair difference, but its remaining root−1 may occur in C.

Each full pair tagged a contributes0 to odd moments,2a^j to moment2j, and product−a. Since h is equal on the two sides, equal original signatures are exactly equal tag power sums1,2,3 and tag product. This holds in the actual characteristic p>3.

Fix A and fix a candidate(h−4)-subset C'⊂B. The residual four tags have fixed power sums1,2,3 and fixed nonzero product. Newton identities with denominators1,2,3 recover e1,e2,e3; the product gives e4. Thus their monic quartic is unique. Each admissible B contributes exactly binom(h,h−4)=binom(h,4) choices C', and each C'⊂available tags\A has at most one completion. This proves the floor bound. For h≤4, the same elementary coefficients determine B=A, so disjoint nonempty solutions are impossible.

After ordered A,B are fixed, the common root subset has size136−2h in the remaining255−4h points (or256−4h in the relaxed full domain). Its choices are precisely the stated binomial coefficient. This neither loses nor double-counts any ordered collision: the support pair recovers A,B,C uniquely. There is no division by2; the sum is intentionally ordered. The diagonal contributes exactly the number of supports. Feasibility gives h≤59 punctured and h≤60 full.

## Closure under rotations and full complement

A rotation by ζ^t multiplies the support product by ζ^(136t). Since support products are nonzero, preserving the signature requires136t=0 modulo256, giving gcd(136,256)=8 possibilities. Additional moment conditions only shrink this stabilizer. Same-sector equal-signature relation is an equivalence relation; rotations normalize the opposite-pair partition and act invertibly on signatures. In a fixed signature fiber its generated closure with rotations is therefore contained in at most eight rotated copies of the sector relation. Summing over signatures gives at most8 E_full ordered pairs. Relaxing the puncture to the full domain is legitimate and can only enlarge the count.

Full complement changes weight136 to120, negates the first six moments because their full-root sums vanish, and sends product u to−1/u. It normalizes sector relations and commutes with rotations. An even number of complements cancels after commuting/conjugating; an odd number cannot end at weight136. Thus full complement adds no further pairs. This does not cover complements relative to changing punctured universes, exactly as the note states.

## Exact arithmetic and interpretation

Independent sums reproduce E_punctured and E_full exactly and verify

    496 E_punctured < Q,
    250(8 E_full) < 13Q,
    Q=binom(255,136)(274980728111395088−1)+1.

Thus the enlarged class contributes less than0.052 of the stated sufficient global collision threshold. This does NOT bound the actual global second moment or the maximum fiber, and it cannot be added as a disjoint bonus to a generic lower bound without separate accounting. It only rules out reaching Q by exhausting the specified whole-opposite-pair relations and their allowed closure. Other changes of partial pattern remain outside the result.
