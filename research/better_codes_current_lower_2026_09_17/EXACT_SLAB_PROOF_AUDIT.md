# Exact weighted-slab rank charge: independent proof audit

**Verdict:** replacing the current delta-times-channel charge by the exact weighted-slab cardinality is mathematically valid for the subspace actually counted in the pinned selector proof. This is a new combinatorial rank lemma and recursive-budget port, not an already proved numerical substitution in the existing Lean theorem. No new interpolation or factor-peeling hypothesis is required.

## The actual map and subspace

In pinned `LowerGeometry.lean`, `nestedExponents` (line264) consists of exponent vectors(x,i,j,z) satisfying

 i+j+z≤T, i+j≤Y, j≤S, x+wi+(w−1)j<D.

`highBandMap` (line319) reads coefficients at

 x=max(Dlow−wi−(w−1)j,0)+a, 0≤a<delta,

with all admissible spatial indices(i,j,z). The thinned version further restricts i+j≤floor((Dhigh+S−1)/w), a condition automatically satisfied by every monomial of the high box.

The selector `exists_batchExitStage_of_bandBudgetThin_succ` (line5177) applies this map to an injective q:V→polynomials with q(V) contained in the Dhigh box and Dlow=max(Dhigh−delta,0). In its base and inductive cases it bounds rank merely by the full coordinate-target dimension. Coordinates corresponding to monomials outside the Dhigh box are identically zero on q(V). Counting only the remaining coordinates is legitimate.

The map from band indices to exponents is injective: i,j,z are read directly from the exponent vector and a is recovered by subtracting its fixed startingx. Its surviving coordinates are exactly the monomials in the high box but not the low box. The existing kernel-containment lemma remains unchanged.

## Exact cardinality and strict endpoints

Define C(D,T,Y,S) as the number of the above nested exponents, and

 Slab(D,delta,T,Y,S)=C(D,T,Y,S)−C(max(D−delta,0),T,Y,S).

Equivalently, for j=0..min(S,Y,T), i=0..min(Y,T)−j,

 Slab=Σ (T+1−i−j)·min(delta,max(D−wi−(w−1)j,0)).

The weighted interval is **Dlow≤x+wi+(w−1)j<Dhigh**. The lower endpoint is included and the upper excluded. This distinction accounts for the exact integer boundary savings. IfD<delta, the formula counts the entire high box, as it should. IfD=0, it is zero.

This is not the unrestricted source coefficient counter with only total and slope caps: the quotient's additional Y cap must be retained. In an implementation named `coeffCount`, both terms must count the same four-parameter nested box(T,Y,S), changing onlyD.

## Required new rank lemma

For any linear map q with image inside the Dhigh box,

 finrank(range(highBandMap_cut ∘ q)) ≤ Slab(Dhigh,delta,T,Y,S).

A direct proof factors the image through the coordinate subspace supported on the surviving band indices, whose cardinality is the slab count. Alternatively, project the high coefficient space onto its quotient by the low coefficient space; this quotient has dimensionSlab. The latter is a general codimension argument and does not use field characteristic.

Replace the two full-target dimension estimates in the selector's base and successor cases by this lemma. Rank-nullity then gives exactly the same positive-dimensional low subspace and the same strict remaining-budget inequality as before. The subsequent universal-factor split, quotient selection, contact decrease, terminal contradiction, and helper-count argument remain unchanged.

## Recursive budget and conservative contact bounds

Define ExactBudget with zero at fuel0 and recurrence

 ExactBudget(D,T,Y,S;k+1)=Slab(D,delta,T,Y,S)
   +ExactBudget(max(D−delta−dc,0),max(T−dT,0),max(Y−dY,0),max(S−dS,0);k).

The exact slab is monotone inD because each channel lengthmin(delta,max(D−weight,0)) is monotone. It is also monotone inT,Y,S by inclusion of spatial channels and their z multiplicities. Therefore the existing conservative contact argument still works: replacing actual contact by its lower bounddc=wy−r gives a larger D cap at every stage. Both the rounded initial cap and the sharper actual-sourceD−dc initial cap are valid upper bounds. Increasing contact/subtraction degrees decreases the recursive budget.

MoreoverSlab≤delta·channelCount(T,min(Y,thinTop(D,S)),S), since all surviving channels satisfy the thin cap and have at mostdelta x exponents. Thus the new budget is never worse than the incumbent thin budget. Quantitative savings remain to be evaluated; this proof audit does not assert that they suffice for a benchmark improvement.

## Implementation obligations

Add the exact slab cardinality definition/evaluation theorem, image-support rank lemma, recursive budget monotonicity/domination lemmas, and selector/source-routing analogues using the new budget. Preserve the existing kernel nullity lower bound and all helper/characteristic gates. Route thresholds and receipts must then be regenerated against the new strict budget inequality. Existing Lean theorems cannot accept the smaller budget without these new proofs.

Primary source is pinned cdb451f13fdc6c84f5fe363e77ee13a89bd30974, cached `tmp/current-lower-primary-cache/LowerGeometry.lean`. The analytic agent is independently deriving fast slab evaluation and boundary savings.
