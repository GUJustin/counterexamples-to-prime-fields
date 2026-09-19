# Fixed-domain factor recurrence closes the short-tail extra-head bank

This is an exact obstruction for the specific compiler in `GROWING_DIMENSION_EXTRA_HEAD_COMPILER.md`, not a general obstruction to growing-dimension constructions.

Let P be a fixed squarefree monic polynomial of degree N=5K+r, where 0<=r<K. Consider monic divisors

L=X^(4K)+c X^(3K)+a X^(2K)+b X^K+V,

where deg(V)<=B and B+K+r<2K. No assumption on the leading coefficient or constant term of V is needed. Then P has at most FIVE such divisors.

## Exact coefficient recurrence

Write u=X^K and the complementary divisor as

C=P/L=u A+D,  deg(A)=r, deg(D)<K.

The polynomial A is monic. Since deg(VC)<2K,

P=u^5 A+u^4(D+cA)+u^3(cD+aA)+u^2(aD+bA) + terms of degree <2K.

Let P_i, of degree <K, be the fixed coefficient blocks in P=sum_i u^i P_i. Thus

A=P_5,
D=P_4-cA,
P_3=cP_4+(a-c^2)A,
P_2=aD+bA.

If all divisors have the same c, the equations successively determine D,a,b,C and hence L uniquely. Otherwise choose two distinct c values. Subtracting their P_3 equations proves P_4=alpha*A for a scalar alpha. The remaining equations then give fixed scalars beta,gamma such that

P_3=beta*A, P_2=gamma*A,
a=c^2-alpha*c+beta,
b=gamma-a(alpha-c),
C=A(u+alpha-c).

These identities hold for every divisor in the family, not merely the selected pair.

Every distinct c consequently supplies a full root set of X^K+alpha-c in the roots of P. These sets are pairwise disjoint. Each consists of K distinct field elements whenever P is split: this follows directly from squarefreeness and divisibility, without needing a separate characteristic guard. They are also disjoint from the r roots of A. Thus m*K+r<=N=5K+r, proving m<=5. The same degree argument works over an algebraic closure if P is not split.

## Application to the proposed first-order window

For K=20*l, B=l and an n=108*l nonzero evaluation domain, adjoining zero gives a squarefree P of degree N=108*l+1=5K+(8*l+1). For l>=1, r<K and

B+K+r=29*l+1<40*l=2K.

Each proposed simply split locator has all its roots in this augmented domain, hence divides P. The entire bank therefore has size at most five, irrespective of field size. The earlier compiler identity and first-order/Johnson inequalities remain algebraically correct, but this recurrence prevents their use with a growing split-support bank.

The recurrence identifies the actual failure mechanism: the high coefficient blocks force every complementary support to be a fixed support plus one complete X^K fiber. It is not an assumption that the original supports were unions of fibers.

## Precise escape condition

The proof uses deg(VC)<2K. To evade this exact argument while retaining the same four high monomials, one must at least allow B+N-4K>=2K, i.e. B+N>=6K, or change the high-head pattern. This condition is necessary only to escape this recurrence; it does not assert existence. At N approximately5.4K it requires B approximately0.6K, far larger than the B=.05K used in the first-order placement. No new construction is established here.
