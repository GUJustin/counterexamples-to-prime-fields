# Three norm selectors already force an old-edge collision

## Statement and scope

Let the field have characteristic different from two. Let r_0,...,r_7 be nonzero with pairwise distinct squares. Suppose three monic degree-eight root selectors Q_i(T)=product_j(T-epsilon_ij r_j) have pairwise Hamming distance four. Write

Q_i(T)=E_i(T^2)+2T A_i(T^2),
B_i(Y)=(E_i(Y)-E_0(Y))/(2Y).

Assume the constants E_i(0) agree, so the B_i are polynomials. Let a_i be the leading coefficients of A_i, and assume a_i are nonzero with pairwise distinct squares. If for every pair i,j an old edge y_ij is nonzero, disjoint from all r_j^2, and satisfies

A_i(y_ij)=A_j(y_ij)=0,  B_i(y_ij)=B_j(y_ij),

then all three y_ij are equal. Consequently the guarded simple-root norm-selector construction cannot produce the proposed bank: it requires six distinct old edge squares. This excludes both the dependent and independent Hadamard selector types.

This statement concerns the polynomial norm-factor construction with eight distinct nonzero root squares. It does not by itself establish that every C2-symmetric bank admits such a norm presentation. In particular the common-factor and nonpolynomial-C alternatives in deriving that presentation remain separate questions.

## Pair reduction

For a pair, write Q_i=E(T)D(T), Q_j=E(T)D(-T), with E,D monic quartics, and write E=e(Y)+T o(Y), D=d(Y)+T p(Y). At an old edge,

2A_i=ep+od=0,  2A_j=-ep+od=0.

Because the edge is nonzero and off the root squares, E and D are nonzero at either square root. Therefore the only possibilities are o=p=0 or e=d=0. In the latter case Q_i and Q_j have even parts Yop and -Yop, respectively, with Yop nonzero, so B_i differs from B_j. This is forbidden. Hence o=p=0.

Writing e_1,e_3 for the first and third elementary sums of the signed roots of E, and d_1,d_3 for those of D, gives

e_1 d_3-e_3 d_1=0,  y_ij=-e_3/e_1.

The quantities e_1,d_1 are nonzero because they are proportional to a_i+a_j and a_i-a_j. Thus this reduction has no hidden leading-denominator exception.

## Pair the columns

Absorb row zero into the root signs. The next two rows are balanced and mutually orthogonal. Their four sign cells each have size two. Order the cells so the three rows are

    + + + +
    + + - -
    + - + -.

Write the two roots in cell g as m_g+n_g,m_g-n_g, and h_g=m_g^2-n_g^2. The three quartic compatibility equations are linear in h. Their coefficient matrix M is the submatrix of paired_root_gate.json with rows 0,1,3. It always kills the two vectors

    1=(1,1,1,1),    v=(m_0,-m_1,-m_2,m_3).

These vectors are independent under the leading guards. Indeed v constant would give m=(z,-z,-z,z), whose three signed sums all vanish.

We show rank M=2. Put

A=m_0m_1m_2, B=m_0m_1m_3,
C=m_0m_2m_3, D=m_1m_2m_3,
S_0=A+B+C+D, S_1=A+B-C-D, S_2=A-B+C-D.

For row pairs (0,1),(0,2),(1,2), the two by two minors, up to sign, are respectively S_0,S_1,S_2 multiplied by the six quantities

m_2+m_3, m_1+m_3, m_1-m_2,
m_0-m_3, m_0+m_2, m_0+m_1.

All six quantities are nonzero: up to the unit two they are the pairwise sums and differences of the three signed leading sums

l_0=m_0+m_1+m_2+m_3,
l_1=m_0+m_1-m_2-m_3,
l_2=m_0-m_1+m_2-m_3,

and a_i=-l_i.

If rank M were at most one, S_0=S_1=S_2=0. Solving these linear equations in A,B,C,D gives (A,B,C,D)=(A,-A,-A,A). If A is nonzero, all m_g are nonzero; taking ratios yields m=(z,-z,-z,z), again making all three leading sums zero. If A is zero, every triple product is zero, so at most two m_g are nonzero. On two coordinates there are only two sign patterns up to overall sign; two of the three leading sums must then agree up to sign. This also violates the guards.

Thus rank M=2 and every solution has

    h_g=H+K v_g.

For pair 01, the agreeing cells are 0,1, so

e_1=2(m_0+m_1),
e_3=2(m_0h_1+m_1h_0)=H e_1.

For pair 02 the same computation uses cells 0,2. For pair 12 it uses cells 0,3 with opposite signs, giving e_3=2(m_0h_3-m_3h_0)=H e_1. Therefore every old edge is -H. This proves the claim.

## Exact certificates and the reciprocal family

three_selector_gate.py/json independently records both kernel identities, every maximal minor being zero, all eighteen two by two minors, and all three edge identities. These are integer polynomial identities, so the proof only excludes characteristic two. Generation took less than one second and involves no parameter scan or Groebner computation.

The prior reciprocal pencil is exactly this forced kernel: h_g=H+K epsilon_g m_g, epsilon=(1,-1,-1,1). Completing the square gives

(r_g,+-K epsilon_g/2)(r_g,--K epsilon_g/2)=H+K^2/4.

If the right side vanishes, four roots share the square K^2/4, violating the root guards. Otherwise one can scale to roots epsilon_g c+u_g and epsilon_g c+1/u_g. The remaining three independent-selector equations factor through the scalar relation

2c(u_0u_3-u_1u_2)=e_3(u)-e_1(u),

as recorded in reciprocal_selector_gate.py/json. This gives a large family satisfying all six algebraic compatibility equations, but its old edges coincide at c^2-1. It is therefore a degenerate family, not a positive bank.
