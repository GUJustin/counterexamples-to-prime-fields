# Shift-zero cubic lift: exact one-pole obstruction

Scope: characteristic zero, arbitrary extension coefficient field. The fourteen-node Paley seven-cubic word is pulled back by X=U³, with all 42 nodes distinct. There is no proper rational function N(U)/(U-b), deg N≤10, pole off the domain, agreeing at 21 or more nodes. This concerns this operation and this cover only.

Write ζ for a primitive seventh root, η=ζ+ζ²+ζ⁴, α=(η−1)/2, and λ=3(η+3)/4. The seven quad-bucket base nodes ζ^j have values ζ^(5j); the seven triple-bucket nodes αζ^j have values λζ^(5j). The seven original cubics have respectively four and three incidences per bucket node. Their triple incidence matrix M satisfies MMᵀ=2I+J and M+Mᵀ=J−I; the quad matrix is Q=I+M.

## Fiber reduction

The details, including the general depressed cubic, are in FIBER_PATTERNS_AND_LINEAR_GATE.md. Every proper witness with at least 21 agreements has exactly 21 and one of two patterns: (I) two matches on every triple fiber and one on every quad fiber; (II) one full triple fiber and its paired empty quad fiber, two matches on every other triple fiber, and one on every other quad fiber. In particular every triple fiber has at least two matches.

Choose β³=α, put V=U/β, and replace N by N(βV)/β and b by b/β. Decompose the normalized numerator uniquely as A(X)+VB(X)+V²C(X), X=V³, with degrees at most 3,3,2. Its triple fibers are X=ζ^j. Choose an omitted root on each such fiber (arbitrarily for a full fiber):

    t_j=ζ^(5j) ω^(s_j),   s_j∈{0,1,2},   ω³=1, ω≠1.

Let d=C/λ, and brackets mean interpolation/remainder modulo X⁷−1. The necessary five linear constraints are

    [dt]_4=0, [dt]_5=−1, [dt]_6=0,
    [dt²]_4=0, [dt²]_6=0.

They are also sufficient for the numerator degree constraints at these chosen pairs. Reconstruction is

    B/λ=X⁵+[dt], e=[dt²]_5, A/λ=[dt²]−eX⁵.

All matrix entries lie in Q(ζ₂₁). With F_k=Σ_j ζ^(kj)ω^(s_j) and G_k=Σ_j ζ^(kj)ω^(2s_j), the columns indexed d=0,1,2 are F_(d+5−l) for l=4,5,6 and G_(d+10−l) for l=4,6. The right side is (0,−7,0,0,0).

## Finite exact certificate

`rank21.py/json` evaluates the 105 orbits under cyclic position rotation and addition of a common phase. The only consistent representatives are:

| phase tuple | coefficient rank | solutions |
|---|---:|---|
| 0000000 | 2 | d=−1+eX², arbitrary e |
| 0000001 | 3 | d=−1+ζ²X² |
| 0000002 | 3 | d=−1+ζ²X² |

The orbit sizes are 3,21,21. All other 2,142 assignments are inconsistent. This is independently certified by `independent_rank_minors.py/json`: it enumerates all 2,187 tuples directly, without orbit reduction or Gaussian elimination. For each inconsistent tuple it supplies a nonzero augmented 4×4 minor; for each of the 42 nonconstant consistent tuples a nonzero coefficient 3×3 minor. All determinants are computed by the permutation formula modulo 43 using the primitive 21st root 9. A nonzero reduction of an integral cyclotomic determinant certifies that determinant is nonzero in characteristic zero. The displayed solutions supply consistency, so no converse inference from modular rank is used.

Global phase changes and cyclic rotations preserve consistency and properness: they are induced by scaling V by a cube root of unity or a seventh root of unity, with the corresponding nonzero scaling of the word and numerator. They thus permit using the three displayed representatives.

For 0000000 direct reconstruction gives

    C=λ(−1+eX²), B=λe, A=−λX³,
    N(V)=−λ V(1+V⁷)(V−e).

It is improper for every e. Both exceptional representatives give precisely the same factorization with e=ζ²: their altered omitted root is at j=6 where C(ζ⁶)=0, so it does not change the equations. Thus every consistent assignment is improper, proving the stated obstruction. No assumption that the unknown coefficients lie in the cyclotomic field is needed: ranks and the explicit affine solution spaces persist under any field extension.
