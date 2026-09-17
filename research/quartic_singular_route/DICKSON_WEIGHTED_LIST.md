# A weighted Johnson bound for every solution of the Dickson cubic equation

Let p=4k+1 be prime, k≥2, n=4k, D=k−1, and E=F_p^*. Work over any extension field K of F_p. The exact classification in DICKSON_SOLUTION_CLASSIFICATION.md identifies all degree-at-most-D solutions of the shifted cubic ODE as

    P_t=G_t−X^k,  t in {0} union (F_p^*)²,
    G_t=sum_{j=0}^k binom(2k+1,2j+1)t^(k−j)X^j.

Thus the solution bank has 2k+1 members, including P_0=0. This note bounds the sublist close to ANY received word w:E→K, not just the customary Dickson word. It is an upper bound for this particular equation's complete solution set, not for all Reed–Solomon codewords.

## Finite statement

Let L be the number of bank members agreeing with w at at least A coordinates. Put

    Delta=A²−3nD/4,
    B=2An+9n²/8−3nD/4.

If Delta>0, then

    L < B/Delta,

or equivalently L≤ceil(B/Delta)−1. In particular, any fixed positive margin

    A/n > sqrt(3D/(4n)) + epsilon

bounds L by a constant depending only on epsilon. As D/n→1/4 the threshold tends to sqrt(3)/4≈0.433013. This is below the quarter-rate first-order threshold. Consequently this specific ordinary-core equation cannot produce growing lists near that first-order threshold, despite its growing list at agreement 3/8 when p≡1 mod8.

If LA≥n, the stronger exact quadratic constraint is

    Delta L²−B L+n²≤0.                           (1)

No nearest-list or characteristic-extension assumption beyond the stated classification is needed; the received values may lie anywhere in K.

## 1. Shared values and the endpoint correction

At x∈E let q=x^(2k)∈{1,−1}, and shift the received value to h=w(x)+x^k. The parameter identity, valid for all bank members, is

    t[(1+q)²−4G_t(x)²]
       =4x G_t(x)²[q−G_t(x)²].                  (2)

If x is square (q=1), any value other than +1 or −1 determines t uniquely. If x is nonsquare (q=−1), every nonzero value determines t uniquely. Thus the only values that can be shared by distinct bank members are square-coordinate values ±1 and nonsquare-coordinate value 0. A received value outside F_p has no matches at all.

At a square coordinate x=s², take t=a² and write

    G_t(s²)=((a+s)^e−(a−s)^e)/(2s), e=(p+1)/2.

When a≠±s and G_t(x)=sigma∈{±1}, both nonzero characters chi(a+s),chi(a−s) equal sigma. Indeed unequal characters would instead give G_t(x)=±a/s, which equals ±1 only at the excluded endpoints. Differentiating s G_t(s²) in the square-root variable (holding the parameter a fixed) gives

    2x G_t′(x)+G_t(x)
       =(e/2)[(a+s)^(e−1)+(a−s)^(e−1)].

Since e=1/2 in F_p, this yields

    G_t′(x)=−sigma/(4x),   provided t≠x.         (3)

At the single exceptional parameter t=x, one binomial term is zero and the other has character sigma. The derivative instead is −3sigma/(8x). This incidence must not be assigned multiplicity two. Parameter t=0 is not exceptional at nonzero x; directly G_0=X^k gives the derivative in (3).

## 2. Discard at most n incidences, not 3n/2

For the chosen list of L candidates, retain incidences as follows.

* At square x with h=±1, retain every match except parameter t=x.
* At nonsquare x with h=0, retain every match.
* At every other coordinate discard all matches; there is at most one by (2).

There is at most one discarded incidence PER COORDINATE: the endpoint and unique-value cases are disjoint. If m_x is the retained incidence count and S=sum_x m_x, then

    S≥LA−n.                                    (4)

Assign weight omega_x=2 at squares and 1 at nonsquares. For any two distinct retained candidates agreeing at a square coordinate, (3) says their derivatives agree too. Subtracting the common X^k shift preserves derivative equality, so P_t−P_u has a root of multiplicity at least two there. At retained nonsquare coordinates it has a root of multiplicity at least one. Since deg(P_t−P_u)≤D,

    sum_x omega_x binom(m_x,2) ≤ D binom(L,2).   (5)

This uses actual polynomial-root multiplicity, with no unjustified derivative condition at the exceptional endpoints.

## 3. Weighted Cauchy and the exact constants

There are n/2 coordinates of each weight, hence

    C=sum_x 1/omega_x = 3n/4,
    W=sum_x omega_x = 3n/2.

By (5), the trivial bound m_x≤L, and weighted Cauchy,

    S² ≤ C sum_x omega_x m_x²
       ≤ C[D L(L−1)+W L]
       = CD L²+C(W−D)L.                         (6)

If LA≥n, square the nonnegative lower bound in (4) and combine with (6). Expansion gives exactly (1), with B=2An+C(W−D). For L>0, (1) implies Delta L²−B L<0 and hence L<B/Delta. If LA<n, the same final bound follows because L<n/A and B/Delta>n/A: indeed W>D, B>2An, and 0<Delta≤A². L=0 is immediate. This also specifies where the nonnegativity condition needed for squaring is used.

For reference, writing alpha=A/n and rho=D/n gives

    B/Delta=(2alpha+9/8−3rho/4)/(alpha²−3rho/4).

Here rho=1/4−1/n. The conclusion concerns this classified ODE bank even over arbitrary extension fields; it does not settle the general ordinary-core escape.

## Exact finite checks

`check_dickson_weighted_list.py` verifies all shared-value derivative formulas (including endpoints), all 2,214 pairwise weighted multiplicity budgets, and the integer finite bound on 126 received words for p=13,17,29,41,73,97. The words comprise the standard received word and twenty reproducible pseudorandom controls per field; only the finite controls use sampling, while all pair and derivative checks are exhaustive. Results are saved in `check_dickson_weighted_list.json`. These checks supplement the proof, not the arbitrary-word quantifier.
