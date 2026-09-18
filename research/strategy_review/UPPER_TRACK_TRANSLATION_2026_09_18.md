# Upper-track admissibility and our constructions: exact translation audit

Checked official sources on September18,2026. The live leaderboard still reports 116.13 upper and68.11 lower. Fresh primary files are cached in `tmp/upper-track-primary-2026-09-18/`: TargetUpper, IRSProfile, Solution, OrbitPencil, PrescribedTop, and HalfRadiusCollision. No submission or protocol experiment was performed.

Primary URLs:
- https://better.codes/
- https://github.com/proximity-prize/proximity-prize/blob/main/ProximityPrize/Benchmark/TargetUpper.lean
- https://github.com/proximity-prize/proximity-prize/blob/main/ProximityPrize/Benchmark/IRSProfile.lean
- https://github.com/proximity-prize/proximity-prize/blob/main/ProximityPrize/SubmissionUpper/OrbitPencil.lean
- https://github.com/proximity-prize/proximity-prize/blob/main/ProximityPrize/SubmissionUpper/HalfRadiusCollision.lean

## What must actually be certified

The field is F=F_(p^6), p=2130706433. The domain is the fixed base-field multiplicative subgroup of order n=262144, embedded in F. There are eight rows, each of dimension131072 (degree at most131071). The upper certificate proves winning-set density strictly greater than2^−128 for every radius from the claimed grid point through, but not including,131073/262144. This is a mathematical reduction-threshold certificate, not an end-to-end attacking prover.

The current certificate starts at i=122369, agreement139775, uses OrbitPencil until i=122641 and then the existing PrescribedTop suffix. To score116.12, the smallest sufficient integer agreement is139782, i=122362. The unrounded scores at139781 and139782 are116.12048033388065 and116.11915923655923 respectively. Thus a new construction can reuse the existing suffix if it covers the seven-coordinate earlier starting point through the old handoff; proving a single radius without a suffix argument is insufficient.

The exact field size is

    Q=93571093019388561295270373781649880353786165192103559169.

An injective line-label family needs at least

    floor(Q/2^128)+1 =274980728111395088

winning labels. The existing fixed-word-list lemma supplies density L/(Q+L−1), with agreement supports and the usual no-nonzero-codeword-on-m-coordinates condition. Its exact list threshold is floor((Q−1)/(2^128−1))+1, the same integer274980728111395088 here. A list of that size on the fixed domain at agreement139782 would therefore be concrete useful input. A bank near different received words does not satisfy the fixed-word premise.

## Translation of the current new families

**Seven-word prime/number-field banks.** Their count remains seven under polynomial pullback, field extension, and common-zero padding. The existing list lemma consequently guarantees only7/(Q+6), about2^−183.125: roughly55.1 bits below the required density. It needs a list about3.93·10^16 times larger. Even granting a fresh-coordinate compiler the optimistic upper bound nL on labels from these seven witnesses gives at most1835008 labels, far below274980728111395088. This is an obstruction to using this fixed bank and that compiler, not an upper bound on every possible new construction.

The native quarter-rate bank has agreement one half, below the needed139782/262144≈0.53323 if merely enlarged to the benchmark's dimension. Common-zero padding can improve agreement and rate, but cannot repair list cardinality. Moreover our domains are freely chosen; being realizable over some large split prime is not a certificate on this fixed NTT subgroup. Here p≡2 mod7: seventh roots lie in F_(p³)⊂F but not the base field containing the NTT domain. Thus the literal two-μ7-orbit construction does not sit inside the specified domain. This statement concerns the literal realization, not every possible coordinate transformation.

**Native Dickson bank.** At this prime its native length is p−1=2130706432, degree parameter k=(p−1)/4=532676608; shifted codewords have degree k−1, over four thousand times the allowed131071. The subgroup index is (p−1)/n=8128, divisible by four. On the prescribed NTT subgroup X^k=1, so the standard Dickson received word (1+X^(2k))/2−X^k becomes identically zero. Reducing each shifted codeword modulo X^n−1 preserves its values there, but any resulting nonzero polynomial of admissible degree≤131071 cannot agree with zero at139782 points. The only such nearby candidate is the zero polynomial. Thus literal subgroup restriction plus degree reduction cannot translate that native word/bank into the required upper certificate. Other words or genuinely new nonlinear operations are not ruled out.

**Quadratic-extension ordinary-CA construction.** Extension fields are not disallowed by this benchmark: F_(p²) embeds in F_(p⁶). The issue is the actual parameters. The proved family in RANDOM_DIRECTION_QUADRATIC.md has rate1/8, agreement3/16, n=16Δ with Δ≈p/8 to p/6, and guarantee J≥n²/192. It cannot be instantiated at n262144 while retaining the fixed characteristic p2130706433. Even formally transplanting that lower guarantee to this n gives only about3.58·10^8 labels; the optimistic entire n² scale is6.87·10^10, still about4.00 million times below the needed count (about21.93 density bits). These are comparisons of the proved mechanism/guarantees, not a universal upper bound on ordinary-CA exceptions.

A hypothetical construction providing a positive fraction of all p² labels could numerically exceed the threshold, since p²≈4.54·10^18. No such construction at the fixed short domain, half rate, required agreement, and required violating-input condition has been proved. Counting exceptions to ordinary CA alone also omits the selected linear-constraint and suffix premises of the protected target.

## Strategic conclusion

### Update after the cubic-extension one-fiber theorem

The new theorem over F_(p³) has length 2p²−O(p), dimension three, exactly p far parameters, p³−2p singleton parameters, and p parameters with lists of size p. Its nearby-mixture probability is 1−p^−2, with a source separation of order p. This is a substantial improvement to the abstract extension-field construction, but not an instantiation of this benchmark. Although F_(p³) embeds in the benchmark F_(p⁶), its native domain and rate do not match the prescribed short base-field subgroup and half-rate code.

Three exact transfer audits now explain the gap more specifically:

* [Möbius evaluation changes](../binary_characteristic_transfer/quadratic_frobenius_core/MOBIUS_PRIME_DOMAIN_OBSTRUCTION.md), with the standard quadratic GRS multiplier, either admit at most twelve prime-field parameter nodes or turn the restricted received line into quadratic codewords. The proof also covers transformations over F_(p⁶) whose images lie in the construction's F_(p³) domain.
* [Polynomial evaluation changes](../binary_characteristic_transfer/quadratic_frobenius_core/POLYNOMIAL_PRIME_DOMAIN_COMPILER_AUDIT.md) of degree D≤65535 either give codewords or leave at least 229377 matches with one codeword on the fixed 262144-node domain. The two source explainers agree on the same dominant block. Even the explicitly considered patching at zero parameters leaves at least 196609 matches. These quantities exceed both the frozen upper-track threshold139782 and lower-track threshold181275; these inherited compilers do not preserve the far-input/common-agreement obstruction. Arbitrary replacement constructions are outside this conclusion.
* The [fixed witness-span bound](fixed_witness_span_gate/INDEPENDENT_AUDIT.md) rules out simply raising the polynomial degrees while preserving a two-dimensional witness family. At N262144, degree bound131071, and agreement139782, a fixed two-dimensional family with no common evaluation zero has at most56 codewords near one fixed word. If ordinary common agreement is below that threshold, it can supply at most14794337 qualifying line labels. Both are far below274980728111395088. More generally, under the same hypotheses a line family needs span dimension at least nine even to escape this counting obstruction; nine is not a sufficient construction.

These are restricted mathematical transfer obstructions, not bounds on every possible upper-track certificate, eight-row construction, or protocol. The consequence for research selection is concrete: a useful benchmark construction must introduce new witness structure or abandon these inherited compilers. The published one-fiber theorem alone supplies no Stwo security ceiling.

There is currently no concrete translation from these new banks to a better116.13 certificate. The exact useful target is a fixed-domain list or admissible line-label family of at least274980728111395088 at139782 agreements, plus the narrow suffix handoff. The existing B1024 packet family is the closest archived numerical certificate attempt: its guaranteed68579341025511059 labels are short by a factor slightly above four, whereas our small positive banks are many orders of magnitude short. This audit does not prove that the packet family is optimal or that a new global construction is impossible. It shows why the present asymptotic/short-domain progress is not yet an upper-track improvement.
