# Why several root-product classes cannot be merged in this template

The proposed shortcut is to retain the six common leading coefficients
at M=256,h=136 while merging at least five product classes. That would
remove the numerical deficit if all resulting witnesses shared one
received affine line. The standard rational identity forbids this,
even when each root polynomial is allowed its own nonzero normalization.

## Lemma: normalized root products on an affine rational line

Let E be a field and put Y=X^B. Let R be monic, R(0) nonzero, and
T=Y(Y-alpha), with alpha nonzero. Fix polynomials F0,F1. For distinct
parameters gamma in a set S, suppose

    F0 + gamma F1 - T P_gamma = c_gamma R V_gamma(Y),

where c_gamma is nonzero, V_gamma is monic of degree h, deg P_gamma<k,
and D=deg R+Bh exceeds k-1+2B. Suppose the constants V_gamma(0) belong
to a set C of cardinality M.

Then either all V_gamma(0) are the same, or |S|<=M.

Proof. Write a,b for the coefficients of X^D in F0,F1. The degree
inequality and monicity imply c_gamma=a+b gamma. In particular this
affine expression is nonzero on S. Evaluating the identity at X=0 gives

    V_gamma(0) = (F0(0)+gamma F1(0))/(R(0)(a+b gamma)).

A fractional linear function with nonvanishing denominator is either
constant or injective: equality at two distinct arguments implies
F1(0)*a-F0(0)*b=0, in which case it is constant throughout S.
Thus a nonconstant function maps S injectively into C, proving |S|<=M.
No assumption on the characteristic or the base field is needed.

For the candidate B=1024,M=256,h=136,k=131072, deg R=1023,

    D=140287 > k-1+2B=133119.

The root products lie in mu_256 (the sign is positive because h is even).
Therefore any bank of more than256 labels of this form has one common
product. A family of roughly2^58 labels cannot merge even two products
through scalar normalization or affine reparametrization within this
identity. Normalizing all constants to one merely moves the varying
product into the monic leading term; the lemma explicitly covers that
attempt through c_gamma.

## Common polynomial shifts cannot identify the existing separate lines

For a fixed core R and pole alpha, the standard line associated with a
reference V is

    f0=R V(Y)/[Y(Y-alpha)],  f1=-R/(Y-alpha).

Let V and W have different constants. If shifting f0 by a multiple of
f1 and a codeword P could identify their lines, then on the evaluation
domain

    T P = R(V(Y)-W(Y)+sY)

for some scalar s (up to an immaterial sign convention). Both sides have
degree below n=262144, so equality at all n distinct evaluation points
is a polynomial identity. The left side vanishes at0 while the right
side equals R(0)(V(0)-W(0)), which is nonzero. This is impossible.
Thus taking codeword cosets or changing the affine origin does not make
these separately constructed product-class lines coincide.

## Scope

These are exact obstructions to the pinned rational construction and its
scalar normalizations. They require the displayed polynomial identity
with a common R and denominator T. They do not rule out a different
denominator, a support-dependent core, additional error roots, or a new
construction whose identities wrap modulo the evaluation-domain
polynomial. In particular, they are not a global upper bound on the
largest list or on all possible received lines.

The archive's `better_codes_further.md` already noted that equal norms
do not supply equal constants and that normalizing constants changes
leading coefficients. The lemma above gives the explicit affine-line
obstruction, including arbitrary nonzero scalar normalizations, rather
than merely charging another generic coefficient constraint.

No improved better.codes bound follows.
