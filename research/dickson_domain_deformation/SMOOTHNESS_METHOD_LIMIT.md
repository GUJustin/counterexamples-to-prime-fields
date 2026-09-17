# Why full-row Jacobian lifting cannot produce a growing fixed-gap bank

This elementary parameter count applies to the free-domain incidence
method, not to Reed–Solomon lists themselves. A large bank can exist on
a locus with dependent equations. Full row rank of all incidence
equations is simply unavailable once the list is larger than O(1/eta).

Let L>=2 distinct polynomials P_i of degree<k, k>=2, agree with one word
on selected sets of sizes A_i>k. Let m be the number of covered nodes;
thus m>=3. At each covered node eliminate the common received value by
subtracting one reference candidate. There are

    E=sum_i A_i-m equations in V=m+L*k variables.

At every realization with distinct nodes and distinct candidates, the
Jacobian has a kernel of dimension at least k+4, over any field. Hence

    rank J <= m+(L-1)k-4,
    dim leftker J >= sum_i(A_i-k)-2m+k+4.             (1)

A negative lower bound means only the trivial bound zero. Uncovered
nodes, if retained as variables, add free kernel directions and do not
change (1).

## Kernel directions

Adding the same arbitrary degree<k polynomial to every P_i gives k
independent directions. Scaling every P_i gives one more, independent
of common addition because some P_i-P_j is nonzero.

Three further directions come from projective changes of the node
coordinate. Their node components are respectively 1, x, x^2. They are
independent on m>=3 distinct nodes in every characteristic. Polynomial
components can be taken as

    delta x=1:    delta P_i=-P_i',
    delta x=x:    delta P_i=-X P_i',
    delta x=x^2:  delta P_i=(k-1)X P_i-X^2 P_i'.

Each component has degree<k; in the last one the coefficient of X^k
cancels. For the first two, the total variation of P_i(x) is zero.
For the third it is (k-1)xP_i(x), the same for incident candidates.
Thus all three annihilate every defining incidence differential. Their
independent node components also separate them from the k+1 directions
with zero node components. This proves the kernel bound without any
characteristic restriction or genericity assumption.

If A_i>=k+eta*n on an n-node domain, (1) implies that full row rank
requires

    L*eta <= 2m/n-k/n-4/n <= 2-rho-4/n.

In particular, no full-row-rank Hensel argument using all these equations
can yield L growing at a fixed positive gap. A scalable lifting proof
must account for many exact equation dependencies, use a different
presentation with controlled relations, or use a different construction.
It cannot follow merely by finding larger full-row-rank finite seeds.

## Application to the two Dickson tests

All nodes are covered. For p17, E=32,V=48,k=4 and the kernel lower bound
is8; rank32 is possible and certified. For p41, E=260,V=240,k=10, so
rank<=226 and there are at least34 unavoidable row dependencies. The
generator finds rank216, but only the explicit obstruction certificate
is used for the independent negative lifting conclusion.

This count alone does NOT obstruct lifting. In particular, a redundant
presentation of a smooth characteristic-zero locus can have dependent
rows. The p41 first-correction inconsistency is additional information,
not a consequence of the dimension count. Neither statement excludes
ramified realizations or arbitrary growing lists.
