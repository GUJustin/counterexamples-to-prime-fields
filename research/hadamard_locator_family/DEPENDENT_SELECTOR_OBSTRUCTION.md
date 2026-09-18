# Dependent norm selectors cannot realize the guarded eight-section bank

Work over a field of characteristic different from two, passing to its algebraic closure for roots. Let eight nonzero scalars r_j have pairwise distinct squares. Let four even-parity sign rows epsilon_i have pairwise Hamming distance four, and put

Q_i(T)=product_j(T-epsilon_ij r_j)=E_i(T^2)+2T A_i(T^2).

Their even parts have the same leading and constant coefficients. Set C=E_0 and B_i=(E_i-C)/(2Y). Then A_i has degree at most three and B_i degree at most two. The candidate sections are F_i^±(T)=±A_i(T^2)+T B_i(T^2). We impose the necessary saturated-bank guards: the eight leading coefficients ±a_i are distinct, and the six old edge squares y_ij are distinct, nonzero, and disjoint from the r_j^2.

## Why only the odd/odd pair condition is admissible

For a pair of rows write Q_i=E(T)D(T), Q_j=E(T)D(-T), where E and D are the monic quartics on the four agreeing and four differing columns, with signs from row i. Write E=e(Y)+T o(Y), D=d(Y)+T p(Y). Then

2A_i=ep+od,  2A_j=-ep+od.

At an old fourfold edge all four sections F_i^±,F_j^± must agree. Consequently A_i=A_j=0 and B_i=B_j. At a nonzero edge disjoint from all root squares, neither E nor D vanishes at either square root. Thus e and o cannot simultaneously vanish, nor can d and p. The two equations ep=od=0 leave precisely:

* o=p=0; or
* e=d=0.

In the second case the even parts of Q_i,Q_j are Yop and -Yop. Since Yop is nonzero, their difference is nonzero, and B_i differs from B_j. This contradicts the fourfold agreement. Hence **o=p=0 is necessary**. It is also sufficient for the required pairwise fourfold agreement at that edge.

If the elementary first and third symmetric sums of the signed E-roots are e_1,e_3, and those of D are d_1,d_3, this condition is

e_1 d_3-e_3 d_1=0,  y_ij=-e_3/e_1=-d_3/d_1.

The leading-coefficient guards imply e_1,d_1 are nonzero: they are proportional to a_i+a_j and a_i-a_j. This reduction does not discard an admissible zero-denominator branch.

## The dependent selector type

After absorbing the first row into the signs of the roots, take the group sign rows

    + + + +
    + + - -
    + - + -
    + - - +

with two root columns in each group g=0,1,2,3. Write the two roots in group g as m_g+n_g and m_g-n_g, and put h_g=m_g^2-n_g^2. For two groups u,v having signs sigma_u,sigma_v, the quartic symmetric sums are

e_1/2=sigma_u m_u+sigma_v m_v,
e_3/2=sigma_u m_u h_v+sigma_v m_v h_u.

Therefore the six necessary odd/odd conditions are linear in the four h_g. Let M be their coefficient matrix, with pair rows 01,02,03,12,13,23. Its rows sum to zero. Setting h_3=0 after subtracting the common constant gives the first three columns, a 6 by 3 matrix K.

Put A=m_0m_1m_2, B=m_0m_1m_3, C=m_0m_2m_3, D=m_1m_2m_3 and

S_0=A+B+C+D, S_1=A+B-C-D,
S_2=A-B+C-D, S_3=A-B-C+D.

Direct determinant identities are

    det K[0,1,2] = -2 S_0^2,
    det K[0,3,4] = -2 S_1^2,
    det K[1,3,5] = -2 S_2^2,
    det K[2,4,5] = -2 S_3^2.

These integer polynomial identities, the complete matrix, and all its nonzero maximal minors are recorded by paired_root_gate.py/json. No numerical specialization is used.

If K had rank less than three, all four S_i would vanish. The four by four Hadamard transform is invertible in characteristic different from two, so A=B=C=D=0. Thus at most two of the m_g are nonzero.

But a_i=-sum_g epsilon_ig m_g. The twelve pairwise sums and differences a_i±a_j are, up to signs and the unit 2, exactly the twelve quantities m_u±m_v for u<v. Their nonvanishing implies that at most one m_g is zero. This contradiction proves rank K=3.

Hence the only solution of M h=0 is h_0=h_1=h_2=h_3=h. Each quartic then has e_3=h e_1, so every edge square is -h. The six distinct-edge guard fails. **No dependent-selector norm construction realizes the required saturated eight-section bank.**

## Scope and selector completeness

For four balanced orthogonal sign rows, normalize the first row to all plus. The next two rows partition the eight columns into four cells of size two. Orthogonality of the fourth row says its plus counts in these cells have form (t,2-t,2-t,t), with t=0,1,2. The cases t=0,2 are the dependent type above, after row or column sign changes. The case t=1 has each of the eight sign columns once and is the independent type (characters 0,1,2,4 on F_2^3).

Thus the obstruction removes exactly the dependent type. It does not exclude the independent selector family, other locator constructions, or arbitrary eight-section banks.
