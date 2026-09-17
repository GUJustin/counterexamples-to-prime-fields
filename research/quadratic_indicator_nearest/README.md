# Exact nearest list of the quadratic-residue indicator

September 17, 2026. An elementary restricted-family upper bound; no novelty
claim. This closes this alternative as a growing-nearest-list source.

Let q be an odd prime power congruent to1 modulo4, k=(q-1)/4, and put
w(x)=(1+x^(2k))/2 on F_q*. Among polynomials of degree at most k,
the maximum agreement is2k and exactly SIX polynomials attain it:
the constants0,1 and

    P_(u,v)(X)=(X^k-u)/(v-u),  u^2=-1, v^2=1.

These four nonconstant candidates have multiplicative orbit size2 under
mu_(2k), and are invariant under mu_k. The assertion also holds for
polynomial coefficients in any field extension of F_q.

## Proof of maximum and classification

For a nonconstant P of degree at most k, its agreements with w occur
at zeros of P or P-1, so there are at most2k. The two constant candidates
already attain2k. Equality for a nonconstant candidate forces degree k,
exactly k simple roots of P on the nonsquares, and exactly k simple roots
of P-1 on the squares. Thus

    X^(2k)+1 = P A,      X^(2k)-1 = (P-1) B

for polynomials A,B of degree k. If the leading coefficient of P is c,
both A and B have leading coefficient1/c. Subtraction gives

    P(A-B)+B=2.

Since deg(A-B)<k, degree comparison forces A-B to be constant lambda.
It is nonzero, and B=2-lambda P implies lambda=-1/c^2. Consequently

    c^2 X^(2k)+c^2 = P^2+(2c^2-1)P.

Set R=P+c^2-1/2. Then

    (R-cX^k)(R+cX^k)=c^4+1/4.

The second factor has degree k, because the characteristic is odd.
A nonzero constant on the right is impossible. Thus the right side is
zero and R=cX^k. In particular P=cX^k+t. The divisibility conditions
then force u=-t/c to satisfy u^2=-1 and v=(1-t)/c to satisfy v^2=1,
giving exactly the four polynomials displayed above. Conversely, each
has k roots in the required nonsquare coset and k one-values in the
required square coset, so all four attain equality.

Extension coefficients cannot add candidates:2k>=k+1 agreements at
base-field points and values force coefficients into F_q by interpolation.
The case k=1 is included. No bound on characteristic relative to k is
needed beyond odd characteristic.

## Discovery and finite checks

The C++ search exhausts every possible k-element zero set among the2k
nonsquares for p17 and p41. Its locator H determines candidates cH;
a nonzero value of H repeated k times on the squares determines c.
The70 and184,756 root subsets give exactly the six polynomials above.
The algebraic proof, rather than these finite scans, establishes the
general statement. Full coefficient lists are in p17.log and p41.log.
An independent Python verifier checks the lists, all agreements, and the
closed form at additional primes.

The rate is (k+1)/(4k), tending to1/4, and agreement is1/2. This places
the limiting parameters above the first-order curve, but the list size
is the constant6. The smallest finite cases need not themselves meet a
particular first-order theorem's regime and characteristic requirements.
This is not a lower-bound improvement or a better.codes result.

## Stronger prime-field rigidity

NEAR_RIGIDITY.md proves that for prime p=4k+1, the same six polynomials
are the entire list at every agreement threshold greater than 5k/3.
At degree strictly less than k, only the constants 0 and 1 occur.
Consequently this word has a constant list throughout the quarter-rate
first-order range, not just at its nearest threshold. A polynomial abc
argument proves the statement; a full 17^5-polynomial census tests its
cutoff over F17. The prime-power generality above applies to the exact
nearest classification, not to this stronger statement.

Moreover the original Dickson word is this indicator minus X^k.
For prime p>5 its entire degree-<k nearest-list problem has maximum
agreement at most floor(5k/3), since none of the four classified
nonconstant polynomials is monic. Thus enlarging the known Dickson
candidate bank cannot reach the first-order regime on the full domain.
