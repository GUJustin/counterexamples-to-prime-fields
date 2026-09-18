# The common C is polynomial on the guarded finite-pole Ceva chart

Work in characteristic zero (or characteristic not2 with the same displayed guards). Assume a valid sign-twisted eight-sextic realization in the general shifted finite-pole Ceva chart. All fourteen Y nodes are nonzero and distinct, and all eight signed candidate leading coefficients are distinct. Use the conventions of POLYNOMIAL_IDENTITY_GATE.md.

Let beta_i, i=1,2,3, be the stored ratios q-bc,q-c,q-b. They are nonzero and pairwise distinct by the six distinct-edge guards. The physical leading coefficient of B_i is

 u_i=sigma*(1-a_i)+tau*beta_i
    =beta_i*(tau-sigma*t*(S-2beta_i)).

Here sigma,t are nonzero: sigma=0 makes the all-plus quadratic coincide with its reversal, and t=0 makes candidate leading coefficients coincide.

## Every B_i has degree exactly2

The Y8 coefficient of H_ij=0 is

 -u_j*(a_i²-1)+u_i*(a_j²-1)=0.

All a_i²-1 are nonzero. If one u_i were zero, all three would vanish. But u_i/beta_i is a nonconstant affine function of three distinct beta_i, with slope2*sigma*t≠0. Hence not all can vanish. Therefore every u_i is nonzero.

## The three B_i have no common root

Each B_i vanishes at its old edge e0i because B0=0. Since the three e0i are distinct, a common divisor has degree at most1. Suppose it has root r. Then

 B_i(Y)=u_i*(Y-r)*(Y-e0i).

At an old edge eij, equality B_i(eij)=B_j(eij) implies, provided r≠eij,

 u_i*(eij-e0i)=u_j*(eij-e0j).

The stored ratios satisfy the exact same edge identity

 beta_i*(eij-e0i)=beta_j*(eij-e0j).

Among the three distinct edges12,13,23, at most one equals r. The other two form a connected graph on labels1,2,3. Every edge difference in the displayed ratios is nonzero. Thus u1/beta1=u2/beta2=u3/beta3. This contradicts the nonconstant affine formula above. The argument includes r=e0i and all repeated-root possibilities for individual B_i.

Consequently gcd(B1,B2,B3)=1.

## Polynomial norm is necessary

The identities H_ij=0 imply that

 C(Y)=(A_i²-A0²-Y*B_i²)/B_i

is independent of i. Any denominator in reduced form divides every B_i; the gcd result therefore proves C is polynomial. Its degree is exactly4, since each numerator has leading coefficient a_i²-1≠0 and each B_i has degree2.

Thus R(Y)=C(Y)²-4Y*A0(Y)² has degree exactly8. At every new Y node, the squared incidence equations give C=-2T*V, so R=0. There are eight distinct nonzero new Y values. Hence R is squarefree, has no zero root, and is disjoint from the six old edge values. In particular, a valid realization in this chart cannot evade a simple-degree8 norm-selector theorem through a rational C or an extra norm factor.

The four degree8 polynomials

 Q_i(T)=C(T²)+2T²*B_i(T²)+2T*A_i(T²)

satisfy Q_i(T)Q_i(-T)=R(T²). A valid bank therefore supplies the simple norm-factor configuration studied independently by the frontier agent.

Scope: this proof uses the established finite-pole Ceva parametrization and its nonzero/distinct stored beta ratios. It does not silently include the affine involution chart at infinity; that chart requires its own beta/leading analysis.
