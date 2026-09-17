# Majority received words: matching quadratic dependence above 3/8

2026-09-17. Positive construction within the classified Dickson ODE bank. This is not tightness of the general first-order proximity threshold.

## Finite theorem

For every integer L>=1 and every prime p=1 mod8 satisfying

    p >= 4096 L^3 4^L,                                  (1)

choose a_i=i for i=1,...,L and n=p-1. There is an explicitly defined received word on F_p^* such that each of the L distinct polynomials P_(a_i) from the Dickson bank agrees on at least

    (3/8+1/(16 sqrt(L))) n                              (2)

coordinates. Every selected polynomial solves the SAME primitive cubic ODE from DICKSON_CUBIC_ORDINARY_CORE.md, and the entire domain remains ordinary core for this new received word.

Such primes exist arbitrarily far out by Dirichlet's theorem for the progression 1 mod8. In conjunction with DICKSON_SHARP_LIST_THRESHOLD.md, the worst-case list size within this complete ODE bank above 3/8+epsilon has order Theta(epsilon^(-2)), allowing the prime to grow with epsilon. This is uniform upper and existential lower dependence, not a claim for each fixed finite p.

For example, for 0<epsilon<=1/32 choose L=floor(1/(256epsilon^2)). Then L>=1/(512epsilon^2), and (2) is at least the requested 3/8+epsilon agreement.

## 1. Explicit majority word

Use shifted values W(x)=w(x)+x^k, where k=(p-1)/4. On nonsquare x put W(x)=0. On square x=s^2!=0 put

    S(s)=sum_{i=1}^L [chi(s+a_i)+chi(s-a_i)],
    W(s^2)=+1 if S(s)>=0, and -1 otherwise.

The tie is resolved in favor of +1. Since chi(-1)=1, S(-s)=S(s); hence this is a well-defined word on x, independent of the choice of square root. Finally set w(x)=W(x)-x^k.

For each candidate its nonsquare agreements are exactly n/4, by the already proved character identity. On square coordinates away from s=+a_j,-a_j for every j, its agreement is exactly the Boolean event that its two character signs both equal the majority sign. At the removed coordinates we need no agreement guarantee.

Both W=0 on nonsquares and W=+1 or -1 on squares make all derivative coefficients of the ODE vanish. Thus changing the shared square bucket by majority preserves the full ordinary core; this does not manufacture a fake equation or replace the actual polynomial solutions.

## 2. Exact symmetric-cube calculation

Let xi_i,eta_i be 2L independent uniform signs, let S=sum_i(xi_i+eta_i), and let sigma=+1 when S>=0 and -1 otherwise. For every i the candidate agreement indicator is

    F_i=(1+sigma xi_i)(1+sigma eta_i)/4.

Symmetry of all 2L sign coordinates and sigma*S=|S| give

    E F_i = 1/4 + E|S|/(4L)
          = 1/4 + binom(2L,L)/(2*4^L).                 (3)

Indeed E(xi_i eta_i)=0 and E(sigma xi_i)=E|S|/(2L). The random-walk identity is E|S_(2L)|=2L binom(2L,L)/4^L, obtainable by telescoping adjacent binomial coefficients.

Writing b_L=binom(2L,L)/4^L, one has b_L>=1/(2sqrt(L)). One elementary proof observes b_1 sqrt(1)=1/2 and

    [b_(L+1) sqrt(L+1)/(b_L sqrt(L))]^2
       =(2L+1)^2/[4L(L+1)]>1.

Thus the ideal square-coordinate probability exceeds 1/4 by at least 1/(4sqrt(L)), and the ideal full-domain agreement exceeds 3/8 by at least 1/(8sqrt(L)). The latter factor one half is essential.

## 3. Uniform finite-field error without enumerating all patterns

Put m=2L and let b_1,...,b_m be the distinct shifts a_i,-a_i. For any Boolean function F on {+1,-1}^m write its normalized Fourier expansion

    F(epsilon)=sum_{J subset[m]} hatF(J) prod_{j in J} epsilon_j.

Parseval gives sum_J hatF(J)^2=E F^2<=1 for indicators. At a regular s, substitute epsilon_j=chi(s+b_j). For a nonempty J, the polynomial prod_{j in J}(s+b_j) is squarefree and is not a square. The classical character estimate gives

    |sum_s prod_{j in J}chi(s+b_j)| <= m sqrt(p).

A suitable primary source already used elsewhere in the manuscript is Bourgain--Garaev--Konyagin--Shparlinski, *On the hidden shifted power problem*, arXiv:1110.0812v2, Lemma 17 (constant additive phase): https://arxiv.org/pdf/1110.0812 . We use only its product-character bound.

Cauchy--Schwarz on Fourier coefficients gives

    sum_{J nonempty}|hatF(J)| <= 2^(m/2),

so the discrepancy of the Fourier-evaluated total from p E F is at most m 2^(m/2)sqrt(p). At a zero character coordinate, the multilinear Fourier extension is the expectation of F after replacing each zero by an independent random sign, and therefore lies in [0,1]. Removing the at most m such points, and s=0, loses at most m+1. Consequently every candidate's number of regular matching s is at least

    p mu_L - E_L,
    mu_L=1/4+b_L/2,
    E_L=2L 2^L sqrt(p)+2L+1.                          (4)

This bound is uniform over the actual parameter choices, requiring only their distinct shifts. It applies separately to EACH candidate with the same error; no average-over-candidates step is substituted for simultaneous agreement.

The square map is two-to-one, so each candidate has total agreements at least

    n/4 + (p mu_L-E_L)/2.

Dividing by n and using p=n+1 gives at least

    3/8+b_L/4-E_L/(2n).                              (5)

## 4. The displayed prime-size condition suffices

Since p>=2, n>=p/2, whence

    E_L/(2n) <= 2L 2^L/sqrt(p)+(2L+1)/p.

Under (1), the first term is at most 1/(32sqrt(L)). The same condition implies p>=32(2L+1)sqrt(L), so the second is at most 1/(32sqrt(L)). Therefore the error in (5) is at most 1/(16sqrt(L)). Combining this with b_L/4>=1/(8sqrt(L)) proves (2).

## What this sharpens

The upper theorem holds for any received word and bounds the complete ODE bank by ceil(epsilon^(-2)); the majority construction supplies a constant multiple of epsilon^(-2) simultaneous actual solutions. At epsilon=0, the original word already has a linear bank. Thus both the 3/8 transition and the reciprocal-square blow-up above it are sharp for this family.

All techniques here are classical: a majority bias calculation, Fourier expansion, and the product-character estimate. No priority claim is made without a separate search. The result does not give a superlinear prime-field label count, improve better.codes, or move the first-order proximity threshold. Its significance is an exact quantitative description of an explicit globally constrained solution family, including a simultaneous lower construction for every sufficiently small slack.
