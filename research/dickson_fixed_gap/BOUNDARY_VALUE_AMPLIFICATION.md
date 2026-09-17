# Boundary lists, value diversity, and ordinary correlated agreement

September 17. Pure coding-theoretic lemma; locally proof-reviewed.
This is a conditional route, not a superlinear counterexample theorem.

Let D be N distinct elements of F_p and let w:D->F_p. Fix k>=2 and
suppose the maximum agreement of any degree-<k polynomial with w is
exactly M>k. Let L be any nonempty family attaining that maximum.
Take q distinct unused base-field coordinates U, with

    1 <= q <= M-k+1.

For x in U put V_x=|{P(x): P in L}|. Over every extension F of F_p of
degree at least two, there is a received line for a Reed--Solomon code
on N-1+q base-field coordinates, of dimension k-1, with at least

    ceil((M/N) sum_{x in U} V_x)

distinct nearby labels at agreement threshold M, and no correlated
agreement of that size at all. This statement permits value collisions;
it does not require the field to be large enough for injective evaluation
of the entire list at every padding point.

## Proof

For each possible anchor a in D let L_a={P in L:P(a)=w(a)}, and let
V_{a,x}=|{P(x):P in L_a}|. For each distinct value v at x, choose one
P with P(x)=v. It agrees with w at M possible anchors. Consequently

    sum_{a in D} V_{a,x} >= M V_x.

Sum over x in U and select an anchor a for which
sum_x V_{a,x} >= (M/N) sum_x V_x. In particular L_a is nonempty.
On D\{a}, set f(x)=(w(x)-w(a))/(x-a), g(x)=0. Every candidate

    Q_P(X)=(P(X)-w(a))/(X-a), P in L_a,

has degree <k-1 and exactly M-1 old agreements. No polynomial of that
degree has M old agreements: multiplying by X-a and adding w(a) would
give an old degree-<k polynomial with M+1 agreements. The assertion also
holds over F; k matching base-field nodes force base-field coefficients.

Choose theta in F\F_p. At each x in U set f(x)=theta*x and g(x)=1.
For each distinct candidate value v=Q_P(x), designate the label
z=v-theta*x. Evaluation of Q_P at x is an invertible affine transform
of evaluation of P, so the number of labels in this block is V_{a,x}.
The blocks are disjoint because (v-v')=theta*(x-x') with v,v',x,x' in
F_p forces x=x'. A selected candidate has exactly one agreement on U
and its M-1 old agreements, hence exactly M total.

If a correlated explanation has nonzero direction polynomial, it has
at most k-2 zeros on the old domain and at most q new agreements, so
at most k-2+q<=M-1 common agreements. If its direction polynomial is
zero, its agreement is confined to the old domain and the boundary
argument again gives at most M-1. This proves the claim.

## Application to the three-coset route

For the family in UNBOUNDED_BOUNDARY_LISTS.md, N=3k and M>=5k/4, and
there are k unused base-field points. Thus q can be a positive fraction
of k. If value diversity averaged over these unused points were
unbounded along the family, this lemma would yield a superlinear
nearby-label count with no correlated agreement, and a capacity gap
bounded away from zero. The characteristic-based Elias condition would
then hold for all sufficiently large p.

The required unbounded value diversity is NOT proved. An unbounded
polynomial orbit does not imply an unbounded value set on one coset:
an arbitrary two-valued function on k points can be interpolated by a
degree-<k polynomial and may have a large orbit. The special maximum-
agreement condition on the other three cosets would have to be used.

Also, a gap bounded below is not automatically one fixed exact gap
throughout a family. Any claimed contradiction to a remainder controlled
only separately at each exact gap would need to address that distinction.
No such contradiction is asserted here.

## Exact-rate conditional formulation

The rate need not drift. In the prime-selection argument impose p=5 mod7
instead of p=-1 mod7, leaving all other small odd prime conditions and
p=9 mod16 unchanged. The CRT class is still coprime to its modulus,
k still has no small odd prime factor, and now k=1 mod7. Set

    q=(k-15)/7,  n=3k-1+q=22(k-1)/7,  K=k-1.

For sufficiently large k, q is positive, lies within the unused coset,
and satisfies q<=M-k+1. The resulting rate is exactly 7/22, while its
gap at threshold M is greater than 7/88.

Take the entire nearest-codeword list, which is invariant under H.
Its value diversity V is the same at each unused-coset coordinate,
because multiplication by H permutes both the coordinates and the
polynomial list. The lemma gives

    J >= (5/12) q V,
    J/n >= (5/264-o(1)) V.

Thus unbounded V along these selected primes would produce superlinear
ordinary-CA failure counts at one exact rate and gaps uniformly bounded
away from zero, with all evaluation points still in the prime field and
strictly below characteristic Elias for large p. This remains conditional
on V being unbounded. It does not make the actual agreement fraction M/n
constant, and the earlier fixed-gap-remainder qualification still applies.
