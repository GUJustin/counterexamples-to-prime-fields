# Degree513–519 packet maps on the prescribed NTT domain

2026-09-18. Independent bounded audit. No improved fiber map or benchmark certificate is obtained. The general polynomial-map question remains open; the specific near-power/cheap-tag candidate below is excluded.

## Exact compiler ledger first

Fix p=2130706433, n=262144, k=131072, target agreement139782, fourteen common nonleading packet coefficients, and a common packet-root product. Let H be a polynomial of degree e, with selected nonzero tags having full e-point fibers in D=μ_n. Select h fibers and a disjoint fixed c-point core with locator R. The existing two-denominator compiler is

    Δ=V0−V, γ=Δ(α)/α,
    P=R[Δ(H)−γH]/[H(H−α)].

The fourteen heads give degΔ≤h−15 and the product gives Δ(0)=0. Hence

    degP≤c+(h−17)e,
    agreement=he+c,
    h≤floor((k−1−c)/e)+17.

This includes every degree contribution: replacing X^512 by a higher-degree map does not preserve the old allowable packet count/core size automatically. Partial fixed cores are permitted algebraically and must not be confused with the original full-fiber-minus-one core c=e−1.

For the original h272, e513 allows c246..256 and therefore can reach the target arithmetically; e514 allows c0..1. For e≥515, h272 already exceeds the witness-degree cap before adding any core. Reducing h can recover room, so this is not a general exclusion of those degrees.

`NEAR_POWER_PARTIAL_CORE_LEDGER.json` records a bounded exact scan over0≤c<e, with the smallest h attaining the target, full-fiber pool at most M=floor(n/e), and one reserved fiber when c>0. Under the OPTIMISTIC assumption that all tags lie in μ512, the best elementary guarantees are:

| e | M | h | c | agreement | optimistic guaranteed bank |
|---|---:|---:|---:|---:|---:|
|513|511|272|256|139792|1875165481005117658|
|514|510|272|0|139808|1875165481005117658|
|515|509|271|261|139826|467624764352815196|
|516|508|271|0|139836|467624764352815196|
|517|507|270|270|139860|116612060057184697|
|518|506|270|0|139860|116612060057184697|
|519|505|269|283|139894|29078857538620941|

The target count is274980728111395088. The first four degrees pass this optimistic count ledger; the last three do not. These are pigeonhole guarantees, not upper bounds on actual fibers. No asserted map realizes any row. For arbitrary nonzero F_p tags the product condition costs p rather than512, losing a factor p/512≈4.16million. The corresponding generic guarantees are far below target. Thus plentiful large fibers alone do not solve the count problem.

## Easy proposed families

* Any degree512 polynomial, including X^512+aX, has fibers of size at most512. With the same fourteen-head compiler and0≤c<512 the best agreement is139775; it cannot supply the seven extra agreements.
* An affine-conjugate power of degree e has full-field fiber sizes at most gcd(e,p−1), apart from the single zero fiber. For e513 and514 these gcds are1 and2. Möbius conjugation on the projective line preserves this small fiber bound, up to an excluded/added point at infinity. These are not large split-packet maps.
* For H=X^s(X^512+a), s odd, a≠0: within each μ512 coset, X^512 is constant and X↦X^s is injective. Every nonzero fiber therefore has at most512 points. The possible zero fiber also has at most512 points. This closes s1,3,5,7 as mechanisms for enlarged packets, but does not close even s.
* For first-kind Dickson D_e(X,a), a≠0, write x=u+a/u. For x∈F_p, u lies either in F_p^* or in the norm-a coset in F_(p²)^*. A fixed Dickson value makes u^e satisfy a quadratic equation. Thus a safe full-field fiber bound is2[gcd(e,p−1)+gcd(e,p+1)]. For e513..519 these bounds are8,8,4,20,4,8,8. This elementary identity excludes first-kind Dickson packets of the needed size, including affine input/output changes. It is not a claim about every rational map or second-kind Dickson variant.

## The degree514 even near-power with cheap μ512 tags

Take H=X²(X^512+a), a≠0. Put Y=X^512∈μ512. Since

    H(X)^512=Y²(Y+a)^512,

a coordinate maps to μ512 iff its Y value is a root of

    R(Y)=Y²(Y+a)^512−1 mod(Y^512−1).

This property is constant on each of the512 original cosets, each containing512 domain points. Write R=Σ_{k=0}^{511}r_kY^k. For3≤k≤511,

    r_k=binom(512,k−2)a^(514−k)≠0.

Claim: R cannot have510 or more roots in μ512. If it did, select a monic quadratic Q=Y²−sY+t whose roots include every missing root, adding roots from μ512 if necessary. Then t≠0 and Y^512−1 divides QR. Since deg(QR)≤513, its coefficients of degrees2..511 vanish. For k=5,6,7 this gives

    r_(k−2)−s r_(k−1)+t r_k=0.

Divide by r_k and clear the nonzero denominators to obtain

    a²(k−2)(k−3)−sa(k−2)(516−k)
       +t(515−k)(516−k)=0.

This is a polynomial of degree at most2 in k, with three distinct roots, so it vanishes identically. Evaluating at k=2 gives t·513·514=0, a contradiction in F_p. Hence at most509 old cosets map into μ512, containing at most260608 domain points. Consequently at most floor(260608/514)=507 FULL degree514 fibers can have tags in μ512.

Even granting no reserved core,507 candidate tags cannot certify the required bank: at the degree514 admissible core/count choices, the maximal guarantee is below target. For example h272,c0 gives ceil(binomial(507,272)/(512p^14)), and h271 requires a positive reserved core and gives ceil(binomial(506,271)/(512p^14))=101551461894817669<target. Thus this candidate does not fix the seven-coordinate shortfall by the existing elementary head/product pigeonhole guarantee. It also cannot realize the prospective509–510-full-fiber profile. This is not an upper bound on a specially concentrated coefficient fiber.

The same root argument works for tags in a multiplicative coset βμ512: replace the constant1 by β^512, leaving all used interior coefficients unchanged. It does not automatically cover additive translates of the tag subgroup.

## General near-partition identity, not a classification

If M distinct tags have full e-point fibers in D and their union leaves exactly u domain points, let U be the monic locator of those remaining points and take H monic (rescale tags otherwise). Then necessarily

    X^n−1=U(X) W(H(X)),
    W(Y)=∏_{selected tags}(Y−tag), degU=u=n−Me.

For e=512+s,1≤s≤7, the maximal pool M=512−s leaves u=s². Thus a nearly uniform maximal-fiber map would supply a highly constrained composition identity with a degree1,4,9,16,25,36,or49 cofactor. This is a concrete algebraic target for a future noncandidate-specific argument, not a proved classification. Rational H requires a separately cleared-denominator degree ledger and is not silently covered by the polynomial formulas above.

Next useful work would need either a genuinely different map realizing these near-partition identities together with a cheap tag-product range, or a quantitative coefficient-fiber concentration proof. A large random scan of polynomial maps is not supported by the present evidence.

## Independent audit: maximal degree513 pool is impossible

The following additional general closure passes independently; it does not require cheap subgroup tags. For p>n≥3, define

    S_n(X)=(X^n−1)/(X−1).

Over the algebraic closure, all its critical points are simple and their critical values are pairwise distinct. Indeed

    (X−1)² S_n'(X)=N(X)=(n−1)X^n−nX^(n−1)+1,
    N'(X)=n(n−1)X^(n−2)(X−1).

Neither0 nor1 is a critical point of S_n: S_n'(0)=1 and S_n'(1)=n(n−1)/2≠0. Away from0,1, a root of N is simple by the displayed derivative, and therefore gives a simple root of S_n'. At such a critical point x, the equation N(x)=0 gives

    S_n(x)=n x^(n−1).

Equal critical values at x,y force x^(n−1)=y^(n−1); their N equations then force x^n=y^n. Since the points are nonzero, x=y.

This implies polynomial indecomposability. Suppose S_n=W∘H with both degrees≥2. All degrees are below p. Choose a root β of W', with multiplicity m≥1. If x is a root of H−β with multiplicity e, then the chain rule gives a zero of S_n' of multiplicity (m+1)e−1. Simplicity forces m=e=1 for EVERY root of H−β. Hence H−β has degH≥2 distinct roots, all critical for S_n and all with critical value W(β), a contradiction. This proof is over the algebraic closure and therefore also excludes decompositions over the base field.

For any a∈μ_n, the polynomial (X^n−1)/(X−a)=a^(n−1)S_n(X/a) is likewise indecomposable, since invertible input/output scalings preserve decomposability.

Now511 complete degree513 fibers in μ_262144 would occupy262143 points, leaving one point a. Their fiber product would give

    (X^262144−1)/(X−a)=W(H(X)),
    degW=511, degH=513,

contradicting indecomposability. Thus NO polynomial of degree513 has the maximal511-full-fiber pool on this domain, regardless of the tags. This argument does not exclude510 or fewer full fibers. In particular,510 total full fibers with one reserved partial core still give the optimistic μ512 pigeonhole guarantee ceil(binomial(509,272)/(512p^14))=875077224469054907, above the required count. Therefore the maximal-pool closure does not close the general degree513 route or establish a benchmark impossibility.
