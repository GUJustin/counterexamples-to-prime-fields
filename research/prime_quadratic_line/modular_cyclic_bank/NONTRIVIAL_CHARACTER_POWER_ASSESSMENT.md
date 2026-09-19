# Nontrivial character powers: precise remaining construction problem

2026-09-19. This assesses an unclosed route; it supplies no new construction.

Let n=hr divide p−1, h,r>=2, chi(x)=x^h on D=mu_n, and consider
w(x)=x chi(x)^k, with gcd(k,r)=1 and k not congruent to ±1 modulo r.
For abc!=0, agreement with P=aX²+bX+c is exactly

    R(x)=a x+b+c/x=chi(x)^k.

The fiber argument still gives T<=r+gcd(2,r), independently of k:
on chi(x)=zeta the quadratic is aX²+(b−zeta^k)X+c; two roots require
zeta²=(c/a)^h. The degree bound is now kh+1 for 1<=k<r, which does
not generally imply sqrt(n)+O(1). Thus this is a logical escape from
the current adjacent-exponent theorem, not evidence of its attainability.

## Exact missing mechanism

Any agreeing point is a root of P(X)^r−X^r, of degree 2r. But splitting
this polynomial in D is not enough. For each eta in mu_r, roots of
R(x)=eta come in the pair x and c/(a x), when both are distinct and
exist. Agreement requires the further alignment chi(x)=eta^(k^−1),
where k^−1 is taken modulo r. Except for at most gcd(2,r) character
fibers, at most one root of a pair can satisfy this alignment. A large
bank therefore needs simultaneous prescribed character values across
many different quadratic fibers. No identity currently forces them.

For T>=c0 sqrt(n) with c0>1, the fiber bound forces r/h>=c0²−o(1).
A multiplicative orbit of a full-coefficient quadratic has exactly n
members: its three coefficient characters have consecutive exponents,
so their stabilizers intersect trivially. The orbit would distribute T
incidences per coordinate. This orbit fact supplies a bank once a rich
seed exists; it does not supply the rich seed or any nonbank separation.

## A non-obvious narrowing of the first candidate family

For k=2 one needs r odd. The elementary bounds permit their best scale
near r=2h, but the two nearest odd choices are already closed:

- If r=2h+1, m=2h+1=r.
- If r=2h−1, m=2h+1=r+2.

Swap the factors h and r in n=hr. These exponents are then exactly the
adjacent-divisor cases covered by the new theorem. Thus those apparent
near-Johnson families have T<=sqrt(n)+2 as well. The next offsets,
such as r=2h±3, are not automatically covered by that theorem. There
is no coefficient identity or successful example presently attached
to those offsets, so they do not justify a large prime sweep.

## Existing finite evidence and proximity requirements

A replay of the existing 698 profiles found only two nontrivial-power
instances with full-coefficient A>sqrt(n): (p,n,m,h,r,k) equal to
(17,16,7,2,8,3) and (17,16,11,2,8,5). Both have A=5, maximizer list
16, and outside-bank maximum 4. They are existing small seeds, not
new results. Neither offers the nonbank slack required by the current
quartic-padding route, whose recorded gate asks A−B>=4. A large ordinary
bank alone would also not establish a proximity-gap counterexample:
source and common agreement still require separate control.

The useful next step is an explicit algebraic family enforcing the
character alignment R(x)=chi(x)^k on many fibers, together with a
codewide nonbank cap. Enlarging the existing census without such a
mechanism would only repeat an unmotivated search.
