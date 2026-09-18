# Universal common-norm bridge for the sign-twisted doubled-Hadamard ansatz

Work in characteristic different from two. Assume the precise sign-twisted doubled-Hadamard incidence model of C2_CEVA_REDUCTION.md: eight sextics F_i^±(T)=±A_i(T²)+T B_i(T²), six old fourfold blocks at ±sqrt(e_ij), and sixteen new transversal nodes in four quadratics and their reversals. All twenty-eight nodes are distinct; all fourteen square values are nonzero and distinct. The eight signed leading coefficients are distinct. This note proves a contradiction for this model without assuming any Ceva chart or involution normal form.

Subtract the common odd polynomial to set B_0=0 and scale to make a_0=1. Write A_i=a_i C_i with C_i=product_{j!=i}(Y-e_ij). In particular A_0=C_0. Let the all-plus transversal quadratic be L_0(T)=T²-sigma T+p, with sigma,p nonzero. Both facts follow from its two roots being nonzero and disjoint from the roots of L_0(-T). Set R_0(Y)=(Y+p)²-sigma²Y.

## 1. Physical beta coefficients, without exceptional divisions

The all-plus difference A_i(T²)-A_0(T²)+T B_i(T²) is divisible by (T²-e_0i)L_0(T). Write its quadratic quotient as

(a_i-1)T²+beta_i T+z_i.

Comparing even and odd parts gives the polynomial identity

(Y+p)B_i=sigma(C_0-a_i C_i)+R_0 beta_i(Y-e_0i).  (1)

No division by C_i(-p), p+e_ij, or an involution coefficient has occurred. The leading coefficient u_i of B_i is

u_i=beta_i-sigma(a_i-1).  (2)

At an old edge e_ij with i,j in {1,2,3}, both A_i,A_j vanish and B_i=B_j. Subtract (1) for i,j. Since R_0(e_ij) is nonzero by disjointness of old and all-plus nodes, this yields

beta_i(e_ij-e_0i)=beta_j(e_ij-e_0j).  (3)

All edge differences here are nonzero. Thus either all beta_i are zero or all are nonzero. In the nonzero case they are pairwise distinct: beta_i=beta_j in (3) would imply e_0i=e_0j.

The all-zero case is impossible. In that case the quadratic quotient above is even for each difference F_i^+-F_0^+. Its roots are precisely the two remaining new transversal nodes shared by this pair, since its six prescribed roots have already exhausted the sextic degree. Their quadratic therefore coincides with its reversal, contradicting the distinct complementary transversal nodes. Hence all beta_i are nonzero and distinct.

## 2. Complement slopes give a complete amplitude line

For any pair i,j the monic residual quadratic after removing its old edge and L_0 has T coefficient

s_ij=(beta_i-beta_j)/(a_i-a_j), with beta_0=0.

This follows from its T^5 coefficient using (2). The incidence pattern identifies the residual quadratic for pair (0,i) with the reversal of that for its complementary pair (j,k). Thus s_0i+s_jk=0. Put d_i=a_i-1. The three resulting linear equations are

(beta_2-beta_3)d_1+beta_1 d_2-beta_1 d_3=0,
beta_2 d_1+(beta_1-beta_3)d_2-beta_2 d_3=0,
beta_3 d_1-beta_3 d_2+(beta_1-beta_2)d_3=0.  (4)

Let S=beta_1+beta_2+beta_3. The vector v_i=beta_i(S-2beta_i) lies in the kernel. The coefficient matrix has rank exactly two. Its determinant vanishes; among its two by two minors are, up to sign, beta_i(S-2beta_i) for i=1,2,3. They cannot all vanish: since beta_i are nonzero this would give S=2beta_i for all i, and summing gives S=0 and then every beta_i=0. Thus a maximal minor is nonzero. The kernel is consequently the line

a_i=1+t beta_i(S-2beta_i).  (5)

Here t is nonzero because a_i differs from 1. This proves completeness of the amplitude line without any finite-pole involution parametrization. Combining (2) and (5) gives

u_i/beta_i=1-sigma t(S-2beta_i).  (6)

This is a nonconstant affine function of the three distinct beta_i.

## 3. Polynomial identities and gcd(B_1,B_2,B_3)=1

At a new node, with Y=T² and common received value V, each selected candidate satisfies (V-TB_i)²=A_i² and V²=A_0². Eliminating V gives

H_ij=Y B_i B_j(B_i-B_j)-B_j(A_i²-A_0²)+B_i(A_j²-A_0²)=0.

This polynomial has degree at most eight. It vanishes at all eight new square values, and also at e_0i,e_0j,e_ij. These eleven values are distinct, so H_ij is identically zero.

Its leading coefficient yields

-u_j(a_i²-1)+u_i(a_j²-1)=0.

All a_i²-1 are nonzero. If one u_i vanished, all would vanish, contradicting (6). Hence every B_i has degree exactly two.

Each B_i vanishes at e_0i. Since these three values are distinct, a common divisor can have degree at most one. If they shared a root r, then B_i=u_i(Y-r)(Y-e_0i). At any e_ij other than r, equality of B_i and B_j gives

u_i(e_ij-e_0i)=u_j(e_ij-e_0j).

Comparing with (3) makes u_i/beta_i=u_j/beta_j. Among the three distinct edges12,13,23, at most one equals r; the other two connect all three labels. All three ratios would therefore be equal, contradicting (6). This includes r=e_0i and repeated roots of an individual B_i. Therefore gcd(B_1,B_2,B_3)=1.

The identities H_ij show that the rational function

C=(A_i²-A_0²-Y B_i²)/B_i

is independent of i. Its reduced denominator divides every B_i, so C is polynomial. Since a_i²-1 and u_i are nonzero, deg C=4.

## 4. The norm is simple and has eight roots

Set R(Y)=C²-4Y A_0². Its degree is eight. At any new square value at least one B_i is nonzero, by the gcd result. The new-node equations then give C=-2TV, so R=0. There are eight distinct nonzero such values. Thus R has exactly these simple roots and is disjoint from every old edge.

The four degree-eight polynomials

Q_i(T)=C(T²)+2T²B_i(T²)+2T A_i(T²)

satisfy Q_i(T)Q_i(-T)=R(T²). All Q_i have the same nonzero leading coefficient, which may be divided out simultaneously. Since R has eight distinct nonzero roots, every resulting monic Q_i chooses exactly one square root from each of the eight opposite pairs. Their constant terms agree, so the Hamming distance between any two sign selectors is even.

In fact every pair has Hamming distance four. Distances zero or eight would make A_i=A_j or A_i=-A_j, contradicting the leading guards. For distances two or six, factor Q_i=E D,Q_j=E D(-T), with one of E,D a monic quadratic and the other degree six. At an old edge the same odd/odd versus even/even argument in THREE_SELECTOR_OBSTRUCTION.md applies: A_i=A_j=0 and B_i=B_j force both odd parts to vanish. But the odd part divided by T of the quadratic is the constant equal to minus the sum of its two signed roots. It is nonzero because opposite roots would have the same square, which is forbidden. Thus distances two and six are impossible.

Every pair therefore has distance four. The normalized A_i still have distinct signed leading coefficients; all old edges remain nonzero and disjoint from the norm roots. THREE_SELECTOR_OBSTRUCTION.md applies to any three selectors and forces their three old edges to coincide, a contradiction.

## Conclusion and exact scope

There is no realization of the stated sign-twisted doubled-Hadamard C2 incidence ansatz in characteristic different from two with distinct domain nodes and the saturated leading guards. The argument treats the affine opposite-edge involution, finite-pole charts, p+edge=0, all coefficient-rank exceptions, and a possible rational common C directly; none is discarded by parametrization.

This does not exclude all eight-section constructions or all incidence designs. It excludes this particular involution-compatible doubled-Hadamard model. The algebraic pair obstruction and its exact determinant certificates are in THREE_SELECTOR_OBSTRUCTION.md and three_selector_gate.py/json.
