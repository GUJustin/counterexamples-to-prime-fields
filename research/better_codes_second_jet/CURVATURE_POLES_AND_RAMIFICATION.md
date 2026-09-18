# Curvature poles do not by themselves pay for higher tails

Status: a proved local bound and a scoped counterexample; no improved benchmark certificate. This audits the proposed replacement of the carrier denominator by a fractional source-root pole budget.

## 1. The valid normalized-curve bound

Let k be algebraically closed, L/k a one-variable function field, and X a separating element. At a finite place of X choose a uniformizer t and put d=ord_t(dX/dt). Thus d is the local different exponent of the separable map to the X-line. Write D=d/dX. For every f in L,

    ord(Df) >= ord(f)-1-d.

Indeed Df=(df/dt)/(dX/dt), and formal Laurent differentiation lowers order by at most one. For regular f the stronger first-step bound is ord(Df)>=-d. Consequently, for q=max(0,-ord(f)) and j>=1,

    pole(D^j f) <= q+j(d+1)                 if q>0,
    pole(D^j f) <= j(d+1)-1                 if q=0.

These are upper bounds; characteristic-p cancellation can improve them. They do not require factorial division. Conversion to Hasse coordinates of order j does require j! nonzero. Wild ramification can have d>e-1, so replacing d+1 by the ramification index e is only justified in the tame case. If X is inseparating, dX=0 and there is no derivation of L extending DX=1.

Globally the separable-map identity div(dX)=Diff-2(X)_infinity makes the missing resource explicit. A bound on poles of one algebraic curvature coordinate does not bound the different by itself.

## 2. Exact tame counterexample

Take e>=2, X=t^e and Y=t^(2e+1), in characteristic zero or characteristic p>3e. Then

    R=DY=((2e+1)/e)t^(e+1),
    V=D^2Y/2=((2e+1)(e+1)/(2e^2))t=Ct,
    DV=(C/e)t^(1-e).

Thus V is regular at t=0 and satisfies the monic equation V^e=C^e X, whose source Newton bound gives zero finite curvature poles. Nevertheless the third derivative D^3Y=2DV has a pole of order e-1. Here d=e-1, and the regular-input inequality above is sharp.

A relative version preserves a challenge parameter: put Z=t^e-X and DZ=0, so Dt=1/(e t^(e-1)); the same formulas hold and V^e=C^e(X+Z). Over k(Z), this is the same finite ramification calculation at X=-Z. This example is NOT asserted to be an actual proper first-tail component of the benchmark. In characteristic zero its high derivatives do not vanish, and it does not satisfy the required first-tail cut. It refutes only an unqualified lemma controlling all later tails solely by curvature poles.

## 3. A separate obstacle: the derivation need not descend

The normalized function field of a proper first-tail component need not carry the ambient ODE derivation. If the component ideal contains the first tail, its derivative is the next tail; the construction does not assume that next tail belongs to the ideal. An induced derivation on a quotient exists only when its ideal is stable under the derivation.

For a minimal illustration, on the ambient surface with derivation partial_y and curve y=0, the rational function y/x restricts to zero but its derivative restricts to 1/x. Restricted values alone lose the transverse jet. This is a general algebraic illustration, not a benchmark component counterexample.

Even a favorable bound for invariant curves cannot be applied to proper first-tail components without proving invariance or controlling those transverse jets. On an invariant curve satisfying D^(w+1)Y=0, characteristic zero imposes a much stronger differential identity. Positive characteristic introduces differential constants in L^p; no polynomial-in-X classification is asserted here without height and characteristic hypotheses.

## 4. What the pinned proof actually pays

Primary source: proximity-prize/proximity-prize at cdb451f13fdc6c84f5fe363e77ee13a89bd30974. Local cache paths below refer to that pin.

* `tmp/current-lower-primary-cache/LowerFoundation.lean:32840`: `movingPoleTarget` is max(2*all-coordinate pole, yz-coordinate pole + pole(G/H)). It is not merely the curvature pole.
* `LowerFoundation.lean:33068`: `coordinate_filteredCut_pole_le` bounds an explicitly constructed ambient rational cut after restricting it to the curve. Its bound is `flagPole(C)+k*(flagPole(base)+movingPoleTarget)`.
* `LowerFoundation.lean:33306`: `MovingPoleBudget` contains coordinate and moving budgets separately. `sum_filteredCut_pole_le` retains `weightedCost(C)+k*(weightedCost(base)+movingCost)`.
* `tmp/current-lower-primary-cache/LowerGeometry.lean:21049` and the following `SecondJetActiveMovingBudget.exists_budgets`: the second-jet source root multiplicity bounds the moving-cost sum by the source budget divided by the root multiplicity. This is already the legitimate fractional source gain.
* `LowerGeometry.lean:13494`: the hybrid first-tail provider separately retains rational-coordinate/weighted-inertia costs as well as moving cost; it does not derive higher tails by differentiating in the normalized first-tail field.

The inspected proof does not explicitly introduce a different divisor. Rather, its ambient rational-coordinate numerators and denominators avoid needing an induced derivation. It would be inaccurate to identify their cost exactly with the different without another theorem. What is established is that the source-root gain pays only one summand, and dropping the remaining summand is unsupported.

## 5. Exact remaining lemma needed for a gain

A useful replacement must bound the restrictions of the actual filtered tail cuts, including transverse jets at non-invariant first-tail components. One sufficient route would be a new pole inequality replacing BOTH the coordinate term and the moving term by a smaller joint source-and-carrier resource, with a proved global sum over the actual components. A normalized curvature-root Newton bound alone does not do this. The ramification example blocks the unrestricted invariant-curve shortcut; non-invariance blocks transferring even that shortcut automatically to the benchmark.

No numerical search was run for this audit. It supplies no reduction of the current 7.65% full-ledger deficit.
