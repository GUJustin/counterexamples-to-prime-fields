# Binary-affine locator fibers in odd characteristic

September 16, 2026. Proof self-reviewed twice, with passing exhaustive finite checks and
sharpness examples. No independent review or novelty claim.

## Statement

Let D={alpha_1,...,alpha_n} be distinct elements of a field of characteristic
other than two. Suppose a binary-affine subspace C=b+V of {0,1}^n has
binary dimension r. Interpret each word as a subset of D. Assume every
subset has exactly t elements and its monic degree-t locator polynomial
has the same first s coefficients below the leading coefficient, where
0<=s<t. Then

    r <= floor(min(t,n-t)/(s+1)),
    |C| <= 2^floor(min(t,n-t)/(s+1)).                  (1)

The characteristic need not exceed n or s. This is a statement about
locator prefixes, not merely power sums when Newton identities cannot
be inverted. At a fixed gap s/n>0, this bounds the entire affine binary
family by a constant independent of n.

## Proof by multiplicative character extraction

Parameterize the family injectively by u in F_2^r, writing its j-th
indicator as

    x_j(u)=b_j+<a_j,u> mod 2,

with a_j in F_2^r. The nonzero column labels a_j span F_2^r because the
parameterization is injective. Let epsilon_j=(-1)^b_j. For a nonzero
label a, let C_a^+ and C_a^- be the coordinate sets with a_j=a and
with b_j=0 and b_j=1, respectively.

Every word has integer weight t. Expanding this weight in the ordinary
real-valued characters chi_a(u)=(-1)^<a,u> shows that
|C_a^+|=|C_a^-| for each nonzero a. Write their common size as h_a.
In every word exactly h_a coordinates of their union are selected.
Consequently, if c nonzero labels occur, then

    t >= sum_a h_a,    n-t >= sum_a h_a,    r<=c.

It remains to show h_a>=s+1 for every occurring label.

Let L_u(X) be the locator of the subset at u, and let L_0 be one reference
locator. Equality of the first s coefficients says, in the Laurent series
field at infinity,

    L_u/L_0 = 1+O(X^(-s-1)).

For a fixed nonzero a form the rational function

    product_u L_u(X)^(chi_a(u)).

The sum of the characters is zero, so this equals a product of ratios
L_u/L_0 and is 1+O(X^(-s-1)). On the other hand, the exponent of X-alpha_j
in this product is the integer

    sum_u chi_a(u)x_j(u) = -epsilon_j * 2^(r-1)

when a_j=a, and zero otherwise. If F_a^+, F_a^- are the monic locators
of C_a^+, C_a^-, this proves

    (F_a^-/F_a^+)^(2^(r-1)) = 1+O(X^(-s-1)).

Both polynomials have degree h_a, so their ratio has leading term one.
Since the characteristic differs from two, raising this ratio to the
power 2^(r-1) preserves
the order of its first nonzero Laurent coefficient. Therefore

    F_a^-/F_a^+ = 1+O(X^(-s-1)).

The two disjoint root sets give different monic polynomials. Their
nonzero difference has degree at most h_a-s-1, forcing h_a>=s+1.
Summing over the c occurring nonzero labels and using r<=c proves (1).
The case r=0 is immediate and does not require the character product.

## Sharpness over suitable odd prime fields

Put B=s+1. Choose an odd prime with sufficiently many distinct full
fibers of X^B. Use r disjoint pairs of B-element fibers. In each pair
choose exactly one fiber, independently, and optionally add fixed
selected and unselected coordinates.

Each fiber locator is X^B-c, so the varying product has no changes in
its first B-1=s coefficients. Multiplication by the common fixed locator
preserves this prefix. This is an affine binary family of dimension r
with t>=rB and n-t>=rB. Choosing the fixed coordinates appropriately
attains (1) whenever the desired r=floor(min(t,n-t)/B) is used.
Suitable primes p=1 mod B can be arbitrarily large; for B=1 any large
odd prime suffices. The field and evaluation domain are not prescribed.

## Consequences for the existing finite examples

* At (n,t,s)=(64,34,2), every affine binary subfamily has dimension <=10
  and at most 1024 members. The certified integer locator fiber has more
  than 5.55e12 members, so the large fiber is necessarily highly nonlinear
  as a subset of the Boolean cube.
* At (157,68,5), the corresponding bound is dimension <=11 and size <=2048,
  far below the certified integer class of more than 2.81e19 members.
* For the 511-variable-packet seed with 272 selected packets and 14 fixed
  leading coefficients, every affine binary subfamily has dimension <=15
  and size <=32768. This cannot by itself supply the incumbent bank size.

Thus XOR-linear support families and independent binary choices cannot
supply an unbounded fixed-gap list in odd characteristic. This does not
exclude nonlinear binary families, or transfers of other ideas from the
binary-field constructions. The existing Prouhet block construction is
one allowed but small example.

## Why characteristic two differs

In characteristic two the exponent 2^(r-1) can raise Laurent vanishing
orders; the crucial implication in the proof fails. A concrete violation
uses D=F_16 and the supports

    {x : Tr_{F_16/F_2}(a*x)=1},

where a ranges over an affine binary hyperplane of F_16 not containing
zero. This is a dimension-three affine binary family of 8-element subsets
on 16 points. Each locator is a normalized trace polynomial plus a
constant, with only degrees 8,4,2,1,0. Their first three coefficients
below degree eight are all zero. Hence (n,t,s,r)=(16,8,3,3), whereas
(1) would give r<=2.

This example concerns indicator-affine support structure. It makes no
claim that all binary-field counterexample constructions are of this form.


## Exact checks

`verify.py` enumerates 103,416 small affine binary
spaces over evaluation domains in F_7, F_101, and F_9. All 8,407
constant-weight families satisfy the bound and the extracted per-character
locator-prefix conditions. One F_9 example has prefix length three,
checking the case where odd characteristic is not greater than the prefix.
Twenty prime-field fiber examples attain the dimension bound. The F_16
trace family explicitly violates its odd-characteristic conclusion.
These checks supplement the written argument.
