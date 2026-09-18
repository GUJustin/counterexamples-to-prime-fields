# Complete characteristic-zero obstruction for the Paley quadratic-cover route

Status: proved algebraic reduction plus independently replayed finite linear certificates. No proper degree(7,1) witness with14 agreements exists on ANY rational quadratic lift of the Paley seven-cubic word over a characteristic-zero field extension. Both finite poles and the pole at infinity are included. This concerns this specific seven-bank and augmentation mechanism, not arbitrary eighth-word constructions.

## Pole normalization and full fibers

Work over an algebraic closure. A proper witness is a rational section of degree6 with one extra simple pole outside the core. A source PGL2 change moves that pole to infinity. The old cleared sections still have degree<=6, while the witness becomes a polynomial N of exact degree7. Write the cover as X=R(U)/S(U), degree2, coprime, with14 unramified fibers comprising28 distinct core points. Infinity is outside the core.

There are at most3 full fibers. Indeed, if four were full, interpolate their received values by a cubic T(X). Then N-S³T(R/S), of degree at most7, vanishes at8 distinct points and is zero, contradicting degN=7.

Choose14 matched points. Full and empty fibers are disjoint sets F,E of equal size f<=3. Their incidence inequalities are exactly those proved in FIBER_GATE.md. The complete lists have sizes1,7,42,252 for f=0,1,2,3. Let T_F be the degree<=f-1 interpolant of the full-fiber values (zero if f=0), and Q_F=product_{x in F}(X-x).

After division by the full-fiber product,

    v=(N/S³-T_F(X))/Q_F(X)=M(U)/S(U)^(3-f),
    deg M=7-2f=2m+1, m=3-f.

At every one of the14-2f single fibers, v has the fixed value

    v_x=(w_x-T_F(x))/Q_F(x).

## Norm coefficient bounds, including infinity and ramification

The function v does not belong to k(X). If S has degree2, v has one simple pole at U=infinity over a finite X-value; a pullback rational function would have poles on the whole degree2 fiber, or even pole order at a ramified point. If S has degree1, the two points over X=infinity have v-pole orders m+1 and at most m, unequal. If S is constant, X has a double pole at infinity whereas v has the odd pole order2m+1. Each case excludes v in k(X).

Thus v generates k(U)/k(X), and its minimal relation has degree2 in v. Clearing its trace and norm denominators gives

    A(X)v²+B(X)v+C(X)=0,
    deg A<=1, deg B<=m+1=4-f, deg C<=2m+1=7-2f,
    A!=0.

For clarity, when S has degree2 the sole additional finite pole lies over x0=X(infinity). Trace and norm have at most a simple pole at x0. Their infinity orders are at most m and2m, respectively, because v has order at most m times the X-pole order at each S-root. Multiplying by X-x0 gives the displayed degree bounds. This argument also covers a ramified S-root and ramification at U=infinity. If degS=1 or0 there is no finite extra pole; the trace and norm infinity orders are at most m+1 and2m+1 directly. Cancellation in M only reduces these pole orders.

Consequently every witness supplies a nonzero vector in the linear system obtained by evaluating this relation at the fixed single-fiber values. The system has14-2f rows and15-3f columns. This is a necessary linear gate without cover variables.

## Exact rank certificate and characteristic-zero transfer

Use K=Q(zeta_7), the Paley constants from compactpaley_seven_appendix.tex, and reduce at the prime zeta_7 ->16 modulo29. All14 base points remain distinct; every interpolation denominator and Q_F(x) at a single fiber is a unit. The exact finite matrices have:

| f | patterns | columns | rank in every pattern |
|---:|---:|---:|---:|
|0|1|15|14|
|1|7|12|12|
|2|42|9|9|
|3|252|6|6|

For f>=1, a nonzero full-column minor modulo29 is a nonzero minor over K. Hence no nonzero relation exists, even after any extension of K. This is elementary linear-rank specialization, not an inference from modular nonlinear ideal computations.

For f0, rank14 modulo29 proves the characteristic-zero kernel has dimension at most1. There is already an explicit nonzero LINEAR relation. Put s=alpha^7 and t=c alpha². On the14 points the received word is

    W(X)=(a+b X^7)/X²,
    b=(t-1)/(s-1), a=(s-t)/(s-1).

Indeed X^7 is1 or s, and X²W is respectively1 or t. Therefore X²v-a-bX^7=0 lies in the permitted coefficient space and has A=0. It spans the kernel. No relation with A!=0 exists, contradicting the minimal quadratic relation. This completes all strata.

## Reproducibility and independent verification

`all_fiber_norm_gate.py/json` records every matrix and chosen independent row/column indices. `verify_norm_gate.py` independently reconstructs the incidence masks from the two Paley exponent sets, enumerates the complete302-pattern set, rebuilds every matrix using coefficient-polynomial Lagrange interpolation, and computes each chosen minor by exact integer Bareiss elimination before reduction modulo29. All302 certificates PASS, recorded in `norm_gate_independent_verification.json`. The f0 kernel is independently checked to have A=0. No symmetry quotient is needed for these302 tiny matrices.

The original fixed-cover pilot is now superseded in characteristic zero by this all-cover obstruction. The alternative orbit2 seven-cubic bank has different received-word geometry and is not covered by this theorem.
