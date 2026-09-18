# Explicit residue identities for the dependencies needed by a seventh word

## Correct dimension target

The independently checked six-word bank has length60, degree cap14, exactly180 selected agreements, and full incidence-Jacobian rank180. Its raw local dimension is30. The common-polynomial, value-scaling, and full projective-coordinate gauges have dimension15+1+3=19, leaving eleven local parameters; using only affine-coordinate gauges incorrectly leaves twelve.

More generally, seven degree-at-most-D candidates at n=4(D+1), each with n/2 selected agreements, have

    7(D+1)+2n−7n/2 = D+1

as their full-row-rank expected raw dimension. But the gauge directions have dimension D+5 on a nondegenerate configuration: D+1 common-polynomial additions, one value scaling, and three projective-coordinate changes. Thus at least four row dependencies are needed. If there are extra stabilizers, their actual rank must be checked rather than assumed.

The proper-one-pole extension problem has two rather than one analogous excess gauge directions in the current six-word chart. The family is projectively stable: under x=(at+b)/(ct+d), multiply values by (ct+d)^D. A rational numerator of degree D+1 divided by x−beta transforms into another numerator of degree at most D+1 divided by a linear polynomial. The affine chart excludes a transformed pole at infinity, an open condition. Therefore omitting the third projective gauge would undercount the needed dependencies.

## A complete, explicit certificate for incidence-Jacobian dependencies

Let S_i be the selected agreement set of candidate P_i, let

    A_i(X)=product_(j in S_i)(X−x_j),

and assume all domain nodes distinct. Write a row dependency as weights lambda_ij for j in S_i. Linearizing the incidence equations P_i(x_j)=w_j shows that the exact conditions are

    sum_(j in S_i) lambda_ij x_j^r=0       (0<=r<=D),
    sum_(i:j in S_i) lambda_ij=0,
    sum_(i:j in S_i) lambda_ij P_i'(x_j)=0.

The first family concerns polynomial coefficients, the second received values, and the third node positions.

Equivalently, there are polynomials U_i with

    deg U_i <= deg A_i−D−2

(and U_i=0 if the upper bound is negative), not all zero, such that

    sum_i U_i(X)/A_i(X)=0,
    sum_i U_i(X) P_i'(X)/A_i(X)=0.         (R)

The correspondence is lambda_ij=U_i(x_j)/A_i'(x_j). To prove it, interpolate U_i at the simple roots of A_i. The partial-fraction expansion of U_i/A_i has residues lambda_ij. Vanishing of the first D+1 moments is exactly decay O(X^(−D−2)) at infinity, giving the displayed numerator bound. The last two dependency conditions say that the two sums in (R) have no finite poles. Each summand in the first sum decays; each in the second has degree at most −3. Hence both sums vanish identically. The converse follows from their residues and infinity expansions. This proof works in every characteristic; distinctness makes A_i' nonzero at its roots.

If Lambda is the full domain locator and B_i=Lambda/A_i is the complement locator, (R) becomes two polynomial identities

    sum_i U_i B_i=0,
    sum_i U_i B_i P_i'=0.                 (P)

For the seventh-word problem, four independent tuples (U_i) would be explicit certificates of the necessary dependencies. These identities are stronger deliverables than a dimension heuristic: a proposed construction can be tested against them directly.

## One tempting automatic construction of (P) is impossible

A natural way to produce both identities is fixed-label Lagrange interpolation. Take distinct constant labels s_1,...,s_7 and weights

    c_i=1/product_(j!=i)(s_i−s_j).

Then sum_i c_i f(s_i)=0 for every polynomial f of degree at most five. Suppose one tries to arrange

    B_i(X)=B(X,s_i), deg_s B<=d,
    P_i(X)=P(X,s_i), deg_s P<=e,
    d+e<=5,

so that U_i=c_i (or a common polynomial multiple) automatically gives both identities. Here the degree constraint is imposed on P itself, not merely its derivative; derivative degree may behave differently in positive characteristic.

This mechanism cannot realize seven distinct degree-at-most-D candidates, each with at least n/2 selected agreements, at n=4(D+1).

Indeed, let r_j be the number of selected candidates at node j and E=sum_j r_j>=7n/2. Pairwise root counting gives

    sum_j binom(r_j,2)<=21D.

If every positive r_j were at least four, the left side would be at least (3/2)E>=21n/4=21D+21, a contradiction. Thus some node has 1<=r_j<=3. At that node B_i(x_j) is zero for the 7−r_j nonincident candidates and nonzero for the incident candidates. Therefore the nonzero label polynomial B(x_j,s) has at least four distinct roots, forcing d>=4. The degree sum then forces e<=1.

But label degree at most one makes the candidates an affine polynomial pencil P_i=P_0+s_i P_1. Since they are distinct, P_1 is nonzero and has degree at most D. At most D coordinates can support more than one agreement, while every other coordinate supports at most one. Thus

    E<=7D+(n−D)=n+6D < 7n/2,

again a contradiction. Hence this low-label-degree barycentric shortcut cannot supply the required dependencies.

## What a useful next construction must supply

A surviving residue-based mechanism would need nonconstant, candidate-dependent U_i, a higher-degree label description with nontrivial cancellations, or a different geometric identity giving both equations (P). The simple label interpolation construction above fails for a precise incidence reason. This note supplies no seventh word or generic existence theorem, and does not rule out other realizations of the residue identities.
