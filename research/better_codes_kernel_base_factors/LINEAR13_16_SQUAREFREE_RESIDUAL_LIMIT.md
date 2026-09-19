# The squarefree residual discriminant does not close linear multiplicities 13--16

September 19, 2026. Exact binding-shape resource check, with no optimizer
or parameter scan. The proposed local discriminant cost is valid. It
rejects the previously displayed e=13,14 profiles, but small explicit
changes restore feasibility for **all four** multiplicities. No global
polynomial or benchmark improvement is asserted.

Use the setup and rank function of
[LINEAR17_OWN_SYSTEM_EXCLUSION.md](LINEAR17_OWN_SYSTEM_EXCLUSION.md):

    n=262144, w=131071, A=(Y-P)^e H, h=43-e,
    e∈{13,14,15,16}, deg_Y H=h, wt(H)≤h w+12.

This note assumes Disc_Y H is nonzero. At the target characteristic,
which exceeds h, this is equivalent to H being squarefree over k(X,Z).
**Non-squarefree H is outside this discriminant argument.** Discarding
the at most 12 zeros of lc_Y H gives the usual good coordinates.
The explicit surviving profiles below have no bad coordinates at all.

## Local discriminant cost

At a good coordinate write t=X-x, translate the received symbol to zero,
and put

    nu(s)=max(0,ceil(s/2),s-12),
    phi(s)=max(0,s/2,s-12).

The leading-coefficient contact condition says that the Newton polygon
of A lies above ordinate phi(a-j) at horizontal coordinate j.

At a graph coordinate, changing from received-symbol centering to
W=Y-P(X,Z) preserves this condition: the two centers differ by a multiple
of t, and a translation sends (u,j) to (u+v,j-v), which cannot decrease
u+j+min(u,12). Since A=W^e H, the centered H coefficients satisfy

    ord_t H_j ≥ nu(a-e-j).

At a nongraph coordinate, the graph factor has a unit constant term in
the received-symbol coordinate. Its Newton polygon has the endpoint
(0,0); the Newton polygon product formula therefore puts the entire
Newton polygon of H inside that of A. Consequently the Newton polygon
of H lies above phi(a-j). In particular nongraph contact is at most h.

Thus let b=max(a-e,0) on graph coordinates and b=a on nongraph
coordinates. In each case 0≤b≤h and NP_H(j)≥phi(b-j). The monic
normalization of H at a good coordinate changes no valuations.
If its roots have valuations v_1≤...≤v_h, then

    ord Disc(H) ≥ 2 sum_(i<j) min(v_i,v_j)
                = 2 sum_(j=1)^(h-1) NP_H(j).

The first inequality is ord(alpha_i-alpha_j)≥min(v_i,v_j);
the equality is the usual root-slope description of the Newton polygon.
Therefore

    ord Disc(H) ≥ D(b),
    D(b)=sum_(s=1)^(b-1) max(s,2s-24)
        =binom(b,2)+binom(max(b-24,0),2).                 (1)

In particular full contact h costs D(h), and contact h-1 costs D(h-1).
Weighted homogeneity of the discriminant gives the global upper budget

    deg_X Disc(H) ≤ h(h-1)w+24(h-1).                    (2)

Indeed each coefficient H_j has degree at most (h-j)w+12; the
discriminant has coefficient degree 2h-2 and weighted coefficient degree
h(h-1) when H_j is assigned weight h-j.

These local costs are attained by squarefree models in the states used
below. For b≥24 put

    C_b(Y,t)=prod_(i=1)^12 (Y²-i t)
               *prod_(j=1)^(b-24) (Y-j t).

All factors are distinct and separable over k((t)). Their pairwise
resultants are nonzero. The 12 individual quadratic discriminants cost
12; their pairwise resultants contribute 4*binom(12,2); quadratic-linear
pairs contribute 24(b-24); and linear-linear pairs contribute
2*binom(b-24,2). The sum is exactly D(b). Its contact is b.
For residual degree h and contact h-1 use (Y-1)C_(h-1), which adds a
unit root and no discriminant valuation. At graph nodes multiply by
Y^e; at a nongraph node with graph offset -1 multiply C_h by (Y+1)^e.
These realize contacts 43, 42, and h respectively. They are local models
only, with no claim that they glue under the global degree bounds.

## Exact replacement profiles

The old profiles had 60000 nongraph contact-h nodes, 71073 graph
contact-42 nodes, and 131071 graph contact-43 nodes. Their excesses
over (2), for e=13,14,15,16, are respectively

    1515852, 347244, -559218, -1203534.

Thus the first two profiles are incompatible with nonzero Disc(H).
Move the following numbers of graph nodes from contact 43 to contact 42:

| e | h | Moved | Nongraph h | Graph 42 | Graph 43 | Discriminant slack |
|---:|---:|---:|---:|---:|---:|---:|
| 13 | 30 | 44584 | 60000 | 115657 | 86487 | 4 |
| 14 | 29 | 10852 | 60000 | 81925 | 120219 | 20 |
| 15 | 28 | 0 | 60000 | 71073 | 131071 | 559218 |
| 16 | 27 | 0 | 60000 | 71073 | 131071 | 1203534 |

Every row has n coordinates. The e=13 discriminant total is 114032462,
below its budget 114032466; the e=14 total is 106430304, below 106430324.
The moved counts are simply the ceilings of the old excess divided by
D(h)-D(h-1), respectively 34 and 32; no LP optimization is needed.

All previously tested resources still pass:

| e | Rank surplus over C-1 | Minimum graph-coefficient slack | Best graph-power helper excess |
|---:|---:|---:|---:|
| 13 | 156587816555 | 44596 | 182564 |
| 14 | 148394795615 | 10864 | 156296 |
| 15 | 107094664275 | 12 | 107148 |
| 16 | 51418264275 | 12 | 47148 |

Here C-1=6802316684344. Using this full rank requirement is stronger
than using the bad-node allowance. Each row has 202144 graph coordinates,
fewer than the routing threshold 211941. Moving contact 43 to 42 only
reduces every tested centered-coefficient order sum. The helper check
evaluates its entire permitted range q=0,...,55:

    q w+60000h+N42 max(42-q,0)+N43 max(43-q,0).

Its minimum remains strictly greater than the own-system cap 55w.

The exact script
[linear13_16_residual_discriminant.py](linear13_16_residual_discriminant.py)
checks these integers, every graph-coefficient budget, every helper
power, and the local contact models. Its
[receipt](linear13_16_residual_discriminant.json) passed under the
60-second/384-MiB [guard](linear13_16_residual_discriminant.resources.json).

Thus rank plus this discriminant resource does not exclude the e=13,14
squarefree-residual cases, even after retaining the previously tested
coefficient, routing, and helper inequalities. The failure of the old
specific profiles is real, but is not a closure theorem for either
multiplicity. The surviving profiles remain necessary-resource examples,
not globally realized polynomials or lower-bound constructions.
