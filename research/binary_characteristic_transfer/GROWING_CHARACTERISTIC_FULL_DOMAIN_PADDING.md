# Fixed-rate locator populations with growing characteristic and internal padding

September 18, 2026. Proposed theorem in the prime workspace; the binary repository was read only. The compiler is already in the binary paper, Corollary `cor:arbitrary-domain-all-rates` and Remark `rem:fixed-characteristic-all-rates`. The contribution here is a uniform growing-characteristic specialization with padding inside the seed domain. The native theorem is independently audited in GROWING_CHARACTERISTIC_FULL_DOMAIN_PADDING_AUDIT.md. No manuscript edits or numerical enumeration.

## Theorem (uniform form)

Fix a real rate 0<rho<1 and integers s≥2, d≥s+2. Let p be a sufficiently large prime, D an Fp-linear space of size N=p^d in a finite field F of size q, and use the STRICT degree-<J code, where J=floor(rho N). Put

    t=p^(d-s), K0=t/p², M=[d choose s]_p,
    Delta=floor((1-rho)t/2), T=J+Delta.

There are words f,g on D such that

    agr_J(g)=CA_J(f,g)=J,
    #Bad_T(f,g)≥ceil(q M/(q+M-1)).

Here Bad uses additive challenges f+z g and includes zero. Subtract at most one for a nonzero-label statement. If M>(q-1)², EVERY challenge is bad. In this case f itself is near, so this is expressly not a both-far native pair.

One explicit sufficient collection of finite conditions is

    p≥4/(1-rho),   p^(s+1)≥2/rho,
    (1-rho)² p^(d-s)/64 > log(4)+s(d-s) log(p).

All hold for sufficiently large p with rho,d,s fixed. The logarithms only certify existence of a padding set, not a computational search bound.

If D lies in a subfield B and [F:B]≥s+1, a separate choice has

    agr_J(f)=agr_J(g)=CA_J(f,g)=J,

and at least M DISTINCT NONZERO bad labels at the same threshold. In particular take B=F_(p^d) and F=F_(p^(d(s+1))). This changes the challenge alphabet and failure probability; it is not a both-far version of the all-native-label conclusion.

## 1. Uniform population and coefficient recovery

Range over all codimension-s subspaces W of D. Their monic p-linear locators have degree t:

    L_W(X)=sum_i a_i X^(t/p^i), a_0=1.

Missing coefficients are zero. With s-1 head parameters theta_j, recursively set

    b_0=1,
    b_j=theta_j-sum_(i<j) b_i a_(j-i)^(p^(s-1-i)).

Coefficient elimination gives the EXACT identity

    sum_(j=0..s-1) b_j L_W^(p^(s-1-j))
      = X^(N/p)+sum_(j=1..s-1) theta_j X^(N/p^(j+1))
        + z_W X^(t/p)+R_W,
    deg R_W≤K0, R_W(0)=0.

Thus with the head divided by X as f0 and g0=X^(pK0-1), the polynomial h_W=-R_W/X has degree at most K0-1 and matches f0+z_W g0 on W minus zero. Division by X is polynomial division throughout.

The labels are distinct affine functions of theta. In the coefficient of theta_j in z_W, the term a_(s-j)^(p^(s-1-j)) is accompanied only by previously recoverable locator coefficients. Starting at j=s-1 recovers a_1,...,a_(s-1); the constant term then recovers a_s. Frobenius is bijective, with no factorial or characteristic-size hypothesis.

If these coefficients exhaust the locator, equality proves W=W'. Otherwise their difference has degree at most p^(d-2s-1), while the two subspaces share at least p^(d-2s) roots. Root counting again proves equality. This handles d=2s, including the principal d=8,s=4 specialization: all locator coefficients have already been recovered. There is no hidden assumption d>2s.

The exact population has UNIFORM bounds

    p^(s(d-s)) < M < 4 p^(s(d-s)).

The Gaussian product divided by its leading power is
prod_(j=1..s)(1-p^(-(d-s+j)))/(1-p^(-j)); each ratio exceeds one. For the upper bound its numerator is at most one and the denominator exceeds 1/4 uniformly for p≥2: separate j=1 and apply product(1-x_j)≥1-sum x_j to j≥2. Thus fixed-p Theta notation is unnecessary.

## 2. One internal padding set for all supports

Set w=J-pK0+1. The finite conditions ensure 0≤w≤N and w/N≤rho. Choose a uniformly random w-subset B of D. For a fixed W, X_W=|B intersect W| has factorial moments

    E binom(X_W,j)=binom(t,j)(w)_j/(N)_j
                 ≤binom(t,j)(w/N)^j.

For 0≤theta≤1 this implies

    E exp(theta X_W)≤[1+(w/N)(exp(theta)-1)]^t
                   ≤exp((w/N)t(theta+theta²)).

Markov with theta=epsilon/2 gives

    Pr[X_W>(rho+epsilon)t]≤exp(-epsilon²t/4),

using w/N≤rho≤1. This deliberately conservative elementary constant avoids any reliance on a sharper concentration theorem. With epsilon=(1-rho)/4, the displayed finite condition and the bound on M make the union probability less than one. Therefore ONE exact-size B works simultaneously for every W, before any compiler parameters are chosen.

Multiply both sources and every witness by L_B. The padded direction g is monic of exact degree

    w+pK0-1=J.

Every witness has degree at most

    w+K0-1=J-(p-1)K0<J.

The matching set contains B union (W minus zero), of size

    w+t-1-|B intersect W|+1_(0 in B)
      ≥J+t-pK0-|B intersect W|
      ≥J+(1-rho-epsilon-1/p)t
      ≥J+(1-rho)t/2.

The zero coordinate is explicitly accounted for; including it in B only helps. Overlapping padding roots do not require additional multiplicities: L_B vanishes once at every point of B and preserves every old match outside B.

Since g is monic of degree J, no strict degree-<J polynomial agrees with it on more than J distinct coordinates. Interpolation on any J coordinates proves equality and supplies simultaneous explanations for both sources on those coordinates. Hence agr_J(g)=CA_J(f,g)=J exactly.

## 3. Pooling, individual-source projection, and ordinary lists

For independently uniform theta_j in F, two distinct affine labels collide with probability at most 1/q. If n_z are their occupancies, some parameter choice satisfies

    sum_z n_z²≤M+M(M-1)/q.

Cauchy and integer rounding therefore retain at least ceil(qM/(q+M-1)) distinct labels. Multiplication by the common nonzero polynomial L_B does not alter the labels or strict degree bounds. If M>(q-1)² the displayed fraction exceeds q-1, so all q labels occur. No claim about a deterministic efficient parameter-selection algorithm is made.

For the both-far extension version, choose 1,theta_1,...,theta_(s-1),tau linearly independent over B, and replace the first seed source by f0+tau g0. The labels are z_W-tau. Triangular recovery makes all M distinct, while the tau coefficient makes them nonzero. Projecting any strict-degree explanation of the padded first source onto its tau coefficient would explain the padded g on exactly the same coordinates. Therefore its agreement is at most J; interpolation attains J. This projection works because D and L_B have coefficients in B. The previous common-agreement and second-source proofs are unchanged.

There is also an ordinary-list consequence in the code of dimension J+1: from a strict witness h_z to f+z g, the polynomial h_z-zg agrees with f at the same T coordinates and has degree at most J. Its degree-J coefficient is -z, so distinct labels give distinct codewords. This enlarges the code dimension by one; do not call it the original strict code.

## 4. Concrete growing-characteristic regimes

For the full native domain D=F_(p^d), q=N:

| d,s | Guaranteed native labels | Characteristic | Guaranteed additive gap |
|---|---|---|---|
|4,2| strictly more than N/2 | N^(1/4) | floor((1-rho)N^(1/2)/2) |
|5,2| fraction at least 1-O(N^(-1/5)) | N^(1/5) | floor((1-rho)N^(3/5)/2) |
|7,3| fraction at least 1-O(N^(-5/7)) | N^(1/7) | floor((1-rho)N^(4/7)/2) |
|8,4| ALL N labels | N^(1/8) | floor((1-rho)N^(1/2)/2) |

For d=4,s=2, M=(p²+1)(p²+p+1)>q, so the harmonic count exceeds q/2. For d=8,s=4, M>p^16=q², so the all-label conclusion is exact even at equality of the leading exponents. For the other rows, the missing fraction is at most (q-1)/(q+M-1)≤q/M, giving the stated powers with uniform constants.

The same d=8,s=4 domain admits a separate both-far construction in F_(p^40), of size N^5, with M=[8 choose4]_p>N² distinct nonzero labels and the same square-root-order gap. Its guaranteed failure fraction is of order N^-3, not one. More generally the both-far version has M=Theta(N^(s(d-s)/d)) with uniform Gaussian constants, gap Theta_rho(N^(1-s/d)), and field size N^(s+1). For the initially proposed d=11,s=5, internal padding gives M=Theta(N^(30/11)) and gap Theta_rho(N^(6/11)) in a field of size N^6, improving the outside-seed count/gap exponents 25/11 and 5/11 at the same characteristic N^(1/11). The d=11,s=4 choice instead gives count exponent 28/11, gap exponent 7/11, and field size N^5. These preserve the same strict fixed-rate code and both individual agreements J; the tradeoff between the two s choices is explicit.

## 5. Matched baseline and limitations

The existing prime-workspace LOCATORS_TREES_NORMS_TRANSFER.md ALREADY contains the growing-characteristic r=1,d=10,s=4 native-all-label consequence. Its seed H has size N/p, its padding avoids H entirely, and it gives p=N^(1/10), gap p^5-p^4, and CA=J. Thus merely restating that example would not be new. Internal padding raises the characteristic exponent to 1/8 while retaining native failure probability one and square-root-order gap. The gap's explicit leading constant changes, so this is not a coordinate-for-coordinate dominance assertion.

The binary frontier's incomplete Artin--Schreier packet result has p=Theta(N/log N), exact quarter rate, gap Theta(N/log N), challenge field p^4, and guaranteed bad fraction Omega(1/N). It has much faster characteristic growth and larger gap. It does not provide the present native constant/perfect failure guarantee. These are distinct tradeoffs.

The published prime-workspace K=3 first-order families have vanishing rate and characteristic exceeding message degree; some are over prime alphabets and others over extensions. The present construction has FIXED positive rate, but T/N=rho+Theta(p^-s) tends to capacity and is eventually below any fixed positive margin above capacity, including the fixed-rate first-order boundary. Also J~rho p^d is much larger than p. Thus the DKT characteristic guard p>message degree is not met. No first-order tightness, prime-alphabet counterexample, or protocol consequence follows.

The additive domain requires dimension d≥s+2≥4 over Fp. There is no prime-field endpoint: extension-field coordinates cannot be reinterpreted as a prime-field affine received line. The result is a quantified growing-characteristic bridge from the existing locator compiler, with a stronger internal-padding tradeoff, not a new compiler or a solution of the fixed-rate prime-alphabet problem.
