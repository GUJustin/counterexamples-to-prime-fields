# Quarter-rate converse with exact weights and arbitrary multiplicity

September 17, 2026. New extension of the restored fixed-multiplicity
support converse. Locally audited with independent exact matrix checks;
no independent human/formal review. This is still a dimension-counting
method limitation, not an intrinsic code lower bound.

## Exact model and conclusion

Let N>=12 be divisible by4, k=N/4, D=k-1, and let A be an integer with
k<A<=N. Let m>=1 be ANY integer, including multiplicities that grow with
N. Take a finite monomial jet support S closed under decreasing the Y_0
exponent. For each (u,b) in S retain all X^x Y_0^u Y_1^b satisfying

    x+D*u+(D-1)*b < m*A.

Jets with no permitted X coefficient can be discarded. Let G be the
exact global source dimension and R its exact local rank in the quotient
by (T^i E^j : i+2j>=m), E=Y_0-TY_1. Characteristic zero or greater than
every retained total jet degree is assumed.

If the interpolation certificate uses the sufficient count G>N*R, then,
with a_0=(3+sqrt(133))/31 and c_0=(1-2a_0)/8,

    A/N > (1-8/N)*(a_0+c_0/m)+8/N^2.                 (1)

In particular, uniformly over every m=m(N),

    A/N > a_0-8*a_0/N+8/N^2.

Thus allowing growing multiplicity cannot improve the asymptotic
quarter-rate agreement threshold for this exact model. Relative to
N*a_0, a finite-length improvement in the required agreement is bounded
by a constant number of coordinates. This extension is proved here for
monomial supports with the displayed full coefficient ranges. The earlier
nonmonomial theorem remains a fixed-jet-space leading-benefit result.

## Exact rank with the global coefficient cutoff

Fix q=u+b and write

    L_q=m*A-(D-1)*q,
    U_q={u : (u,q-u) in S and u<L_q}.

The exact source dimension on this diagonal is

    G_q=sum_{u in U_q}(L_q-u).

In the local expansion, the grade g=x-b is preserved. The coefficient
cutoff is x<m*A-D*q+b, or g<m*A-D*q, independent of b. Put ell=q+g.
The same binomial-Vandermonde argument as the restored rank formula gives

    R_q=sum_{ell=0}^{min(m,L_q)-1}
                min(#{u in U_q : u<=ell}, m-ell),     (2)

with an empty sum if L_q<=0. The row capacities q+1 and ell+1 need not
be displayed because the active-column count is already at most both.
The characteristic guard makes the relevant binomial minors nonzero.
Both G and R are sums over q.

The local rank is independent of the coordinate and received value:
X-translation preserves the full coefficient prefixes, and Y_0-translation
preserves S and only lowers the weighted degree. Thus R is the local
rank used in the n-times-local-rank certificate, not a special rank at
one artificially chosen received symbol.

## A half-rank lemma

For any integer L>=1 and U subset {0,...,L-1}, set

    G_U=sum_{u in U}(L-u),
    R_U=sum_{ell=0}^{L-1} min(#{u in U:u<=ell},L-ell).

Then G_U<=2*R_U. Here is an injection proof, requiring no asymptotics.
List u_1<...<u_t. The G_U cells are pairs (j,ell) with u_j<=ell<L.
The R_U retained cells additionally satisfy j<=L-ell. Send each discarded
cell to

    (j',ell')=(L-ell,L-j).

Since j>j', both j' and ell' are valid. Distinctness of the ordered u's
implies u_j>=u_j'+j-j', so u_j'<=ell-j+j'=L-j=ell'. The image is
retained because j'<=j=L-ell'. This map is injective. Hence the number
of discarded cells is at most the number retained, proving the lemma.

If 0<L_q<m, (2) is at least R_U with L=L_q. Thus G_q<=2R_q. For N>=2,
such a diagonal contributes G_q-NR_q<=0 and may be removed without
harming positive surplus. Empty diagonals may also be removed.

## Reduction to the already audited saturated comparison

Keep only diagonals with L_q>=m, obtaining S_0. This removes a final
segment of total degrees, so downward Y_0 closure is preserved. On S_0,
formula (2) is exactly the saturated local rank r_m(S_0), and

    G_0 > N*r_m(S_0)

whenever G>N*R. Every retained q satisfies

    q <= m*(A-1)/(D-1).

Write a=A/N. The exact source contribution of (u,b) is

    (m*A-D*q+b)/N = m*a-q/4+(q+b)/N.

Since b<=q, this is at most m*a_star-q/4, where

    a_star = A/N + 2*(A-1)/(N*(D-1))
           = (A*N-8)/(N*(N-8)).

Each retained jet has a positive exact coefficient count, so its benefit
at a_star is positive too. Consequently the restored quarter-rate
saturated comparison has positive surplus at agreement a_star.
If a_star<1/2, its audited finite-multiplicity converse gives

    a_star > a_0+c_0/m.

If a_star>=1/2, the same inequality is automatic, since
 a_0+c_0/m <= a_0+c_0 <1/2. Rearranging gives (1).

No passage to a continuum limit with m fixed was used in this reduction.
The only imported input is the restored saturated comparison, which
already holds separately for every integer m. Thus the final statement
is uniform in m and N under the explicit characteristic guard.

## Exact checks and limits

verify_finite_length.py independently expands all permitted X coefficient
columns and computes their rank for1920 small instances, confirming (2).
It checks the half-rank inequality on32752 nonempty subsets through L14,
and replays the deletion and benefit domination on the same1920 cases.
All pass under the384MiB watchdog. These checks corroborate the formulas;
the injection and reduction above prove the quantified statement.

A failed count G>N*R does not prove that the global interpolation kernel
is zero. Dependencies among different coordinates can make the true
global rank smaller than N*R. The theorem also does not cover arbitrary
global sources with selectively omitted coefficient monomials, other
local ideals, or a finite-length nonmonomial degeneration. It gives no
lower bound on actual Reed–Solomon list size or line exception counts.
