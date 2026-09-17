# Explicit YS-cutoff interpolation source

## Applicability

A source restricted to `nestedCoefficientBox K D w L Y S` is mathematically legitimate even when Y is smaller than floor((D+S−1)/w). Keep D=mA and restrict the existing coefficient-array domain to those arrays whose reconstruction lies in this nested box. Restrict the original linear interpolation constraint map to that domain. Its rank cannot exceed the original map's rank, so

 dim restrictedKernel ≥ C(D,L,Y,S)−n·localRankBound(m,L,S).

No Y≥m−1 assumption is needed for this conservative inequality. Such a condition might matter to an exact restricted-rank formula, but the unchanged upper bound is valid for everyY. Preserve whatever conditions are needed to evaluate the chosen original localRankBound formula, including2S≤m andL≥m+S−1 for the current closed expression.

The coefficient dimension is the exact nested count

 C(D,L,Y,S)=Σ_{j=0}^{min(S,Y,L)}Σ_{i=0}^{min(Y,L)−j}
   (L+1−i−j)·max(D−wi−(w−1)j,0).

The old unrestricted fast coefficient counter is not this count when the newY cutoff binds.

## Exact theorem changes

The restricted kernel has a natural injective linear inclusion into the original `ConstraintKernel`. Reconstruction and every interpolation/vanishing condition are inherited through that inclusion. All source witnesses in the argument must come from the restricted kernel; universal divisibility must likewise quantify over this restricted family.

The shape hypothesisD+S≤w(Y+1) in `MovingFiberRouting6811.lean` is used to derive nested membership/YS degree, not to establish an additional vanishing fact:

- `divisor_or_helper_count`, line109: replace `flag_box_ys_bound ... hshape` by the explicit source membership hypothesis;
- `kernelReconstruct_mem_nested`, cachedLowerGeometry line4681: replace this shape-derived wrapper by the restricted source's defining membership;
- `kernelQuotient_regularProduct_nested`, line4703: invoke existing `quotientLinear_nested_data` directly with the restricted reconstruction, its injectivity and nested membership;
- `counts_of_batchExitStage` currently fixes its parameter space to the fullConstraintKernel. Generalize it to a finite-dimensional source space with injective linear inclusion intoConstraintKernel, or duplicate the restricted version. At each point, apply the existing vanishing/power lemma to the included original-kernel vector.

The generic batch selector already accepts an arbitrary finite-dimensional sourceV and injective polynomial mapq. Its exact-slab version requires no new source-specific geometry. Helper and characteristic gates use the actual newY. Fuel and quotient degrees use the new caps.

The source-routing wrapper's old proofD≤w(Y+1)−S no longer applies. Use actualD in the thin/exact-slab contact cap: D−dc, where dc=wy−r. This bound follows directly from the contact lower bound. Retaining the old rounded contact cap with an explicitly smallerY would be invalid.

## A structural limit on routing gains from trimmingY

There is an exact monotonicity statement explaining the observed near cancellation when rank is kept unchanged. FixD,L,S, delta>0 and factor weights1≤r≤y≤t. Let dc=wy−r, and use the **actual-D exact-slab budget**, with source capY and fuel

 fY=min(floor(L/t),floor(Y/y),floor(S/r)).

WriteBY for the sum of slabs at levels h=1..fY, with contact cap

 Dh=max(D−h·dc−(h−1)delta,0)

and spatial caps(L−ht,Y−hy,S−hr). Then, forYsmall≤Ylarge,

 B_large−B_small ≤ C(D,L,Ylarge,S)−C(D,L,Ysmall,S).

Consequently C−B, and hence C−nR−B for unchangedR, cannot increase when the sourceY cap is reduced. Such a reduction cannot advance the routing threshold at fixedD,L,S under this rank estimate.

### Injection proof

Use the formal monomial

 M=Yvar^(y−r) Rvar^r Zvar^(t−y).

It has exactly contact degreedc, YS weighty, slopeweightr and totalweightt. This is a combinatorial indexing device; no actual irreducible factor is assumed to equalM.

For every slab monomial at levelh, multiply its exponent vector by adding the exponent vector ofM^h. The result lies in the original source box. Its contact weight lies in the half-open strip

 [max(D−h·delta,0), D−(h−1)delta),

possibly with a larger lower endpoint due to the addedh·dc. Distinct levels therefore have disjoint images. Within each level the map is injective.

Compare the two sourceY caps. For a level present in both budgets, every coordinate removed by the smaller quotientYS cap acquires totalYS weight greater thanYsmall after the shift byM^h. For a level lost because the smallerY decreases fuel, hy>Ysmall, so its entire shifted image is outside the smaller source box. All lost budget coordinates therefore inject into the deleted source monomials, proving the inequality. Natural subtraction causes no difficulty: a contact cap truncated to zero contributes an empty slab.

### Scope of this limit

This is not an exclusion of every explicitY source. A smallerY can lower helper cost or characteristic usage while retaining already-positive routing margin. It may also permit a largerL under a characteristic cap. A genuinely smaller restricted local-rank estimate can change the comparison. The lemma concerns only the sameD,L,S and unchanged rank bound, with actual-D exact slabs; it should not be applied to the old rounded cap that itself depends onY.

Status: mathematical proof audit and port design, not a compiled Lean implementation or complete benchmark certificate.
