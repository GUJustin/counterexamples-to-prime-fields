# Linear first-order exceptions from a fixed singular cover

September17,2026. Working extension for independent audit. This is a
conditional theorem about actual solutions of a first-order identity,
not a proof that every interpolant meets its singular-cover hypothesis.

## Statement for implicit equations

Let Q(X,z,u,v) be nonzero, with total jet degree<=B and challenge degree
<=H, where B>=1 and H>=0. Let D>=1 and char(F)=0 or p>D. Fix n distinct coordinates, a received
line f+zg, and integer agreement D<A<=n. A nearby solution pair(z,P), deg P<=D,
is called bad if no degree-<=D polynomial agrees with g on its FULL
agreement set (equivalently, it has no full common witnesses).

Suppose a fixed coordinate set S has size s, and E0 is a set of at most
E labels such that every nearby bad pair outside E0 has at most e
SINGULAR AGREEMENTS outside S:

    #{x outside S: P(x)=f(x)+zg(x), Q_v(x,z,P(x),P'(x))=0}<=e.

The hypothesis is uniform over the candidate pairs being bounded. It
does NOT require a candidate-independent separant. Put

    kappa=min(s,floor((2s+D)/3)), L=A-e-kappa,

and assume L>=1. With

    tau=max(0,2D-3), b0=1+tau(B-1),
    T0=b0+tau H, K=H+B T0, q=B+H,
    C=q K+q T0*(n-D)/(A-D)+q n,

the number of bad labels is at most

    E+(n/L) C+n.                                  (1)

The final n can be omitted when kappa=s. If B,H are fixed,
A-D>=eta n, and L>=lambda n for positive fixed eta,lambda, this is O(n).
The X-degree of Q is unrestricted. The result applies to implicit
nonlinear equations in v=P', subject to the stated uniform cover.

## Proof

The established nonsingular-agreement theorem in
`../quasilinear_first_order/REGULAR_AGREEMENTS.md` bounds labels admitting
a bad witness with at least L nonsingular agreements by(n/L)C. This
statement already covers implicit equations and solution-dependent
separants; no new fixed-separant assumption is introduced here.

Outside those labels and E0, choose one bad witness per remaining label.
It has at most L-1 nonsingular agreements and at most e singular agreements
outside S. Therefore it has at least

    A-(L-1)-e=kappa+1

agreements within S. If kappa=s, this is impossible.

Otherwise let B0=kappa+1<=s. By its definition,

    3B0-2s>D.

Two witnesses at one label would agree on at least2B0-s>=3B0-2s>D
coordinates, so the witness with this property is unique. For three
DISTINCT labels, their S-agreement sets have common intersection of size
at least3B0-2s>D. On this intersection the three candidates satisfy the
same affine relation as the labels, since the received word varies
affinely. This is therefore a polynomial identity. If at least three
labels remain, all their candidates lie on the one base-field affine
codeword pencil determined by the first two. If fewer remain, their
number is at most2<=n.

For any affine codeword pencil P_z=F0+zG0, let I be its coefficientwise
common agreement set with f+zg. A coordinate outside I contributes an
extra agreement at at most one label. If a candidate has no extra
agreements, its full agreement set is I and F0,G0 are full common
witnesses. Hence every bad label on the pencil is one of at most n
extra-agreement labels. This proves(1).

This proof uses actual agreement sets and keeps every singular candidate
covered by the uniform hypothesis. It does not discard solutions merely
because their substituted separant is identically zero.

## Factored value-independent separants

For Q=R(X,z)v-Apoly(X,z,u), suppose

    R(X,z)=R0(X)R1(X,z), R0!=0, R1!=0,
    deg_X R1<=e, deg_z R1<=h.

Take S to be the roots of R0 among the actual domain coordinates,
s=|S| (not necessarily deg R0). At most h labels make R1(X,z)
identically zero: use any one nonzero X coefficient to bound them.
Outside those labels, R1 has at most e roots. Thus the theorem applies
with E=h. This includes a fixed singular locus and a bounded number of
moving roots, and imposes no restriction on the value degree of Apoly
beyond the fixed jet degree B.

The same argument applies to implicit equations whenever their substituted
separants admit this root cover uniformly; merely factoring Q_v formally
is insufficient if the remaining factor vanishes identically for some
candidate family. Such families must be covered or counted separately.

## Parameter gain and relation to earlier results

For s>D, L=A-e-floor((2s+D)/3). Up to integer rounding, positive linear
slack requires

    s<(3A-D)/2-(3/2)e-(3/2)lambda n.

This can allow s>A, unlike the earlier separant-degree condition A>s+e.
For s<=D the theorem reduces to the familiar L=A-e-s and adds no n term.

If s<=2D and A>5D/3+e+lambda n, the condition holds. At quarter rate,
the first-order threshold approaches A/D=4(3+sqrt(133))/31, about1.87517,
strictly greater than5/3. Thus a fixed separant of degree at most2D,
or such a fixed factor with o(n) moving roots, cannot produce superlinear
first-order-regime bad labels at a fixed margin in this setting.

The known quadratic isolated Wronskian example has separant
(z-X²)R(X), deg R=D+1. It fits the factored cover with s<=D+1 and e=2;
its many actual algebraic solutions therefore do not imply many nearby
bad labels. The earlier family-specific constant bound is stronger,
but this explanation applies to a wider class of identities.

No analogous conclusion follows for a large moving singular set without
a small fixed cover. That remains a genuine structural target for
counterexamples, particularly when combined with nonlinear interference
in top-degree elimination.
