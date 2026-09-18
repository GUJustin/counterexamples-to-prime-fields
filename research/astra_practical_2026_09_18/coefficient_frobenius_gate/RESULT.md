# Coefficient Frobenius: a trace compiler, with no count improvement

September18,2026. Checked the cached `TargetUpper.lean`, `Benchmark__IRSProfile.lean`, `OrbitPencil.lean`, and `HalfRadiusCollision.lean`. No stronger practical construction or certificate results. This operation fixes the evaluation domain; it is different from the failed Frobenius changes of evaluation points.

On D contained in Fp, coefficient conjugation satisfies h^(p)(x)=h(x)^p and preserves deg h<k. The benchmark still requires one E-affine challenge, acting identically on all eight rows, and one common agreement support. Its fixed-word lemma requires distinct messages near ONE word and gives L/(|E|+L-1); it does not combine lists near conjugate words.

## Constructive relative-trace identity

Put E=Fp6, K=Fp^d with d dividing6, r=6/d, and tau(z)=z^(p^d). Let alpha have degree6 over Fp, alpha_i=tau^i(alpha), and

    B_alpha(Y)=product_(i=0)^(r-1)(Y-alpha_i) in K[Y].

For any C(Y) in Fp[Y] of degree e<=r-1, set

    c_i=C(alpha_i)/B_alpha'(alpha_i),
    L(z)=sum_i c_i*tau^i(z)=Tr_(E/K)(c_0*z).

The exact partial-fraction identity is

    sum_i c_i/(Y-alpha_i)=C(Y)/B_alpha(Y).

Thus L is K-linear, acts coefficientwise without increasing witness degree, and sends the standard packet residual to

    L( R*V_U(Y) / [Y(Y-alpha)] )
       = R*V_U(Y)*C(Y) / [Y*B_alpha(Y)].                 (1)

If C has e distinct unused base-field packet tags as roots, (1) adds exactly e full agreement packets. This is a valid constructive use of coefficient Frobenius.

To keep the same affine label, gamma_U=(V_0(alpha)-V_U(alpha))/alpha must belong to K. Then applying L to f+gamma_U*g-h_U gives the E-affine family F+lambda*G at lambda=gamma_U, with a polynomial witness H_U=L(h_U). The source direction is

    G=-R*C(Y)/B_alpha(Y).

At B=1024 and deg R=1023, its agreement with a degree-<131072 polynomial is at most131071+rB. This is at most137215 for r<=6, below139782. The usual zero-constraint far-direction premise therefore survives. The outstanding issue is the number of distinct labels, not this premise.

## Exact finite ledger

The most favorable elementary count takes C=1, using the denominator degree to save leading-coefficient conditions instead of reserving extra packet tags. Keep136 selected tags among255 and agreement140287. To force degree at most131071, it suffices to prescribe t=7-r top coefficients, the product (256 possibilities), and the image of V_U(alpha)/alpha in E/K (6-d base-field coordinates).

The latter number is an exact linear dimension: evaluation of degree-<6 remainders identifies Fp6 with E. It is not an assertion that subset signatures are uniformly distributed. Pigeonhole gives:

| d | r | top coordinates | E/K coordinates | guaranteed support-family size |
|---:|---:|---:|---:|---:|
|1|6|1|5|68579341025511059, but labels lie in Fp|
|2|3|4|4|1|
|3|2|5|3|1|
|6|1|6|0|68579341025511059, the original count|

For d=2,3 the exact average is C(255,136)/(256*p^8)=0.0151058815. This is a limitation of the displayed guarantee, not an upper bound on the true fibers. The d=1 row has at most p distinct labels. Distinct supports in a common label fiber are distinct fixed-word witnesses, not extra line labels. Generic pole injectivity must not be silently carried across the new residue constraints.

Fixing that d=1 label as well gives the direct fixed-word construction

    F=R*V_0(Y)/[Y*m_6(Y)],
    H_U=R*(V_0-V_U)(Y)/[Y*m_6(Y)],

where m_6 is an irreducible sextic over Fp. One common top coefficient, common product, and common remainder modulo m_6 give deg H_U<=1023+1024*127=131071, exactly140287 agreements, and32186199 distinct witnesses. **This is exactly the count and parameters already proved in `research/better_codes_revisit_2026_09_17/SAME_DOMAIN_PADDING.md` using seven top coefficients plus product.** The sextic remainder redistributes the same seven field coordinates; it is a different identity, not an improved fixed-word guarantee. Its existing density bound is approximately2^(-160.99), below the required2^(-128).

## The automatic paired-subfield case is an existing packet compiler

Suppose alpha²=a belongs to Fp3 and tau(alpha)=-alpha. For paired supports write V_U(Y)=W_U(Z), Z=Y². Then gamma_U=Delta W_U(a)/alpha; rescale the direction to g/alpha and the label to beta_U=alpha*gamma_U in Fp3. This avoids the generic projected-residue conditions, so it must be checked separately.

The two normalized traces have the exact residuals

    (1+tau)/2:          R*W_U(Z)/(Z-a),
    (1-tau)/(2alpha):   R*Y*W_U(Z)/[Z(Z-a)].

The first is the ordinary one-pole compiler on packets of size B'=2B. It exchanges the small product key for one additional top coefficient. At B'=1024 the count denominator is p^7, versus256*p^6 for the existing two-pole construction: a loss of p/256, approximately8.32 million.

The second, with label beta_U/a, is the ordinary two-pole compiler with multiplier RY. If deg R=B-1, this multiplier has degree2B-1 but only B-1 zeros on D, because Y never vanishes. It is dominated by an actual B'-1-point core. For B=512, its inherited agreement is139775; replacing its deficient core by the ordinary1023-point core gives the existing140287-agreement B1024 construction. No additional label family appears. On the 2-power domain, rotation pairing is the available nontrivial orbit symmetry compatible with a quadratic subextension of E; the displayed free-subfield mechanism supplies no gain.

## Why conjugate rows cannot multiply this bank

For a fixed received word, any coordinatewise semilinear code automorphism fixing that word (possibly after a fixed codeword translation) fixes every witness having at least k agreements: the transformed witness agrees with the original witness on the same k nodes. Polynomial uniqueness forces equality. In particular, the six-row word (f,f^p,...,f^(p5)) has exactly the scalar list: each nearby tuple is forced to be (h,h^p,...,h^(p5)). Its selected-functional image cannot exceed that unchanged witness count.

For an arbitrary violating E-affine instance, a single support S can certify at most one challenge. If lambda1!=lambda2 worked on S, subtracting their messages and dividing by lambda1-lambda2 would explain the second source on S; subtracting lambda1 times that explanation gives the first source. The same operations preserve the selected linear constraints mu1+lambda*mu2. This contradicts the `ViolatingInstance` premise, including the nonzero-constraint fixed-word setting.

There is a sharper canonical-support check for B1024 conjugate rows. Each existing support has136 full packets plus a1023-point core. Distinct supports intersect in at most135*1024+1023=139263<139782. Thus jointly successful conjugate canonical rows must use the same U; their labels must satisfy the corresponding conjugation equations, rather than ranging independently. Conjugation preserves supports and cannot yield six admissible labels from one such support.

## Verification

`verify.py` / `verify.json` pass over the actual prime in the explicit field Fp[alpha]/(alpha^6+alpha²+20). Rabin tests certify irreducibility, and alpha^(p³)=-alpha. Four trace compilers for d=1,2,3,6 pass on a32-node base-field subgroup, including nonbase subfield labels, degree preservation, exact added packets, and the two paired identities. The full262144-node degree/count statements above are symbolic consequences; no full-domain numerical scan or new rental was used.
