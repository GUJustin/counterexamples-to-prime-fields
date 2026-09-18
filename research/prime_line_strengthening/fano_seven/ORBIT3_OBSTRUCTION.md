# Global exclusion of non-Fano orbit 3 in characteristic different from two

Use the ordered representative in design_orbits.jsonl, with quadruple nodes
b_0,...,b_6 indexed by the C blocks. Extend constants to an algebraic closure.
All fourteen nodes and seven cubic sections are distinct.

## A forced involution and complete amplitude parametrization

The common triple156 point leaves the following other pair roots:

    pair15: b_3,b_5; pair16: b_4,b_6; pair56: b_0,b_1.

Divide the three pair differences by their common triple-point linear form.
The resulting three pair-root quadratics are dependent, pairwise coprime,
and span a basepoint-free pencil. Its separable degree-two map has a deck
involution. Exactly as in NONFANO_ORBITS_01_OBSTRUCTION.md, choose a fixed
point at infinity different from the remaining quadruple node b_2. The seven
quadruple coordinates are therefore

    (b_0,...,b_6)=(u,-u,d,v,z,-v,-z).

The guards are u v z != 0, u^2,v^2,z^2 pairwise distinct, and
 d not in {±u,±v,±z}. Triple nodes may be at infinity; binary cubic identities
below remain valid in that case.

Interpolate the seven quadruple received values by W of degree at most six.
Candidate P_i is its remainder modulo the monic quartic L_i of the four
quadruple nodes containing i. Subtracting a common cubic reduces to

    W=aX^4+bX^5+cX^6,

with a nonzero amplitude vector (a,b,c).

## Six necessary linear rows

The remaining triples, in row order0,...,5, are

    123,124,257,346,357,467.

For each triple choose its pair {i,j} having just one quadruple root, with
 i<j, and write k for the remaining index. Thus the chosen orders are

    (i,j,k)=(1,2,3),(1,2,4),(5,7,2),(4,6,3),(5,7,3),(4,6,7).

Put A=P_i-P_j, B=P_i-P_k. Let q be A's single quadruple root; let V0,W0
be the monic quadratics of the two quadruple roots of B and B-A respectively.
Define

    U=W0(q)V0-V0(q)W0,       V=W0(q)V0.

The shared triple root forces A V-B U=0. Indeed, after dividing by that
root, the quadratic pair is uniquely determined up to scalar by these five
prescribed roots. All evaluations at q are nonzero. The same identity holds
if the shared triple root is at infinity.

Define row M_j to be the coefficients of (a,b,c) in [X^5](A V-B U).
This is an explicit6-by3 polynomial matrix in u,v,z,d, with no divisions.
Every putative realization gives M(a,b,c)^t=0; hence all three-row minors
must vanish. `nonfano_involution.py 3` constructs precisely this matrix from
monic polynomial division; its row contents are all1.

## Two exhaustive branches

Write M_ijk for the determinant of rows i,j,k. Direct expansion gives

    M_012=(d+v)(z-u)(u+v)(z-v)^2(v+z) F G,

where

    D_F=u^2+2vz+z^2,           N_F=u^2(v+2z)+vz^2,
    D_G=u^2+uv+3uz-vz,        N_G=z(-u^2+3uv+uz+vz),
    F=N_F-dD_F,               G=N_G-dD_G.

All displayed factors outside F,G are nonzero. Both rational branches are
well-defined. If D_F=0 then N_F=-2z(v+z)^2 != 0. If D_G=0, use the nonzero coefficient u-z of v in D_G to obtain

    v=-u(u+3z)/(u-z),
    N_G=-4uz(u+z)^2/(u-z) != 0.

Thus F=0 implies d=N_F/D_F, and G=0 implies d=N_G/D_G.

### Branch G=0

The exact substituted minor is

    M_034 = 16uvz^2(z-u)^2(u-v)^2(u+v)^3(u+z)^4
                 * (z-v)^2(v+z) / D_G^3.

Every factor is nonzero, so this branch is impossible.

### Branch F=0

Set

    E1=u^2v-u^2z-3uv^2-2uvz-3uz^2-v^2z+vz^2,
    E2=3u^2v+u^2z-uv^2+2uvz-uz^2+v^2z+3vz^2,
    J=u^2v+3u^2z+3vz^2+z^3.

Here J=D_F(d+z) is nonzero. The exact minors become

    M_023 = -2z(z-u)^3(u-v)^2(u+v)^3(u+z)(z-v)(v+z) J E1 / D_F^3,
    M_245 = -2z(z-u)^3(u-v)^3(u+v)^3(u+z)^2(z-v)(v+z)^2 E2 / D_F^3.

All factors except E1,E2 are nonzero. Hence E1=E2=0. But

    E1+E2=4(u-v)(uv-z^2),

so uv=z^2. Substituting v=z^2/u into E1 yields

    E1=-z(u+z)^2(u^2+z^2)/u^2.

Consequently u^2+z^2=0 and v=-u, violating distinctness. This excludes the
second branch and completes the global odd-characteristic obstruction.

## Exact verification and scope

- nonfano_involution_3.json records the complete six rows and20 minors;
  its bounded job took11.23seconds, peakRSS below71MiB.
- nonfano3_branches.py/json records the exploratory rational branch reductions.
- nonfano3_exact_minors.py/json records the three exact substituted determinant
  identities above, including scalar factors2 and16 and all denominators;
  its bounded job took1.66seconds, peakRSS below66MiB.

The proof strips no factor without a nonvanishing guard. Its only scalar
characteristic exclusion is2. It rules out this entire ordered incidence orbit,
not merely a parameter sample; it says nothing about the remaining orbit2.
