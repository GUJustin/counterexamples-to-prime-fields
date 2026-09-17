# Coupled split Dickson families: exact equations and the common-core gate

2026-09-17. Bounded constructive exploration. No new prime-field fixed-gap counterexample is claimed.

## A split family with degree independent of the characteristic

Let e=2d+1 be odd, p>e, and e divide p-1 or p+1. For nonzero square u=a^2 define

    G_u(X)=sum_{j=0}^d binom(e,2j+1) u^(d-j) X^j.

This is monic of degree d. Its root set is uR, where

    R={ ((zeta-1)/(zeta+1))^2 : zeta in mu_e, zeta!=1 },

with zeta and zeta^-1 yielding the same root. There are exactly d distinct nonzero roots. If e|p-1 they lie in F_p immediately. If e|p+1, Frobenius sends zeta to zeta^-1 and negates (zeta-1)/(zeta+1), so their squares lie in F_p. This proves complete prime-field splitness even when d is much smaller than p.

Indeed, putting X=s^2, one has 2s G_{a^2}(X)=(a+s)^e-(a-s)^e; solving gives the displayed roots. No Euler simplification requiring e=(p+1)/2 was used.

This is a genuine candidate family for the line-only criterion in LINE_ONLY_GATE.md. However, splitness alone is insufficient: the roots of many locators must lie in one core of O(d) points, and the padding evaluation vectors must be scalar multiples.

## Exact scalar-residue condition and what transformations preserve

For distinct parameters u_i and padding coordinates x_j, let M_ij=G_{u_i}(x_j). The scalar-residue requirement is exactly that M has rank one and no zero entries. The scalar outputs obtained must also be distinct if they are to count as distinct line labels.

The matrix factors as

    M = (u_i^(d-h))_{i,h=0..d}
        diag(binom(e,2h+1))
        (x_j^h)_{h=0..d,j}.

All diagonal entries are nonzero because p>e. Vandermonde ranks and Sylvester's inequality give

    rank(M) >= min(L,d+1)+min(q,d+1)-(d+1).

Consequently rank one requires min(L,d+1)+min(q,d+1)<=d+2. In particular q>=2 implies L<=d; when both sizes are at most d+1, L+q<=d+2.

A fixed Mobius change of evaluation coordinate transforms locators by a common denominator to degree d and individual nonzero normalizations. On domains avoiding its pole these are nonzero row and column scalings, so evaluation rank and root-set cardinalities are unchanged. Selecting a coefficient fiber restricts u to roots of one equation c u^h=b; it cannot increase the number of labels. These observations do not cover a different Mobius map for each locator.

## The decisive common-core theorem

**Claim.** Suppose d tends to infinity and p/d tends to infinity in the split family above. For every fixed C, a set E of at most C d field elements can contain at most 2C distinct root translates uR for all sufficiently large d. In particular, the family cannot supply an unbounded bank on a constant-rate common core at arbitrarily large alphabet/core ratio.

The proof uses Corvaja--Zannier, *Greatest common divisors of u-1, v-1 in positive characteristic and rational points on curves over finite fields*, JEMS 15 (2013), Theorem 2, PDF page 3:
https://ems.press/content/serial-article-files/31918

Their theorem bounds common 1-points of multiplicatively independent rational functions with nonzero differentials by

    max{3 (2 deg(U) deg(V) chi)^(1/3), 12 deg(U) deg(V)/p},

where chi is the Euler characteristic after deleting all zeros and poles. We apply it over the algebraic closure; this avoids any issue about the square root of a translate ratio.

For c!=1, choose a with a^2=c. Then a!=0,+1,-1. Define phi(t)=(t-1)/(t+1) and the Mobius map

    M_a(t)=phi^-1(a phi(t))
          =((1+a)t+1-a)/((1-a)t+1+a).

Each x in R intersect cR has exactly two preimages t in mu_e with M_a(t) in mu_e. Inversion t->t^-1 gives the second preimage. The forbidden points t=1,-1 and zeros/poles cannot occur: x!=0 and e is odd.

Apply the theorem to U=t^e and V=M_a(t)^e on the projective line. Their zero/pole sets consist of four distinct points, so chi=2. They are multiplicatively independent modulo constants since M_a has its zero and pole away from 0 and infinity. Their differentials are nonzero since p does not divide e. Both degrees equal e. We obtain

    |R intersect cR| <= M,
    M=max{ (3/2)(4e^2)^(1/3), 6e^2/p }.                 (1)

Now let L distinct translates u_iR lie in E. Each has d elements and every two overlap in at most M points. If r_x is the number of translates containing x, Cauchy--Schwarz gives

    (Ld)^2 <= |E| sum_x r_x^2
            <= |E| [Ld+L(L-1)M].

Thus

    |E| >= Ld^2/[d+(L-1)M].                            (2)

Since e=2d+1, equation (1) yields M/d=O(d^(-1/3)+d/p), which tends to zero in the specified regime. For |E|<=Cd and M/d<=1/(2C), (2) implies L<=2C. This proves the claim.

This is an obstruction to THIS scaled Dickson family, not to all split polynomial families. It remains true after a fixed Mobius transformation of the common domain.

## The subgroup special case and exact finite certificates

If R lies in a coset of a multiplicative subgroup of size N, then R is the full root set of G_1 and G_1 divides X^N-c for some c. Equivalently all nonconstant coefficients of the integer remainder of X^N modulo G_1 vanish modulo p. This gives a complete finite prime test: p must divide their gcd.

The script cyclotomic/check_subgroup_remainders.py tests precisely e=5,7,11,13,17,19 and N=2d,3d,4d. It factors each exact gcd, checks N|p-1 and e|p-1 or p+1, and checks roots for the surviving small primes. Among these 18 shapes all valid primes have p/N at most 19/6. This is a finite certificate for these shapes, not an asymptotic classification.

There is also a direct general bound: use U=t^e and V=c^-1 phi(t)^(2N), whose degrees are e,2N and whose chi equals 2. All e-1 nontrivial e-th roots are common 1-points. Hence

    e-1 <= max{6(eN)^(1/3), 24eN/p}.

For N=O(e), e tending to infinity, the first term is o(e), so p<=(24+o(1))N. The finite certificates agree with this analytic obstruction. The stronger arbitrary-core theorem above removes the subgroup assumption entirely.

## Agreement scope and the remaining positive target

As independently pointed out by the audit agent, the split locator bank by itself only supplies d agreements for dimension d via candidates G_u-X^d. It is on the capacity boundary. A fixed-gap ordinary-common-agreement amplifier additionally requires an agreement surplus or the scalar-residue padding condition. The full-characteristic Dickson example gets its surplus from a separate Euler-character identity; that identity was not recovered for small e.

The attempted positive mechanism therefore stops here: one-parameter scaled Dickson roots cannot simultaneously give a growing bank, an O(d) core, and p/d tending to infinity. Continuing numerical subgroup searches would ignore a proved obstruction.

An escape would need locators whose roots are not translates of one fixed rational image of a cyclic group, or parameter-dependent transforms with genuinely shared core geometry. No such identity has been constructed in this exploration. The LC condition remains a valid precise target; this note neither proves it impossible nor supplies it.
