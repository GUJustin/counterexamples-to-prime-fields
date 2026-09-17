# Nonmonic moving derivative coefficients: a shared denominator stays linear

September17,2026. Generalization for independent audit. This supersedes the
unproved-extension paragraph at the end of BOUNDED_CHALLENGE_GENERALIZATION.md.

## Statement and numerical caps

Let D>=1 and F be any field. Consider

    T(X,z)P'-P²+R(X,z)P-S(X,z)=0, deg P<=D.          (1)

Let deg_X T=t>2D, deg_X R<=t-1, deg_X S<=t+D-1, and assume

    deg_z T<=a, deg_z R<=a, deg_z S<=b

for fixed nonnegative integers a,b. Write tau(z)=T_t(z)!=0 and
r(z)=R_(t-1)(z). Assume every pivot

    d_j(z)=j tau(z)+r(z), 1<=j<=D                  (2)

is a NONZERO polynomial. It may vanish at particular challenges.
Set

    delta=aD, K=b+a(D-1),
    M=max(2delta,2delta+a,delta+a+K,2K,2delta+b),
    L=max(delta+1,K).

For any received line on n distinct coordinates and agreement A>D,
outside at most

    delta+3M+n(M+2L)/(A-D)+2n                      (3)

labels, every nearby actual solution of(1) has the full common-witness
property with degree-<=D polynomials. Thus the bound is O_{a,b,eta}(n)
when A-D>=eta*n and D<=n. No regularity/separant assumption is needed.

The result is about solutions covered by this equation, not every close
RS candidate in the absence of such an identity. It does not assert
that generic first-order interpolants have the required triangular form.

## Polynomial pivots and a single common denominator

Write P=c+sum_(j=1)^D a_j(z)X^j, initially over F(z). In the coefficient
of X^(t+j-1), P² is absent since t>2D, and c is absent since j>=1 and
R has X-degree at most t-1. The coefficient of a_j is d_j. Thus

    d_j a_j=S_(t+j-1)-sum_(i>j) K_ji a_i,

where each K_ji=i T_(t+j-i)+R_(t+j-1-i) has z-degree<=a.
Let Delta_j=product_(h=j)^D d_h, and Delta=Delta_1. Descending induction
shows

    a_j=N_j/Delta_j, deg N_j<=b+a(D-j).

Indeed multiplying the numerator equation by Delta_(j+1) clears every
higher denominator Delta_i, which divides Delta_(j+1). Its terms all have
degree at most b+a(D-j). Passing to the common denominator gives

    a_j=W_j/Delta,
    W_j=N_j Delta/Delta_j,
    deg W_j<=b+a(D-1)=K, deg Delta<=delta.

Thus repeated pivots or overlaps among their roots do not produce an
O(D²) degree. The product denominator suffices and remains of degree O(D).
Discard the at most delta roots of Delta. On its complement the recurrence
is bijective between actual solutions and pairs(z,c) satisfying the
remaining coefficient equations.

## Residual bidegrees and isolated labels

Put W=sum_(j>=1)W_j X^j, so P=c+W/Delta. Multiply(1) by Delta².
The constant-X equation is

    E0=-Delta²c²+Delta²R_0 c+Delta T_0 W_1-Delta²S_0. (4)

Every other coefficient has c-degree at most1. All their coefficient
polynomials in z, as well as those of E0, have degree at most M: the
possible degrees are 2delta, 2delta+a, delta+a+K, 2K and 2delta+b.
In particular the residual remains QUADRATIC in c.

The same resultant/proportionality argument as PROOF.md applies on
Delta!=0. A c-independent nonzero residual has at most M roots. A
quadratic--linear resultant has degree at most3M; a determinant of two
linear residuals has degree at most2M. If both kinds vanish identically,
all solutions away from one linear coefficient's roots lie on a persistent
rational graph. Remaining isolated labels number at most M. If every
linear residual vanishes, the nonvertical part of E0=0 has no isolated
components. Therefore at most3M nonexcluded labels are isolated.

Delete vertical factors of E0, which can only be supported on Delta=0
because its c-leading coefficient is -Delta². The remaining plane equation
has at most two reduced horizontal components and their summed bidegrees
are at most(M,2). The actual curve components form a subset of these.

## Actual agreement incidences

A match at coordinate x is now

    Delta c+W(x,z)-Delta(f(x)+zg(x))=0.             (5)

Its z-degree is at most L and its c-degree is1. On a component C with
bidegrees(s,r), unless the equation is identically zero, the resultant
has degree at most s+rL. Away from Delta=0 a root gives at most one
point satisfying(5). Across all curve components the degree allowance
is at most M+2L for each coordinate.

If a component has at most D persistent agreement coordinates, each
A-near point contributes at least A-D nonpersistent incidences. This
bounds their labels by n(M+2L)/(A-D). More than D persistent coordinates
force P=F0+zG0 by interpolation over the base field. Such an affine graph
has the full-witness property outside at most n extra-agreement labels.
There are at most two components. Including discarded pivot roots and
isolated labels gives(3).

## The resonant boundary

Under p>D and tau!=0, at most ONE pivot can vanish identically:

    d_j-d_i=(j-i)tau !=0 for 1<=i<j<=D.

If d_(j0)=0, the recurrence above that index still works. At j0 it yields
a compatibility condition rather than determining a_(j0). If that
condition is a nonzero rational function of z, its numerator already
restricts solution labels to finitely many roots. If it vanishes
identically, an additional free message coefficient survives. The proof
above does not cover this case. In particular one must not silently divide
by a zero pivot or treat that coefficient as polynomially determined.

The surviving coefficient enters subsequent top equations linearly, so a
future multihomogeneous analysis with two coefficient parameters may still
give linear degree. That is a possible extension, not a theorem here.

## Comparison with the known sharp isolated families

The quadratic isolated example in first_order_actual_components is

    (z-X²)(R P'-R'P+P²)+2X R P-2R²=0,
    deg R=D+1.

Its derivative coefficient has degree t=D+3. Its linear-P coefficient has
leading coefficient D+3 while the derivative leading coefficient is -1,
so its would-be pivot is D+3-j, nonzero under its p>D+2 hypothesis.
Thus its quadratic isolated count is NOT caused by resonance.
Instead, the nonlinear coefficient z-X² has X-degree2, so the P² term
can have degree2D+2, which reaches or exceeds the top elimination range.
For D>=3, also t<=2D. This family is outside the triangular hypothesis
for every D>=1. Dividing by z-X² introduces rational X coefficients and
does not repair the hypothesis.

Likewise the actual-curve example R P'-R_X P+P²=0 with
R=X^(D+1)+zX-1 has t=D+1<=2D and nonzero pivots under its stated
characteristic guard. The surface example (X-z)P'-D P=0 does have the
resonance j=D, but exhibits only linear actual degree growth.

The constructive boundary suggested by existing examples is therefore
NONLINEAR INTERFERENCE in the top-X equations, often t about D, rather
than simply adding nonmonic coefficients or bounded challenge degrees.
A lower-bound search should build actual agreement into such an equation;
repeating the existing isolated-root count alone remains insufficient.
