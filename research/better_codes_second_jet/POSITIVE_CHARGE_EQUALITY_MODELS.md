# Equality in the positive R-degree contact charge

## Conclusion

Equality epsilon(F)=r(w-1), with n>2w, does not in general force a graph factor, even in characteristic zero and even for an irreducible polynomial. Two exact counterexamples distinguish the higher-R-degree obstruction from a separate Frobenius obstruction. No benchmark improvement follows.

The universal proof does force the leading coefficient B=[Y^q R^r]F to be constant, the weight to be qw+r(w-1), and every contact to equal q. Those consequences are valid but do not determine the lower R-coefficients.

## 1. An irreducible equality carrier with no graph factor, in any characteristic

Let n distinct nodes have squarefree locator Lambda. Choose r>=2 and w>=2 with

    2w<n<=w+r(w-1).

For the zero received word define

    F(X,Y,R)=Y*R^r+Lambda(X).

Its exact R-degree is r, its leading R-coefficient has Y-degree q=1 and constant leading coefficient, and its weighted degree is w+r(w-1). At each node x,

    F(x+t,tR+t^2 E,R)
      =t R^(r+1)+t^2 E R^r+Lambda(x+t)

has exact contact one. The order-one coefficient R^(r+1)+Lambda'(x) is nonzero. Therefore

    epsilon(F)=r(w-1).

Over k[X,R], F is primitive as a linear polynomial in Y because gcd(R^r,Lambda)=1. It is irreducible over the fraction field and hence in k[X,Y,R]. In particular Y does not divide F. The concrete choice w=3,n=7,r=2 works in characteristic zero or any field containing seven distinct nodes, and may be taken in arbitrarily large prime characteristic.

This is an exact obstruction to a claimed general-r factorization (Y-P)^q H(R-P'). The top coefficient still correctly extracts P=0; the locator term fits in the lower-R weight budget. It is not a construction of many actual polynomial solutions or of a retained benchmark source.

## 2. The exact contact-one normal form explains the escape

Suppose q=1 and equality holds. The top homogeneous jet piece is c Y R^r: any term of the same total jet degree with smaller R-degree would have excessive weight. The coefficient of t^0 R^r in the contact identity gives c r_x+C(x)=0, where C=[Y^0 R^r]F and deg C<=w. Hence P=-C/c has degree at most w and matches the word.

Apply the jet translation Y->Y+P(X), R->R+P'(X). It preserves the weighted caps and contact, and makes the word zero. Contact at least one is now exactly the assertion

    F(X,0,R) is coefficientwise divisible by Lambda(X).

Consequently the normalized polynomial has the precise form

    F=Y H+Lambda J,
    wt(H)<=V-w,  wt(J)<=V-n,

with the corresponding inherited R-degree bounds. This is an ordinary polynomial decomposition obtained by separating the Y-constant coefficient; it is not a localized ideal assertion.

For r=1, V=2w-1<n, so J=0 and the graph factor is forced. For r>=2, J can be nonzero, as the preceding irreducible model demonstrates. Thus the absence or presence of locator room, rather than equality in the scalar charge alone, controls this particular escape.

## 3. A distinct characteristic-two obstruction already at r=1

Take k containing F_8, domain F_8, n=8,w=3, and received word r_x=x^4. Let

    F=R*(Y^2-X)+Y+X^4.

It has r=1,q=2 and weighted degree8. In characteristic two, x^8=x at domain nodes, and direct substitution yields

    F(x+t,x^4+tR+t^2 E,R)
       =t^2*(R^3+E)+t^4*(R E^2+1).

Thus all contacts are exactly two and epsilon(F)=8-3*2=2=r(w-1). The two coefficients of this linear polynomial in R are coprime: a common factor of Y^2-X and Y+X^4 would force the nonzero polynomial X^8-X to vanish identically. Hence F is primitive linear in R and irreducible.

The word has no degree-at-most-three polynomial interpolant: such a polynomial would differ from X^4 in degree at most four and vanish at eight nodes. Thus even extraction of a low-degree graph from equality fails here. This does not contradict all-characteristic ZERO-charge rigidity: the present charge is positive.

The same construction works on F_n in characteristic two for n a power of two, replacing X^4 by X^(n/2), whenever n>2w and n/2<=3w-1. Its contact remains exactly two and its weight is3w-1. No finite search is used.

## 4. Implication for the next proof target

Any near-equality theorem for general r must retain the lower-R locator terms or impose an additional restriction eliminating them. For first contact this restriction is exactly V<n. For larger contact, a useful theorem would describe the filtered first-jet contact ideal with its weighted caps, not infer divisibility by a graph from the scalar equality alone.

These examples do not assert universal primary-kernel divisibility, a compatible second-jet retained source, or a large selected bank. Those additional hypotheses remain possible sources of a genuine routing improvement.
