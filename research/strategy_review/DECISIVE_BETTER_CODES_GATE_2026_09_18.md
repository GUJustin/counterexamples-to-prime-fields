# Decision: one global filtered-kernel gate, not another parameter scan

## Benchmark and actual deficit

Checked the official https://better.codes/ on September 18, 2026: the displayed interval remains **68.11–116.13 bits**. The reproducible frozen lower proof is commit `cdb451f13fdc6c84f5fe363e77ee13a89bd30974` of proximity-prize/proximity-prize. This note does not assert that the live GitHub tip was checked today.

The authoritative local target is `better_codes_current_lower_2026_09_17/FULL_TARGET_RECONSTRUCTION.md`, not the early source-only diagnostics. The next score cell needs integer agreement **181275**, versus incumbent 181284. Its complete reconstructed numerical ledger has worst charge **296022915414629475**, allowance **274980720453263170**, and therefore needs **21042194961366305** of final charge saving (7.65% of the allowance). There are **2841 failing contexts among 5238**. The worst final context is (36,127,9489); the important inherited-prefix origin is (17,45), with binding singleton (12,43,3206). A local improvement must propagate through this entire ledger.

A different, smaller number is the old primary-A interpolation deficit. Its columns are C=13123663101701085 and local-rank sum is R=13125118926520320. Strict positive nullity by a rank argument needs cokernel at least **1455824819236**. This is only about 0.0111% of R. It is NOT the final prize deficit, and restoring this source alone does not prove 68.12.

## What is genuinely left

The strongest precise unclosed algebraic mechanism in the inspected files is **cancellation in the original-weight filtered global contact ideal**, equivalently a simultaneous Hermite–Padé degree defect. Unlike support optimization, this uses dependencies between constraints at different evaluation coordinates. The exact all-m ideal and its approximation equations already exist; no new source dictionary or interpolation matrix needs to be invented.

Evidence: `better_codes_primary_nonrectangular/global_character_gate/mixed_contact_module/WEIGHTED_REES_PADE_TARGET.md`, `ALL_M_WEIGHTED_CONTACT_IDEAL.md`, and `UNION_GRAPH_POLAR_AND_ADJOINT.md`. The first distinguishes unavoidable cokernel R−C from the one extra relation actually needed. The last explains why saturation can matter, but also why graph multiplicity does not automatically imply order-115 contact.

This is an unclosed mechanism, **not a currently promising proved improvement**. Generic small global maps have full rank; the inspected list-conditioned small example also has full rank. Neither a uniform defect nor a sufficient list-conditioned defect has been found. Riccati generators, their multiplicative products, capped-box support optimization, and merely counting Rees syzygies have already failed in their recorded scopes. Do not rerun them.

## One exact next lemma

Here is the clean uniform version, deliberately stated as a conjectural gate rather than a theorem. Let the domain be the actual Koala NTT domain, n=262144, w=131071. For every admissible pair of received rows u0,u1, let K115(u0,u1) be its weighted first-jet contact ideal. Then ask whether

    K115(u0,u1) intersect V != {0},

where V is the ORIGINAL source box

    wt_(X,Y,R,Z)=(1,w,w−1,0) < 20846625,
    deg_R <=35,  deg_(Y,R,Z)<=274277,
    deg_(Y,R)<=159.

Equivalently the global contact map restricted to V has rank at most C−1. If S is the domain locator and g the order-two Hermite coordinate, the exact test is to find nonzero F in V satisfying

    (partial_Y^[j] F)(X,g,R,Z) = 0 mod S^max(115−2j,0)

for every j. All caps apply BEFORE substitution. A shifted approximant-basis argument must retain those original caps; freely bounding transformed coefficients is invalid.

This is a mathematically definite lemma with a definite counterexample. It preserves the FULL primary kernel and its existing universal-factor interface. A list-conditioned variant is potentially weaker, but must state an explicit list threshold and prove that the benchmark case split supplies that hypothesis. A fixed-word list at one challenge is not such an adapter. No adapter is established in the inspected files, so it would be misleading to propose a list-conditioned rank result as an immediate benchmark certificate.

## Success, failure, and stopping rule

* Algebraic success: prove the displayed uniform nonzero-kernel statement, with the Koala characteristic and challenge caps, or supply a fully quantified case-split replacement. This is a source repair only.
* Algebraic failure: a certified full-column-rank instance on the actual domain disproves the uniform statement. A small analogous instance only rejects a proposed scale-uniform lemma; it does not decide this frozen instance.
* Benchmark success: feed the valid source repair into the existing downstream generator and require EVERY context to fit allowance 274980720453263170, with all quotient-avoidance and characteristic gates, before proposing a Lean port. Saving one source's 0.0111% is not enough evidence.
* Stop now unless someone can supply a new filtered-degree identity or a concrete compressed exact-rank certificate. A matrix with about 1.3e16 columns is not a rental job. Repeating small random ranks, old source scans, or product examples is not a decisive test.

The alternative joint source/carrier pole inequality remains open too, but `better_codes_second_jet/CURVATURE_POLES_AND_RAMIFICATION.md` shows its missing transverse-jet and ramification terms. It currently has no complete numerical adapter that pays the final deficit. It is less ready for a bounded decisive experiment than the exact contact-ideal gate above.

## Recommendation

Pause better.codes computation. The record supports one precise open algebraic gate, not a justified next large search. Resume only for a proposed proof of that gate (or a comparably explicit new inequality with an all-context adapter). Keep the successful prime-field constructions separate: they do not improve the frozen prize domain or its numerical security certificate. No manuscript change or benchmark improvement is claimed.

## September 18 follow-up: the monomial injectivity test is closed

The original-cap cyclic compression at f=X^181275, g=0 has 48 maximal character supports, but every one has more than the exact one-node image dimension 182580. Consequently none can be injective. The local rank independently reproduces the existing full row count 13125118926520320, so this supplies no new uniform rank saving. See `NTT_CONTACT_LOCAL_RANK_AUDIT_2026_09_18.md` and the revised compression note. Do not allocate a matrix for the proposed 48-profile normality test. This closes that special-word falsification attempt, not the uniform kernel gate. A different exponent must first pass the character-dimension ceiling; a sparse perturbation must first justify a kernel-to-cokernel argument.

The full monomial family is now closed for this test: `MONOMIAL_EXPONENT_DIMENSION_GATE_2026_09_18.md` combines elementary helpers outside181275<=a<=211940 with independently verified original-coordinate dimension witnesses for all30666 remaining exponents. Every monomial word, scalar multiple, and low-degree codeword translate has a helper. This is a special-family positive statement, not the universal source repair. Sparse non-codeword perturbations remain subject to the exact first-order criterion and derivative preimage in the two NTT_CONTACT deformation notes.
