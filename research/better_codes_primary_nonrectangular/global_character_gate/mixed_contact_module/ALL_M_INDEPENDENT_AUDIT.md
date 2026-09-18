# Independent audit of the all-m weighted contact ideal

Status: PASS, with the coefficient-ring precision below. No benchmark gain is asserted.

## Local filtration and globalization

In k[R,Z][h,L], the substitution h=t and L=t^2 E sends a monomial h^u L^v to t^(u+2v) E^v. Distinct powers of E remain independent, so the kernel modulo t^m is precisely the weight-at-least-m monomial ideal. Free E is essential. In particular, at m=3 the ideal is (h^3,hL,L^2), not (h^3,L). This agrees with the archived row indexing containing the extra E exponent and weight two.

The Hermite conditions give H=L+h^2 C, with C polynomial in the coefficient variables and h. Both triangular changes L↔H preserve the weighted filtration, regardless of m. Also S=h times a unit at each marked node. Therefore the proposed generators have the correct localized ideal at every node. Both the proposed ideal and the intersection of local contact ideals contain S^m; Chinese remainder decomposition modulo S^m makes these local equalities global. No unstated bound on m or characteristic, beyond squarefree nodes, is needed.

The formulas A=f-S(f'/S' mod S), B=S(1/S' mod S) satisfy the four Hermite conditions directly. Replacing f by f+Zg works over k[R,Z]. Moreover (S,H)=(S,Y-f), since A-f and B are multiples of S. The two claimed inclusions with ordinary ideal powers follow from the elementary inequalities u+v<=u+2v<=2(u+v).

## Quotient and syzygies

The ring k[X,Y,R,Z] is free of rank n over k[S,H,R,Z], with basis 1,X,...,X^(n-1). One can first divide in the monic variable H, then expand each X-polynomial by the monic polynomial S. Thus the quotient basis consists exactly of X^d S^u H^v for d<n and u+2v<m. Its rank over k[R,Z] is n floor((m+1)^2/4). The contact-graded Hilbert series is n/((1-t)(1-t^2)); this is not an original-weight Hilbert series.

In k[S,H,R,Z], the adjacent monomial syzygies H G_j-S^2 G_(j+1), with the final drop-one relation for odd m, generate all relations. This follows either by successive elimination of the highest H exponent in a relation or from the two-variable monomial ideal resolution. The free extension above preserves exactness and gives all ambient-ring syzygies.

**Ring precision:** these relations generate as a module over k[X,Y,R,Z] (or first over k[S,H,R,Z] followed by the free extension). They do not form a finite generating list over k[R,Z] alone: arbitrary X,Y multiples are still needed. The claimed finite free k[R,Z]-rank pertains to the quotient, not to a finite presentation of the syzygy module over that coefficient ring.

## Concrete filtered cancellation target

The simplest exact consequence is a simultaneous-Pade formulation, already at m=2, rather than a new unfiltered relation. Restrict to candidates F=C(X)Y+D(X)R+E(X). Membership in K_2=(S^2,H) is equivalent to

    D ≡ -CB (mod S^2),    E ≡ -CA (mod S^2).

Indeed subtracting C H leaves precisely the two indicated coefficients, which must be divisible by S^2. For a received affine line, split E and A into their intercept and Z coefficients. Thus any proposed bounds on the original X degrees, Y/R caps, and challenge degrees yield a fully explicit simultaneous approximant problem for C. The multiplication/remainder matrices use the fixed Hermite data; a low-degree C causing unusually low-degree simultaneous remainders is exactly a genuine original-weight cancellation. This formulation supplies a checkable filtered certificate instead of confusing contact length with source dimension.

For arbitrary m the same principle applies to combinations of the universal generators, but the Hermite coordinate change is not weight-preserving. A nearby list may constrain the simultaneous remainders; the all-m ideal theorem alone does not prove such a constraint or any rank excess. A useful positive next lemma would force an approximant within the primary caps from the list hypothesis, and must compare its degree to the generic simultaneous-approximation threshold. No further unstructured gate or asymptotic advantage follows merely from the universal syzygies.
