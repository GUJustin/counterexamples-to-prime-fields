# Rich lists in an affine coefficient plane at large characteristic

September 19, 2026. A consequence of the existing Stevens--de Zeeuw
point-line bound, not a new incidence theorem or a positive construction.

Provenance: the September 18 [prime direct-list assessment](../binary_characteristic_transfer/quadratic_frobenius_core/PRIME_DIRECT_LIST_NEXT_GATE.md) already proves that a fixed affine quadratic coefficient plane over a prime field cannot contain a linear-sized bank with square-root agreement. This note gives the quantitative rich-list bound O_delta(n^(7/8)) and states its extension to any field of characteristic zero or characteristic p>=n. The central prime-field fixed-plane obstruction is the earlier result.

## Statement

For each fixed delta>0 there are constants C_delta and n_delta such
that the following holds. Let F be any field of characteristic zero, or
of prime characteristic p with n<=p. Let n>=n_delta, and let w be any
word on n distinct elements of F. Inside ANY affine plane of the
three-dimensional space F[X]_{<=2}, at most C_delta n^(7/8)
polynomials agree with w on at least delta sqrt(n) coordinates.
The constants do not depend on the plane, word, domain, or prime.
A line or point of coefficient space is covered by extending it to a
plane. The large-n qualification is necessary: one or two matches alone
do not give a field-independent list bound.

## Proof

Write the plane as H0+a H1+b H2 with H1,H2 linearly independent
polynomials of degree at most two. Remove the at most two coordinates
where H2 vanishes. At every remaining coordinate x form

    y_x=H1(x)/H2(x), z_x=(w(x)-H0(x))/H2(x).

Agreement with H0+a H1+b H2 is exactly incidence of (y_x,z_x) with
Z=aY+b. Distinct polynomials give distinct lines. For a fixed y, the
polynomial H1-y H2 is nonzero of degree at most two. Consequently
every projected point has multiplicity at most two. Keeping one copy
of each point leaves each qualifying line with at least
(delta sqrt(n)-2)/2 incidences. For sufficiently large n this is at
least delta sqrt(n)/4.

Pad the projected point set to exactly n distinct points of F^2;
this is possible since F contains the n original domain coordinates. Padding only increases incidences. Let K
be the number of qualifying lines. Theorem 3 of Stevens--de Zeeuw,
*An Improved Point-Line Incidence Bound Over Arbitrary Fields*,
https://arxiv.org/pdf/1609.06284 (v4, page 2), gives

    I << n^(11/15) K^(11/15)

when n^(7/8)<K<n^(8/7) and n^(-2)K^13 << p^15.
If K>=n, apply the theorem to any n of the lines: the lower bound is
(delta/4)n^(3/2), while the upper bound is O(n^(22/15)). This is
impossible once n is sufficiently large in terms of delta. Its
positive-characteristic condition follows from n^11<=p^11=o(p^15);
in characteristic zero no such condition is needed.
Thus K<n. If K<=n^(7/8) there is nothing to prove. Otherwise apply the
same theorem to all K lines (the characteristic expression is again
at most n^11 in positive characteristic). Rearranging gives

    K^(4/15) <<_delta n^(11/15-1/2)=n^(7/30),
    K <<_delta n^(7/8).

This proves the statement. Both the domain folding multiplicity and
the removed denominator zeros have been accounted for.

## Consequence for transferring the norm-one bank

The norm-one nearest bank lies in the coefficient plane spanned by
1 and X^2. Its length-N word has N/2 distinct witnesses, each with
Theta(sqrt(N)) matches. The theorem rules out realizing this same
population and agreement scale over PRIME alphabets while preserving
an affine coefficient plane. It also rules out retaining a constant
fraction of that population on a domain of comparable length with
a constant fraction of the agreements.

Common translation/scaling of all message polynomials and a Mobius
coordinate substitution with its degree-two GRS multiplier act by
invertible affine maps on quadratic coefficient space. They preserve
its affine dimension. Even if such a map is initially defined over an
extension, an image bank of prime-field polynomials with affine span
at most two over that extension has affine span at most two over F_p:
rank of a matrix with F_p entries is unchanged by scalar extension.
Thus these operations cannot transfer the full norm-one bank into a
prime-field example with the same asymptotic list parameters.

This is a geometric obstruction to a specified transfer. It is NOT a
bound on the complete list in the three-dimensional quadratic space,
not an obstruction to every prime-field construction, and not a bound
on received-line exceptional labels. In particular it leaves open
banks that spread through coefficient space, or smaller banks that
could still yield a superlinear line count by a different mechanism.
The original extension-field construction evades the proof's characteristic
condition: its length is of order p^2 rather than at most p. Increasing
ambient extension degree alone does not evade this obstruction on a
short domain n<=p. Thus the same asymptotic plane-list restriction also
applies to the short-domain regime over extensions of large practical
primes. The unspecified incidence constant and onset give no numerical
list bound or security-bit estimate for a particular deployed parameter.

The central distinction is therefore domain length relative to
characteristic, together with the plane restriction on witnesses, not
simply prime versus extension alphabet. No claim is made for unrestricted
three-dimensional quadratic banks.
