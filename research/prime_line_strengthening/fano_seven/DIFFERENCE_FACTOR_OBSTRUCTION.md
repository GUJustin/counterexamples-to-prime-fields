# An independent difference-factor obstruction for the Fano support

**Proved:** seven distinct polynomials of degree at most three cannot realize
the selected support consisting of seven Fano triples and their seven
complements on fourteen distinct coordinates in characteristic different
from two. This is an elementary proof, independent of the determinant
normalization used in the parallel audit.

Index the seven polynomials P_i by the points of the Fano plane. For each
Fano line l, let t_l denote its triple-node coordinate and u_l its complementary
quadruple-node coordinate. Assume all fourteen coordinates are distinct and
that the indicated polynomials agree with the received value at those nodes.
Put

    B_i(X)=product_(l containing i)(X-u_l).

These are monic cubics with distinct zero sets, so no two are proportional.

For points i,j on line l, let k be the third point of l. The selected common
agreements of P_i,P_j occur at t_l and at the two complement nodes belonging
to the other two lines through k. Since the difference is nonzero of degree
at most three, these are exactly its three roots and

    P_i-P_j=c_ij*(X-t_l)*B_k/(X-u_l),  c_ij!=0.

The cyclic triangle identity on l consequently forces a dependence among
B_i,B_j,B_k with all three coefficients nonzero. Conversely, if i,j,k are
not collinear in the Fano plane, evaluate any purported dependence at
u_(line through i,j). It kills B_i and B_j, but B_k is nonzero there. Thus
its B_k coefficient vanishes; the remaining pair is independent. Every
noncollinear triple of the B's is therefore independent.

For completeness, the resulting Fano-representation contradiction is explicit.
Label the lines

    123,145,246,347,167,257,356.

Take independent vectors B_1,B_2,B_4 as a basis. Rescaling the representatives
and basis allows

    B_3=e1+e2,   B_5=e1+e3,
    B_6=e2+lambda*e3,  lambda!=0.

The lines347,167,257 force B_7 to be proportional to e1+e2+e3 and force
lambda=1: the first line equates its first two coordinates, the third its
first and third, and the second makes the third lambda times the second.
All these coordinates are nonzero by the noncollinear-triple independence.
The last line356 would then make

    (1,1,0), (1,0,1), (0,1,1)

linearly dependent. Their determinant is minus two, impossible outside
characteristic two. This proves the obstruction.

The proof uses only prescribed incidences, polynomial degree three, and distinct
coordinates. It does not presume that these are the only received-word matches,
and does not classify other possible seven-cubic support designs.
