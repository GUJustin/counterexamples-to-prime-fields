# Orbit2 degree-ten net: initial geometric profile

This is a separate net from the Paley example. The saved basis is over
F83, at the cubic-field embedding q=4 for q^3-10q^2+3q+1. No cyclic
symmetry is assumed.

## Integral characteristic-zero model without a large symbolic solve

There are exactly 217 prescribed Hasse equations and 220 weighted
monomials. The saved rank-217 minor is a unit at the chosen prime above
83. Consequently the exact characteristic-zero matrix has rank 217,
and its kernel is free of rank three over the DVR. Solving the pivot
variables with each free variable set to one gives an integral basis
reducing exactly to the saved modular RREF basis. Unlike an overdetermined
system, there are no remaining rows whose exact vanishing needs a
separate lifting argument. The archived exact orbit2 bank and its
reduction supply the coefficients of this matrix.

## Basepoints

The initial saved basis has F0 and F1 sharing the old zero graph Y=0;
this does not mean the entire net has a fixed component. The pair used
for the resultant audit was changed to F0+F2, F1+2F2, F2, with determinant
one. The two resultants have no residual common root after division by
the forced base-coordinate factor of degree 364. Specialized gcds at all
fourteen known X coordinates have exactly the prescribed ordinate and
multiplicity. The leading-Y restrictions and weighted-infinity
restrictions have gcd one. All fourteen tangent-cone triples have rank
three and no common projective direction.

Thus this net has precisely fourteen basepoints, each resolved by one
blowup; there are NO two extra points as in the Paley net. Its moving
class has L^2=16, K.L=12, c2=18, p_a=15, and jet Chern number 90.
Basepoint-freeness transfers by properness of the relative base locus.
The tangent rank-three checks also prohibit multiplicity jumps at all
fourteen basepoints.

## Ramification and old graph contributions

The affine jet-minor gcd is one. The determinant has weighted degree 97,
bidegree (94,28), and 1,511 terms. Dividing by the seven old graphs leaves
one irreducible factor Gamma of weighted degree 76, bidegree (76,21),
and 986 terms. The smooth F83 point (1,75), with gradient (64,11), proves
that Gamma is geometrically irreducible.

For each old graph the two parameter-line normal sections, after removal
of the 27 forced base orders, are coprime quartics with maximum degree
four. Their map to the old parameter line has degree four and is
separable. The determinant is simple along every old graph. Hence those
seven components contribute 28 to the degree-90 jet cycle, leaving a
residual effective degree-62 cycle.

Before applying the cycle statement globally one should explicitly retain
the boundary jet-rank check: exceptional maps are nonconstant of degree
4 or 6, while the original boundary restrictions have degrees at most
4 and 10 and are nonconstant. These are below 83 and therefore separable.
This excludes divisorial rank-one jet loci at the boundary. It does not
assume that Gamma consumes the entire remaining cycle or that its image
has degree 62; interpolation must certify that as in the Paley audit.

Files: profile.py/json/resources.json, finish_profile.py, and
old_graph_degrees.py/json. No rational member or complete exclusion is
claimed by this initial profile.

## Completed Gauss interpolation

`sample_gauss.py` produced 4,102 distinct normalized images over
F83[r]/(r^3-r-3), with source points and rank-two witnesses, in 8.75s.
`verify_gauss_samples.py` independently replayed all source equations,
12,306 jet-kernel equations, and every rank-two witness with standard
library tuple arithmetic (3.21s). This is source-point interpolation,
not a scan for candidate net members.

`interpolate.py` uses no assumed symmetry. It takes 760 Frobenius-orbit
representatives and expands each field equation into three F83 rows.
The full 2,280-by-2,016 homogeneous-degree-62 matrix has rank 2,015.
Its unique relation has 1,990 terms and was independently evaluated at
all 4,102 images. Runtime 5.91s, peak 198MiB.

Since 4,102>62^2, Bezout forces every degree-62 relation to contain the
geometrically irreducible Gauss image. A smaller-degree image would
supply more than one independent degree-62 multiple, contradicting the
kernel dimension. The image therefore has degree 62 and exhausts the
entire residual cycle, with multiplicity one and no other components.
The same relative regular-sequence/proper-cycle-specialization argument
as the Paley audit identifies this equation as the reduction of the
characteristic-zero residual discriminant. The closed multiplicity-15
locus remains to be tested; no rational-member exclusion is inferred
from interpolation alone.
