# A polynomial-field uniqueness consequence of an external list bound

September 17, 2026. This is a dependency audit, not an independent proof
of the external theorem. Not integrated into the manuscript's standalone
polynomial-field corollary.

Theorem 1.1 of Fernando Granha Jeronimo, ECCC TR26-169 (September 5,
2026), states that for each fixed gamma>0, ordinary prime-field RS lists
at agreement K+ceil(gamma*N) have size <=N^C(gamma), for all sufficiently
large N, all dimensions K<=(1-gamma)N, and every prime p>=N. The exponent
and threshold are independent of p. Primary source:
https://eccc.weizmann.ac.il/report/2026/169/
The theorem's statement and Sections 5.3.2 and 6 were read for scope;
this does not amount to independently auditing its interpolation and
geometric arguments.

Assuming that stated theorem, polynomial-size fields suffice even for
whole-line uniqueness in our prescribed-gap construction. The smaller
pool T is the list on the N=mB-1 old coordinates at threshold A-q,
rather than all polynomials determined by K old coordinates.
For the parameters n=Bt/a, K=rho*n, q=n-mB+1, A=Bt, define

    d = m - (1-eta)*t/a > 0.

The strict inequality is precisely the strict padding inequality from
PRESCRIBED_GAP.md. Then A-q-K=B*d-1. Choose gamma=d/(2m)>0. For all
large B, A-q >= K+ceil(gamma*N), so T has at most N^C candidates,
uniformly in the field. Every candidate near the padded line belongs
T. The selected candidates are in T and have A-1 old agreements.

Separate all of T at the padding coordinates and choose all labels
P(x_j)-b_j distinct as in UNIQUE_NEARBY_PADDING.md. It suffices that
p exceeds a constant (depending on the fixed seed and gamma) times
B^(2C+1). Every nearby polynomial then has exactly A-1 old agreements
and exactly one padding agreement, and each nearby word is unique.

Choose an integer E>max(2m,2C+1,1), and take the least prime 1 modulo
B^E. Linnik gives B^E<p<=C0 B^(E L0). This both allows the simultaneous
power-residue shift and supplies the separation bounds for all large B.
Thus p=n^{O_rho,eta(1)}, n=o(p), exact rate/gap, bad-label coefficient
and whole-line uniqueness follow together, conditional on the cited
field-size-independent polynomial list theorem.

This implication uses an upper list bound to reduce the pool needed
for the lower-bound construction. It does not prove a new list upper
bound, bound the code's global maximum by one, give a competitive
polynomial exponent, or improve a prescribed-code benchmark. Unlike
the standalone POLYNOMIAL_FIELDS.md exponent, no explicit
O(eta^-2/log(1/eta)) field exponent is supplied for this version.
