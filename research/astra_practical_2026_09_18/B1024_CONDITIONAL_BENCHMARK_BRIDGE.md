# Complete conditional B1024 benchmark bridge

September18,2026. **Mathematical conditional theorem: PASS.** No improved fiber is asserted, no protected files were changed, and no new Lean theorem was compiled. The suffix and radius semantics are checked against the actual cached Lean definitions, not left as unspecified future conditions.

## Precise hypothesis and conclusion

Let p=2130706433, F=Fp^6, q=p^6, n=262144, k=131072, and

    L*=274980728111395088.

Suppose there exist at least L* distinct136-subsets U of mu256 minus1 whose monic root polynomials V_U share their six nonmonic leading coefficients (degrees135 down to130) and their constant coefficient/root product.

**Then the pinned benchmark admits the mathematical assertion represented by**

    ProtocolClaimUpper 11612 122362.

This is conditional on the stated fiber hypothesis and uses the existing `PrescribedTop.winningSetDensity_gt_epsilon` theorem for the suffix. It concerns the benchmark's winning-set-density threshold, not an end-to-end attacking prover or a new protocol-game lower-coupling theorem.

## Pole, witnesses, and support

Retain exactly L* supports. For distinct supports, (V_U-V_V)/Y is a nonzero polynomial of degree at most128. The exact inequality

    p+128*C(L*,2) < q

therefore permits a pole alpha outside Fp avoiding every collision. Fix V0 from the family and put Y=X^1024. Let R be the monic locator of1023 of the1024 points in the domain fiber Y=1, omitting one point. Thus degR=1023, R(0)!=0, and that core is disjoint from all selected packet fibers.

Define on the prescribed NTT domain

    f0=R V0(Y)/[Y(Y-alpha)],
    f1=-R/(Y-alpha),
    gamma_U=(V0(alpha)-V_U(alpha))/alpha,
    P_U=R[(V0-V_U)(Y)-gamma_U Y]/[Y(Y-alpha)].

All denominators are nonzero on the domain because its points and Y-values lie in Fp*, whereas alpha does not. The numerator in square brackets is divisible by Y and Y-alpha. Its degree in Y is at most129, so the quotient has degree at most127 and

    deg P_U <=1023+1024*127=131071 < k.

Moreover

    f0+gamma_U f1-P_U=R V_U(Y)/[Y(Y-alpha)].

Each witness therefore agrees on its136 full packets and the fixed core, a support of size

    A=136*1024+1023=140287.

The chosen pole makes all L* gamma_U distinct. This is a received-line construction, not a fixed-word-list argument.

## Far direction and zero-constraint violation

For any polynomial Q of degree<k, an agreement with f1 is a root of

    (X^1024-alpha)Q+R.

This polynomial has degree at most132095 and is nonzero. Indeed, if Q=0 it is R!=0; otherwise an identity (X^1024-alpha)Q=-R would equate a polynomial of degree at least1024 with one of degree1023. Thus f1 has at most132095 matches with any admissible scalar row polynomial.

Embed each scalar source in row0 of the eight-row benchmark word and put zero in the other seven rows. Embed P_U in the same manner as a legal message/codeword. Set the selected linear constraint vector v=0 and both claimed values mu1=mu2=0.

The pinned definition `RelaxedRelationFor` requires ONE common coordinate set S with

    (1-delta)n <= |S|

on which both source words agree with their respective exact encoded messages; every message also satisfies its stated linear constraint. With v=0,mu1=mu2=0 the linear constraints are automatic. Any supposed simultaneous explanation would, in row0 of the second source, explain f1 by a degree<k polynomial on S. Hence it is impossible whenever (1-delta)n>132095. Nonzero entries in other rows of a hypothetical explaining message cannot evade the row0 root bound.

This supplies a genuine `ViolatingInstance`; no requirement that f0 individually be far has been added or assumed.

## Entire real-radius window, with exact endpoint rounding

For every real/NNReal radius

    122362/n <= delta < 122641/n,

one has

    139503 < (1-delta)n <=139782 <140287.

The right inequality ensures that each witness support of size140287 satisfies the non-strict cardinality test in `RelaxedRelationFor`. The left inequality ensures violation because139503>132095. This proof holds for all real radii in the interval, not just grid points; no unproved monotonicity lemma is used. At the lower endpoint the required agreement is exactly139782. At the handoff radius it is exactly139503, and the suffix theorem applies inclusively there.

The actual `winningSetFor` definition uses f0+gamma*f1 and combined value mu1+gamma*mu2. Thus every distinct gamma_U is winning for this zero-constraint violating instance. By the definition of `winningSetRatio` and its supremum,

    winningSetDensity >= L*/q > 2^(-128),

where the strict integer inequality L*2^128>q holds exactly.

## Suffix, admissibility, and score

The existing cached theorem

    PrescribedTop.winningSetDensity_gt_epsilon

accepts every delta with122641/n<=delta<IRSProfile.minRelativeDistance. The latter equals131073/n. Combining its inclusive lower bound with the new half-open window proves the ENTIRE required suffix

    [122362/n,131073/n).

The unsafe grid point is admissible because0<122362<131073. The score obligation at116.12 is the exact integer inequality

    2^218788 <=139782^12800,

obtained from 2^(-11612/100)<=(139782/262144)^128 by raising to the hundredth power and clearing powers of two. It was checked with exact Python integers alongside the pole and strict-density inequalities. Thus there is no remaining mathematical rounding or suffix gap.

## Primary definitions inspected and true remaining work

Cached primary files under `tmp/upper-track-primary-2026-09-18/`:

- `TargetUpper.lean`: `ProtocolClaimUpper`, including the full `Set.Ico` suffix and score;
- `Benchmark__IRSProfile.lean`: field, domain, eight rows, row dimension, and distance;
- `OrbitPencil.lean`: existing zero-constraint row0 embedding, far-direction argument, and winning-set construction;
- `PrescribedTop.lean`: inclusive suffix theorem at122641/n;
- `SubmissionUpper__Solution.lean`: current piecewise suffix assembly and integer score proof pattern.

The actual relation definitions were also fetched from the dependency pinned by the official manifest, ArkLib revision `e65197892890b8fd9b0dc05b8980273cf1d595cc`, and cached as `ArkLib__Definitions.lean` and `ArkLib__SoundnessBounds.lean`:

https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/ProofSystem/ToyProblem/Definitions.lean

https://github.com/Verified-zkEVM/ArkLib/blob/e65197892890b8fd9b0dc05b8980273cf1d595cc/ArkLib/ProofSystem/ToyProblem/SoundnessBounds.lean

Official benchmark sources:
https://github.com/proximity-prize/proximity-prize/blob/main/ProximityPrize/Benchmark/TargetUpper.lean
https://github.com/proximity-prize/proximity-prize/blob/main/ProximityPrize/SubmissionUpper/OrbitPencil.lean
https://github.com/proximity-prize/proximity-prize/blob/main/ProximityPrize/SubmissionUpper/PrescribedTop.lean

The genuine missing mathematical input is the fiber hypothesis. The remaining formalization is to implement the1024-by256 packet partition and six-coefficient fiber assumption, port the elementary divisibility/degree/support and pole-injection lemmas, instantiate the zero-constraint winning-set proof, and package the score and existing suffix into `ProtocolClaimUpper 11612 122362`. These are not already kernel-checked for this parameter set. The present note removes the formerly vague mathematical suffix/admissibility condition; it does not claim a submitted or verified Lean certificate.
