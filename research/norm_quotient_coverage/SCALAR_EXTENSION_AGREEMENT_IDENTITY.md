# Exact agreement identity for a base-field pencil after scalar extension

The length-48 prime-field certificate does not gain new nearby labels by
embedding its domain and words into a larger field. For every extension
E/F65537 and every lambda outside F65537, its exact agreement remains 25,
below the nearby threshold 27. This is an identity for arbitrary linear
codes under scalar extension, rather than a restriction on the canonical
subset-product witnesses.

## General lemma

Let F be a field, let E/F be a finite field extension, let D be a finite
coordinate set, and let C be an F-linear code in F^D. Its scalar extension is

    C_E=span_E(C) subset E^D.

For w in E^D, define

    agr_(C_E)(w)=max_{c in C_E} |{x in D:w(x)=c(x)}|.

For f,g in F^D, define the base-field common agreement

    CA_C(f,g)=max_{c_f,c_g in C}
       |{x in D:f(x)=c_f(x) and g(x)=c_g(x)}|.

Then:

1. Every base-field word w in F^D satisfies

       agr_(C_E)(w)=agr_C(w).

2. The common agreement of two base-field words is unchanged:

       CA_(C_E)(f,g)=CA_C(f,g).

3. For every lambda in E\F,

       agr_(C_E)(f+lambda*g)=CA_C(f,g).             (1)

These statements concern the maximum over all extension-field
codewords, so arbitrary witnesses cannot evade them.

### Proof

Because 1 and lambda are F-linearly independent, there are F-linear
maps pi_0,pi_1:E->F with

    pi_0(1)=1, pi_0(lambda)=0,
    pi_1(1)=0, pi_1(lambda)=1.

For instance, extend {1,lambda} to an F-basis of E and take the two
coordinate maps. Coordinatewise application of either map sends C_E
into C: if h=sum_i alpha_i c_i with c_i in C, then
pi_j(h)=sum_i pi_j(alpha_i)c_i belongs to C.

If f+lambda*g agrees with h in C_E on a set S, applying pi_0 and pi_1
shows that f agrees with pi_0(h) on S and g agrees with pi_1(h) on S.
Therefore |S|<=CA_C(f,g), proving the upper bound in(1).

Conversely, choose base-code witnesses c_f,c_g attaining CA_C(f,g),
and form h=c_f+lambda*c_g in C_E. At every coordinate,

    f+lambda*g-h=(f-c_f)+lambda*(g-c_g).

Both parenthesized quantities lie in F. Since 1,lambda are independent,
the expression vanishes exactly when both do. Hence h has precisely
the common agreement set, proving equality in(1).

For the first statement, use any F-linear pi:E->F with pi(1)=1.
Projecting an extension-code witness gives a base-code witness on all
its matching coordinates. Inclusion C subset C_E gives the opposite
inequality. Projecting each witness separately proves the corresponding
common-agreement statement. No interpolation threshold is needed.

## Reed–Solomon degree convention

Suppose D is a set of distinct elements of F and

    C=RS_F[D,J]={ (h(x))_(x in D): h in F[X], deg h<J }.

Then C_E=RS_E[D,J], because every E-coefficient polynomial of degree<J
can be expanded coefficientwise in an F-basis. Moreover the projections
above commute with evaluation at x in F and preserve the strict degree
bound J. Thus(1) applies to all E-polynomial witnesses of degree at most
J-1. It does not assume that the extension-field witness itself has
base-field coefficients.

The base-field location of D, or more generally the scalar-extension
description of the code, is part of the hypothesis. Arbitrarily moving
the evaluation points to E is a different code.

## Exact profile of the length-48 certificate

Use the saved domain and words from `below_elias_prime_fixture/README.md`:

    F=F65537, |D|=48, J=24,
    Y=X^2, R=X-1,
    f=R*(Y^13-3^13)/(Y-3),
    g=-R/(Y-3).

They are F-valued on D subset F. The verified base-field profile is

    agr_C(f)=agr_C(g)=CA_C(f,g)=25,
    agr_C(f+lambda*g)=27 for every lambda in F*.

After scalar extension to E=F_(65537^d), the complete pencil profile is

    agr_(C_E)(f+lambda*g)
      =27, if lambda in F65537*,
      =25, if lambda=0 or lambda outside F65537.

The projective direction g also has agreement 25. The explicit common
witnesses in the finite certificate combine as c_f+lambda*c_g to attain
25 for every outside-field label. The lemma excludes every possible
extension-field witness with more than 25 matches there.

Thus the nearby pencil labels are exactly the same 65536 base-field
labels, regardless of d. If a label is uniform on all of E, the exact
nearby fraction is

    65536 / 65537^d.

If it is uniform on E*, the fraction is 65536/(65537^d-1).

| Extension degree d | Field size | Nearby pencil labels |
| ---: | ---: | ---: |
| 3 | 281487861809153 | 65536 |
| 4 | 18447869999386460161 | 65536 |
| 5 | 1209018056149790439571457 | 65536 |
| 6 | 79235416345888816038194577409 | 65536 |

On the affine interpolation line (1-t)f+t*g, precisely the 65535
parameters in F65537\{0,1} have agreement 27. Both endpoints and every
parameter outside F65537 have agreement 25. For t!=1 this follows by
scaling and substituting lambda=t/(1-t); that fractional linear map
sends outside-field parameters to outside-field parameters.

This is the precise obstruction to treating the prime-field example as
an example with almost every extension-field challenge nearby. A pencil
defined over a proper subfield, with common agreement below the nearby
threshold, can have no qualifying labels outside that subfield after
scalar extension. The lemma leaves constructions whose source words
genuinely use extension-field values as a separate question.
