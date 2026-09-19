# Three-edge paths with moving extra errors force rational leaf weights

2026-09-19. A necessary condition beyond the fixed-extra model; not a counterexample or a global label bound.

Use the elliptic domain, nonkernel fibers D_a of size ell, fiber locators F_a=N_H-aB_H, and C_H from TWO_FIBER_LINEAR_RESOURCE_BOUND.md. Let ell>50 be prime, k=n-4ell+1, r=4ell-1. Fix a genuine two-dimensional syndrome plane L.

For each chosen edge {a,b}, fix a nonzero syndrome point in L and one error vector e_ab supported on D_a union D_b union E_ab, where |E_ab|<=5 and E_ab is disjoint from its own two fibers. Assume the restriction of e_ab to EACH of its two fibers has more than ten nonzero coordinates. Values need not be constant or canonical, and extra sets may vary by edge.

## Path identity

Take a simple path a-b-c-d of such chosen edges. The adjacent syndrome points are distinct: if their errors were proportional modulo the code, their difference would be supported on at most 3ell+10<=r coordinates, hence zero by the MDS property. On the exclusive leaf fiber, however, the first error has more than ten nonzero coordinates while the other error can meet it in at most five extra coordinates, a contradiction.

A relation alpha*s(e_ab)+beta*s(e_bc)+gamma*s(e_cd)=0 therefore has alpha,gamma nonzero. Its corresponding codeword w is nonzero: on D_a the other two errors can affect at most ten coordinates, whereas e_ab has more than ten nonzero entries.

Let J be the monic locator of all extra coordinates of the three errors lying outside D_a union D_b union D_c union D_d, and put d_J=deg J<=15. The shortened-code identity is exactly

    w(X) = Phi(X)/(F_a F_b F_c F_d J) * Q(X),
    deg Q <= d_J.

Here equality means the unique degree-<k polynomial representing w, and Q is nonzero. Divisibility holds because w vanishes outside the displayed support; the degree bound follows from k-1=n-4ell. Since J has no roots on these four fibers, evaluating on D_a and using the quotient-map identity gives

    e_ab(x)/C_H(x) = c * Q(x)/J(x)

at all but at most ten points of D_a, where c is a nonzero scalar depending on the path and relation. The same holds at the other leaf D_d. Thus each oriented edge extendible to a simple three-edge path has a rational model of numerator and denominator degrees at most fifteen on its leaf, with at most ten discrepancies. The denominator has no roots on that leaf.

## Independence from the chosen path

Choose two extensions of the same oriented edge a->b. Their rational models agree with the same e_ab/C_H on at least ell-20 points of D_a. Their cross-multiplied difference has degree at most thirty. Since ell>50, it vanishes identically. Therefore there is a UNIQUE reduced rational function R_(ab,a) obtained from all such paths; uniqueness is as a rational function, not as a choice of numerator/denominator normalization.

In particular, its reduced denominator divides every path locator J. It therefore divides their polynomial gcd. If the only extra coordinates shared by all these path locators lie in a set Z of size d, then R_(ab,a) has at most d distinct finite poles, all in Z. The reduced numerator degree is at most the reduced denominator degree, since the original model has deg Q<=deg J and cancellation reduces both degrees equally. Hence both reduced degrees are at most d. If this intersection is empty, the intrinsic model is constant. Actual leaf discrepancies may still remain.

The actual discrepancy set is contained in the intersection, over all extensions a-b-c-d, of (E_bc union E_cd) intersect D_a. Thus two extensions with disjoint such contamination sets imply exact agreement on the entire leaf. Without that additional condition the rational model need agree with the actual error on only ell-10 leaf coordinates. No common rational model across different edges or subgroups is claimed.

## Scope and next requirement

This generalizes the rigid one-dimensional shortened-code step for zero extra errors: with up to five moving extras per edge, the path instead has a shortened code of dimension at most sixteen, and its leaf weights have the intrinsic rational description above.

The >10 nonzero entries per endpoint fiber and ell>50 hypotheses are explicit. Thin leaf errors are not counted here. The result alone neither bounds the number of edges nor proves that their received plane belongs to a fixed finite-dimensional subgroup space. A further compatibility argument across edges would be needed to recover a global count. Conversely, a proposed dense positive construction in this model must supply these rational leaf weights and their cross-edge compatibility; arbitrary independent moving extras cannot be treated as free parameters.
