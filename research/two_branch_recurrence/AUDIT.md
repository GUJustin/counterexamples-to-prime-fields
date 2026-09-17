# Independent audit of triangular Riccati actual-incidence bounds

September 17, 2026. Independently reviewed PROOF.md,
BOUNDED_CHALLENGE_GENERALIZATION.md, SHARED_DENOMINATORS.md, and the
root agent's earlier audit. The stated fixed, moving-monic, and
nonresonant nonmonic theorems pass this mathematical audit. This is not
formal verification, independent human review, or a novelty determination.

## Fixed and moving-monic recurrences

For degree at most D, the coefficient of X^(t+j-1), j>=1, is above every
P² contribution when t>2D. The c=P(0) term is absent under the stated
R-degree restrictions. The remaining system is upper triangular in the
nonconstant message coefficients; division by j is valid in characteristic
zero or p>D. Descending recurrence gives the claimed challenge degrees.
The constant-X residual is monic quadratic in c, and all other residuals
are linear in c. The quoted Bdeg,Adeg,Cdeg,E bounds include every term,
including moving T coefficients. Zero coefficients cause no problem.

The isolated-label proof correctly distinguishes a nonzero c-independent
residual, a nonzero quadratic-linear resultant, a nonzero determinant of
two linear residuals, and the persistent proportional graph case. It
includes singular points and vanishing linear leading coefficients.
If only the monic quadratic remains there are no isolated components.
Monicity excludes vertical factors, so at most two horizontal reduced
components occur and their summed bidegrees obey the stated bounds.

## Shared denominator: nonmonic nonresonant case

For d_j=j*T_t+R_(t-1), every d_j is assumed nonzero as a polynomial,
not nonvanishing at every scalar. The recurrence is valid off their
product Delta. Its rational coefficients can be written N_j/Delta_j,
Delta_j=product_(h=j)^D d_h, with deg N_j<=b+a(D-j).
Multiplication by Delta/Delta_j adds at most a(j-1), hence ALL common
numerators have degree at most K=b+a(D-1). The denominator has degree
at most delta=aD. There is no quadratic-in-D degree accumulation.

Multiplying the identity by Delta² leaves a quadratic constant-X
residual and linear nonconstant-X residuals. The single uniform bound
M=max(2delta,2delta+a,delta+a+K,2K,2delta+b) covers their coefficients.
A quadratic-linear resultant then has degree at most3M, and a pair
determinant at most2M. The proportional-graph exceptional coefficient
has degree at mostM. These establish the stated3M isolated-label bound
on Delta!=0; discarded roots of Delta cost at mostdelta additional labels.
Vertical factors of the constant residual can only lie over Delta=0,
because its quadratic leading coefficient is -Delta².

For a matching coordinate the linear equation in c has coefficients
of degree at most L=max(delta+1,K). Its resultant with a component of
bidegrees(s,r) has degree at most s+rL. This includes the powers of
Delta needed to clear the matching graph's denominator. Since Delta
is nonzero on the retained locus, each resulting scalar gives at most
one point satisfying that coordinate's matching equation. Summed over
components, the per-coordinate nonpersistent incidence bound is M+2L.
The final bound delta+3M+n(M+2L)/(A-D)+2n therefore checks out.

## Actual agreement and common witnesses

The proofs do not infer proximity from a count of formal solutions.
For components with at most D persistent coordinates, each A-near
candidate contributes at least A-D nonpersistent incidences. This
converts the resultant degree count into an actual nearby-label bound.
If more than D coordinates agree persistently, interpolate their given
base-field affine word values to force the ENTIRE message polynomial
to equal F0+zG0 on that component. Thus the witnesses are base-field
polynomials, not merely functions on a geometric component. Every other
coordinate contributes at most one extra-agreement label for that
pencil. At most two components give the2n term. Multiple candidates at
one label do not invalidate an upper bound obtained by counting points.

## Full two-branch locator corollary

For T the domain locator, n>4D, and affine received branches of degree
at most n-1, product coefficients above degree n+D-1 give at most two
labels unless they vanish identically. In the remaining case, if both
branch degrees exceed D, their sum has degree at most n-2 and the fixed
triangular theorem applies. If one branch is a degree-D codeword pencil,
every other solution matches the second branch on n-D domain points.
Pairwise uniqueness follows from n-2D>D. Three-label interpolation needs
n-3D>D and supplies the second affine pencil. These are exactly implied
by n>4D. Thus the claimed actual agreement conclusion, including the
low-degree branch case, is justified.

## Scope and constructive boundary

An identically zero pivot is NOT covered by the shared-denominator
statement. At most one such pivot can occur under p>D and T_t!=0,
but its surviving free coefficient requires a separate proof. No current
claim should quietly replace that coefficient by a determined function.

The previously constructed quadratic isolated family has nonzero pivots
under its characteristic guard. Its nonlinear coefficient and low
leading-X separation cause P² to enter the proposed elimination range.
Thus it lies outside this theorem because of nonlinear interference,
not because nonmonicity or bounded challenge variation alone defeats
the argument. Those distinctions in SHARED_DENOMINATORS.md are correct.

These are genuine actual-incidence theorems for candidates satisfying
one identity in the specified class. They do not supply that identity
for arbitrary nearby RS candidates, establish general first-order MCA
linearity, improve better.codes, or rule out interference-regime
constructions. Fixed challenge-degree bounds are essential to the
claimed uniform O(n) constants.

## General nonlinear-value Newton-degree criterion

The later NEWTON_DEGREE_CRITERION.md also passes independent audit.
The nonlinear X-degree restrictions put every P^j term, j>=2, below
all D elimination equations. The same shared denominator has degree
aD, and all nonconstant message numerators have degree at mostaD.
After multiplication by Delta^ell, each residual has bidegree at most
(M,ell), M=a(ell D+1). Selecting one nonzero X-coefficient h of A_ell
ensures a residual with c-leading coefficient h*Delta^ell. Discarding
roots of h and Delta costs at mosta(D+1) labels.

The curve/point separation is justified. Over the algebraic closure,
every common curve is an irreducible factor of the gcd U of all nonzero
residuals. A vertical common curve forces h*Delta to vanish at its
z-coordinate, so none survives on the chosen open set. Reduced
horizontal factors have summed bidegrees at most(M,ell). An actual
isolated point cannot lie on any of these curves; embedded scheme
structure there is irrelevant to counting actual points.

After dividing all residuals by U, their gcd is1. For a chosen nonzero
quotient G, every factor of G is absent from at least one other quotient.
Over the infinite algebraic closure, finitely many proper linear
conditions can therefore be avoided to choose a constant linear
combination H coprime to G. Division and constant combinations preserve
the upper bidegree bounds. Their proper intersection has degree at most
2Mell on P1 x P1. This bounds every remaining isolated point, including
singular points, without the false inference that linear independence
implies coprimality. A constant quotient gives the easier empty case;
M=0 produces no isolated z-labels.

The actual matching equation has bidegree at most(aD+1,1). The same
persistent-coordinate argument gives total nonpersistent incidence
allowance n[M+ell(aD+1)], and at mostell affine witness components.
Thus the full displayed bound

  a(D+1)+2ell*M+n[M+ell(aD+1)]/(A-D)+ell*n

is valid. As before, the result covers only candidates satisfying the
specified identity, with fixed a and ell, nonzero polynomial pivots,
and the stated Newton-degree separation. It is broader than the Riccati
case but is not an unrestricted first-order proximity theorem.

The general Newton criterion is in fact characteristic-free when ALL
polynomial pivots d_i are explicitly assumed nonzero. The recurrence
never divides by i alone. Coefficients i may vanish in the field, but
this is harmless if the corresponding pivot remains nonzero. All later
root counts, interpolation, curve gcds, resultants and proper intersection
bounds hold in arbitrary characteristic; inseparability does not increase
the number of distinct points beyond the degree bound. Thus its original
p>D guard is redundant. The separate assertion that at most one pivot
can vanish identically DOES require p>D and should retain that guard.
