# Exact 3/8 transition for the complete Dickson ODE solution bank

2026-09-17. Positive family-specific theorem. This proves a constant list bound strictly above the existing linear-list agreement threshold; it is not a statement about all Reed--Solomon codewords.

## Theorem

Let p=1 mod8 be prime, n=p-1, k=n/4. Let B be the complete degree-at-most-k-1 solution set of the cubic ODE classified in DICKSON_SOLUTION_CLASSIFICATION.md. Thus

    B={0} union {P_a=G_a-X^k : a in F_p^*/{+1,-1}},

and |B|=n/2+1. For ANY received word on F_p^*, even with values in an extension field, and 0<epsilon<=5/8, the number of members of B agreeing on at least (3/8+epsilon)n coordinates is at most

    ceil(epsilon^(-2)).                               (1)

At agreement exactly 3n/8, the existing Dickson word has n/2 nonzero bank members. Thus 3/8 is the exact transition from a linear bank to a uniformly bounded list for this complete ODE solution family.

The proof requires only exact pair correlations of quadratic characters, not a Weil error term or a limit p->infinity.

## 1. Coordinate buckets

Fix L distinct nonzero bank members, choosing representatives a with distinct a^2; put their set of representatives equal to A. Let chi be the quadratic character, with chi(0)=0. At each coordinate shift the received value by x^k, so that agreements concern G_a(x). This does not change the list count.

For nonsquare x, the Frobenius identities in the ODE note give

    J_a G_a=0,    J_a^2+xG_a^2=a^2-x.

Thus G_a(x)=0 exactly when chi(a^2-x)=1. Every nonzero G_a(x) satisfies

    G_a(x)^2=a^2/x-1.

Distinct a^2 give distinct squares of these nonzero values, so every nonzero bucket contains at most one bank member. If N0(x) counts the zero bucket, the largest bucket is at most N0(x)+1.

For each a, the number of nonsquare x with chi(a^2-x)=1 is n/4. Indeed

    sum_{x nonsquare} chi(a^2-x)
      = [sum_{x!=0}chi(a^2-x)-sum_x chi(x(a^2-x))]/2
      = [(-1)-(-1)]/2=0.

Therefore

    sum_{x nonsquare} N0(x)=Ln/4.                    (2)

For square x=s^2!=0, Euler's criterion gives

    G_a(s^2)=((a+s)chi(a+s)-(a-s)chi(a-s))/(2s).

Away from s=+a,-a, equal signs give the shared values +1 or -1; opposite signs give +a/s or -a/s. Again every bucket outside {+1,-1} is a singleton, since its squared value determines a^2. At s=+a or -a the value is chi(2a)=chi(a), using chi(2)=1. These endpoints also belong to the shared buckets.

Let N+(x),N-(x) denote the actual shared bucket sizes. Their exact totals are

    sum_{x square} N+(x)=sum_{x square} N-(x)=Ln/8.    (3)

To verify the endpoint-sensitive formula, for epsilon0 in {+1,-1} put

    I_a,epsilon0(s)
       =(1+epsilon0*chi(a+s))(1+epsilon0*chi(a-s))/4.

Its sum over all s in F_p is n/4, using the quadratic-character correlation -1. Removing s=0 subtracts one exactly when epsilon0=chi(a). At each of s=+a,-a the true bucket indicator exceeds I by 1/2 in exactly that same case. These corrections cancel. Dividing by two for s->s^2 proves (3).

## 2. Exact second moment of the shared-bucket imbalance

Define

    S(s)=sum_{a in A}[chi(s+a)+chi(s-a)].

The 2L shifts are distinct, and S(-s)=S(s). At x=s^2,

    N+(x)-N-(x)=S(s)/2+E(x)/2,

where E(a^2)=chi(a) for each selected parameter and E is zero elsewhere. In particular sum_x |E(x)|=L.

The exact character identities are

    sum_s chi(s+b)^2=p-1,
    sum_s chi(s+b)chi(s+c)=-1  for b!=c.

For completeness, the latter follows by counting y^2=(s+b)(s+c): after completing the square, its solutions correspond to nonzero factor pairs with a fixed nonzero product, hence there are p-1 solutions and the character sum is -1. No external character-sum estimate is needed.

Consequently

    sum_s S(s)^2=2L(p-1)-2L(2L-1)=2Lp-4L^2.         (4)

Cauchy--Schwarz on the n nonzero s gives

    sum_{s!=0}|S(s)| <= sqrt(n(2Lp-4L^2)).            (5)

Equations (3)--(5) yield

    sum_{x square} max(N+(x),N-(x))
       <= Ln/8 + (1/8)sqrt(n(2Lp-4L^2)) + L/4.       (6)

Here the factor 1/8 accounts for halving the absolute imbalance, its factor 1/2 in S, and the two-to-one map s->s^2.

## 3. Uniform total-agreement bound and list size

At a square coordinate, allowing singleton buckets costs at most one beyond max(N+,N-). At a nonsquare coordinate it costs at most one beyond N0. Summing over all n coordinates, (2) and (6) prove the exact bound

    total agreements of the selected L candidates with ANY word
      <= 3Ln/8+n+L/4+(1/8)sqrt(n(2Lp-4L^2)).         (7)

A received value outside F_p contributes zero agreements, so extension alphabets do not change this bound.

If all selected candidates agree on at least (3/8+epsilon)n coordinates, divide (7) by Ln to obtain

    epsilon <= 1/L+1/(4n)+(1/8)sqrt((2Lp-4L^2)/(L^2*n)).

Since L<=n/2 and p=n+1<=2n, this implies

    epsilon <= 9/(8L)+1/(4 sqrt(L)).                 (8)

If L>=epsilon^(-2), its right side is at most

    epsilon*(9epsilon/8+1/4) <= (61/64)epsilon

for 0<epsilon<=5/8, a contradiction. Hence the number of nonzero bank members is strictly less than epsilon^(-2). Adding the zero solution gives at most ceil(epsilon^(-2)), proving (1).

## Scope and attribution

The lower list at exactly 3/8 is the already established full-length Dickson agreement calculation. The ODE and its exact solution classification specify the family to which the new upper bound applies. The moment estimate above is an elementary character-correlation argument; no novelty claim is made for that technique. No broader priority search has yet been performed for this specific threshold statement.

This does not bound the entire Reed--Solomon list outside the ODE bank. It does not create additional prime-field line labels, improve better.codes, or establish first-order proximity tightness. It gives a sharp family-specific explanation: enlarging this classified bank above its native 3/8 agreement cannot retain a growing list, regardless of how the received word is changed on the same full domain.
