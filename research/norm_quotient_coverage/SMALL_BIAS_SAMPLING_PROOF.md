# Logarithmically many norm tags suffice for full product coverage

The proposed random-tag step is valid. Fix E=Fp^d, q=p^d, d>=2,
and a generating element b of E/Fp. For fixed interior subset density,
a uniformly chosen set of O(log q) distinct base-field tags has positive
probability of representing every nonzero extension-field element as a
product of exactly the required number of distinct factors b-a. One
successful tag set works for every subset size in a fixed density interval.
The proof also permits a nonzero tag a0 to be reserved before sampling.

All logarithms below are natural. This is an existence proof for a fixed
b, with no claim that one G works simultaneously for all poles b. No
enumeration of characters, random experiment, or computational job is
required. The proof relies on the original Katz affine-line estimate and
the already verified elementary fixed-cardinality Cauchy bound.

## Exact sampling inequality, without replacement

Delete any fixed e tags T from Fp and let U=Fp\T, N=p-e. Katz gives,
for every nontrivial multiplicative character chi of E*,

    |N^(-1) sum_{a in U} chi(b-a)| <= mu,
    mu=((d-1)sqrt(p)+e)/(p-e).

The only hypothesis on chi is that it is nontrivial on E*. Characters
trivial on Fp* are included. The only hypothesis on b is Fp(b)=E.
Source: [Katz, An Estimate for Character Sums, Theorem 1, p.197](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf).

For any 1<=s<=N, choose G uniformly from the s-element subsets of U.
For any beta>mu,

    Pr[exists chi !=1: |sum_{a in G} chi(b-a)| > beta*s]
      <= 4(q-2) exp[-s(beta-mu)^2/4].                 (S)

Here is a self-contained proof of the concentration step. If a real
population x_1,...,x_N lies in [-1,1], has mean xbar, and S is the sum
of a uniform s-subset, then for every real t,

    E exp(tS)
      = e_s(exp(tx_1),...,exp(tx_N))/C(N,s)
      <= [N^(-1) sum_i exp(tx_i)]^s.

The elementary-symmetric-mean inequality follows by pair averaging.
At fixed sum of the positive arguments, the polynomial in any chosen
pair has the form A*y_i*y_j+B*(y_i+y_j)+D, with A>=0. On the compact
nonnegative simplex a maximizer has at least s positive entries since
the all-equal tuple gives positive value. For s>=2, averaging any unequal
pair then strictly increases the value (the coefficient e_(s-2) of the
other entries is positive). Thus the maximum is the all-equal tuple;
s=1 is immediate.

For one uniform entry X, the second derivative of
psi(t)=log E exp[t(X-xbar)] is a variance in an exponentially tilted
distribution. It is at most1 since X is in [-1,1]. With psi(0)=psi'(0)=0,
this proves psi(t)<=t^2/2 for every real t. Consequently

    E exp[t(S-s*xbar)] <= exp(s*t^2/2),
    Pr[|S-s*xbar|>s*u] <= 2 exp(-s*u^2/2).

Apply this to the real and imaginary parts separately. If a complex
deviation has modulus greater than s*v, one coordinate has absolute
value greater than s*v/sqrt(2). The resulting probability is at most
4 exp(-s*v^2/4). Take v=beta-mu and union-bound over the q-2 nontrivial
characters to get (S). This proves the exact finite sampling-without-
replacement statement directly; no independence assumption is hidden.

## Product coverage for a successful tag set

If a particular G satisfies the simultaneous bound beta*s with beta<1,
the fixed-cardinality Cauchy lemma gives, for theta=r/s and 0<r<s,

    |sum_{S subset G, |S|=r} prod_{a in S} chi(b-a)| / C(s,r)
      <= (s+1) exp[-theta(1-theta)(1-beta)s].

Thus every c in E* is a product of exactly r distinct factors if

    (q-2)(s+1) exp[-theta(1-theta)(1-beta)s] < 1.     (P)

Its representation count has the explicit lower bound

    C(s,r)/(q-1) *
      [1-(q-2)(s+1)exp(-theta(1-theta)(1-beta)s)].

This directly counts distinct coordinates. No bounds on chi^j are
assumed, so the exceptional powers for small-order characters cause
no problem. Once the character-bias event holds, (P) applies
deterministically to every r satisfying it.

## A simple finite constant for every fixed interior density

Fix 0<eta<=1/2, put kappa=eta(1-eta), and set

    C=max(128, 8/kappa),
    s=ceil(C log q).

Reserve a0 in Fp* and sample from U=Fp*\{a0}, so e=2. Assume

    q>=C+2,
    s<=p-2,
    ((d-1)sqrt(p)+2)/(p-2)<=1/4.                    (H)

Then (S) at beta=1/2 bounds the failure probability by

    4(q-2) exp(-s/64) <= 4 q^(1-C/64) <= 4/q < 1.

For every successful G and every integer r with eta<=r/s<=1-eta,
the total nontrivial-character error in (P) is bounded by

    (q-2)(s+1) exp(-kappa*s/2)
      <= (s+1)/q^3 <= 1/q < 1.

Indeed C*kappa/2>=4, and
s+1<=C log q+2<=Cq+2<=q^2 since q>=C+2.
In particular every product has at least

    C(s,r)/(q-1) * (1-1/q)

representations. This single G works simultaneously for all such r.

For fixed d and eta, (H) holds for every sufficiently large prime p:
q=p^d grows, s=ceil(C*d*log p)=o(p), and the mean bound tends to zero.
If desired, p>=16d^2 already suffices for the mean condition when d>=2;
the separate sample-capacity inequality must still be checked.
For a fixed target rate rho, choose any
eta<min(rho,1-rho); bounded floor/core corrections then eventually put
the compiler's actual r/s in this interval. This gives an explicit finite
constant C depending only on the chosen density interval, with d entering
through q=p^d and the finite hypotheses.

## A smaller constant for the central density interval

If only 1/4<=r/s<=3/4 is needed, an alternative exact choice is

    s=ceil(64 log[8(q-2)]),

under the same mean and sample-capacity conditions. Its failure
probability is at most1/2. The product error is at most

    (q-2)(s+1) exp(-3s/32)
      <= (s+1)/(8^6*(q-2)^5)
      <= 1/[512*(q-2)^4] < 1.

For the last inequality, log x<=x-1 gives
s+1<=64 log[8(q-2)]+2<=512(q-2)-62<512(q-2).
This also proves simultaneous product coverage for all central r.

## Compiler handoff and scope

For exact-dimension padding, use the norm domain

    D=N^(-1)(G union {a0}),
    m=(q-1)/(p-1),
    n=(s+1)m.

The reserved fiber N^(-1)(a0) must be included in D for its partial core
to contribute agreement; the product subsets themselves use only G.
The quotient compiler then has normalized one-fiber source gap
m/n=1/(s+1), which is Theta(1/log q). For fixed d>=2,

    log n=(d-1)log p+O(log log p),
    log q=d log p,

so this is Theta(1/log n), and q is polynomially bounded in n
(indeed q<=n^(d/(d-1))). The compiler agent owns the exact dimension,
agreement, and line-label bookkeeping. This sampling lemma supplies the
surjectivity hypothesis and creates no additional character exceptions.

The resulting domain is a chosen union of norm fibers. It need not be
the prescribed power-of-two subgroup in the practical better.codes
benchmark. The lemma does not establish a practical benchmark improvement,
nor does this note make a novelty claim for the probabilistic argument.

Integration-ready TeX is `small_bias_sampling.tex`, with labels
`lem:random-tag-character-bias` and
`cor:logarithmic-tag-product-coverage`.
