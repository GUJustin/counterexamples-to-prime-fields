# Prime-field amplification of lists and nearest-codeword lists

September 17, 2026. A generalization/application of the existing anchored
and averaged padding lemmas, not a new fixed-gap lower-bound construction.
It removes the extension-field requirement in the boundary-value note,
at the cost of a quantitative union bound and field-size dependence.

## Arbitrary source lists: full-support MCA version

Let L distinct degree<k polynomials each agree at >=A points with an
arbitrary word on N prime-field coordinates, with A>=k>=2. For any
1<=q<=p-N, the same construction below gives a line of dimension k-1
and length N-1+q with at least

    ceil[p*(1-(1-mu/p)^q)]

full-support MCA-bad labels at agreement threshold A. Choose an anchor
with ell>=AL/N incident candidates, and define mu using ell exactly as
below. Neither maximality of A nor an upper bound on q beyond p-N is
required for this version.

Indeed each anchored candidate has >=A-1 old agreements and any label
in its padding image adds one new agreement. A direction interpolant
of degree<=k-2 would vanish at >=A-1>=k-1 old coordinates, forcing it
to be zero, but it must equal1 at the new agreement point. Thus it
cannot explain the candidate's entire agreement support. Other nearby
candidates, including persistent ones, do not change this conclusion.
No claim of absence of ordinary correlated agreement follows here.

For p>=2NL and q<=N this gives J>=q*A*L/(4N). Thus polynomial source
lists L=N^c at a fixed gap give full-support exceptional counts of
order N^{c+1}, with the exact new gap (A-k+1)/(N-1+q) explicitly
accounted for. This is the existing appended-coordinate compiler with
an averaged field-size condition, not a new list construction.

### Exact rate-and-gap halving

Suppose A>=k+1 and p>=2N+1. Take q=N+1, so the new length is exactly
2N, and use dimension k (one larger than the minimal anchored dimension).
Every selected quotient still lies in the code. Its old agreements
number >=A-1>=k, forcing any degree<k direction interpolant to vanish
identically, which contradicts a new agreement with direction1.
The averaging proof gives the stronger saturation-aware bound

    J >= ceil[p*A*L/(p+3*A*L)] >= min(A*L,p)/4.

Indeed R>=p/2 implies mu>=ell*p/(p+2*(k-2)*ell). Since q>=N and
k-2<=N, putting t=A*L/p and using N*ell>=A*L gives

    q*mu/p >= N*ell/(p+2*N*ell) >= t/(1+2*t).

Use 1-(1-u)^q>=1-exp(-qu)>=qu/(1+qu), valid for0<=u<=1,
to obtain J>=p*t/(1+3*t). For t<=1 this is at least p*t/4;
for t>=1 it is at least p/4. If the source has exact rate
rho=k/N and gap eta=(A-k)/N,
the output has EXACT rate rho/2 and gap eta/2. There is no parameter
drift or residue-class qualification. The hypothesis p>=2N+1 provides
all N+1 padding coordinates. In particular, p need not be of order NL
unless one wants the unsaturated order-NL count.

Consequently a source list lower bound L=N^c at fixed rho,eta over
superpolynomial prime fields would force Omega(N^{c+1}) full-support
exceptions at fixed rho/2,eta/2. Any universal O(n^b) full-support bound
at those output parameters forces source lists O(N^{b-1}), whenever the
field is large enough for the displayed construction. In particular,
a universal linear full-support bound would imply constant fixed-gap
list sizes whenever p/N tends to infinity: if L were unbounded, both
A*L/N and p/N would diverge. This is a one-way implication;
no converse from constant lists to a linear line bound is proved.

This explains why the extra power of n in a list-to-MCA transfer can be
necessary IF the list exponent itself is attained. Neither premise is
established by the present lower-bound constructions.

## Nearest-codeword source lists: ordinary CA version

Let D subset F_p have N distinct points, k>=2, and let w:D->F_p have
maximum agreement exactly M with degree<k polynomials. Assume M>k and
there are L distinct polynomials attaining M. For any

    1<=q<=min(p-N,M-k+1),

there is a received line over F_p on n=N-1+q points for dimension K=k-1,
with no ordinary correlated agreement at threshold M, and at least

    ceil[p*(1-(1-mu/p)^q)]

nearby scalar challenges. Here an anchor can be chosen with ell>=ML/N
incident candidates, R=p-N, and

    mu=ell*R/[R+(ell-1)*(k-2)].

All evaluation points, received values, witnesses, and challenges lie in
the SAME prime field. No received-polynomial degree assumption is needed.

## Proof

Choose an anchor a in D contained in at least ML/N agreement supports.
For the ell corresponding candidates form

    Q_P=(P-w(a))/(X-a),
    f(x)=(w(x)-w(a))/(x-a), g(x)=0   (x in D minus {a}).

The Q_P are distinct of degree<=k-2, each with exactly M-1 old agreements.
No degree<=k-2 polynomial has M old agreements: multiplying by X-a and
adding w(a) would contradict maximality of M for the original word.

For unused x let s_x be the number of values {Q_P(x)}. Every pair of
distinct Q_P agrees on at most k-2 points, so Cauchy--Schwarz gives

    (1/R)*sum_x s_x >= ell*R/[R+(ell-1)*(k-2)] = mu.

Choose the q unused points with largest s_x, set g=1 there, and choose
their f values independently uniformly in F_p. The expected union of
the label sets {Q_P(x)-f(x)} has size

    p*(1-product_x(1-s_x/p)) >= p*(1-(1-mu/p)^q).

Every label in this union has M agreements with a selected candidate.
For any hypothetical common witness pair F,G of degree<=k-2: if G=0,
its joint agreements lie on the old domain and number at most M-1; if
G is nonzero, there are at most k-2 old and q new joint agreements,
at most k-2+q<=M-1. Hence no correlated agreement at threshold M.

## Explicit large-prime consequence

If p>=2NL, then R>=p/2 and R>=(ell-1)*(k-2), hence mu>=ell/2.
Also q<=N and ell<=L imply q*ell/(2p)<=1/4. Therefore

    J >= p*(1-exp(-q*ell/(2p))) >= q*ell/4 >= q*M*L/(4N).

Thus boundary lists of size L in prime fields at least of order NL
give order NL exceptional challenges when M/N and q/N are positive
constants. Polynomial-size L=N^c gives exponent c+1; merely unbounded
L gives a superlinear count without necessarily any fixed exponent gain.
L may be replaced by any selected subfamily before applying the lemma.

The new parameters are exactly

    rate=(k-1)/(N-1+q), gap=(M-k+1)/(N-1+q).

These equations must be enforced when claiming a separately fixed exact
gap or rate; uniform positive lower bounds alone do not establish that
quantifier. The construction gives no whole-line list uniqueness and
does not assert a far point. Its conclusion is ordinary-CA failure.

## Implication for the existing Dickson route

The extension-field separation trick was convenient, not inherently
necessary. However, the existing Dickson source has N proportional to p.
Its field cannot satisfy p>=2NL for growing L, and every prime-field
line has only p=O(N) scalar labels. Consequently this lemma does NOT
turn that source into superlinear prime-field exceptions. A source over
larger prime fields remains the missing ingredient. Passing to a larger
prime does not preserve characteristic-specific polynomial identities.

This proof uses the same incidence and random-translation argument as
AVERAGED_PADDING.md, but maximality of the source agreement replaces
its global received-polynomial degree assumption.
