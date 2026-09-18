# Sign-twisted involution and the exact Ceva reduction

No realization is asserted. This supplies a small explicit algebraic system outside the cyclic-seven-plus-zero and preserved-quadratic-word constructions.

## Symmetry gate

The two-Hadamard double-coset calculation has four types: intersections14,6,2,0, with orbit sizes1,7,14,8 under AGL3(2) of order1344. For the disjoint type the ordered common group has168 elements and the full union group336. Every order2 or3 element of the common group fixes four domain blocks, impossible for a nontrivial P1 automorphism. An order4 element has such an involution power. The extra involutions in the union group fix two candidate labels and no nodes. They too are impossible: at a fixed base point outside the domain, saturation makes all candidate fiber values distinct; an affine fiber transformation fixing two of them is the identity, so cannot swap the other candidates there. Order6/8 powers reduce to these exclusions. Thus the only possible nontrivial symmetry for the disjoint type contains a cyclic7 action, returning to the archived seven-plus-zero mechanism. This is not a symmetry-free exclusion of that design.

Instead take TWO COPIES of the affine-hyperplane design and translate candidate labels by a fixed nonzero vector. This involution has four candidate pairs. The six fixed masks consist of two full candidate pairs; swap their two block occurrences. The other16 nodes are paired across complementary sign masks. Thus the domain involution is free, represented by T -> -T.

The necessary fiber character is the SIGN twist

    F_i^+(T)=A_i(T²)+T B_i(T²),
    F_i^-(T)=-A_i(T²)+T B_i(T²), i=0,1,2,3,

with deg A_i=3, deg B_i<=2. The untwisted version makes each paired difference odd of degree<=5, contradicting its six prescribed roots.

## Edge and transversal nodes

Write six distinct nonzero edge values e_ij. The fixed masks occupy nodes ±sqrt(e_ij), where both signs of candidates i,j agree. Set

    C_i(Y)=product_{j!=i}(Y-e_ij), A_i=a_i C_i.

After removing a common odd polynomial take B0=0. The conditions B_i(e_ij)=B_j(e_ij) parameterize B1,B2,B3 by three shared values u12,u13,u23, using quadratic interpolation at their three incident edges. All eight leading coefficients ±a_i must be distinct.

The other16 nodes are ± the roots of four monic quadratics L_epsilon(T), one for each even sign pattern modulo global negation. Each represents the equality of the four selected signs. The all-plus quadratic is

    L0(T)=T²-sigma T+p.

The complete node locator is

    K(T)=product_edges(T²-e_ij) * product_patterns L_epsilon(T)L_epsilon(-T).

The essential guard is that K is squarefree. In particular sigma,p are nonzero and every L is coprime to its reversal and to the edge locators.

## Why the viable edge class is Ceva

Put (a,b,c,d,e,f)=(e01,e02,e03,e12,e13,e23), reserving a_i for leading coefficients. The condition is

    F=(e-a)(d-b)(f-c)-(d-a)(f-b)(e-c)=0.

It equals the determinant of the rows (1,-a-f,af), (1,-b-e,be), (1,-c-d,cd): the three opposite-edge pairs therefore belong to one projective involution.

To derive it, let t,s be the distinct roots of L0, and compare the common-value equations at t,s. Partial fractions give three equations

    sum_{j in {1,2,3}, j!=i} v_ij/C_i'(e_ij)=0,

where

    v_ij=[u_ij(p+e_ij)-a0*sigma*C0(e_ij)] /
          [(p+e_ij)²-sigma² e_ij].

The denominators are nonzero by the node guard. The triangle matrix determinant is a nonzero edge-difference factor times F. If F!=0 then all v_ij=0. This forces the all-plus family into the special beta_i=0 case of the formula below; its remaining pair quadratics are even, so their roots collide with their reversals. This violates squarefreeness of K.

The possible intermediate denominators do not rescue F!=0: if p+e_ij=0 for an edge among1,2,3, then v_ij=0 contradicts sigma*C0(e_ij)!=0. If -p=e0i, the equations for the other two candidates force their leading coefficients to vanish. Thus every guarded realization satisfies F=0.

## Explicit all-plus pencil on an open chart

Normalize a0=1. On the chart C_i(-p)!=0 the whole all-plus family is explicit. Set

    beta0=0,
    beta1=tau/(d-a), beta2=tau/(d-b),
    beta3=tau*(e-a)/[(d-a)(e-c)],
    R(Y)=(Y+p)²-sigma²Y,
    a_i=[C0(-p)+sigma*p*beta_i*(-p-e0i)]/C_i(-p),
    B_i=[sigma*C0-sigma*a_i*C_i+R*beta_i*(Y-e0i)]/(Y+p).

The last numerator vanishes at -p, so B_i is a polynomial of degree<=2. Ceva gives all edge equalities, and the three all-plus differences are divisible by L0. The formula is an exact two-dimensional amplitude kernel before normalizing a0; tau is the remaining pencil parameter. The divisor C_i(-p)=0 is a separate chart, not excluded globally by this parametrization.

The code ceva_pencil.py verifies the determinant identity and all polynomial identities on the rational fixture edges1..6; the derivation above gives their symbolic reason. The initial rank5 observations on arithmetic/geometric edge fixtures were special, not generic: both fixtures have an opposite-edge involution.

## Remaining small equations

Define

    H_ij=[a_i product_{k!=i,j}e_ik-a_j product_{k!=i,j}e_jk]/(a_i-a_j).

Exact division yields

    F_i^+-F_j^+=(a_i-a_j)(T²-e_ij)L0(T)L_ij(T),
    L_ij=T²+[(beta_i-beta_j)/(a_i-a_j)]T+H_ij/p.

For a partition (0,i)|(j,k), matching the internal pair roots requires

    H_0i=H_jk,
    (beta0-beta_i)/(a0-a_i)=-(beta_j-beta_k)/(a_j-a_k).

The three slope equations have only two independent conditions. Equivalently, for some gamma and S=sum a_i,

    beta_i=gamma*(a_i-1)*(a_i+1-S/2).

The remaining CROSS equality is indispensable:

    L_0i(T) divides A0(T²)+A_j(T²)-T B_j(T²).

This contributes two scalar equations for each partition. Omitting it produces false apparent constructions. All roots must finally pass the squarefree K and ±leading-coefficient guards.

## A complete fixed-edge control

For edges1..6, the beta ratios are (0,2,3,4). The slope conditions give a=(1,1+10v,1+9v,1+4v). The three H conditions coincide and force v=-7/44, giving

    a=(1,-13/22,-19/44,4/11).

These leading coefficients and their negatives are distinct. All-plus compatibility then forces p=-7/2 and sigma*tau=15/88 in this beta normalization. The cross-pattern coefficients have gcd1 in Q[sigma], so this fixture does NOT realize the bank for any sigma. cross_pattern_fixture.py/json records the exact calculation. The variable opposite-edge-involution class remains open; no field scan has been run.
