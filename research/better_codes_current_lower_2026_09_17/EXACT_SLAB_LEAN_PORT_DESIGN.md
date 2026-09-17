# Lean-facing exact-slab port design

This document is a declaration/proof specification, **not compiled Lean code**. It uses the pinned namespaces and actual call sites. No `sorry`-bearing source file or theorem claim is introduced.

## 1. Definitions beside the existing band map

Namespace: `ProximityPrize.SubmissionLower.LocatorLowQuotient`.
Existing definitions: `nestedExponents`, `nestedCoefficientBox`, `HighBandIndex`, `highBandExponent`, `highBandMap` in cached `LowerGeometry.lean` lines264–325 (original module `LocatorNestedProjection`).

Define `slabCount w Dhigh delta T YS S : Nat` by the same spatial sigma sum as `channelCount_eq`, but with summand

`(T + 1 - y - r) * min delta (Dhigh - w*y - (w-1)*r)`.

Here y ranges0..min(T,YS), and r ranges0..min(S,T−y,YS−y). Natural subtraction is intended. This definition is finite, executable, and has no subtraction between large cardinalities.

For fixed parameters define:

- `Cut := min YS (LocatorArbitraryPowerAvoidance.thinTop w Dhigh S)`;
- `FullIndex := HighBandIndex delta T Cut S`;
- `LiveIndex := {c : FullIndex // highBandExponent w Dlow c ∈ nestedExponents Dhigh w T YS S}`.

`LiveIndex` is finite by subtype inference. Its predicate can equivalently check only the contact-degree inequality, because the other three bounds are already imposed by `FullIndex` and Cut≤YS.

### Needed combinatorial declarations

1. `highBandExponent_injective`: for fixed w,Dlow,delta,T,YS,S, the map from `HighBandIndex` to exponents is injective. No positivity assumption is needed. Recover spatial coordinates from exponents1,2,3 and recover the offset from exponent0 by cancellation of its fixed starting value.

2. `liveIndex_card_eq_slabCount`, assuming1≤w and Dlow=Dhigh−delta:

`Fintype.card LiveIndex = slabCount w Dhigh delta T YS S`.

Prove the row identity

`#{a < delta : (Dlow - W) + a + W < Dhigh} = min delta (Dhigh - W)`

for W=w*y+(w−1)*r. Split W<Dlow versus Dlow≤W; handle Dhigh<delta with natural subtraction. The cut does not discard any live row by the existing `ys_le_thinTop`. Sum over spatial indices and z multiplicities. Alternatively construct an explicit equivalence with the sigma index whose final factor is `Fin (min delta (Dhigh-W))`.

3. `slabCount_eq_box_card_sub`: optional conceptual/evaluation lemma, expressing slabCount as the cardinality of high nested exponents minus low nested exponents. It is not needed for the rank proof if declaration2 is proved directly.

4. `slabCount_mono`: monotone in Dhigh,T,YS,S for fixed w,delta. Use the uncropped spatial sum or a direct injection; do not derive monotonicity by subtracting two monotone coefficient counts. Every row's `min delta (Dhigh-W)` is monotone, and increasingT also increases the z multiplicity.

5. `slabCount_le_thin`: `slabCount w Dhigh delta T YS S ≤ delta * channelCount T (min YS (thinTop w Dhigh S)) S`. Each live row has at mostdelta offsets. This verifies conservative compatibility with the incumbent bound.

## 2. Image-support rank lemma

Suggested declaration specification:

```
highBandMap_cut_comp_finrank_le_slabCount
  [Field K] [AddCommGroup V] [Module K V] [FiniteDimensional K V]
  (Dhigh Dlow w delta T YS S : Nat)
  (hw : 1 <= w) (hDlow : Dlow = Dhigh - delta)
  (q : V ->ₗ[K] MvPolynomial (Fin 4) K)
  (hmem : forall v, q v ∈ nestedCoefficientBox K Dhigh w T YS S) :
  finrank K ((highBandMap w Dlow delta T
    (min YS (thinTop w Dhigh S)) S).comp q).range
    <= slabCount w Dhigh delta T YS S
```

The arrows/unicode here are schematic; exact elaboration and implicit arguments are to be checked during implementation. **Injectivity ofq is not required for this rank upper bound.**

Proof design:

- Let band be the displayed composite.
- For every v and every nonlive coordinatec, `band v c=0`: a nonzero coefficient would place its exponent in the support ofqv, contradictinghmem and nonliveness.
- Restriction of a function in `band.range` to LiveIndex is linear and injective. To prove injectivity, equality on live coordinates gives equality there, while both functions vanish on nonlive coordinates. Use function extensionality.
- Finrank of the range is therefore at most the dimension of `(LiveIndex -> K)`, which equals its finite cardinality.
- Apply `liveIndex_card_eq_slabCount`.

This avoids changing `bandOne`, `lowOne`, or the existing kernel-to-low-box proof. It also avoids quotient-space machinery and does not impose new characteristic assumptions.

## 3. Recursive budget declarations

Namespace: `ProximityPrize.SubmissionLower.LocatorArbitraryPowerAvoidance`, beside `powerBandBudgetThin` (line2281).

Define `powerBandBudgetExact w Dh delta dc dT dY dS T YS S` by

```
0       -> 0
(k + 1) -> slabCount w Dh delta T YS S
          + powerBandBudgetExact w (Dh-delta-dc) delta dc dT dY dS
              (T-dT) (YS-dY) (S-dS) k
```

Needed lemmas mirror the existing thin ones:

- monotonicity for larger Dh,T,YS,S and smaller dc,dT,dY,dS;
- monotonicity in fuel;
- domination by `powerBandBudgetThin`.

Use `slabCount_mono` and natural-subtraction monotonicity in the induction. No problematic difference-of-cardinalities monotonicity is needed. Exact initial capD−dc is admissible by the same monotonicity.

For fixedsource,r,y, budget is nonincreasing as factort increases on the source-covered domain: each postdivisiontotalL−ht decreases and fuel decreases; all other per-level caps remain fixed. This justifies the existing binary threshold search with the new budget, providedt≤L.

## 4. Exact old-to-new call-site map

Namespace: `ProximityPrize.SubmissionLower.LocatorBatchProductRoute`.
Clone `exists_batchExitStage_of_bandBudgetThin_succ` (line5177) as `exists_batchExitStage_of_bandBudgetExact_succ`, changing its budget hypothesis only.

| Existing proof item | Replacement |
|---|---|
| Base-case `bandOne`, `lowOne`, `hwidth` | Unchanged |
| Base-case `hrangeOne`, lines5220–5231, full target-space dimension estimate | New rank lemma; RHS=`slabCount w Dhigh delta T YS S` |
| Base-case `hfirst` and rank-nullity arithmetic | Unfold exact budget at fuel1; use new slab RHS |
| `qOne`, its injectivity, `hqOneBox`, universal-factor split and terminal argument | Unchanged |
| Successor-case `hrangeOne`, lines5337–5349 | Same new rank lemma |
| Successor-case `hlowOneRank` and `hbudget`, lines5350–5380 | Replace thin budget and first charge with exact budget/slabCount |
| Recursive selector invocation | Invoke exact-budget induction hypothesis |
| Quotient injectivity, weighted-degree subtraction identities, exit-stage reconstruction | Unchanged |

The existing `mem_low_of_highBandMap_cut_eq_zero` remains the kernel-containment lemma, including its current `hwidth` proof. The sameq is injective wherever the selector needs injectivity; the new rank lemma simply needs fewer hypotheses.

## 5. Consumer and receipt port

In `MovingFiberRouting6811.lean`, namespace `Lower80860.BatchPowerRoute`, clone `exists_strict_helper_split_of_batch_source_thin` (line980) with exact budget. Its call to the selector is atline1094. Preserve all capacity, terminal, field, helper-gate and charge hypotheses.

For a local singleton, call the new consumer withA={F}. The strict proper subset is empty, so its conclusion gives the factor charge directly. Charge can remain the exact stage-zero helper bound, dominating every stage. No global `PhaseSourceSound` object is needed.

For globally reused phases, add an exact route predicate carrying the actualD (or source multiplicitym) and prove the corresponding batch adapter. The old `SourceNumbers` structure omitsD, so an exactD threshold must not be silently interpreted as its old rounded `Routeable` predicate. Extend or pair the structure with the missing degree metadata. Update threshold and phase receipt soundness accordingly.

Only after these mathematical declarations compile should a passing numerical threshold/receipt be treated as certified. This plan deliberately separates the now-audited mathematical validity from the not-yet-performed Lean implementation.
