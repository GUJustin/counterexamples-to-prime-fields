# Global odd-characteristic exclusion of ordered design orbit6

The enumeration's orbit6 has a Fano T and another Fano C. Relabel its candidates by

    1->1, 2->2, 3->3, 4->4, 5->7, 6->5, 7->6.

Then the two ordered designs become

    C=123,145,167,246,257,347,356,
    T=123,147,156,245,267,346,357.

We prove there is no cubic realization over any field of characteristic different from two. All fourteen nodes and seven candidates are assumed distinct.

## General cubic parametrization from the quadruple nodes

Normalize the seven complementary-quadruple nodes, in the displayed C order, to

    infinity,0,1,u,v,w,z.

Their finite values are pairwise distinct and different from0,1. Subtract P1 so P1=0. Each pair has three prescribed common nodes, hence its cubic difference has no further root. In particular the three outsiders at a quadruple node have distinct values different from that quadruple's value.

Let the selected quadruple values at0,1,infinity be j,k,l. They are all nonzero because P1 is an outsider at these three nodes. Scale values to make j=1, and write K=k/j, L=l/j. Define

    Q2=(X−w)(X−z), Q3=(X−u)(X−v),
    Q4=(X−v)(X−z), Q5=(X−u)(X−w),
    Q6=(X−v)(X−w), Q7=(X−u)(X−z).

The complete family of cubics satisfying all seven C-quadruple incidences is

    Pi=Qi*((K/Qi(1)−1/Qi(0))*X+1/Qi(0)), i=2,3;
    Pi=Qi*(L*(X−1)+K/Qi(1)), i=4,5;
    Pi=Qi*(L*X+1/Qi(0)), i=6,7.

Indeed, the four quadruples containing candidate1 force each Pi to have its two displayed b-roots. The remaining quadruple equalities specify exactly the values at0,1 or the leading coefficients of the remaining linear factors. There are no omitted restrictions or divisions by possibly zero quantities: all Qi(0),Qi(1) are nonzero by distinctness.

The triple T123 needs a common root of P2,P3 outside all b-nodes. Their quotient linears therefore have the same root. Since the values j,k are nonzero, this forces

    (1−u)(1−v)/(uv)=(1−w)(1−z)/(wz).

Consequently, with s=w+z−1,

    v=wz(1−u)/(wz−us).                         (1)

The denominator cannot vanish, since its defining equation would then force u=1.

## The two triples through candidate1

T147 and T156 require the quotient linears for P4,P7 and for P5,P6, respectively, to have a common root outside the b-nodes. Their leading coefficients all equal L!=0. They must therefore be identical, giving

    L=K/[(1−v)(1−z)]−1/(uz),
    L=K/[(1−u)(1−w)]−1/(vw).                   (2)

Substitute (1) and the first equation (2) into the second. The exact difference factors as

    −(us−w)*G / [u w² z (u−1)(w−1)(z−1)²],

where

    G=K w² z(u−z)+(u−w)(w−1)(z−1)².

Every denominator is nonzero. Hence either us=w or G=0.

The branch G=0 is inadmissible. In that branch

    K=(u−w)(w−1)(z−1)²/[w² z(z−u)],
    L=[us−2wz+w]/[w² z(z−u)].

But the leading coefficient of P2 is

    K/[(1−w)(1−z)]−1/(wz)=L.

Thus candidate2, an outsider, shares the value of the selected quadruple4567 at infinity. This is an additional pair agreement and contradicts saturation of the cubic root bounds.

We are left with the branch

    u=w/s, v=z/s.                             (3)

Here s!=0, and s!=1 because otherwise u=w would collide. All other distinct-node guards remain in force.

## Four linear-quotient determinants on the remaining triples

For every pair i,j, divide Pi−Pj by its two prescribed C-quadruple root factors. The result is a linear polynomial. An off-b common root for a T-triple forces the determinants of the appropriate two linear coefficient rows to vanish.

For T245 use pair quotients

    (P2−P4)/[(X−1)(X−z)],
    (P2−P5)/[(X−1)(X−w)].

For T267 use

    (P2−P6)/[X(X−w)], (P2−P7)/[X(X−z)].

For T346 and T357 use, respectively,

    (P3−P4)/[(X−1)(X−v)], (P3−P6)/[X(X−v)],
    (P3−P5)/[(X−1)(X−u)], (P3−P7)/[X(X−u)].

Let each determinant be leading-times-constant minus constant-times-leading in the displayed pair order. Substitute (3) and the first equation (2). Set

    A=K wz(w+z), H=(w−1)(z−1)(s−1),
    F3=−K w²z+(w−1)(z−1)²,
    F4= K wz²−(w−1)²(z−1),
    Delta=w² z²(w−1)²(z−1)².

Exact simplification gives

    D245=2(z−w)(A+H)/[w² z²(w−1)(z−1)],
    D267=2K(z−w)(A+H)/[wz(w−1)²(z−1)²],
    D346=2s² F3(A−H)/Delta,
    D357=−2s² F4(A−H)/Delta.

All denominators and z−w are nonzero. Thus D245=0 forces A+H=0. The guard s!=1 gives H!=0, so A−H=−2H!=0 in the specified characteristic. Consequently D346=D357=0 force F3=F4=0. Dividing these two nonzero equalities yields

    w(w−1)=z(z−1),
    (w−z)(w+z−1)=(w−z)s=0.

This contradicts w!=z and s!=0. Orbit6 therefore has no odd-characteristic or characteristic-zero realization.

## Exact artifacts and scope

`orbit6_amplitudes.py/json` records the generic amplitude ratios. `orbit6_quotients.py/json` derives the through-candidate1 factor and the four linear-quotient determinants directly from the complete cubic parametrization. `orbit6_branches.py/json` performs the exact generic and exceptional substitutions. All jobs were bounded by384MiB/60seconds; the two substantive successful jobs took4.05 and3.39seconds.

The proof is algebraic in characteristic different from two. It does not rely on a sample of node parameters, does not divide by an unexamined branch factor, and explicitly handles the us=w exceptional branch. It excludes ordered orbit6 only, not the remaining incidence designs.
