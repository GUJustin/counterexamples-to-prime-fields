# Sharp isolated-solution growth at every fixed derivative order

September 16, 2026. Twice self-reviewed proof; exact checks pass.
The authoritative integrated statement is in `appendix.tex`.
No independent coauthor review or novelty claim is asserted.
This is a sharpness result for actual algebraic solution counts, not
for full-support proximity-gap error.

## 1. A general upper bound for actual isolated regular solutions

Let d>=1, D>=d, characteristic zero or p>D. Let
Q(X,z,u_0,...,u_d) have jet degree <=B and challenge degree <=H,
with S=Q_{u_d} nonzero on the regular solutions under consideration.
No restriction on its X-degree is needed. In the reduced closure of
actual regular pairs (z,P), deg P<=D, let J0 count isolated components.
Then, putting

    tau=max(0,2(D-d)-1), b=1+tau(B-1),
    K=H+B(b+tau H), q=B+H,

one has J0<=q*K^(d+1)=O_{d,B,H}(D^(d+1)).

Choose a Taylor center transcendental after the actual solution locus.
Set A=Q_X+sum_{i<d}u_{i+1}Q_{u_i}. The reconstruction derivation is

    delta=partial_X+sum_{i<d}u_{i+1}partial_{u_i}-(A/S)partial_{u_d}.

For j>d, the reconstructed jth derivative has denominator
S^(2(j-d)-1), jet numerator degree <=1+(2(j-d)-1)(B-1), and challenge
degree <=(2(j-d)-1)H. This follows from the same quotient-rule recurrence
as Appendix H, with the shift d replacing 1. Clearing to S^tau gives
all Taylor coefficient numerators jet degree <=b and challenge degree
<=tau H. Factorials are invertible since p>D.

Substitute the reconstructed polynomial and all its derivatives into Q,
clear S^(tau B), and take X-coefficient residuals. Each residual has total
initial-data degree <=K. Together with Q(t,z,u_0,...,u_d)=0, of degree
<=q, these describe exactly the actual solutions on S!=0. Initial jets
and reconstruction are inverse regular maps on this open locus.

There are d+2 initial-data variables. Starting with the initial
hypersurface, cut successively by d+1 generic linear combinations of
the residuals. At each step discard positive-dimensional components
where all residuals vanish: none contains a target isolated regular
point. Every remaining component through a target point has a nonzero
residual, so a generic combination cuts its dimension. This retains
the isolated targets through all d+1 steps. Iterated Bezout bounds the
degree by q*K^(d+1). This argument does not assert that the unpruned
intersection is globally finite. On the regular open locus the initial
hypersurface is smooth because Q_{u_d}!=0, so its local dimension at
each target is exactly d+1; no target is prematurely lost in pruning.

## 2. A family attaining the exponent

Fix r=d+1>=2 and let R be monic squarefree of degree N=D+1, all roots
nonzero. Assume characteristic zero or p>D+r. Put

    phi_j=X^j (1<=j<r), phi_r=X^r+z,
    F_j=R phi_j'-P phi_j,
    Q_r=Wronskian(F_1,...,F_r),

where the Wronskian has derivative rows 0,...,r-1 and z is constant.
Then Q_r is a differential polynomial of exact order r-1, jet degree r,
and challenge degree one. Its separant is

    partial Q_r / partial P^(r-1)
      = (-1)^r C_r R^(r-1) [X^r+(-1)^(r-1) z],
    C_r=product_{j=1}^{r-1} j!.

To see this, replace the last derivative row by its highest-jet
coefficient -phi. Move that row to the top; the other rows have
successive highest phi-derivative coefficients R. The determinant is
(-1)^r R^(r-1) W(phi_1,...,phi_r). The latter Wronskian is
C_r[X^r+(-1)^(r-1)z], by the monomial Vandermonde formula.
The pure P^r coefficient is (-1)^r W(phi), so the jet degree is exactly r.
Thus Q_r is nonzero and every polynomial solution is regular.

Each F_j has X-degree <=D+r<p. A polynomial Wronskian of polynomials of
degree less than p vanishes iff the polynomials are linearly dependent
over constants: echelon a basis by distinct leading degrees and use the
nonzero Vandermonde of these degrees. In characteristic zero there is
no degree restriction for this criterion.

The first r-1 columns are linearly independent for every polynomial P.
Otherwise R H'-P H=0 for a nonzero H in span(X,...,X^(r-1)). Such an H
has a root at zero of multiplicity between 1 and r-1, and H'/H has a
nonzero simple pole there, contradicting R(0)!=0 and polynomial P.
Consequently Q_r=0 iff there is a unique monic polynomial

    H=X^r+sum_{j=1}^{r-1}h_j X^j+z

with R H'-P H=0. Its roots must be roots of R, with multiplicities
between 1 and r<p, and every root multiset of size r gives a solution

    P=R H'/H,    z=H(0).

Partial-fraction residues distinguish all multisets. Thus there are
exactly binom(N+r-1,r)=binom(D+r,r)=Theta_d(D^(d+1)) actual regular
isolated polynomial--challenge pairs, with no positive-dimensional
solution component. Their polynomial degree is exactly D (leading
coefficient r). For d=1, this determinant is the negative of the
explicit quadratic equation in Theorem H.3.

## 3. Distinct labels over polynomial-size prime fields

A multiplicative B_r root set, including repeated factors, makes all
size-r products distinct. Such sets of N elements exist by greedy
exclusion in prime fields of size O_r(N^(2r-1)). When adding x,
new products have the form x^j c for 1<=j<=r and c an old product of
r-j roots. Collisions with old products forbid O_r(k^(2r-1)) choices.
Collisions between unequal j forbid O_r(k^(2r-3)) choices, because
the resulting nonzero equation in x has degree at most r. Equal-j
collisions are already excluded by the old B_r property, which implies
B_s for every s<=r by padding with an old root. Also exclude zero and
old roots. The k=0 step can be initialized at one nonzero root.
A prime above the resulting O_r(N^(2r-1)) bound permits the induction.
The case N>=2 holds here. The integrated proof gives the exact forbidden
count as two sums of multiset coefficients. Finite fixtures reach 969,
495, and 462 distinct labels at orders two, three, and four.

## 4. Why even this larger family has constant fixed-gap nearby counts

All normalized candidates W=P/R are sums of r simple reciprocals,
counting multiplicities. At any labeled affine line among these rational
functions, choose a residue coordinate on which two candidates differ.
Every candidate on that line has a residue in {0,...,r}; its residue is
an injective affine function of the distinct label. Thus at most r+1
candidates lie on one labeled affine line, for any label assignment.
This also uses that different candidates have different residue vectors.

Any noncollinear triple has a nonzero rational relation numerator of
degree at most C=3r-2 after multiplying its three degree-r denominators;
the highest term cancels because all W have leading term r/X.
It therefore has at most C common agreeing coordinates outside roots R.
The number of collinear triples among L distinct selected labels is at
most (r-1)*binom(L,2)/3, counting each triple by its three pairs.

As before, let m=n-r0 and t=A-r0, where r0 counts domain roots of R.
The agreement multiplicities obey

    m*(tL/m-2)_+^3 <= C L^3 + m(r-1)L^2.

If L>=4m/t, the left side is at least t^3 L^3/(8m^2).
If t^3>8C m^2, it follows that

    L <= max(4m/t, 8m^3(r-1)/(t^3-8C m^2)).

This is O_{r,eta}(1) at fixed A-D>=eta*n for sufficiently large n.
No fixed-gap superlinear MCA construction follows from the isolated count.

Unlike the r=2 product labeling, collinear triples really occur for r=3:
roots a=1,b=-2 and multiplicities j=0,1,3 in
H_j=(X-a)^(3-j)(X-b)^j give W_j affine in j and labels
z_j=(-1)^3*a^(3-j)*b^j=-1,2,8, also affine at those three j values.
Any generalization of the r=2 noncollinearity argument must retain the
collinear-triple term above.


## Second review and verification record

The upper bound was reviewed for residual saturation, zero-dimensional
versus positive-dimensional components, generic cuts through all target
points, ordinary derivative factorials, and degrees after differentiation
of the reconstructed polynomial. The argument controls isolated points,
not the total degrees of all higher-dimensional solution components.

The construction was checked for the Wronskian characteristic guard,
independence of the first r-1 columns, the sign of the separant,
root multiplicities, and the geometric-versus-scheme interpretation.
The Sidon induction includes both old/new and new/new collisions,
and equal-power collisions reduce to the old B_r property.

For agreement counting, label assignment means one label for each
candidate. Selecting one candidate per distinct nearby label then gives
distinct residue vectors. The r=3 negative example rules out dropping
collinear triples. An r=4 fixture with multiplicity labels attains the
r+1=5 line occupancy and all ten allowed collinear triples. The implicit
convexity inequality and its two-case explicit consequence retain both
terms. No quadratic MCA claim is made.

`verify_family.py`: 760 polynomials, 5270 polynomial--challenge pairs,
15 separant checks through order five, two small-characteristic negative
controls with one extra solution each, four triple fixtures including
nontrivial and maximally collinear controls, and six prime-field B_r
fixtures. `verify_reconstruction.py`: four equations of orders two
through five and 360 finite Taylor checks. Both standard integer/prime-
field evidence and symbolic degree bounds support the written proof;
neither finite checker establishes the generic intersection theorem.
