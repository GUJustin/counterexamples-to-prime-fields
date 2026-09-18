# Independent audit and an exact recursive gluing target

## Audit verdict

The saturation, locator equivalence, and complete-list assertions in
`EXACT_TARGET.md` pass. For even L>=4, convexity with total incidence at
least L*2(L-1) forces every column size L/2, every candidate agreement
exactly2(L-1), and every pair overlap exactlyL-2. The pair differences
therefore have degree exactlyL-2 and distinct leading coefficients.
The locator matrix supplies all required equalities; an additional match
outside a mask creates an extra root of a pair difference. A polynomial
outside the bank has at most2L-4 matches, because summing its intersections
with all L members gives a*(L/2)<=L*(L-2). The L=2 constant-polynomial case
is elementary separately.

The Hadamard block construction is valid as a multidesign. In particular,
the completeness claim is about the actual polynomial list, not only the
specified incidence bank. No polynomial realization follows from the
combinatorial construction alone.

## A recursive construction target with only 2L new polynomial constants

Suppose a bank of size L has already been realized with degreeL-2 on
4(L-1) distinct old nodes, with the union of two Sylvester-Hadamard designs.
Write P_i for its polynomials, w for its word, S_i for the2(L-1) nodes
where P_i agrees, and

    M_i(X)=product_{x in S_i}(X-x).

The Sylvester doubling has labels (i,epsilon), epsilon in{0,1}.
Lift each of the two relabelings of the old design without changing
epsilon. The doubled design decomposes exactly as follows:

* The4(L-1) inherited blocks are B times{0,1}, one per old block.
* The4L new blocks choose exactly one of (i,0),(i,1) for each i.
  For each of the two copies these are the2L graphs of all affine
  Boolean functions on the old label vector space.

This gives4(2L-1) blocks of sizeL, with the required pair counts2L-2.
Each new candidate must agree with the unchanged old word at S_i.
Since its new degree limit is2L-2=deg M_i, it NECESSARILY has the form

    P_(i,0)=P_i+c_i M_i,       P_(i,1)=P_i+d_i M_i.       (1)

Conversely these are all polynomials meeting those inherited constraints.
Thus there is no missing polynomial-coefficient freedom in (1).
The2L constants c_i,d_i must all be distinct; they are precisely the new
leading coefficients. This also makes all new candidates distinct.

The recursive step is now an exact finite algebraic problem: for each
new graph block epsilon_sigma(i), choose a new node z_sigma and value
v_sigma such that

    P_i(z_sigma)+e_(i,epsilon_sigma(i))*M_i(z_sigma)=v_sigma
    for every i,
    where e_(i,0)=c_i and e_(i,1)=d_i.                 (2)

Require the4L new nodes to be distinct and disjoint from the old domain.
Equations(1)-(2), with the constant-distinctness guards, are sufficient
for the complete doubled bank: inherited and new incidences give exactly
the doubled Hadamard design, and the saturation audit applies again.
This is a genuine recursive gluing criterion, not an existence proof.
It is separate from requiring a common automorphism of all nodes.

For a fixed choice of the2L constants, potential new nodes can be found
without searching words. All L quadratics

    Q_i(X,V)=(V-P_i-c_i M_i)(V-P_i-d_i M_i)

must have a common V-root at a new node. Their pair differences are
linear in V. Eliminate V using these linear equations, retaining the
strata where their coefficients vanish; then test the surviving roots
against each graph-block choice. This supplies an exact small-degree-in-V
elimination problem for any proposed recursive identity.

## Additional identity a construction may exploit

Every saturated old bank automatically satisfies

    product_{j!=i}(P_i-P_j) = C_i M_i^(L/2-1),
    C_i=product_{j!=i}(leading(P_i)-leading(P_j)) !=0.   (3)

At each old agreeing node exactlyL/2-1 factors on the left have a simple
root. These account for the full degree, proving(3) exactly. Thus the
M_i entering(1) are not arbitrary degree2L-2 polynomials: they are perfect
power roots of the spectral derivative of product_j(V-P_j) along V=P_i.
A successful recursive identity must exploit this compatibility rather
than merely solve independent high-degree interpolation problems.

## Scope and next constructive seed

The L=4 to L=8 instance uses four known quadratics, their four degree-six
agreement locators, and only eight new leading constants. It asks for
sixteen new graph-block nodes while preserving the twelve old nodes.
This is a different, restricted design target from the disjoint-Hadamard
42-by7 locator problem: only the specifically lifted pair of old designs
is covered. Indeed the two order-four Hadamard designs have identical
blocks, and their inherited doubled blocks retain repeated masks. With
the unmodified lifts above, both order-eight copies coincide. One may
independently switch the new bit by any function of the old label in each
copy; this preserves inherited blocks and equations(1), and only changes
the graph-block choices in(2), but cannot remove those inherited repeated
masks. Repeated masks alone do not prove a common quadratic cover.
Failure of this recursion would not exclude the disjoint L=8 target.
No numerical search or positive solution is claimed here.
