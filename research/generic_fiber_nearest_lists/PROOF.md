# Generic translated power fibers preserve complete nearest lists

September 17, 2026. Locally audited algebraic argument, with two complete
finite-field fixtures. No independent human review or novelty claim.
This scales block length while preserving a source list; it does not
make that list grow.

## Statement over a function field

Let a_1,...,a_N be distinct elements of an algebraically closed field K,
and let w_i belong to K. Fix k>=1 and an integer B>=2 not divisible by
the characteristic. Let t be transcendental over K. On the BN roots of

    X^B=t+a_i,  i=1,...,N,

put received value w_i throughout fiber i. Use code dimension Bk.
For every integer A>=k+1, the COMPLETE list at agreement threshold BA
is exactly

    { Q(X^B-t) : deg Q<k, Q(a_i)=w_i on at least A source nodes }.

The list is taken over the algebraic closure of K(t), so this is not a
restriction to candidates defined over the ground function field.
Each candidate's agreement count is B times its source agreement count.
Consequently, if the source maximum agreement is M>=k+1, the new maximum
is exactly BM and the complete nearest list has exactly the same size.
The rate k/N and capacity gap (M-k)/N are preserved EXACTLY.
No bound on the interpolation degree of the received word is assumed.

More generally, the same conclusion at threshold BA holds for degree
cap D whenever floor(D/B)=k-1 and BA-B>D. We use this variant below.

## Independent rotations of the fibers

Choose u_i with u_i^B=t+a_i. The splitting field E of all these
polynomials over F=K(t) has Galois group (Z/BZ)^N. Indeed the classes
of t+a_i are independent in F^*/F^{*B}: a product
prod_i(t+a_i)^{e_i} can be a Bth power only if every e_i is divisible
by B, by taking the valuation at t=-a_i. Equivalently, adjoining roots
successively has degree B at each step. At the new place t=-a_i all
previous factors are units with Bth roots in the power-series ring
K[[t+a_i]], whereas the new radicand is a uniformizer. The new root has
ramification index B there, forcing extension degree B. K contains all
Bth roots of unity and B is invertible, so the extensions are Galois.
Thus there is an automorphism rotating any one fiber while fixing all
other fibers pointwise.

## Every sufficiently close candidate descends

Let P, of degree at most D=Bk-1, agree at h>=B(k+1) lifted nodes.
Its coefficients lie in E, because interpolation on D+1 agreeing nodes
recovers P from nodes and received values in E.

For any automorphism sigma rotating only fiber i, at least h-B>=Bk>D
of the agreements lie outside that fiber. At those nodes P and
sigma(P) agree with the same received values. Therefore P=sigma(P).
These rotations generate the Galois group, hence P belongs to F[X].
In particular, one agreement in fiber i forces agreement on its entire
fiber. Write

    P(X)=sum_{j=0}^{B-1} X^j Q_j(X^B-t),   deg Q_j<=k-1.

There are at least k+1 fully agreeing fibers. Reduction modulo
X^B-(t+a_i) shows Q_j(a_i)=0 for j>0 and Q_0(a_i)=w_i on these fibers.
Thus Q_j=0 for j>0. Interpolation on any k source nodes also shows that
Q_0 has coefficients in K, not merely in K(t). Therefore P=Q_0(X^B-t)
for a source candidate. The reverse implication is immediate.
The argument with arbitrary D uses h-B>D and floor(D/B)=k-1 verbatim.

Notice the distinction between independent Galois rotations over K(t)
and deck rotations X->zeta*X of one fixed specialized polynomial.
The latter rotate every fiber simultaneously and alone would not prove
the statement. Introducing transcendental t is essential to this proof.

## Arithmetic specialization to prime fields

Suppose the source coordinates and word are algebraic numbers. For each
fixed B, all but finitely many algebraic choices of t preserve the full
list correspondence at every threshold BA with A>=k+1, as well as the
source agreement profile. Here is a finite certificate formulation.

For each subset S of B(k+1) lifted nodes, degree<Bk interpolation on S
is a rank condition. If it is inconsistent generically, retain one
nonzero augmented Vandermonde minor. If it is consistent generically,
the preceding proof identifies its unique interpolant as a composed
source polynomial; this identity persists wherever the nodes remain
distinct. There are only finitely many S. Taking norms of the retained
nonzero minors to the t-line shows that only finitely many t-values
are excluded. Also exclude t=-a_i and all specialization poles.
Consequently one can choose t rational outside a finite excluded set.
All resulting nodes lie in a number field.

Reduce this finite configuration at sufficiently large completely split
primes of a normal closure. Exclude primes dividing the finitely many
nonzero rank minors, denominators, and node or value differences used
above. The SAME complete list correspondence then holds over F_p,
indeed over its algebraic closure. Such split primes are arbitrarily
large. Their size is not quantitatively controlled here.

This does not transfer a bank available only in one positive
characteristic to other characteristics. Applying the function-field
statement to that bank retains its characteristic and may require an
extension field. The prime-field conclusion above requires a
characteristic-zero source.

## Exact fixed-parameter unique-nearby lines from arbitrary finite seeds

Let a characteristic-zero source have dimension k=d+1, d>=1, maximum
agreement M>=d+2, and complete nearest list L. Choose a source coordinate
a_* through which ell nearest polynomials pass. Averaging gives an
anchor with ell>=ceil(M L/N). Fix any positive integer r.
For every B>=2, the preceding construction and sufficiently large split
primes produce a received line with

    n=B(N+r), dimension Bd, threshold BM,
    rate=d/(N+r), gap=(M-d)/(N+r),
    exactly (Br+1)*ell nearby labels,

such that every nearby word has exactly one nearby codeword and maximum
agreement BM. Every other label, including zero, has maximum agreement
BM-1. In particular ordinary correlated agreement at threshold BM fails.
Both rate and gap are fixed exactly as B varies. Far/near separation is
only one coordinate. No global list-size bound is asserted.

To prove this, first use degree cap Bd on the BN lifted nodes. The
variant above applies at BM, since M>=d+2 implies BM-B>Bd. Its complete
nearest list consists precisely of the source nearest polynomials
composed with X^B-t. Remove one node x_* over a_* and divide both word
and each anchored candidate by X-x_* after subtracting w_*.
The resulting word on BN-1 nodes has dimension Bd and maximum agreement
BM-1, with complete nearest list exactly ell. Indeed multiplying any
candidate by X-x_* and adding w_* gives degree at most Bd and restores
an agreement at x_*. A better candidate would contradict maximum BM;
an equally good candidate corresponds exactly to a source nearest
polynomial through a_*.

Apply ../prime_field_tightness/UNIQUE_BOUNDARY_AMPLIFICATION.md to this
anchored source with q=Br+1. Its sufficient field inequalities can always
be met by taking a sufficiently large split prime: use the uniform pool
bound U<=binom(BN-1,Bd) and threshold T=Bd+1. The exponent in its
outside-pool error is

    (BM-1)+1-T = B(M-d)-1 >= 1.

All quantities other than p are fixed after B is fixed. That compiler
gives the exact profile and count above. Since zero is farther than the
nearby threshold, there cannot be ordinary correlated agreement.

For the finite lifted Dickson seed, N=16,k=4,M=6 and L>=8. An anchor
has ell>=3. Taking r=8 gives n=24B, dimension3B, threshold6B, and both
rate and gap equal1/8. At least24B+3=n+3 labels are uniquely nearby.
The complete value of ell for that characteristic-zero seed is not
computed here. This illustration is not stronger than all existing
fixed-gap lower bounds, and is not a superlinear example.

## Verification and remaining limitation

`verify.py` independently exhausts all determining supports for the
source a=(-2,-1,0,1,2), w=(2,1,0,1,2), k=2, M=3, L=2, and two
finite-field specializations. B=2 over F1009 at t=3 checks210 supports;
B=3 over F10009 at t=53 checks5005 supports. Their complete nearest
lists have size2 and agreements6 and9 respectively, exactly as predicted.
Noncomposed controls have agreements4 and6, below the claimed thresholds.
These finite checks support the implementation, not the general proof.

The transformation preserves list size rather than multiplying it.
It therefore supplies a flexible way to use arbitrary finite
characteristic-zero seeds, but does not settle fixed-gap exponent
optimality. A growing source bank is still needed for that purpose.
