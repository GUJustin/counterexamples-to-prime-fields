# Prime-field transfer with random directions

September 17, 2026. Independent mathematical derivation. Conditional
results only: the required short-domain prime-field source ratio remains
unproved. No new unconditional prime-field superlinear theorem follows.

## 1. The direction certificate needs no quadratic field size

Let a core over F_p have N distinct coordinates, dimension K, true
maximum T-1, and Delta=T-K>0. Append t fresh coordinates, n=N+t<=p.
The audited direction failure bound is

    B = 2^n p^(-Delta) (1-1/p)^(-t).

An explicit sufficient condition is

    Delta log p > n log 2 - t log(1-1/p).

Since -log(1-1/p)<=1/(p-1), it suffices that
Delta log p > n log 2 + t/(p-1). In particular, for fixed c>0,
Delta>=c n and n growing, B tends to zero whenever p>=n. Thus the
random-direction certificate itself imposes no p>>r^2 requirement and
no p/r divergence when n=Theta(r). Field size matters separately for
the supply of evaluation points and distinct challenge labels.

## 2. Conditional ordinary-CA theorem without common-zero padding

Suppose there are unbounded r and prime-field sources from orbit descent:
length 4r, dimension r, true maximum m in [3r/2,5r/3], and r distinct
nearest candidates. Suppose p>=8r. Keep this entire source as the core
and append t=4r coordinates. Set n=8r, K=r, T=m+1, and
Delta=m-r+1. The final rate is exactly 1/8 and its capacity gap is

    Delta/n in [1/16+1/(8r), 1/12+1/(8r)].

For sufficiently large r the direction bound is below one, because
Delta>=r/2+1 and n=8r. A good direction excludes all ordinary-CA
witnesses independently of all fresh intercepts.

Let S=p-4r>=p/2. The mean evaluation diversity of the r candidates on
fresh points is at least

    mu = r*S/[S+(r-1)^2] >= r*p/(p+2r^2).

Choose the 4r most diverse points, then a good direction, then random
independent intercept translations. Their expected union is at least

    p*[1-exp(-4r^2/(p+2r^2))].

The argument x=4r^2/(p+2r^2) is at most 2. Since
1-exp(-x)>=(1-exp(-2))*x/2 and
p*r^2/(p+2r^2)>=min(p,r^2)/3, this gives

    J >= (1/2)*min(p,r^2),
    J/n >= (1/16)*min(p/r,r).

(The actual constant from these inequalities exceeds 0.57 in the
first line.) Ceilings can be applied to the integer J. Hence if the
same nearest sources satisfy r/p -> 0, this yields superlinear
ORDINARY-CA exceptions over prime fields at exact rate 1/8 and a
capacity gap bounded below by 1/16. Their radii are strictly below
characteristic-based Elias eventually. This is stronger than the
previous full-support MCA conclusion in its type of failure, but does
not assert one exact constant gap.

The ratio condition cannot be removed by any one-parameter affine-line
compiler with n=Theta(r): there are only p scalar labels, so J<=p and
superlinear J/n necessarily implies p/r -> infinity. Random directions
solve the direction-exclusion difficulty, not this cardinality barrier.
The existing orbit argument proves r unbounded, not r/p -> 0.

## 3. Exact gap without claiming an exact rate

Alternatively choose n=16Delta, keep the same core and dimension r,
and append t=16Delta-4r points. Then the capacity gap is exactly 1/16,
but the rate r/(16Delta) varies (asymptotically between 3/32 and 1/8).
Under r/p -> 0 there are enough coordinates eventually, the direction
bound succeeds, and the same diversity/translation argument yields
J=Omega(min(p,r^2)), hence superlinear ordinary-CA exceptions. This
variant must not be described as having both a fixed rate and fixed gap.

## 4. A same-field common-zero alternative with an exponential field bound

There is a deterministic existence replacement for adjoining an
external common-zero coordinate. Let w over F_p on N distinct points
have true maximum M>=K among degree-<K polynomials. For a fresh a,
replace w(x) by (x-a)w(x), append (a,0), and increase dimension to K+1.
All original nearest candidates lift, giving at least M+1 agreements.

There are at most binom(N,M+2) bad choices of a for which the new
maximum exceeds M+1. Indeed, a violating Q that matches at a is
divisible by X-a, and its quotient would have at least M+1 old matches,
a contradiction. Thus it must have M+2 old matches on some support S.
In the quotient of F_p^S by the evaluations of degree-<K+1 polynomials,
this requires

    [x*w] = a*[w].

For a fixed support this equation permits at most one a unless both
classes vanish. The latter is impossible: w is then represented on S
by a polynomial W of degree <=K, and xW also agrees with a degree-<=K
polynomial. Because |S|=M+2>=K+2, this forces deg W<K, contradicting
M. Thus each support excludes at most one scalar a. When M+2>N there
are no such supports and the maximum is automatically preserved.

Consequently p>N+binom(N,M+2) suffices for a good same-field common
zero. Repeating s times succeeds, for example, if

    p > N+s+2^(N+s).

This is only a sufficient bound, not a necessary one. Unlike the
quadratic-extension lemma, it can be exponentially larger than the
source length.

For the descended sources, take s=2Delta-r+1. For large r,
N+s=3r+2Delta+1<5r. Thus the additional conditional hypothesis
p>5r+2^(5r) permits all zeros inside the SAME prime field. Anchor once,
then apply the audited random-direction construction unchanged. It
produces exact rate 1/8, exact gap 1/16, and at least ceil(n^2/192)
ordinary-CA exceptions over F_p. Since this hypothesis gives p>>r^2,
all diversity estimates used for the quadratic-field theorem hold.

This is a genuine prime-field conditional theorem with both parameters
fixed, but its source condition is much stronger than r/p -> 0 and is
not established by Dirichlet plus orbit descent. Arbitrarily large p
alone does not suffice because the selected orbit size r may grow with p.
The same proof allows replacing the exponential sufficient bound by the
actual successive binomial bounds whenever those are smaller.

## 5. Exact arithmetic dichotomy in the existing prime selection

Write k=(p-1)/4 and d=k/r for a nearest polynomial's stabilizer size.
The source primes have v2(k)=1 and no odd prime divisor of k at most R.
Consequently d is either 1, 2, or greater than R. Since p/r=4d+1/r,
the possible ratios are asymptotically 4 or 8, or greater than 4R.
To obtain r/p -> 0 along the existing rough CRT family, it would suffice
to find a nearest polynomial with stabilizer d>2 for arbitrarily large R.
The current proof excludes tiny orbit sizes; it does not exclude the
small stabilizers d=1,2. Dirichlet alone chooses the prime residue class
and does not distinguish these alternatives. Forcing additional factors
of k likewise does not force a nearest polynomial to be invariant under
them. This is the concrete missing stabilizer lemma for that route.

CYCLOTOMIC_PRIME_TRANSFER.md isolates a different sufficient criterion:
a characteristic-zero nearest bank with fixed linear margin and size
tending to infinity would permit arbitrarily large splitting primes for
each source and yield exact fixed-rate, fixed-gap prime ordinary-CA
superlinear examples. The finite-field Dickson lower bound cannot simply
be imported as the missing characteristic-zero source.
