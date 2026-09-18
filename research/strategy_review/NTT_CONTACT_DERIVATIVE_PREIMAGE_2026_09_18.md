# Exact derivative preimage before sparse-deformation pairing

This is an exact ideal calculation under the ORIGINAL caps. No numerical ranks, new source monomials, or universal kernel assertion are introduced.

Let S=X^n−1, with n invertible, and choose the exact Hermite coordinate H=Y−A(X)−B(X)R used by the monomial contact compression. In particular H is monic linear in Y and partial_Y H=1. Write

 K_m=(S^max(m−2j,0) H^j : j>=0).

The frozen source V has Y-degree <=Q=159<p. Its weighted degree is strictly less than W=20846625, whereas mn=115*262144=30146560.

## Coefficientwise preimage

Expand uniquely F=sum_(j=0)^Q f_j(X,R)H^j. Since changing Y to H is a polynomial-ring automorphism,

 F in K_m iff S^max(m−2j,0) divides f_j for every j.

Also partial_Y F=sum_(j>=1)j f_j H^(j−1). Every nonzero j here is invertible because Q<p. Therefore

 partial_Y F in K_m iff
 S^max(m+2−2j,0) divides f_j for every j>=1,

with no condition on f_0. Intersecting these conditions with F in K_m gives exactly

 K_m intersect partial_Y^−1(K_m)
   = K_(m+2)+S^m k[X,R]

on the degree_Y<p range. In characteristic p without that degree bound, invisible H^(p*j) terms would invalidate this description; they are absent under the frozen cap.

For m=115, the new high-H endpoint is S H^58 (and H^59), not H^58 alone: differentiating H^58 gives 58H^57 of contact weight114. The constant-in-H term need only be divisible by S^115, rather than S^117.

## Consequence for the capped deformation kernel

The exact common first-order invisible subspace is

 Z=V intersect (K117+S115 k[X,R]).

Every F in Z is killed in the local target by the first-order variation for EVERY received-word value perturbation, because those variations are scalar multiples of partial_Y F at each node. Therefore any injective first-order obstruction certificate must first establish Z=0. If Z is nonzero, no choice of one or several sparse first-order perturbations can give an injective kernel-to-cokernel map; higher-order deformation may still succeed.

Certainly U=V intersect K117 is contained in Z. There is, however, no justified claim here that U is nonzero or that Z=U. The degree cap proves only

 V intersect S115 k[X,R]={0}:

a nonzero polynomial divisible by S115 has X-degree at least 115n>W, incompatible with the source. Intersection does not distribute across a sum: high-degree terms of a K117 member can cancel those of S115 A(X,R), leaving an element of V. Hence this argument does NOT remove the second summand from the capped preimage. Its presence is exactly the possible E-independent contribution in the first two contact layers.

As an ordinary polynomial map, partial_Y IS injective on V intersect K115, since its zero polynomial kernel is Y-independent and the preceding degree argument excludes such nonzero contact elements. That does not prove injectivity after reduction modulo K115, which is the map actually needed for deformation.

## Precise residual two-layer certificate

For F in Z define

 rho(F)=(f_0/S115) mod S²,
 where f_0=F(X,A(X)+B(X)R,R).

Then ker rho=U, and consequently Z/U embeds in k[X,R]/(S²). All original monomials satisfy i+j<=Q, so f_0 has R-degree at most Q=159. Thus this residual quotient has dimension at most 2n(Q+1), and at most 2(Q+1)=320 in each cyclic character. The latter follows because S is invariant and, for each fixed R-power, the coefficient quotient modulo S² has two dimensions in every X-character. No assertion of surjectivity or actual rank is made; the original X/Y/R caps can make this image much smaller.

An exact reduced test is therefore:

1. Establish whether U=V intersect K117 vanishes, with the original support unchanged.
2. If it vanishes, determine whether a nonzero F in V can satisfy the coefficient divisibilities above with nonzero rho(F). This is a capped compatibility condition, not a freely chosen 320-dimensional residual.
3. Only after Z=0 is established can the shifted pairing against coker M0 possibly be injective. Even then, images of partial_Y F may lie in im M0, so the kernel-to-cokernel test from the earlier note is still necessary.

This isolates the exact common obstruction without proving that it exists. The known source-column surplus over the m115 rank ceiling gives a kernel in K115; it does not imply a kernel in K117 or in Z. No dimension conclusion about these deeper spaces has been established, and no new matrix job is proposed.
