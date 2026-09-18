# Translated-grid correlated label bundles: parameter ledger

September 18, 2026. The proof is in
`translated_grid_polynomial_gap.tex`; a separate constructive audit is
`TRANSLATED_GRID_POLYNOMIAL_GAP_INDEPENDENT_AUDIT.md`.

This supplies polynomially growing fresh-match multiplicity for a
prime-field quadratic bank. It does **not** supply a positive constant
fraction of the native prime labels. No literature-priority assertion
is made here.

## Exact finite ledger inside the asymptotic existence proof

Choose sufficiently large H and a prime p=1 mod4 in (2H^4,4H^4).
Assign disjoint sets of primes in [H/2,H], all in one quartic class,
to the two vertex parts of a C4-free graph. For an edge (a,b), choose
a square theta with theta²=a/b. Unique factorization and p>H^4 make
these bank parameters multiplicatively Sidon.

The projective-plane incidence graph gives
L=Theta((H/log H)^(3/2)) edges. Every bank word
P_theta=theta+X²/theta has A=2L-2 core agreements, on a core of
L(L-1) coordinates.

Set M=floor(L/4), d=floor(M/(64H)), T=A+d, and
n=floor(T²/2)+1. The translated grid x²=(v0+v)/(u0+u),
1<=u,v<=M, retains at least M²/4 distinct noncore coordinates for a
suitable translation. On it g=1/U and f=c0/U, so a bank label is

    lambda+c0 = theta*u0+v0/theta + (a*u+b*v)/(b*theta).

There are at most 3HM possible labels per bank and at most 3M/H
coordinates per fiber. Therefore every bank has at least HM/16
fibers containing at least d retained coordinates. Cross-bank label
collisions are nontrivial affine conditions on the translation. Their
expected count is o(LHM), so at least floor(LHM/32)-1 singleton
threshold labels remain after discarding collisions and one exceptional
zero-polynomial label.

Neutral padding has g=0 and f=X³, at coordinates avoiding every bank
intersection with X³. It changes neither bank agreement nor the source
gap and keeps nonbank agreement below A. The final two sources have
exact individual and ordinary common agreement A. Good witnesses have
agreement at least T, not necessarily exactly T. The threshold obeys

    n*a1(3/n) < A < T < sqrt(2n).

At relaxed threshold A the affine line has exactly L codewords in its
list at every label except one, where zero adds a (L+1)-st. This is a
line-local list statement; it is not a code-wide upper bound.

## Coupled scales and the original open task

At the maximal graph size,

    n = Theta(H³/(log H)³),
    d = Theta(n^(1/6)/log n),
    epsilon=d/n = Theta(n^(-5/6)/log n),
    singleton labels B = Theta(n^(4/3) log n),
    p = Theta(n^(4/3) (log n)^4).

The lower bound for B comes from the construction. The matching order
upper bound for its total exceptional count is the fixed-bank budget:
apart from the zero-polynomial exception, every bad label consumes at
least d of the L*X fresh bank-label incidences. Thus B=Theta(L/epsilon)
and the actual bad-label fraction is Theta((log p)^(-3)), tending to
zero. This does not prove a universal bound proportional to the
relaxed list size divided by epsilon.

Eliminating n gives the lower-count envelope

    B = Omega(epsilon^(-8/5) / (log(1/epsilon))^(3/5)).

This is a coupled lower-bound curve. It neither proves a sharp quadratic
gap exponent nor contradicts upper bounds with different list, rate,
or agreement-excess parameters.

The graph may be thinned. For any L/H tending to infinity with
L<=c(H/log H)^(3/2), the same proof gives

    n~2L²,  d=Theta(L/H),
    B=Theta(n^(3/2)/d),  p=Theta(n²/d^4).

Thus the fixed-bank incidence-budget count is attained up to constants
through a polynomial-gap range. The remaining unachieved part of the
original correlated-bundling target is B=Omega(p), especially with
p comparable to n and d comparable to sqrt(n). The exact-Sidon prime
selection here has a logarithmic density loss even at its largest d.

The mechanism differs from a coherent symmetry orbit: many parallel
integer-grid fibers overlap across banks, while a common random
translation separates their labels. The proof does not require
independence of the fibers or a large stabilizer of an algebraic group.

## Finite evidence is scoped separately

`translated_grid_toy_2026_09_18` contains a verified finite-field replay
with L=27 and d=1, plus a separate integer-fiber test with d>1. The
field replay explicitly overrides the asymptotic d formula; it is not
a finite onset certificate for the polynomial-gap theorem. The theorem
above remains an asymptotic existence statement.
