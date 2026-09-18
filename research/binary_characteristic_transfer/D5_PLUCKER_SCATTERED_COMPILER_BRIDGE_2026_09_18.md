# Five-dimensional compiler: exact scattered bridge and native coverage

September 18, 2026. The trace-dual bridge and published off-scalar input are independently audited in `D5_TRACE_DUAL_LOCATOR_INDEPENDENT_AUDIT.md` and `D5_SCATTERED_LITERATURE_PARAMETER_AUDIT_2026_09_18.md`. The scalar calculation is in `D5_SCALAR_CUBIC_LABEL_CRITERION_2026_09_18.md`; its integer identities are replayed by `verify_d5_scalar_tangency.py`. This note does not invoke the full September 2026 scattered-set classification.

Let E=F_(p^5), and let W range over its three-dimensional Fp-subspaces. Write its monic locator as X^(p³)+a1 X^(p²)+a2 X^p+a3 X. Its compiler label is z=theta*a1+a2^p−a1^(p+1).

## Trace duality resolves the parameter mapping

For U=W^perp under the trace pairing, choose a basis u,v and put Pij=u^(p^i)v^(p^j)−u^(p^j)v^(p^i), with indices modulo five and antisymmetric signs. Orthogonality of Moore rows is exactly Tr(wu)=0. Hodge complementary minors give Delta012=cP34, Delta013=−cP24, Delta023=cP14. The alternating determinant defining the locator therefore gives a1=P24/P34 and a2=P14/P34. Here P34 never vanishes for a genuine rational two-space.

Frobenius gives a2^p=P02/P04 and a1^p=P03/P04. The Plücker relation P02P34−P03P24+P04P23=0 yields

    z=(theta P24−P23)/P34.

Raise its zero numerator to p³. The resulting equation is

    theta^(p³)P02−P01−z^(p³)P12=0.

Up to sign this is the determinant on u,v of the map

    L_(alpha,beta)(u)=(u−alpha u^(p²), u^p−beta u^(p²)),
    alpha=z^(p³), beta=theta^(p³).

Thus the compiler's three-space problem is exactly the two-space collision problem for this map, after Frobenius conjugation. It is not the direct two-space locator formula without trace duality. For theta=1 and z≠1 the map is injective: its second coordinate vanishes only on Fp, and its first coordinate there is (1−z)u. Consequently a missing compiler label is equivalent to maximum scatteredness of L_(z,1). At z=1 the trace polynomial has a four-dimensional kernel; any three-space in it gives label one directly.

## Published off-scalar result and exact scalar remainder

Montanucci–Zanella, Proposition 4.3, proves that beta≠0 and alpha^p/beta^(p+1) outside Fp preclude maximum scatteredness. For p≥37 its proof is theoretical via the displayed Hasse bound; no small-field computation is needed here. Therefore every z outside Fp is attained when theta=1. Source: [accepted manuscript](https://backend.orbit.dtu.dk/ws/files/265791313/Montanucci_Zanella_2021_11_25.pdf), [published article](https://doi.org/10.1016/j.ffa.2021.101983).

The separately checked scalar Pfaffian proof gives absence precisely when z≠1 and H(z)=0, where H(Z)=Z³+2Z²+3Z+1. For p≥37, H(1)=7≠0. Hence the EXACT canonical image is

    E minus {z in Fp : H(z)=0}.

In particular there are at least p^5−3 canonical labels. The sufficiency agrees with the published LP condition z^5−3z²+z+1=(z−1)²H(z), but necessity is supplied by the direct scalar proof, not by assuming that the 2022 classification is complete.

H is irreducible over Q by the rational-root test and has discriminant −23. Its Galois group is S3. Chebotarev supplies a density-one-third set of primes for which H remains irreducible, so every native label occurs along an infinite prime sequence. This gives no bound on the least such prime.

## Internal-padding consequence and exact scope

Apply `GROWING_CHARACTERISTIC_FULL_DOMAIN_PADDING.md` with d=5,s=2,theta=1. For fixed 0<rho<1 and sufficiently large p, set N=p^5, J=floor(rho N), Delta=floor((1−rho)p³/2). There are words f,g on E such that agr_J(g)=CA_J(f,g)=J, and at least N−3 challenges lambda have a strict degree-<J explanation agreeing with f+lambda*g in at least J+Delta coordinates. Along the root-free prime sequence EVERY challenge does.

A sufficient padding onset is p≥4/(1−rho), p³≥2/rho, and (1−rho)²p³/64>log4+6logp, together with p≥37. These preserve exact size w=J−p²+1 and all canonical labels simultaneously. Multiplication by the common padding locator does not assert that the other three labels remain good: the theorem is a lower bound on bad challenges, not an exact final bad-label classification.

The characteristic is N^(1/5), absolute common-agreement gap is Theta_rho(N^(3/5)), and normalized gap tends to zero. The first source is not asserted far; in the all-label case it is itself near. The alphabet is an extension field, and p is much smaller than the message dimension J. This is a growing-characteristic fixed-rate consequence of the existing locator compiler, not a prime-alphabet or first-order counterexample.
