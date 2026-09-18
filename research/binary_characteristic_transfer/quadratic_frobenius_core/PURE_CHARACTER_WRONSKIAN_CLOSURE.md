# Pure-character full-quadratic orbit: Wronskian closure

September 18, 2026. Exact symbolic argument, adapting the archived degree-m ideal/Wronskian method in `research/power_family_mca/PROOF.md`. No finite-field scan. Independent review PASS; see `PURE_CHARACTER_WRONSKIAN_INDEPENDENT_AUDIT.md`. This note supplies the complete argument rather than applying a characteristic-zero gcd theorem to a finite field.

## 1. Precise conclusion

Let n=hr divide p-1, with p prime, and let D=mu_n in Fp. For a,b,c all nonzero, let A count solutions of

    x^h = a x^2+b x+c,  x in D.

For h>=367,

    A <= sqrt(3n/2).

For h<367, A<=366, apart from the irrelevant h<=2 polynomial-identity cases (which cannot have abc all nonzero). Thus no growing-prime family in this full-coefficient pure-character subclass supplies A>sqrt(3n/2) with growing A. In particular it cannot reach an agreement strictly above the low-rate dimension-three first-order curve. This does not cover arbitrary monomial exponents that do not divide n, arbitrary received words, or general quadratic banks.

## 2. Exact paired-root reduction

The elementary bounds are A<=h and A<=2r, for h>=3. The first is the polynomial degree bound, the second counts the r values of x^h, each giving a quadratic equation.

Put K=-b/a, which is nonzero. In any character branch contributing two distinct roots, their sum is K. For each such root x, its companion K-x is nonzero, and

    z=x/(K-x) belongs to mu_h, z!=-1,
    x=Kz/(1+z).

Both x and its companion give distinct z-values. Substitution in the matching equation yields

    R(z)=q(z)(1+z)^(h-2)-K^h=0,
    q(Z)=c(1+Z)^2-aK^2 Z.

We have q(0)=c!=0 and q(-1)=aK^2!=0. If d_2 branches have two matches, A<=r+d_2. Therefore, writing

    k=deg gcd(Z^h-1,R(Z)),

we obtain 2d_2<=k and A<=r+k/2. There are no multiplicity assumptions here: Z^h-1 is squarefree since h<p.

## 3. A uniform small-support gcd lemma

For h>=367 and characteristic zero or p>4h, the polynomials in Section 2 satisfy

    k <= 4h/7+26.                                      (1)

Work over an algebraic closure. Homogenize to the degree-h binary forms

    F0=V^h,
    F1=U^h,
    F2=[c(U+V)^2-aK^2 UV](U+V)^(h-2).

Their root union S in P1 has at most five points: infinity, zero, -1, and the at most two roots of q. Their supports are pairwise disjoint, although q may have a repeated root. Choose a new affine coordinate whose infinity is outside S and outside the finite common-zero set of F1-F0 and F2-K^h F0. The transformed forms become degree-exactly-h polynomials; all their roots are finite. This invertible coordinate change preserves the common-zero count of F1-F0 and F2-K^h F0.

There are 15 homogeneous degree-four monomials in F0,F1,F2, each of degree 4h. Any ratio of two distinct monomials is nonconstant and has rational degree at least h-2. Indeed a change in the F1 exponent gives valuation of magnitude at least h at the original zero point; if that exponent is unchanged, the F2 exponent changes and gives valuation of magnitude at least h-2 at the original -1 point. Rational degree and these valuations are invariant under the coordinate change.

### Independence of the 15 monomials

Suppose a minimal constant linear relation has q<=15 terms. Any q-1 of those polynomials are linearly independent, hence have a nonzero ordinary Wronskian, since their degrees are at most 4h<p. In characteristic zero the same criterion is unconditional. Denote C_q=binom(q-1,2), and let G0 be their common polynomial gcd.

At a point of S, omit a term of smallest vanishing order from the Wronskian. Minimality implies that every such omitted-term Wronskian is a nonzero constant multiple of every other. Its order is at least the sum of the q vanishing orders minus their minimum minus C_q. Summing over S and comparing with the degree upper bound (q-1)4h-C_q gives

    4h-deg G0 <= (|S|-1) C_q <= 4 binom(14,2)=364.

But the rational degree of any ratio of two terms is at most 4h-deg G0 and at least h-2. This contradicts h-2>364. Hence all 15 monomials are independent.

### Ideal subspace and its Wronskian

In the polynomial ring in three formal variables, the homogeneous degree-four component of the ideal

    (Y1-Y0, Y2-K^h Y0)

has dimension 14: its quotient has dimension one in every degree. Evaluation at F0,F1,F2 is injective by the preceding independence. Let W be the nonzero Wronskian of a basis of the resulting 14-dimensional space. Thus

    deg W <= 14*4h-binom(14,2)=56h-91.                 (2)

At each s in S, the codimension-one subspace has a basis with sum of orders at least the sum of the 15 monomial orders minus their maximum. This follows by intersecting the subspace with the spans of monomials of order at least j, for every j; codimension one loses at most one dimension at each level. Cancellations can only improve this bound. A change of basis multiplies W by a nonzero constant, so this local estimate may be used separately at each point.

Over S the sum of all monomial orders is 15*4h=60h. The sum of the maximum monomial orders is 4*3h=12h: the three forms have disjoint root supports and total root degree 3h. Differentiation loses at most binom(14,2)=91 at each point. Consequently

    sum_(s in S) ord_s W >= 48h-5*91=48h-455.          (3)

Let T0 be the common-root polynomial of F1-F0 and F2-K^h F0. None of these common roots belongs to S: at a root of F0, F1 is nonzero; at a root of F1, F0 is nonzero; at a root of F2, K^h F0 is nonzero. Its degree is k. Every evaluated ideal element is divisible by T0. The elementary identity

    Wr(T0 f1,...,T0 f14)=T0^14 Wr(f1,...,f14)

therefore gives an additional 14k zeros of W outside S. Combining (2) and (3) gives

    14k <=8h+364,

which is (1). This proof accounts for repeated roots of q, uses no separability assertion for q, and has the explicit finite-characteristic requirement p>4h.

## 4. Apply the bound throughout the feasible ratio range

Write sigma=r/h. If sigma<=3/8, then 2r<=sqrt(3hr/2). If sigma>=2/3, then h<=sqrt(3hr/2). Thus the elementary bounds already suffice outside

    3/8 < sigma < 2/3.

Inside this interval and h>=367, p>n=hr>(3/8)h^2>4h, so the characteristic requirement in Section 3 is automatic. Equations (1) and Section 2 give

    A <= r+2h/7+13.

The concave function sqrt(3sigma/2)-sigma-2/7 has its minimum over [3/8,2/3] at an endpoint. Its endpoint values are 5/56 and 1/21, respectively. Therefore

    sqrt(3hr/2) - (r+2h/7+13) >= h/21-13 >0

at h>=367. This proves the claimed bound. For bounded h the elementary A<=h precludes the growing target. The proof also works over any field containing mu_n whenever p>4h in the feasible ratio range; the automatic characteristic check uses the prime-alphabet condition n|p-1.

## 5. Assessment

The proposed two-parameter high-gcd gate from `PRIME_DIRECT_LIST_NEXT_GATE.md` is now closed. In its example r/h=3/5, the required gcd degree 0.74h exceeds the proved upper bound 4h/7+26 for h>=367. More generally the entire full-coefficient pure-character family fails the target, not just that example.

This is an adaptation of a proof mechanism already archived locally, with a bounded quadratic factor allowed in the high power. It is not a reason to resume old monomial scans. The unclosed monomial scope is exponents m not dividing n and not in the already closed character-times-linear/reversed classes; no constructive identity in that remaining scope is supplied here. General prime-field three-dimensional quadratic banks remain outside this result.
