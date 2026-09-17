# A constant list throughout the first-order range for the quadratic indicator

September 17, 2026. A restricted-family upper bound, not a general
prime-field proximity-gap theorem and not a novelty claim.

**Theorem.** Let p=4k+1 be prime. On F_p*, put
w(x)=(1+x^(2k))/2. Every polynomial P of degree at most k with more than
5k/3 agreements with w is one of the six nearest polynomials classified
in README.md: 0, 1, and (X^k-u)/(v-u), where u^2=-1 and v^2=1.
The conclusion remains true over any extension coefficient field.
For degree strictly less than k, only the two constants occur.

Thus the list has size at most six at every agreement fraction greater
than 5/12. In particular it cannot grow anywhere above the quarter-rate
first-order threshold (3+sqrt(133))/31, which is greater than 5/12.
This concerns this particular word and full evaluation domain only.

**Corollary (the original Dickson word).** For every prime p=4k+1>5,
the word W(x)=(x^k-1)^2/2 on F_p* has maximum agreement at most
floor(5k/3) with degree-<k polynomials, including extension coefficients.
Indeed W=w-X^k. A candidate P exceeding the cutoff would give the
monic degree-k polynomial Q=P+X^k in the classified six-element list.
Its four nonconstant members have leading coefficient c with
4c^4+1=0; c=1 would force p=5. Thus no such candidate exists.
In particular the ENTIRE nearest-list problem for the original full-field
Dickson word stays below the first-order range, not merely its known
binomial candidate bank. This does not exclude puncturing, changing the
word, or using other evaluation domains.

## Proof

Constants other than 0 and 1 have no agreements. Suppose P is
nonconstant, of degree ell<=k, with A agreements. Let z and o count its
correct zeros on nonsquares and correct ones on squares, respectively.
Then z,o<=ell, A=z+o<=2ell<=2k. Put h=2k-A. The hypothesis gives
0<=h<k/3.

Let U,V be the monic locators of these two agreement sets. Write

    P=UR,       P-1=VS,
    X^(2k)+1=UC,     X^(2k)-1=VD.

Set a=RS and b=CS-DR. Subtracting the two identities after multiplying
by a gives

    Pb+DR=2a.

Here deg a=2ell-A<=h and deg(DR)=ell+h. Degree comparison gives
deg b<=h. Moreover b is nonzero: b=0 would imply D=2S, whereas
deg D=2k-o>ell-o=deg S. Substitution back into the first identity yields

    bP^2-(b+2a)P+a(X^(2k)+1)=0.                 (1)

Divide a,b by their polynomial gcd, preserving (1), and keep the names
a,b for this coprime pair. Write alpha=deg a, beta=deg b; both are at
most h. Define

    Y=2bP-b-2a,       E=b^2+4a^2.

Completing the square in (1) gives

    Y^2+4ab X^(2k)=E.                          (2)

Suppose first that E is nonzero. Its degree is at most 2h<2k.
Consequently Y is nonzero and

    deg Y = k+(alpha+beta)/2.

Coprimality of a,b and odd characteristic imply gcd(ab,E)=1.
Hence the common gcd of the three terms in (2) is a power of X.
If E has positive order v at zero, then ab has order zero there;
since v<=2h<2k, (2) implies v=ord_0(Y^2) is even. Write v=2t.
If E(0) is nonzero, set t=0. Dividing (2) by X^(2t) produces the
pairwise coprime, nonzero identity

    (Y/X^t)^2 + 4ab X^(2k-2t) = E/X^(2t).    (3)

All three degrees are strictly less than p: before division they are
at most 2k+2h<4k+1=p. The polynomial abc inequality therefore applies.
The degree of the radical of the product in (3) is at most

    (deg Y-t)+alpha+beta+1+(deg E-2t).

Applying abc to the middle term gives

    2k+alpha+beta-2t
       <= deg Y+alpha+beta+deg E-3t,

and therefore

    k <= (alpha+beta)/2+deg E-t <= 3h.

This contradicts h<k/3.

For completeness, the needed abc inequality follows from a Wronskian.
For pairwise coprime nonzero F+G=H of degrees less than p, with at
least one nonconstant, F'G-FG' is nonzero. Otherwise coprimality forces
F'=G'=0, which in these degrees forces both to be constant. Each
repeated-root part of F,G,H divides this Wronskian. Degree comparison,
and its two cyclic versions, give max(deg F,deg G,deg H) at most the
degree of rad(FGH) minus one. In (3) the middle term is nonconstant.

It remains that E=0. In F_p, -1 has a square root i, so b=lambda a
with lambda=2i or -2i. Equation (2), after cancellation, becomes

    (2lambda P-lambda-2)^2=-4lambda X^(2k).

The polynomial on the left before squaring is a nonzero scalar
multiple of X^k (unique factorization). Thus P=cX^k+d. Such a
nonconstant polynomial is constant on each of the four quartic
cosets; each coset has size k. It can agree with the zero value on
at most one coset, and with the one value on at most one coset.
Since A>5k/3>k, it agrees on exactly two cosets and has A=2k.
The exact classification in README.md now gives the four stated
nonconstant candidates.

Finally, A>5k/3 implies A>=k+1, including k=1. Interpolation on k+1
base-field agreement points forces the coefficients into F_p even
if extension coefficients were initially allowed.

## Finite checks and scope

The proof uses p=4k+1 to make the Wronskian argument valid in positive
characteristic. Unlike the exact-nearest classification, this argument
does not establish the same near-nearest statement for arbitrary prime
powers q congruent to 1 modulo 4.

The F41 near scan exhausts every degree-at-most-10 polynomial with
at least 19 agreements. Such a nonconstant polynomial has ten correct
zeros or ten correct ones. The former are found by enumerating every
ten-element nonsquare root set and testing its locator's values on
squares. For the latter, for a fixed nonsquare a, the involution up to
inverse scaling Q(X)=1-P(aX) reduces to the former; the implementation
adds the inverse transform. The resulting bank is exactly the six
nearest polynomials. This finite check does not by itself reach the
general theorem's cutoff of 17 agreements for p=41.

The separate F17 brute-force scan enumerates all 17^5 degree-at-most-4
polynomials. Here the theorem's cutoff is seven agreements. Only the
six nearest polynomials reach it; all six have eight agreements.
