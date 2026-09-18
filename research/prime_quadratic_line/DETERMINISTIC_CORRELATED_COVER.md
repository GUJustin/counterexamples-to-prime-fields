# Deterministic full-fiber cover of the greedy quadratic line

**Independent audit: PASS, September 18, 2026.** This gives polynomial absolute source gaps with superlinear exceptional counts and singleton lists throughout the line. It does not control the field size relative to the length.

## Statement

Let `L>=25`, `s>=1` be integers. Choose a prime `p` with `2s | p-1` such that the subgroup `H=(F_p^*)^s` has order greater than `5L^4+32L^2`. Then there is a length

    n=s(2L^2-2L+1)

prime-field RS code of dimension `k=2s+1`, and sources `F,G` with individual and common agreement exactly `A=2s(L-1)`, such that exactly

    M=L(L^2-L+1)+1

nonzero line parameters have a codeword with agreement greater than `A`. Every such list is singleton. Every exceptional label has agreement at least `T=s(2L-1)=A+s`; all but the extra projective parameter have maximum agreement exactly `T`. Thus the same `M` is the exact exceptional count at threshold `T`.

The parameters satisfy `T^2=(k-1)n-s^2`, and lie above the first-order threshold (the original `s=1,L>=25` comparison implies the covered one by monotonicity of the first-order curve in the rate). Alternatively the asymptotic comparison follows directly for all sufficiently large `L`, uniformly in `s>=1`.

## Construction and greedy bound

The even cyclic group `H` contains `-1`. Apply the existing integer Sidon exponents to a generator of `H`: the guard `|H|>32L^2` ensures distinct bank parameters `a_i^2` and distinct core nodes `+/-a_i a_j` for `i<j`. Put

    P_i(Y)=Y^2/a_i^2+a_i^2,   Q_i(X)=P_i(X^s).

Use all `s` preimages of every core node, with `f=a_i^2+a_j^2` and `g=0`. Write `N0=L(L-1)` and `t=N0+1`. Choose `t` distinct fresh base points greedily in `H`, avoiding core and zero, and set on their full fibers `f=x^(4s)`, `g=x^(3s)`.

At a fresh base point `y`, bank `i` has its unique possible label

    lambda_i(y)=(P_i(y)-y^4)/y^3.

Exclude labels 0 and 1, and require all `Lt` labels to be mutually distinct. After `j` fresh points have been selected, at most

    N0+1+j+8L+4jL^2

field elements are forbidden: core/zero/prior points, the degree-four equations for labels 0 and 1, and degree-four equations equating a new label to a prior one. New labels at the SAME base point can coincide only when two bank polynomials agree there, and all those points are already in the core. Since `j<=N0`, the displayed bound is less than `5L^4` for `L>=25`. Thus a permitted point in `H` always exists. All root counts are for nonzero polynomials: the label equations have leading term `-Y^4`.

## Exact classification, including non-descended candidates

Each bank `Q_i` has exactly `A` core matches and, at any fixed finite label, either zero or one fresh full fiber. Therefore it has either `A` or `T` matches. Exactly `Lt` finite labels have a fresh fiber, with one bank at each label.

For every nonbank `Q` of degree at most `2s`, core matches are at most `sL`: count each matching core coordinate against its two agreeing bank polynomials and use the degree-`2s` root bound for each nonzero `Q-Q_i`. At fresh coordinates, matches against `f+lambda g` are roots of the MONIC polynomial

    X^(4s)+lambda X^(3s)-Q(X),

so there are at most `4s` of them over the entire fresh domain. Consequently total agreement is at most `sL+4s<=2s(L-1)=A` for `L>=6`. This proof includes every non-descended candidate; no interpolation or good-reduction argument is required.

The blacklist makes labels 0 and 1 have exact maximum agreement `A`. For common agreement of `(f,g)`, any nonzero degree-at-most-`2s` direction explanation has at most `2s` core matches and `3s` fresh matches, hence at most `5s<A`. The zero direction restricts matches to the core, where the maximum is exactly `A`. Thus common agreement is exactly `A`.

Set `F=f`, `G=f+g`. Their individual agreements are exactly `A`, and common agreement is unchanged by the invertible source transformation. For `z!=-1`, use `lambda=z/(1+z)` and scale the witness by `1+z`; this transports all `Lt` exceptional labels to finite nonzero labels. At `z=-1`, the word is `-g`: zero agrees on all `sN0` core coordinates, while any nonzero candidate has at most `5s<=A` matches. This is one additional singleton. Since `sN0>=T` for the stated `L`, it is counted at threshold `T` as well. These arguments prove the exact line-wide classification above `A`.

## Prime existence, exponents, and what this does not claim

For EACH prescribed pair `(L,s)`, Dirichlet's theorem supplies arbitrarily large primes congruent to 1 modulo `2s`, so the subgroup-order guard can be met. This avoids Bombieri–Vinogradov but gives no claimed effective upper bound on `p/n` and no constant exceptional fraction of the field.

Taking `s=Theta(L^b)`, `0<b<1`, gives gap `Theta(n^(b/(b+2)))` and `M~L^3=Theta(n^(3/(b+2)))`, which is superlinear. Rate and relative source separation still vanish. It also realizes restricted conic-bank order sharpness: in the ORIGINAL normalization the audited bank bound is asymptotic to `4L^3`, whereas this construction has `M~L^3` and may be placed in arbitrarily larger fields. The source change rescales witnesses depending on the parameter, so this fixed-bank comparison is made before that change and then transported by the parameter bijection.

This deterministic cover is simpler than the random off-density argument when field-size control is not required. It does NOT replace the BV construction's prescribed polynomial field-size relation or its constant-density regime. It strengthens the existence of line-wide singleton constructions with polynomial absolute gaps; it does not establish fixed-rate sharpness or a universal upper-bound improvement.
