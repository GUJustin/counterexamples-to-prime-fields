# A proved bounded case: rebuilding derivatives from a curvature-linear denominator

Suppose a polynomial solution P satisfies

    A(X,P,P',Z) P^[2]+B(X,P,P',Z)=0,
    A(X,P,P',Z)!=0,

in characteristic zero or characteristic greater than the derivative orders under consideration. Put V=P^[2]. On this branch the differentiation operator is

    D=partial_X+R partial_Y−2(B/A) partial_R.

This uses the source coefficient A as denominator; it need not use the carrier separant F_R. For every j>=2 there is a polynomial N_j such that

    P^(j)=N_j(X,P,P',Z)/A(X,P,P',Z)^(2j−3).

Indeed N_2=−2B. If e=2j−3 then the exact recurrence is

    N_(j+1)=A²(N_j)_X+A²R(N_j)_Y−2AB(N_j)_R
             −e N_j[A A_X+A R A_Y−2B A_R].

This follows by the quotient rule, so no generic-rank or geometric hypothesis enters the identity.

Assume the curvature-linear source has cumulative flags

    2 deg_V+deg_R<=Bflag,
    deg_V+deg_Y+deg_R<=U,
    deg_V+deg_Y+deg_R+deg_Z<=L.

Then the coefficient A has caps (Bflag−2,U−1,L−1), and B has caps (Bflag,U,L). The recurrence gives

    deg_R N_j <=(2j−3)(Bflag−2)+j,
    deg_(Y,R) N_j <=(2j−3)(U−1)+1,
    deg_(Y,R,Z) N_j <=(2j−3)(L−1)+1.

For example, the slope-degree growth per step is at most2Bflag−3: the terms containing R times a Y derivative, or B times an R derivative, attain this cap. The other two cumulative degrees grow by at most2(U−1) and2(L−1). This proves the displayed formulas by induction. Denominator caps are (2j−3) times the caps of A. Hasse derivatives differ only by the invertible factor j!.

This is a concrete alternative tail representation for a curvature-linear source on its regular A!=0 branch. It does not by itself improve the benchmark: the curvature-linear sources tested so far have activation L too late, and their coefficient caps may still make this representation expensive.

For a higher-curvature retained source, the existing moving budget bounds the pole divisor of the actual curvature root using its multiplicity. It is tempting to replace the polynomial A above by that smaller divisorial budget, but the recurrence does NOT justify that substitution automatically. A proof must control the derivation on the relevant normalized surface/curves, boundary divisors, and repeated differentiation of a rational function specified only through its pole divisor. This is the precise missing extension needed to rebuild the normal tail coordinate from the retained source instead of the carrier-only separant estimate.

The subsequent audit CURVATURE_POLES_AND_RAMIFICATION.md shows two concrete obstacles to that extension: curvature poles alone do not control derivative poles even on an invariant normalized curve, and proper first-tail components need not be invariant under the ambient derivation. The pinned proof instead restricts explicit ambient filtered cuts and retains separate coordinate and moving costs. No removal of the coordinate cost is justified here.
