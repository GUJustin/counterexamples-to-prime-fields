# Elliptic two-coset complements: exact shared-line target

This note gives necessary and sufficient linear-algebra conditions for a SPECIFIED collection of omission supports to lie on one received line. It does not prove existence of that line, source farness, or superlinear distinct labels. No scan or elliptic implementation is included.

## Parameters and actual support population

Let ell>=5 be an odd prime different from the field characteristic, and assume all ell-torsion points of an elliptic curve are rational over the coefficient field. The nonzero torsion points modulo sign give n=(ell²-1)/2 distinct x-coordinates. For each order-ell subgroup H, there are t=(ell-1)/2 nonzero H-cosets modulo sign, each supplying ell x-coordinates. Choose two distinct such classes, giving an omission set U of size2ell.

There are exactly

M=(ell+1)*binom((ell-1)/2,2)

DISTINCT omission sets. Indeed, the lift of U to the torsion group is a union of four affine H-lines. Its translation stabilizer contains H and is not the full torsion plane (its size4ell is less thanell²). Thus its stabilizer is exactly H, recovering the subgroup. The two coset classes are then recovered as well.

For two distinct sets from the same H, their intersection is either0 orell. For different H, it is EXACTLY8: each of the four affine H-lines intersects each of the four affine H'-lines once; these16 points are distinct, nonzero, and sign-paired.

Set strict message dimension k=n-4ell+1 and redundancy r=4ell-1. The unslacked agreement n-2ell is ABOVE the finite Johnson threshold. The proposed tested threshold is T=n-2ell-5, corresponding to at most2ell+5 errors. Its exact Johnson difference is

T²-n(k-1)=-ell²+20ell+30<0 for ell>=23.

The high-rate first-order expansion gives

n*a1(k/n)=n-2ell-13/2+O(1/ell),

so T is eventually above that curve, by a limiting1.5 coordinates. This note does not substitute that asymptotic expansion for any desired finite interpolation certificate. The ell11 fixture can test the algebraic common-line hypothesis, but its slack-five threshold does not have the stated Johnson placement.

## Syndrome formulation

Let P_D(X)=prod_(x in D)(X-x) and put w_x=1/P_D'(x). A parity-check matrix for degree-<k RS has columns

h_x=w_x*(1,x,...,x^(r-1))^T.

Every at-most-r columns are independent. Let S_U be their span for x in U. For any received vector f, write s_f=Hf. Then f+lambda*g has an explanation with all errors supported in U if and only if

s_f+lambda*s_g lies in S_U.

This is necessary and sufficient, since H is surjective and its kernel is exactly the RS code. Any proposed pair of syndrome vectors can be lifted to actual received vectors; this statement alone places no bound on their distances to the code.

For a genuine two-dimensional syndrome plane L=span(s_f,s_g), every support with dim(L intersection S_U)=1 specifies one projective challenge point. A fixed affine chart may omit one such point. If L is contained in S_U, every challenge is explained off U, a degeneracy that cannot be treated as many distinct support-certified exceptions with far endpoints. Different supports may specify the same projective point; counting supports is not counting labels.

## Exact linear Pluecker test

For each support choose a quotient map pi_U:E^r -> E^r/S_U. For w=s_f wedge s_g, the condition L intersection S_U nonzero is equivalent to

(Lambda² pi_U)(w)=0.

Thus a specified collection C admits a common projective syndrome line exactly when

K_C=intersection_(U in C) ker(Lambda² pi_U)

contains a NONZERO DECOMPOSABLE bivector. This is a linear system in binom(r,2) Pluecker coordinates, followed by the usual quadratic decomposability equations. The linear condition alone is necessary, not sufficient. A zero kernel is a rigorous obstruction for that specified collection. A nonzero kernel, its dimension, or a count of its points does not prove a common line or a label count.

Distinct challenges require checking the actual intersection lines, and source farness requires separate avoidance of the appropriate syndrome support varieties. Neither follows from decomposability alone.

## Exact Padé/recurrence alternative

For U of sizeu<r define Q_U(Z)=prod_(x in U)(1-xZ), of degree at mostu (the x=0 factor is1 if present). If s=(s_0,...,s_(r-1)) and S(Z)=sum s_j Z^j, then

s in S_U iff coefficients Z^u,...,Z^(r-1) of Q_U(Z)S(Z) vanish.

Proof: an error supported on U has generating series sum_(x in U) e_x*w_x/(1-xZ), whose numerator over Q_U has degree<u. Conversely these recurrence constraints specify a subspace of dimensionu (the firstu coefficients are free), containing the u-dimensional S_U. The argument includes x=0: its summand is constant and its numerator may have degreeu-1.

For a received pencil S_f+lambda S_g, each U therefore yields an explicit (r-u)-by-2 coefficient matrix. All rows must be proportional with the same lambda. This is an exact practical interface for the fixed-H Padé/isogeny compiler; it must hold simultaneously across H to produce one global line.

## MDS intersections and label collisions

For arbitrary supports U,V of sizes belowr,

dim(S_U intersection S_V)=|U|+|V|-min(r,|U union V|).

For the unslacked2ell-point sets, this equals |U intersection V| whenever the intersection is nonempty, and equals1 when U,V are disjoint. In the nonempty case the intersection is exactly S_(U intersection V).

Consequently, if the canonical errors have FULL support U, two different-H supports cannot specify the same projective challenge: their shared syndrome would have an error representation on the8-point intersection, contradicting uniqueness of representation on U. The same reasoning excludes same-H pairs sharing a coset. Collisions can occur only for disjoint pairs within the same H. This observation requires full error support and applies to unslacked supports, not automatically to the five-extra-errors variant.

Even in that favorable case the automatic collision multiplicity can be as large as floor((ell-1)/4), since a fixed-H collection of pairwise disjoint coset pairs has that size. Therefore the support count by itself only guarantees an order-n label count; a superlinear conclusion needs stronger control of the actual challenge map.

## The five extra omissions must remain explicit

To certify the advertised thresholdT, it suffices to realize the unslacked supports U: their words have n-2ell matches and qualify atT. Alternatively one may allow enlarged supports E_U=U union F_U, |F_U|<=5. Every syndrome and Pluecker statement above then applies to E_U, with its actual size. If the extra omissions vary, the condition is an existential union over their choices, not the single linear system for the original U.

The special intersection simplification no longer persists. For two size-(2ell+5) supports with intersectionc, the MDS intersection dimension is max(c,11), rather than merelyc. Thus the original full-support label-injectivity argument cannot silently be reused after adding five arbitrary omissions.

A finite rank test for the entire unslacked bank would decide only that full-bank candidate. It would not exclude a large subbank, altered omission patterns, or another elliptic compiler. Those scope restrictions are essential for any subsequent bounded computation.
