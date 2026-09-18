# Prime-alphabet random fibers: independent character and finite-parameter audit

The prime-alphabet version passes the character and compiler checks.
Its uniform subgroup estimate is elementary: the mixed sums are Jacobi
sums, whose generic absolute value is sqrt(p), with absolute value1 in
the two exceptional cases. Randomly retaining O(log p) image tags then
gives product coverage of all Fp*, with the same exact source and nearby
agreement profiles as the extension-field compiler.

The asymptotic statement below is conditional on the stated prime family
p=Theta(m^beta), m|(p-1). This note does not re-prove the separate
prime-in-progression existence input. The finite theorem itself has no
such number-theoretic prerequisite beyond its explicit conditions.

## Uniform Jacobi estimate, including every exception

Let p be prime, m>=2 divide p-1, and put L=(p-1)/m. Let

    H=(Fp*)^m=mu_L,
    b in Fp*\H,
    K={characters psi of Fp*: psi|H=1}, |K|=m.

All multiplicative characters, including the trivial one, are extended
by zero at0. Fix any nontrivial character chi of Fp*. Substituting a=b*t
gives the exact identity

    sum_{a in Fp*} chi(b-a)psi(a)
       =chi(b)psi(b) J(psi,chi),
    J(psi,chi)=sum_{t in Fp} psi(t)chi(1-t).

The complete case split is

    psi=1:                J(psi,chi)=-1;
    psi=chi^(-1):         J(psi,chi)=-psi(-1);
    psi!=1, psi*chi!=1:   |J(psi,chi)|=sqrt(p).

The two exceptional twists are distinct because chi is nontrivial.
The case in which both Jacobi arguments are trivial cannot occur.
The first equality is character orthogonality. The second follows from
t/(1-t), which bijects Fp\{0,1} with Fp\{0,-1}. In the generic case,
the identity J(psi,chi)=G(psi)G(chi)/G(psi*chi) and the absolute Gauss-sum
formula |G(nontrivial character)|=sqrt(p) prove the claim.
These identities, with the same zero-extension convention, are documented
in [Conrad, Gauss and Jacobi Sums, Theorem 2.4, Corollary 2.5 and
Theorem 2.6](https://kconrad.math.uconn.edu/blurbs/gradnumthy/Gauss-Jacobi-sums.pdf).

Averaging over K gives, for every nontrivial chi,

    |sum_{a in H} chi(b-a)| <= sqrt(p).

More precisely, if epsilon=1 when chi|H=1 and0 otherwise, exactly
1+epsilon exceptional twists lie in K, so the bound improves to

    sqrt(p) - (1+epsilon)(sqrt(p)-1)/m.              (1)

In contrast with the degree-six extension-field calculation, the generic
rank is already1 here. The estimate is uniform over all chi, including
characters trivial on H. The condition b outside H guarantees that every
factor b-a indexed by H is nonzero.

## Exact finite sampling and product-coverage criteria

Reserve any a0 in H before sampling, and set U=H\{a0}. Every nontrivial
character has population mean of modulus at most

    mu=(sqrt(p)+1)/(L-1).                           (2)

For a uniform s-subset G of U and any beta>mu, the already proved
finite-population exponential-moment argument gives

    Pr[exists chi!=1: |sum_G chi(b-a)|>beta*s]
       <=4(p-2)exp[-s(beta-mu)^2/4].                (3)

The proof in `SMALL_BIAS_SAMPLING_PROOF.md` uses only the population
mean bound, so it applies here directly; its earlier Katz extension-field
hypotheses are not being asserted for degree1.

For a successful G, every Fp* element is a product of exactly r distinct
factors b-a whenever, with theta=r/s,

    (p-2)(s+1)exp[-theta(1-theta)(1-beta)s]<1.       (4)

This is the fixed-cardinality Cauchy coefficient bound followed by
character orthogonality. It uses no nontriviality assumption on chi^j.

A simple sufficient package, valid for any fixed0<eta<=1/2, is

    kappa=eta(1-eta), C=max(128,8/kappa),
    s=ceil(C log p),
    p>=C+2, s<=L-1, L>=4sqrt(p)+5.                (5)

The last inequality gives mu<=1/4. With beta=1/2, the failure probability
in(3) is at most4/p. For every successful G, all integer subset sizes
eta<=r/s<=1-eta satisfy(4) simultaneously, with total Fourier error
at most1/p. Indeed

    (p-2)(s+1)exp[-kappa*s/2]
      <=(s+1)/p^3<=1/p,

using s+1<=C log p+2<=Cp+2<=p^2. Consequently every prescribed product
has at least C(s,r)(1-1/p)/(p-1) representations. All prerequisites in(5)
are finite and checkable.

## Exact degree and agreement bookkeeping

Take one successful G and define

    D={x in Fp*: x^m in G union {a0}},
    n=(s+1)m.

The condition s<=L-1 ensures n<=p-1. Every included tag has exactly m
preimages. For the requested strict degree bound J, write

    J-1=(r-2)m+w, 0<=w<m,

and require2<=r<s together with(4), or the density condition in(5).
Choose w points B in the reserved fiber {x:x^m=a0}, and let R be their
monic locator. Put Y=X^m and

    f=R*(Y^r-b^r)/(Y-b),
    g=-R/(Y-b).

Since b is outside the image H and nonzero, Y-b has no root anywhere
in Fp. The word f is a monic polynomial of degree
A=(r-1)m+w=J+m-1. Root counting bounds each source's agreement by A:
for g the agreement numerator is R+(Y-b)h, which is nonzero since
deg R=w<m. Interpolation of both quotient-variable functions on any
r-1 tags of G, followed by multiplication by R, attains A on the same
coordinates with witnesses of degree<=J-1. Thus

    agr_J(f)=agr_J(g)=CA_J(f,g)=J+m-1.             (6)

For every lambda in Fp*, product coverage provides an r-subset S of G
with V_S(b)=-lambda, where V_S(Y)=prod_{a in S}(Y-a). Let
P_S(Y)=Y^r-V_S(Y) and

    h_S=R*[P_S(Y)-P_S(b)]/(Y-b).

Then deg h_S<=w+(r-2)m=J-1, and

    f+lambda*g-h_S=R*V_S(Y)/(Y-b).

This witness matches at exactly
T=rm+w=J+2m-1 coordinates. Hence all p-1 nonzero pencil labels are
nearby at T; the lambda=0 word and projective direction g are both far.
On the affine interpolation line (1-t)f+t*g, exactly the p-2 parameters
t not in{0,1} are nearby. These are different label counts and should
not be conflated. The witness's exact number T of matches is not an
upper bound on the best agreement of a nearby word.

## Asymptotics under the prime-family input

Suppose m tends to infinity and p=Theta(m^beta), m|(p-1), with fixed
beta>2. Then

    L/sqrt(p)=Theta(m^(beta/2-1)) -> infinity,
    s=Theta(log p)=o(L).

Thus(5) holds eventually, and for J=floor(rho*n) the actual r/s tends
to rho. Any fixed eta<min(rho,1-rho) suffices. The cited beta>12/5
prime-family input, if supplied with these congruence and growth
properties, more than meets the character requirement beta>2.

The exact source gap and capacity margin are

    (T-A)/n=1/(s+1)=Theta(1/log n),
    (T-J)/n=(2m-1)/[(s+1)m]=Theta(1/log n).

Also n=Theta(m log m), so

    p=Theta((n/log n)^beta),
    p/J -> infinity.

This is a prime-alphabet family with a chosen union of monomial fibers.
The evaluation domain generally is not a multiplicative subgroup. The
argument therefore does not supply a certificate on the prescribed
NTT domain, nor establish novelty relative to prior quotient constructions.

An explicit finite instance, independently of any prime-family existence
claim, is saved in `prime_finite_fixture/`: p65537, m2, n2842, J1421,
source/common agreement1422 and nearby agreement1424. Its tag set is
certified by an exact sixth Fourier moment rather than by a probability
claim about an unspecified sample.
