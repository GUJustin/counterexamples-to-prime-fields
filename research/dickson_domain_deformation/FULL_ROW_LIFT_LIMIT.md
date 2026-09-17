# Full-row Jacobian lifting cannot produce growing fixed-gap banks

September 17, 2026. This is a limitation of the sufficient lifting test,
not a nonexistence theorem for characteristic-zero lists or lifts.

Let L>=2 distinct degree-<k polynomials, k>=2, agree with a received
word on respective prescribed supports of sizes A_i. Let c>=3 be the
number of distinct covered evaluation nodes. Allow all covered nodes,
all candidate coefficients, and all received symbols to move. Eliminate
received symbols by choosing one reference candidate at every covered
node and imposing equality to that candidate for every other incidence.

There are E=sum_i A_i-c equations in M=c+Lk variables. At every such
configuration, their Jacobian has a kernel of dimension at least k+4:

* k common polynomial additions;
* one common scaling of all candidate polynomials;
* three projective changes of the evaluation coordinate, with the usual
  degree-(k-1) denominator factor applied to all candidates.

Consequently

    rank J <= c+(L-1)k-4,
    E-rank J >= sum_i(A_i-k)-2c+k+4.                 (1)

In particular, the full-row-rank Hensel criterion requires

    sum_i(A_i-k) <= 2c-k-4.                         (2)

For A_i>=k+eta*n on an n-node code, c<=n implies

    L <= (2n-k-4)/(eta*n) < 2/eta.                 (3)

Thus this sufficient criterion can never certify an unbounded bank at
fixed positive gap, even if both n and the seed prime grow. This closes
a different route from the previously proved generic-fiber obstruction:
searching for larger full-row-rank free-domain incidence seeds cannot
supply the missing growing-list family.

## Explicit tangent motions and independence

Write D=k-1. The three node/polynomial tangent pairs are

    delta x=-1,   delta P=P';
    delta x=-x,   delta P=XP';
    delta x=x^2,  delta P=D*X*P-X^2*P'.

The last polynomial has degree at most D because its top term cancels.
At an incidence P_i(x)=P_ref(x), all three linearized difference
equations vanish. Common additions and scaling also annihilate them.

Any linear dependence among these motions first gives a degree-at-most-
two polynomial vanishing at all c>=3 distinct nodes. Its coefficients
are zero, eliminating the three coordinate motions. The remaining
relation is Q+tP_i=0 for every i. Two distinct candidates force t=0,
and then Q=0. Hence all k+4 motions are independent. The argument works
in every characteristic. Uncovered nodes can be omitted entirely; adding
them back introduces equally many variables and unconstrained motions.

## Consequences for the current Dickson seeds

For the complete binomial bank, n=4k, L=n/2, A=3n/8 and c=n. Criterion
(2) would require n^2/16 <= 7n/4-4, or n^2-28n+64<=0. Thus every such
seed with n>=32 necessarily fails full row rank. The p=17, n=16 seed
passes; the p=41, n=40 seed cannot pass for structural reasons.

At p=41, the full bank has E=260, M=240 and rank216. Equation (1)
already forces at least34 row dependencies; there are44 in fact. The
ten extra dependencies beyond the geometric count match the ten kernel
directions remaining after the14-dimensional normalization used in the
ramified-obstruction certificate. This count alone does NOT imply a
lifting obstruction; the second-order obstruction is still needed.

The liftable ten-candidate subbank has E=110, M=140 and rank110, so it
falls within the necessary limit L<=floor(66/5)=13. Nothing here proves
that all banks of sizes11--13 fail or succeed.

A Jacobian with dependent displayed equations can define a smooth
reduced locus. Accordingly, this is not a claim that every growing bank
must lie at a singular algebraic variety. A route using redundant
identities, a different presentation, or compatible singular lifting
remains possible. The obstruction applies to the specific full-row-rank
criterion for the uncompressed incidence equations.
