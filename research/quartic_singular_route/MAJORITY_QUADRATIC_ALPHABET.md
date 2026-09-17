# Quadratic alphabet bound by tensorizing maximal correlation

## Claimed finite strengthening

For every integer L≥1 and every prime p≡1 modulo 8 with

    p ≥ 2^36 L²,

there exists a received word on F_p^*, with its entire domain ordinary core for the Dickson cubic ODE, such that L distinct nonzero bank polynomials each have agreement at least

    (3/8+1/(32sqrt L))(p−1).

This is an existence theorem obtained by choosing a parameter list and pruning it while keeping the same majority word. It does not assert that the deterministic parameters 1,...,L achieve this bound. The only analytic input is the product-character bound ≤r sqrt p from BGKS Lemma 17 already checked in MAJORITY_AND_SHARP_THRESHOLD_AUDIT.md. All remaining estimates are elementary finite probability and linear algebra.

## 1. Random parameters and completed-sign variables

Put M=2L. Choose a_1,...,a_M independently and uniformly in F_p, initially allowing zero or repeated parameters. For each s≠0, form the 2M real signs chi(a_j+s),chi(a_j−s), permitting zero entries. Let F_i be the Boolean indicator on independent ±1 inputs that pair i agrees with the sign of the sum of all 2M inputs, with ties resolved positively. Let tilde F_i be its multilinear extension. Define

    Z_i(s)=tilde F_i(chi(a_1+s),chi(a_1−s),...,chi(a_M+s),chi(a_M−s)),
    Y_i=(p−1)^(-1) sum_{s≠0} Z_i(s).

A zero input is equivalent to averaging an independent uniform sign in that position. Consequently 0≤Z_i(s)≤1. For a product Z_i(s)Z_i(t), use independent completions at s and t conditional on the parameter vector; its expectation is then exactly the expectation of the product of the two Boolean indicators under the joint completed-sign distribution. This prevents any implicit assumption that the signs at distinct s are independent.

Let mu_M=1/4+binom(2M,M)/(2*4^M), the exact independent-sign mean from MAJORITY_COMBINATORICS.md.

## 2. Exact marginal pair law

For any s≠0, the completed pair U=(chi(a+s),chi(a−s)) has law

    pi(u_1,u_2)=[1−u_1u_2/p]/4.

Indeed both singleton moments vanish and the product moment is −1/p. The law is independent of s, and its total-variation distance from the uniform two-sign law is 1/(2p). The M parameter blocks are independent, so all Y_i have a common mean m, with

    |m−mu_M|≤M/(2p).                            (1)

Here tensor total variation is used only to control the mean, where the much smaller 1/p error suffices. In particular pi(u)≥(1−1/p)/4≥1/6 for p≥3.

## 3. A generic four-sign block has dimension-free maximal correlation

Fix nonzero s,t with t≠s and t≠−s. The four shifts s,−s,t,−t are distinct. Let nu(u,v) be the joint law of the two completed pairs U at s and V at t for one uniform parameter a. Both marginals are pi.

The Fourier expansion of nu−pi⊗pi has:

* four cross-pair moments, each equal to −1/p;
* four triple moments, each of absolute value at most 3/sqrt p by BGKS;
* one quadruple moment minus 1/p², of absolute value at most 4/sqrt p+1/p².

The internal pair moments cancel exactly. Therefore every entry satisfies

    |nu(u,v)−pi(u)pi(v)|
       ≤[4/p+16/sqrt p+1/p²]/16
       ≤21/(16sqrt p).                          (2)

Define the normalized centered matrix

    K(u,v)=[nu(u,v)−pi(u)pi(v)]/sqrt(pi(u)pi(v)).

It is a 4 by 4 real matrix. Its Frobenius norm, and hence operator norm, is bounded by

    ||K||op ≤4*6*21/(16sqrt p)=63/(2sqrt p)<32/sqrt p.   (3)

The conditional-expectation operator from V to U preserves constants and sends mean-zero functions to mean-zero functions; its norm on the latter subspace is at most rho=min(1,32/sqrt p). This is precisely the maximal-correlation bound. Equation (3) follows directly from the matrix entries; no external correlation theorem is needed.

For M independent parameter blocks the conditional-expectation operator is the M-fold tensor power. Decompose each one-block L² space orthogonally into constants and mean-zero functions. The tensor spaces are orthogonal sums indexed by which blocks are mean-zero. On a nonconstant summand at least one factor has norm≤rho, and all other factors have norm≤1. Thus the full mean-zero operator norm is still at most rho, NOT M rho.

It follows for any two [0,1]-valued functions of the completed M-block vectors, and in particular the two Boolean F_i indicators, that

    |Cov(F_i(U_1,...,U_M),F_i(V_1,...,V_M))|
       ≤rho sqrt(Var F_i(U) Var F_i(V))
       ≤rho/4 ≤8/sqrt p.                       (4)

Conditional averaging over the zero completions identifies this covariance exactly with Cov(Z_i(s),Z_i(t)). Both marginals have mean m, so there is no additional mean-comparison error in (4).

## 4. Variance of the coordinate average

Among ordered pairs of nonzero s,t, only t=s or t=−s are exceptional; there are 2(p−1) such pairs. Bound their covariance in absolute value by one. Equation (4) on the others gives

    Var(Y_i)≤8/sqrt p+2/(p−1)≤10/sqrt p,        (5)

for p≥3. This bound is independent of M. Keeping the weaker unit bound on exceptional covariances simplifies the constants.

## 5. Retain half the candidates, preserving the word

Assume p≥2^34 M², which is the displayed condition p≥2^36 L². Set delta=1/(32sqrt M). By Chebyshev and (5),

    Pr[Y_i<m−delta]≤10240M/sqrt p
                         ≤10240/2^17=5/64<1/8.

Thus the expected number of bad indices is less than M/8, and Markov bounds the probability of at least M/2 bad indices by less than 1/4.

The probability that any parameter is zero or that a_i=±a_j for distinct indices is at most

    M/p+2*binom(M,2)/p=M²/p≤2^(-34).

Hence there is a choice with distinct nonzero parameters modulo sign and at least M/2=L good indices. This step does not require independence of the good-index events.

For this choice define the deterministic majority word using ALL M parameters, then retain L good candidates without changing the word. The prime condition implies both

    M/(2p)≤1/(32sqrt M),
    M/(p−1)≤1/(32sqrt M).

By (1), every retained candidate satisfies

    Y_i≥mu_M−1/(16sqrt M).

On regular s all signs are nonzero and Z_i(s) is the actual deterministic majority-match indicator. Removing the at most 2M endpoints costs at most 2M in the sum defining Y_i. On the square half, this removes at most M coordinate matches. Each candidate still has exactly (p−1)/4 nonsquare matches because the nonsquare received value is zero. Its total agreement fraction is therefore at least

    1/4+Y_i/2−M/(p−1)
       ≥3/8+1/(8sqrt M)−1/(32sqrt M)−1/(32sqrt M)
       =3/8+1/(16sqrt M)
       ≥3/8+1/(32sqrt L).

Here b_M≥1/(2sqrt M) was used in mu_M. The majority word is even in s, so it descends to square coordinates. The square symbols ±1 and nonsquare symbol 0 preserve the full ordinary core, exactly as in the previously audited deterministic construction.

## Scope

The proof supplies polynomial-size alphabet dependence for the same family-specific reciprocal-square list lower bound. For epsilon small, take L=floor(1/(1024epsilon²)) and a prime p≡1 modulo 8 satisfying p≥2^36 L²; then the agreement is at least 3/8+epsilon and L=Omega(epsilon^(-2)). The theorem is stated for every prime beyond that threshold in the progression; it does not by itself give an explicit least-prime bound or an efficient deterministic method to find the good parameter set.

This does not reduce the evaluation-domain-to-field ratio: the domain still has length p−1. It does not produce a prime-field superlinear scalar-label counterexample or change the general first-order proximity threshold.
