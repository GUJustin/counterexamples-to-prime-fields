# Independent audit: prime-field quadratic line with N^(3/2) exceptions

September 18, 2026. **PASS** for the revised rational quadratic bank with quartic/cubic fresh values. This is a prime-ambient construction, not an extension-field specialization. No polynomial-list completeness assumptions are left unproved.

## Explicit bank and core

Fix an integer L≥6. Choose distinct positive primes a_1,...,a_L and put A_i=a_i², Q=max A_i. Define rational quadratics

    P_i(X)=X²/A_i+A_i.

Their pair difference has exactly the two roots ±a_i a_j. Unique factorization makes all these pair roots distinct across unordered pairs. At either root the two values equal A_i+A_j. Thus the core has N0=L(L-1) coordinates, its received word is well-defined, and each P_i agrees on exactly A=2(L-1) core coordinates.

Any other quadratic h has at most L core matches: each matching coordinate contributes two equalities h=P_i, while each of the L nonzero differences h-P_i has at most two roots. Thus 2*matches≤2L. This includes candidates over any prime field satisfying the nondegeneracy conditions below, not just rational candidates.

## Fresh coordinates and exact affine spectrum

Set t=N0+1, x_j=Q+j for 1≤j≤t, Xmax=Q+t, and N=N0+t=2L(L-1)+1. Define old sources f,g by

    core: f=the pair-intersection word, g=0;
    fresh x: f=x⁴, g=x³.

The fresh label associated to (i,x) is

    lambda_(i,x)=P_i(x)/x³-x
                 =-x+1/(A_i x)+A_i/x³.

Since x>Q≥A_i≥4, this lies strictly between -x and -x+1. Different integer x give disjoint intervals. At fixed x the labels are distinct because P_i(x)=P_j(x) would force x=±a_i a_j, excluded by x>Q. Hence all M=tL labels are distinct, nonzero, and different from one.

At a labeled challenge, exactly one incumbent gains exactly one fresh match. Every nonincumbent has at most L core matches and at most four fresh matches, because x⁴+lambda x³-h(x) is a nonzero quartic. For L≥6, L+4≤A. Consequently the old affine line has exact agreement A+1 at precisely these M labels, with a singleton list at threshold T=A+1=2L-1. Every other affine label has agreement exactly A and no threshold candidate.

## Exact common agreement

For a nonzero quadratic G explaining g, at most two core coordinates satisfy G=0 and at most three fresh coordinates satisfy G=x³. Thus any simultaneous source explanation with G nonzero uses at most five coordinates. If G=0, it can match only the core; the first-source maximum there is A. Since A≥10, and each incumbent supplies A common core matches, CA(f,g)=A.

In particular f has agreement A because zero is not a fresh label. Likewise f+g has agreement A because one is not a fresh label. Replace the pair by

    F=f,    G=f+g.

Both individual source agreements and their common agreement are exactly A. Common agreement is invariant under this invertible source transformation because the message space is linear.

For z≠-1, the new received word is

    F+zG=(1+z)(f+[z/(1+z)]g).

Its qualifying labels are the M distinct nonzero values z=lambda/(1-lambda). At z=-1, the word is -g: the zero polynomial agrees on all N0 core coordinates and no fresh coordinates. Any nonzero quadratic has at most two core and three fresh matches, hence fewer than T. Thus this extra label has exactly one threshold candidate too.

The converted line has **exactly M+1 nonzero bad labels**, all with singleton threshold lists. At M of them nearest agreement is T; at z=-1 it is N0. All other labels have nearest agreement A. The extra infinity label must not be omitted from an exact count.

## All sufficiently large prime fields

Everything above is rational. A simple explicit sufficient bound is

    p>2 Q² Xmax^7.

Indeed write lambda=nu/d with

    nu=x²+A_i²-A_i x⁴,   d=A_i x³.

Here |nu|<Q Xmax^4 and d≤Q Xmax³. Any nonzero crossnumerator of two labels has absolute value less than 2Q²Xmax^7. The same bound preserves nonzero labels, lambda≠1, and nonzero denominators. It also preserves all core/fresh coordinate distinctions, a_i coefficients, nonzero pair-leading coefficients, and the two roots of each pair difference. Therefore the exact identities and root-count arguments hold for every prime above the bound. No Dirichlet, Chebotarev, or unproved finite-field genericity assumption is needed.

The threshold proofs continue to quantify over all quadratic polynomials over F_p. Characteristic p>2 is automatic; all codewords have degree at most two.

## First order, Johnson, and population scale

The rate is 3/N. Exact arithmetic gives

    T²=(2L-1)²=2N-1<2N=N(K-1).

Thus T is strictly below exact finite Johnson. A safe simple finite onset for crossing the DKT first-order curve is L≥25. In its low-rate branch,

    N*a1(3/N)≤sqrt(3N/2)+3^(1/4)N^(1/4)/2^(3/4)
                <(7/4)L+sqrt(L)<2L-1=T,

using N<2L², sqrt(3)<7/4, and L/4-sqrt(L)-1>0 for L≥25. A sharper onset may be established separately; it is unnecessary for the unbounded family.

Since M+1=L(L(L-1)+1)+1,

    (M+1)/N^(3/2) tends to 1/(2sqrt(2)).

This supplies an unbounded prime-field family with dimension K=3, both sources one coordinate below the tested threshold, exact singleton bad lists, and Theta(N^(3/2)) bad challenges. The rate and normalized first-order/common-agreement margins vanish. It therefore does not establish fixed-rate/fixed-margin tightness or a quadratic lower bound. It materially strengthens the prior extension-field-only N^(3/2) construction by changing the ambient field to prime and keeping complete incidence control.

No main manuscript edits were made.

## Stronger all-prime greedy bound (independent audit)

The construction exists over every prime field with p>max(2Q,5L^4). This uses greedy finite-field fresh nodes, not the earlier consecutive rational fresh nodes. The condition p>2Q preserves all distinct core nodes ±a_i a_j, and preserves the nonzero distinct a_i².

After choosing j fresh nodes, where 0≤j≤N₀=L(L−1), exclude the N₀ core nodes, zero, the j previous fresh nodes, roots giving any new label 0 or 1, and roots giving any of the jL previous labels. Clearing the nonzero denominator x³, a prescribed label satisfies P_i(x)−x⁴−λx³=0. This polynomial always has leading coefficient −1 and degree four. The respective exclusion bounds are therefore

    N₀ + 1 + j + 8L + 4jL².

At a single new node, two incumbent labels coincide precisely when P_i=P_j, which only happens on the excluded core. At j=N₀ the displayed bound is

    4L⁴−4L³+2L²+6L+1 < 5L⁴  (L≥2).

Consequently a permitted fresh node always exists, through all t=N₀+1 choices. All labels are nonzero, different from 1, and globally distinct. Every remaining argument in this audit uses polynomial root counts and thus applies to these finite-field choices unchanged. In particular both endpoint words remain far and the transformed-infinity threshold list is singleton.
