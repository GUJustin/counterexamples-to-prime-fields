# The Dickson cubic ODE bank has no common weighted monic-cubic first integral

This is a corollary distinguishing an actual cubic differential equation from a cubic polynomial first integral. It does not deny the existing rational first integral of different value-degrees.

Let p≡1 mod8 be prime, n=p−1, D=n/4−1. The audited Dickson construction provides L=n/2 distinct nonzero degree-at-most-D polynomials P_a, each agreeing with the original Dickson word at exactly 3n/8 coordinates of F_p^*. For every such prime p≥521, this complete nonzero bank cannot satisfy

    F(X,P_a)=c_a H(X)

for any nonzero H in F_p[X] and any common weighted monic cubic

    F(X,u)=u³+a2(X)u²+a1(X)u+a0(X),
    deg a2≤D, deg a1≤2D, deg a0≤3D,

with constants c_a in F_p. The same impossibility holds after extending constants.

## Proof and threshold

The improved list theorem applies because p>max(3,2D). The observed agreement has surplus

    eta=(3n/8−D)/n=1/8+1/n.

Therefore a bank inside such a first integral would satisfy

    L≤floor[9+(3+108D/n)/eta]
     =floor[249−2784/(n+8)].                    (1)

For n≥488,

    n/2>249−2784/(n+8),

because this is equivalent to n²−490n+1584>0; the polynomial equals608 at n=488 and is increasing thereafter. Thus L=n/2 contradicts (1). Since n is a multiple of eight, n≥488 is the first such integer beyond the positive root of this quadratic. For admissible primes p≡1 mod8, the first prime satisfying this sufficient condition is521: the earlier candidates489,497,505,513 are composite.

In particular the simpler condition p>499 is safely sufficient. The exact numerical threshold here is only the threshold furnished by the deliberately conservative cubic list bound; no claim is made that a first integral exists at smaller primes.

## Conceptual scope

The bank is already known to solve a primitive cubic first-order differential equation. That fact does not provide a monic polynomial first integral of value-degree three with the same weighted coefficient budget. The large list at agreement3/8 proves that no such first integral can contain the complete bank in the above range.

The corollary does not rule out higher-degree first integrals, denominators depending on the candidate value, nonmonic models, or representations exceeding the displayed X-degree budget. In particular the known Dickson rational first integral is outside this statement.
