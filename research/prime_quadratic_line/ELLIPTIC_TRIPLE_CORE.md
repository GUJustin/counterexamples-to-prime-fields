# An algebraic elliptic triple core

Status: independent audit PASS. Manuscript input fragment: `elliptic_triple_core.tex`.

This is a concrete constant improvement of the quadratic-bank padding construction. It does not yet give growing source separation or a growing bucket size.

Let ell>=53 be prime. On any nonsingular elliptic curve E over Q, choose a point P of order ell over the algebraic closure, and let H=<P>. Use the B=ell-1 points H\{O}. Retain exactly the lines through three distinct nonzero points whose group sum is O.

For a fixed nonzero point R, potential second points S range over H\{O,R}. Exclude S=-R (third point O), S=-2R (third point R), and S=-R/2 (third point S). These three exclusions are distinct because ell>3. The remaining ell-5=B-4 choices occur in pairs, so R lies on exactly (B-4)/2 retained lines. There are B(B-4)/6 retained lines. A retained line contains exactly three of the bank points, by Bezout with the nonsingular plane cubic.

## Distinct slopes are achievable

Choose a projective line at infinity avoiding the finitely many bank points and all intersections of two retained lines. Choose horizontal and vertical direction points on it avoiding every retained line. A rational projective coordinate change accomplishing this exists: the forbidden conditions form a finite union of proper algebraic closed sets, and rational matrices are Zariski dense. In the resulting affine plane the retained lines have pairwise distinct finite nonzero slopes. Write the bank points as (a_i,b_i) and form quadratics

    P_i(T)=a_i T²+b_i.

A retained parameter line b=m a+c gives two evaluation nodes T=±sqrt(-m), with received value c. Adjoin these square roots to the number field. Distinct nonzero slopes give distinct nonzero nodes, and each has exactly three matching bank quadratics.

Thus the core parameters are

    N0=B(B-4)/3,   A=B-4,

with uniform agreement A for all B bank members. Any other quadratic has at most floor(2B/3) core matches: its differences with the B bank quadratics contribute at most 2B roots, while each core match is counted three times.

## Padding and exact threshold classification

Put

    T=A+1=B-3,
    n=(T²+1)/2,
    t=n-N0=(B²-10B+30)/6.

On t fresh coordinates use f=x⁴,g=x³, with g=0 on the core. Choose the fresh points so all Bt labels (P_i(x)-x⁴)/x³ are distinct and outside {0,1}. The same finite-field greedy argument applies, now avoiding ALL pairwise bank intersections, including the omitted tangent/two-point secants. There are at most B(B-1) such evaluation coordinates. A prime larger than 5B^4, as well as the finite bad-reduction exclusions, suffices.

A nonbank quadratic has at most floor(2B/3)+4<=B-4=A total matches for every label, since B>=52. Every bank polynomial has A core matches and gains exactly one fresh point at its designated labels. The invertible source change F=f,G=f+g makes both source agreements and common agreement equal A. It yields exactly

    M=B*t+1=(B³-10B²+30B)/6+1

exceptional labels at threshold T, all with singleton qualifying lists; the additional label is the unique direction point, with zero as its witness. All other labels have nearest agreement A.

Since T²=2n-1, the threshold is below Johnson. The same low-rate estimate used for the pair-core construction gives above-first-order agreement for T>=49, hence ell>=53. As B grows,

    M/n^(3/2) -> sqrt(2)/3.

This is a factor 4/3 above the pair-core construction's leading constant 1/(2sqrt(2)). It does not change the exponent 3/2 or the one-coordinate source gap.

## Prime-field realization

All bank coordinates, retained slopes, and evaluation square roots belong to one number field. Pass to its finite Galois closure and discard the finitely many primes at which a needed denominator or nonzero difference vanishes. At every remaining completely split prime, reduction gives the stated configuration in the prime field. There are infinitely many such primes, and they can exceed the greedy padding bound. Unlike the original rational pair core, this argument does not give the construction over EVERY sufficiently large prime or an effective small field bound.

## Scope for growing multiplicity

The construction avoids bounded rational torsion by allowing algebraic torsion points and then splitting primes. Its three-point collinearity closure uses the elliptic group law exactly. Embedding an elliptic curve as a higher-degree plane curve does not automatically replace triples by b-tuples: a three-dimensional linear subsystem of a larger divisor space does not contain every divisor whose group sum is fixed. No growing-bucket analogue is established here.
