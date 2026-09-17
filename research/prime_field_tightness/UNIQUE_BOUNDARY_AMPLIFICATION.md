# Nearest-codeword lists give unique nearby line points

September17,2026. Extension of the existing interpolation-pool padding
argument to arbitrary boundary words and unrestricted padding size.
Locally proof-audited; no novelty or independent-review claim.

## Finite statement

Let w be a word on N distinct points D of F_p, with maximum agreement
exactly M among degree-<k polynomials, where k>=2 and M>=k+1. Let L
be the COMPLETE number of polynomials attaining M. Choose an integer
k+1<=T<=M and let U be the number with at least T old agreements.
For q>=1 put n=N+q and A=M+1. Suppose

    p >= N+q+(k-1)*binom(U,2),                         (1)
    [q*U+binom(q,2)*U^2]/p + binom(n,A)/p^(A-T) < 1.  (2)

There is an n-point Reed--Solomon code of dimension k over the SAME
prime field and a line f+zg with exactly qL nearby labels at threshold A.
Each nearby word has EXACTLY ONE nearby codeword and exactly A maximum
agreements. Every other word on the line has exactly M maximum
agreements. Label0 is among the latter. There is no ordinary correlated
agreement at threshold A, because f itself is farther than that radius.

This is an exact two-distance profile, not a global list-size bound for
the code. Its far/near distances differ by one coordinate, not by a
constant fraction of the capacity gap.

## Proof

Let P be the pool of all U candidates with at least T old agreements.
Each pair differs at all but at most k-1 field points. By (1), choose
q unused coordinates x_j so evaluation on P is injective at each.
On the old coordinates set f=w,g=0; on the new coordinates set
g=1 and choose f(x_j)=b_j independently uniformly in F_p.

The label assigned to (P,j) is P(x_j)-b_j. Within one coordinate they
are distinct. Across different coordinates, each pair collides with
probability1/p. A label is zero with probability1/p. Thus the first
term of (2) bounds the chance that some pool label is zero or two pool
labels collide. Outside that event, every polynomial in the pool has
at most one new agreement at any label, and each nonzero assigned label
belongs to exactly one pool polynomial.

It remains to exclude ALL codewords outside the pool at ALL labels.
Fix an A-subset of the new domain containing r<T old coordinates and
u=A-r new ones. If r<k, the old interpolation equations leave at most
p^(k-r) polynomials, and allowing a scalar z gives at most
p^(k-r+1) new-value vectors P(x_j)-z. The probability that the random
b_j match one of these vectors on this support is at most
p^(k+1-A)<=p^(T-A), since T>=k+1.
If k<=r<T, the old equations determine at most one polynomial. Allowing
z gives at most p new-value vectors and probability at most
p^(1-u)=p^(r+1-A)<=p^(T-A).

Every outside-pool nearby candidate would have such a support, so a
union bound gives the second term of (2). Supports incompatible with
the old word only reduce this count. Possible rank deficiencies in
the new evaluation map also reduce it; injectivity is not assumed.

Choose offsets outside both bad events, which is possible by (2).
A pool polynomial has at most M old and at most one new agreement.
It reaches A exactly when it belongs to the complete nearest list and
uses one of its q assigned labels. All qL labels are distinct and
nonzero; no other nearby polynomial exists, proving uniqueness and
the exact near count. At every other label, a nearest source polynomial
still has M old agreements, and no polynomial has M+1 total agreements.
In particular label0 has maximum agreement M, ruling out correlated
agreement at threshold A for the entire line.

## Consequences for the tightness target

With q=N the rate is EXACTLY halved. If the source gap is eta=(M-k)/N,
the target gap is eta/2+1/(2N). The additive1/(2N) term must not be
silently dropped when asserting a separately fixed exact gap. The
construction is sufficient for exponent lower bounds against statements
uniform over gaps bounded below by a fixed positive constant.

If the source has a growing nearest list and a polynomially bounded
list U at the looser threshold T=k+ceil(eta*N/2), then on prime-field
sequences p=N^{omega(1)} both (1),(2) hold eventually. Indeed U and q
are polynomial in N, while A-T is a positive fraction of N. The output
has exactly NL ordinary-CA failures, each with a unique nearby codeword,
and all remaining scalar challenges are one coordinate farther away.

The requisite polynomial upper bound for U is an explicit dependency
if imported from a capacity list theorem. The primary statement in
Jeronimo, ECCC TR26-169, Theorem1.1 supplies such a bound uniformly
in p at a fixed gap; its statement was checked, not independently
re-proved here: https://eccc.weizmann.ac.il/report/2026/169/ . The finite
lemma above has no external list-theorem dependency.

Without that dependency one may use U<=binom(N,k)<=2^N and T=k+1.
For q=N, the deliberately generous condition p>=8*N^2*4^N implies
(1),(2), since A-T=M-k>=1. Thus sufficiently large prime fields suffice
unconditionally for every boundary source word satisfying the hypotheses.
This does not permit enlarging the field of a characteristic-specific
source construction while assuming its identities survive.

The missing ingredient remains an unbounded fixed-gap NEAREST list in
the required prime-field/length regime. Arbitrary large lists do not
automatically yield large nearest lists: closer codewords may exist.
For arbitrary lists, the earlier exact-scaling compiler proves only
full-support MCA failure, and ordinary CA may coexist.

## Complete finite replay

check_unique_boundary_amplification.py checks every scalar challenge and
every determining pair for two dimension2 examples. OverF263, N5 grows
to n10, with two source nearest codewords, exactly10 unique nearby labels,
and253 other labels with maximum agreement3. OverF2003, N7 grows to n14,
with three source nearest codewords, exactly21 unique nearby labels,
and1982 other labels with maximum agreement3. The latter source word has
interpolation degree6, strictly greater than its maximum agreement3;
it is not covered by the older low-degree-center shortcut. In both cases
the nearby maximum is4, and label0 is farther away.

The checker also exhausts all343 padding-offset triples in a small F7
mechanism fixture. Exactly96 give the asserted three-label two-distance
profile;42 have some outside-pool nearby candidate. This fixture does
not satisfy the sufficient union-bound inequality and is identified as
a mechanism check only. The two main fixtures satisfy it exactly with
failure bounds260/263 and1211/2003.
