# Proof and review record

September 16, 2026. Twice self-reviewed; no independent coauthor review
or novelty claim. The authoritative complete statements and proofs
are in `appendix.tex`.

## 1. Generic evaluation projections

For an actual j-dimensional component C defined before the Taylor
centers, choose j generic forms P(t_i)+lambda_i*z. At an infinity point,
the coefficient and z directions are not all zero, so one form is a
nonzero polynomial of two parameters (t,lambda). Its zero set has
dimension at most one. The incidence of an infinity point (dimension
<=j-1) and j vanishing forms therefore has dimension <=2j-1, less
than the 2j-dimensional parameter space. A generic center misses
infinity. Projective linear projection to P^j is consequently a
morphism with ample hyperplane pullback, hence finite, and its degree
is deg C.

The coefficient functions and z generate the function field. Their
differentials span its j-dimensional cotangent space over the perfect
algebraically closed field. Evaluation forms span those linear
functions, so j independent generic such forms have independent
differentials. The finite projection is separable. Generic affine
fibers are reduced and have deg C points. Generic target values also
avoid singular loci, intersections with other actual components,
and the boundary where the separant at t0 vanishes.

That separant boundary is proper: the actual component has dense
regular locus, and t0 is transcendental after the actual component
is fixed. Choosing t0-dependent arbitrary Taylor images would not
justify the infinity argument; the actual locus must come first.

The same proof works without a challenge. Each form P(t) then has one
parameter. The infinity incidence has dimension <=j-1, below the
j-dimensional parameter space of j forms.

## 2. Source sections and residuals

Taylor reconstruction and degree bounds are exactly those proved and
checked in Appendix I. Before residuals are imposed, the Taylor map
on the initial hypersurface S!=0 already has a linear left inverse:
take its derivatives through order d and retain z. Thus
it is a locally closed immersion. The initial hypersurface is smooth
there since Q_{u_d}!=0.

The first evaluation section is u0=c0-lambda0*z. The initial equation
has degree <=q in d+1 remaining variables. Each subsequent section
has numerator degree <=T; coefficient residuals have degree <=K.
The j-1 further generic evaluation hyperplanes cut the initial
hypersurface properly on the regular open locus, leaving local
dimension <=d+1-j at every selected actual section point.

At each target, the full residual ideal now has isolated zero set:
generic actual sections avoid intersections with other components.
Choose d+1-j generic residual combinations to isolate all targets,
pruning positive-dimensional components on which all residuals vanish.
No such component can contain a target. Iterated Bezout gives
q*T^(j-1)*K^(d+1-j). Components on S=0 can be discarded because
no target lies there; no global zero-dimensional intersection is
asserted. Source sections may be singular away from the targets:
proper dimension cuts, not global smoothness, are what this step needs.

With the challenge fixed, use q=B, T=b, K=B*b and one fewer initial
variable. This gives I0<=B*(Bb)^d and
Ij<=B*(Bb)^(d-j)*b^(j-1) for 1<=j<=d.

## 3. Sharp positive-dimensional family: full classification

For r=d, e>=1, D=re, set L=eP*partial_X-P' and take the Wronskian
of L applied to X,...,X^(r-1),X^r+z. Its separant is
(-1)^r*(product j! for 1<=j<r)*(eP)^(r-1)*(X^r+(-1)^(r-1)z).
The pure P^r coefficient is e^r*Wr(phi_1',...,phi_r'), nonzero.
Its X-degree is bounded by r(r+1)/2, independently of e.

The columns have degree <=D+r-1<p. Zero Wronskian is therefore
constant linear dependence. This gives some projective H of degree
<=r with h0=z*h_r and eP H'-P'H=0. For nonzero P, P/H^e has
zero derivative and rational degree <=D<p, so P=c H^e. Conversely
all such powers work. This handles lower-degree H correctly:
if h_r=0 then h0=0 and z is free. The zero polynomial is in the
closure; it is singular for r>1, regular for r=1.

The initial working proof classified only P(0)!=0 and speculated that
other components could occur. Full projective dependence removes
that uncertainty: all solutions belong to the same relative power
cone. No extra component is asserted.

The family h0=z*h_r is isomorphic to A^1 x P^(r-1), hence irreducible.
Its power-map image is projectively proper over A^1. Its relative
cone is closed and irreducible of dimension r+1, and is the closure
of the dense nonzero regular family.

The full power map P^r -> P^D has no base point, pullback O(1)=O(e),
and is birational onto its image by monic coefficient recovery.
The image degree is e^r. Projection of the joint family forgetting z
is birational onto its affine cone, so joint degree is at least e^r.
On any fixed z, the source is P^(r-1); the same calculation gives
fiber degree exactly e^(r-1). The exact joint degree is unnecessary
and has not been claimed.

## 4. Sharp isolated fibers and affine graphs

For squarefree R of degree D+1 take Wr(R*(X^j)'-P*X^j : 0<=j<=d).
Its separant is (-1)^(d+1)*R^d*product(j!,1<=j<=d), nonzero even
at P=0. For p>D+d the Wronskian criterion classifies all solutions
as R H'/H with H of degree <=d and root multiset supported on R.
The empty multiset gives P=0. Distinct residues distinguish all
binom(D+d+1,d) solutions. A free challenge gives one degree-one
constant-polynomial graph per solution.

This attains the isolated fixed-fiber and joint curve exponents.
It also disproves any attempt to bound the ENTIRE generic fiber by
O(D^(d-1)): the smaller bound excludes its isolated points.

## 5. Linear full MCA for the logarithmic-derivative family

In this family each normalized candidate P/R has residues in
{0,...,d}. A nonhorizontal graph line has at most d+1 distinct-label
points because one residue is injective along it. A horizontal line
fixes P and has at most n bad labels: every genuinely bad support
contains a coordinate with g!=0, forcing one label. This handles
candidate reuse across challenges.

A noncollinear triple has at most 3d-1 common agreeing coordinates
outside R's roots. Its rational numerator degree has that bound;
no cancellation of the leading residue sum is assumed here because
H's degree may vary. Pair counting bounds collinear triples by
(max(n,d+1)-2)*binom(L,2)/3. Convexity yields the displayed cubic
inequality and hence O_{d,eta}(n), as A-D>=eta*n and r0<=D+1.
Only p>d is needed for this residue argument. The family classification
uses the stronger p>D+d guard separately.

## 6. Verification scope

Two exact standard-library checkers pass. Full power-family enumeration
covers 252,730 polynomial--label pairs via 36,140 polynomials, including
zero and all lower-degree boundary powers. Forty sections count 1,574
reduced points, up to 625 in one section. They are exact reduced
sections of the projected power images and fixed-label fibers, not
numerical estimates of the joint degree. Forty-five separants are
checked through order five.

The characteristic-three negative control has 30 extra pairs. A
characteristic-five boundary fixture passes despite lying outside
the sufficient strict guard; no necessity of that guard is asserted.
The fixed-equation checker exhausts 7,203 polynomials and checks
16 separants through order four. It also checks 12,236 rational triples
and a four-label example that reuses the zero candidate on genuinely
bad full supports. Neither checker establishes the
generic-projection/Bezout theorem; that is the written proof above.
