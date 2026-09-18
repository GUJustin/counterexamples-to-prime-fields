# Preserving a quadratic seed blocks the entire doubling step

**Theorem (characteristic different from2).** Let four distinct quadratics
P_i realize the saturated length12/agreement6 bank, on twelve distinct
nodes with each pair appearing twice. There is no saturated eight-sextic
length28/agreement14 bank obtained by retaining these twelve nodes and
their received values, doubling each old label into two candidates, and
replacing each inherited pair block {i,j} by all four doubled labels.
The conclusion allows arbitrary new nodes, arbitrary new graph-block
patterns consistent with saturation, and all eight leading constants.

## Exact algebraic proof

Let S_i be the six old agreement nodes of P_i and let

    M_i=product_(x in S_i)(X-x),
    C_i=product_(j!=i)(leading(P_i)-leading(P_j)).

Saturation makes all four leading coefficients distinct. Each pair
difference has exactly its two prescribed simple roots. Consequently

    D_i:=product_(j!=i)(P_i-P_j)=C_i M_i.               (1)

Any new degree-six polynomial retaining the old received values on S_i
must be P_i+e_i M_i. Thus the proposed eight candidates are necessarily

    Q_i0=P_i+c_i M_i,    Q_i1=P_i+d_i M_i.             (2)

Their degree-six leading coefficients must all be distinct, including
c_i!=d_i. The pair Q_i0,Q_i1 already has its six common roots at S_i.
It cannot agree anywhere else. Every new block has size four and hence
chooses exactly one candidate from each doubled pair. There are sixteen
new blocks. For i!=j, each of the four bit combinations has two inherited
common nodes and must have six overall; it therefore occurs in exactly
four new blocks. Each bit of each pair occurs eight times in new blocks.

At a new node x the four values y_i=P_i(x) are distinct: all roots of
their pair differences belong to the old domain. Put

    d_i(x)=product_(j!=i)(y_i-y_j) !=0.

The elementary Lagrange identities for four distinct values are

    sum_i 1/d_i(x)=0,       sum_i y_i/d_i(x)=0.

If bit epsilon_i is chosen in this new block and V is its received value,
(1)-(2) give

    (V-y_i)/d_i(x)=e_i,epsilon_i/C_i.

Summing yields the node-independent necessary equation

    sum_i e_i,epsilon_i/C_i=0.                        (3)

Write e_i,epsilon_i/C_i=m_i+sigma_i h_i, with sigma_i in{+1,-1}.
The new-block counts established above imply

    sum_blocks sigma_i=0,
    sum_blocks sigma_i sigma_j=16 if i=j, and0 otherwise.

Multiply (3) by sigma_j and sum over all sixteen new blocks. This gives
16 h_j=0. In characteristic different from2, h_j=0, so c_j=d_j for each
j, contradicting distinctness. This proves the theorem without any
assumption of symmetry or common automorphisms.

## Two narrower checks and their scope

For the archived cyclotomic seed all P_i and M_i are even. Its entire
gluing family consists of even sextics. Saturation then forces a domain
closed under x->-x, with no zero node (an even difference cannot have a
simple root there), equal words on each pair, and the same masks. Passing
to X² would give an eight-cubic length14/agreement7 bank, contradicting
the established characteristic-zero global maximum of seven. The
Lagrange proof above is stronger and does not rely on that classification.

The bounded exact script `spectral_seed_gate.py` used the nonsymmetric
quadratics P_u=uX²+u²X+u³ for u=1,2,4,8 and the ansatz
P_i+sigma_i*z*D_i. It computed all eight sign patterns up to global sign.
Only the three2+2 patterns have possible new nodes, each in a quadratic
gcd. This has a general explanation: Lagrange additionally forces
sum sigma_i=0 and sum sigma_i P_i(x)=0. The latter is one of the three
pair-sum quadratics. None is identically zero for a valid quadratic seed,
since a parallelogram identity repeats the roots of disjoint pair
differences. Thus this restricted ansatz has at most six fresh locations,
even allowing its scale to vary, rather than the sixteen required.
The exact test completed0.54seconds under60seconds/384MiB and is now
superseded by the full theorem.

## What remains open

The obstruction depends on preserving the old received values of a
quadratic seed. Pair means of degree four or five need not satisfy (1),
so the argument does not apply to them. Likewise changing the received
values on the inherited twelve nodes can escape the theorem. No claim
is made about arbitrary eight-sextic banks or the disjoint-Hadamard
locator system.
