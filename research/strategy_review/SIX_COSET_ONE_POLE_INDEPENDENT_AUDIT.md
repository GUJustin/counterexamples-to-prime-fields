# Independent audit of the six-coset one-pole obstruction

**PASS.** Independently checked SIX_COSET_ONE_POLE_OBSTRUCTION.md. The
argument excludes the stated proper degree-at-most-50m numerator over a
linear denominator for every integer m>=1. No scan or manuscript change
is needed.

At least94m agreements occur on mu_(196m). The polynomial N^2-P^2 is
nonzero by properness and has degree2d after the initial root count forces
d>=47m. A common root of N^2-P^2 and X^M P-N cannot be the pole or zero.
It lies in mu_(2M) and is exactly an agreement point. If the first
polynomial has zero derivative there, then N'=X^M P', and the derivative
of the second is M X^(M-1)P, which is nonzero. Thus their gcd G is
squarefree and has degree exactly the number t of group agreements.
This checks both directions and multiplicities of the gcd identification.

The quotient degrees e=2d-t and r=M+1-t are exact, and E,Q are coprime.
Direct expansion confirms

    (E+2QN)^2=4EQP X^M+E^2+4Q^2P^2.

The degree comparison gives deg F=d+r; no leading-term cancellation is
possible. For C nonzero, deg C<=max(12m,8m+4)<M, including m=1.
At a zero of Q, C=E^2 is nonzero; at a zero of E, a common zero with C
would require P=0. But E(a),Q(a) are nonzero by properness, and
C(a)=E(a)^2. Therefore the only possible common root of the three terms
is X=0. This analysis also handles a=0, in which case C(0) is nonzero.

If C(0)=0, E,Q,P are units there. Since deg C<M, its order equals the
order of F^2, namely2h<M. After division by X^(2h), the three terms are
pairwise coprime. The radical bounds used in the note are valid even
when roots within E,Q,P overlap, since only upper bounds are needed.
The exact leading degree of 4EQP X^M equals2(d+r), and every normalized
term has degree at most112m+2<200m<p. Thus the characteristic-p
all-pth-power exception cannot occur: at least one term is nonconstant,
and any nonconstant polynomial of degree<p has nonzero derivative.

Mason--Stothers therefore yields precisely

    d<=e+c+1-h<=max(3e+1,e+2r+3),
    3t<=max(5d+1,d+2M+5)<=250m+1.

The last maximum is valid for m=1 as an equality of its two bounds,
and for larger m the first dominates. It contradicts3t>=282m for every
m>=1.

For C=0, factoring over the algebraically closed constant field gives
E=constant*QP. Coprimality makes Q constant. Already E(a)!=0 contradicts
this displayed factorization; alternatively, the note's square-root
argument gives P|F and P|E, hence P|N, contradicting properness. The
latter is also valid for the pole a=0 and uses the even integer M=98m.

The result concerns this exact seed and linear-denominator operation.
It does not rule out a different received word, a different denominator
budget, or a different amplification mechanism.
