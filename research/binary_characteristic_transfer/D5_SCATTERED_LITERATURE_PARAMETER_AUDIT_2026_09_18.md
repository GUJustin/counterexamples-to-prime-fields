# Degree-five native labels: final independent admission receipt

September 18, 2026. **PASS** for the exact compiler/scattered bridge, published off-scalar input, arithmetic consequence, and internal-padding composition. The scalar geometric proof has its separate independent PASS; this receipt uses that proof without purporting to duplicate its geometry audit. No manuscript or binary-repository edits.

## Admitted statement and dependencies

For every prime p>=37, put E=Fp^5. For each three-dimensional Fp-subspace W of E write

    L_W=X^(p³)+a1 X^(p²)+a2 X^p+a3 X,
    z_W=a1+a2^p-a1^(p+1),
    H(Z)=Z³+2Z²+3Z+1.

Then the exact canonical label image is

    {z_W : W} = E minus {z in Fp : H(z)=0}.

The two proof inputs are the published Montanucci–Zanella Proposition 4.3 for off-scalar labels and the independently checked scalar argument in `D5_SCALAR_CUBIC_LABEL_CRITERION_2026_09_18.md`. Lu's full classification is not used. Since H(1)=7, the rank-drop parameter 1 is not a cubic root in the stated range. At most three canonical labels are absent.

## Exact Hodge signs and compiler/scattered mapping

Let U=W-perp for the nondegenerate trace pairing and let Pij be its Moore two-minors. If Dijk are the Moore three-minors of W, the locator coefficients are

    a1=-D013/D012,  a2=D023/D012.

The embedding-vector dot product is the trace pairing. Complementary-minor duality therefore gives

    D013/D012=-P24/P34,  D023/D012=P14/P34,

so a1=P24/P34 and a2=P14/P34. The common duality scalar cancels. P34 is nonzero: its vanishing would force the ratio of a basis of U to be fixed by Frobenius, contrary to Fp-independence. The same argument applies to P04.

Frobenius and index periodicity give a2^p=P02/P04 and a1^p=P03/P04. The Pluecker relation

    P02 P34-P03 P24+P04 P23=0

then proves exactly

    z_W=(P24-P23)/P34.

More generally, head parameter theta replaces P24 by theta P24. Define

    L(u)=(u-z u^(p²), u^p-theta u^(p²)).

Direct expansion on x^(p²),y^(p²), for a basis x,y of U, gives determinant

    P23-theta P24+z P34.

Trace annihilation and Frobenius are bijections on the relevant subspace sets, so attainment is equivalent in both directions to a determinant-zero pair of Fp-independent inputs. It is essential that the two-space is U^(p²), not the original three-space W.

For theta=1 the map L is injective exactly when z!=1: u^p=u^(p²) forces u in Fp, and its first coordinate is then (1-z)u. If injective, its image has rank five; a determinant-zero pair is exactly a projective point of weight at least two. Thus absence is maximum scatteredness. At z=1, pair any nonzero kernel vector with an independent vector: the determinant vanishes and the label is attained directly. No rank-four scatteredness assertion is substituted for this argument.

## Published off-scalar input: exact hypotheses and range

Primary source: Montanucci and Zanella, *A class of linear sets in PG(1,q^5)*, Finite Fields and Their Applications 78 (2022), 101983.

- DOI: https://doi.org/10.1016/j.ffa.2021.101983
- Accepted full text: https://backend.orbit.dtu.dk/ws/files/265791313/Montanucci_Zanella_2021_11_25.pdf
- Locally read: `tmp/scattered_d5_audit/mz.pdf` and `.txt`.

I read Lemma 4.2, the paragraph immediately preceding Proposition 4.3, Proposition 4.3, and the relevant Theorem 5.5 clauses. Proposition 4.3 states that beta!=0 and alpha^q/beta^(q+1) outside Fq imply that L_(alpha,beta) is not maximum scattered. With q=p, alpha=z, beta=1, its hypotheses hold precisely for off-scalar z. Thus every such compiler label is attained.

The proof supplies an absolutely irreducible quartic / genus-at-most-three argument and explicitly uses q+1-6 sqrt(q)>0 for q>=37. Its separate small-field MAGMA assertion is unnecessary. Its irreducibility calculations are invoked as part of the published theorem, not represented here as newly rerun calculations. In particular this receipt does not replace that theorem by an unjustified assertion that arbitrary affine birational models have equal point counts.

For a separate consistency check, published Remark 5.4 makes scalar lambda!=0,1 satisfying

    lambda^5 Norm(beta)^2+lambda(1-3lambda)Norm(beta)+1=0

maximum scattered. At beta=1 this factors as

    (lambda-1)^2 H(lambda).

Thus published sufficiency agrees exactly with the independently proved scalar criterion. Neither a trace-perturbation parametrization nor an equivalence classification is silently identified with the compiler parameters.

## Prime sequence

H has no rational root (the only possibilities are +/-1), hence is irreducible over Q. Its discriminant is -23 by the cubic discriminant formula, so its splitting field has Galois group S3. For unramified primes, having no root corresponds to a 3-cycle. Chebotarev therefore gives density 2/6=1/3 of root-free primes. Removing primes below 37 and the ramified prime 23 does not affect density. Only infinitude is needed; alternatively the theorem may simply use primes passing the explicit root-free test.

## Independent internal-padding composition and finite onset

Fix 0<rho<1 and specialize the already audited internal-padding result to d=5,s=2,theta=1. Here

    N=p^5, t=p³, K0=p, J=floor(rho N),
    f0=X^(p⁴-1)+X^(p³-1), g0=X^(p²-1).

The exact elimination identity is

    L_W^p+(1-a1^p)L_W
      = X^(p⁴)+X^(p³)+z_W X^(p²)+R_W,
    deg R_W<=p, R_W(0)=0.

Hence h_W=-R_W/X has degree <=p-1 and agrees with f0+z_W g0 on W minus zero. The sign of z_W matches the scattered-map audit above.

One explicit sufficient finite onset is

    p>=37, p>=4/(1-rho), p³>=2/rho,
    (1-rho)² p³/64 > log(4)+6 log(p).

All hold eventually for fixed rho. Let w=J-p²+1. These conditions ensure w>=0 and w/N<=rho. The Gaussian population is M=[5 choose2]_p<4p^6. The previously proved hypergeometric estimate and union bound supply ONE w-subset B of E satisfying

    |B intersect W| <= (rho+(1-rho)/4)p³

for every W simultaneously. In particular B does not depend on a later choice of W or label. Multiply f0,g0,h_W by the same locator L_B. The direction g has exact monic degree J, and every witness has degree at most J-p²+p<J. Its support contains B union (W minus zero), of size

    J+p³-p²-|B intersect W|+1_(0 in B)
      >= J+(1-rho)p³/2.

This checks both the zero coordinate and the overlap subtraction. Therefore with

    Delta=floor((1-rho)p³/2), T=J+Delta,

at least N-3 native challenges have a strict degree-<J witness with at least T matches. All N do on the root-free prime sequence. Padding preserves every canonical label; it may create additional witnesses at formerly missing labels, so the result is a lower bound on the final bad-label count, not an exact padded nearest-list profile.

Since g is monic of degree J, root counting and interpolation give agr_J(g)=J. Simultaneous interpolation on any J coordinates, together with the upper bound supplied by g, gives ordinary CA_J(f,g)=J exactly. However H(0)=1, so zero is always an attained canonical label. Thus agr_J(f)>=T: the first source is near even when H has roots. This is **not a both-far native pair**. The separate independent-head extension construction changes the alphabet and does not preserve this native all-label conclusion.

The characteristic is N^(1/5), the code rate tends to rho, and the guaranteed additive gap is Theta_rho(N^(3/5)). The normalized gap tends to zero, and p is far smaller than J. Consequently this is neither a prime-alphabet specialization nor a counterexample under the DKT large-characteristic guard p>message degree.
