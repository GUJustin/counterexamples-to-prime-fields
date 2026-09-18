# Exact gate for the suggested monomials X^(p+r)

This addresses the concrete full-quadratic-core target, not arbitrary received words. Let B=F_(p²), p odd, and evaluate on B*. A quadratic with coefficients outside B has at most two matches with the B-valued word, by projecting onto an external coefficient coordinate. Write Q=aX²+bX+c over B.

## r=1: norm source

At a match X^(p+1)=Q, X^p=Q/X. Applying Frobenius again gives the necessary quartic identity at every match:

    E_Q=a^p Q²+b^p Q X+c^p X²−Q X²=0.

If E_Q is nonzero there are at most four matches. If E_Q is identically zero, its constant coefficient a^p c² vanishes.

* If c=0 and Q is nonzero, divide E_Q by X²(aX+b). The identity becomes a^p(aX+b)+b^p−X=0. Thus a^(p+1)=1 and a^p b+b^p=0. The original matches satisfy X^p=aX+b, the familiar affine F_p-line equation. These witnesses all have zero constant coefficient; their population is p(p+1).
* If a=0 and c≠0, the cubic coefficient forces b=0, and then c^p=c. These are constant norm values, with p+1 matches each for c∈F_p*.
* Q=0 has no matches on B*.

Thus the union of high-agreement families has only O(p²) witnesses and does not have the sought p³ population. The p² branch lies in a two-dimensional coefficient space. Adding the p-scale constant branch does not repair the population exponent.

## Every fixed r≥2: one polynomial elimination, no scan

At a match X^(p+r)=Q, applying Frobenius twice and clearing nonzero powers of X gives

    X Q^r = a^p X^(r²−2r) Q²
            + b^p X^(r²−r) Q + c^p X^(r²).

All exponents are nonnegative for r≥2. The difference has degree at most max(2r+1,r²). If it is nonzero, that bounds the match count independently of p. The identity branches are completely determined by its extreme coefficients:

* r=2: the degree-five term forces a=0; then the degree-four term forces c=0. The remaining identity is b^(p−1)=1. Thus Q=bX, b∈F_p*, and matches are the p+1 points of X^(p+1)=b.
* r=3: the degree-nine term forces c=0. For nonzero Q, divide by X⁴(aX+b). The identity is (aX+b)²=a^p X(aX+b)+b^p X³. Its cubic term forces b=0, and then a∈F_p*. Thus Q=aX², again a p-scale norm-circle family.
* r≥4: the highest-degree term forces c=0. If b≠0, the left side has valuation r+1, whereas every nonzero right-side term has valuation at least r²−2r+2>r+1, impossible. If b=0 and a≠0, the two surviving monomials have exponents 2r+1 and r²−2r+4, unequal because their difference is (r−1)(r−3). Thus there is no nonzero identity branch. The identically zero Q has no matches.

These statements use only exact polynomial coefficients and valuations, not division by factorials or a numerical census. To exclude Θ(p) matches using the nonidentity degree bound, retain the stated scope: r is fixed (or r²=o(p)), and p is sufficiently large. They are not an obstruction when r grows on the sqrt(p) scale or faster.

## Consequence for the proposed construction

The immediate norm and fixed-shift Frobenius monomials do not yield a size-p² core with p³ full-quadratic witnesses having Θ(p) matches. The only growing identity families are affine-line fibers with a missing coefficient, or p-scale norm circles. This closes this specific suggested source family without a brute-force search. It does not rule out rational sources whose denominator produces a different elimination identity, an independently synchronized matrix construction, or r growing with p. No broader full-quadratic impossibility is claimed.
