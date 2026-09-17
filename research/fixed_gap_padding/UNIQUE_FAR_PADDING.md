# A far point and unique nearby witnesses at a fixed gap

September 17, 2026. Strengthens the manuscript's anchored-padding lemma
without changing its rate, gap, or coefficient. Extends
UNIQUE_NEARBY_PADDING.md using multiplicative rather than additive labels.

Let the core have N=mB-1 points and received polynomial w of degree A-1,
with displayed candidates of degree<K agreeing on A-1 core points.
Assume q>=1 and A-q>=K. Let T be every degree<K interpolant of w on
some K core points, and M=binom(N,K), so |T|<=M. Every candidate that
can become nearby after q coordinates are added belongs to T.

Choose q points outside the core and the removed anchor where all P(x),
P in T, are distinct and none equals w(x). Each nonzero P-P' has at
most K-1 roots; each w-P has degree A-1. Thus

    p>N+1+q+(K-1)*binom(M,2)+(A-1)*M

suffices. At each point x_j, choose a nonzero g_j so all labels
(P(x_j)-w(x_j))/g_j are distinct from labels at earlier points.
Each previous label and P exclude at most one value of g_j, so

    p-1>(q-1)*M^2

suffices. Set f=w everywhere, g=0 on the core, and g(x_j)=g_j.

Every nearby candidate is in T, has at most A-1 old agreements, and
has at most one new agreement by label injectivity. Thus it must have
exactly A-1 old agreements and one new agreement. Every nearby word has
exactly one nearby codeword. All labels are nonzero. The zero-parameter
word f=w has maximum agreement exactly A-1, attained by the selected
candidates, and no codeword can agree with f on A points. This also
makes ordinary correlated agreement impossible at threshold A.

The fixed-gap theorem's integer choices already give A-q>=K, so the
same coefficient C_rho(eta) works at every sufficiently small rational
eta. The same polynomial-size-field variant works by separating only
the fixed selected list, replacing M by L in the bounds above; its
whole-line uniqueness remains unproved by that separate argument.

verify_unique_far_padding.py exhausts the full interpolation pool for
(p,n,K,A)=(1571,11,2,5),(114874079,21,5,10). There are respectively
28/6188 determining subsets and18/5918 distinct interpolants. The
boundary lists both have size2, giving6/8 uniquely nearby labels.
Parameter zero has exact agreement4/9. Off-line words with exact list
sizes0,1,2 are also checked. The larger fixture has exact rate and gap
5/21. These checks include all potentially nearby polynomials, rather
than merely the selected moment candidates.
