# Rational maps with full fibers on a multiplicative subgroup

Primary-source audit, September 15, 2026. Pure algebra and finite-field counting. Let `D=mu_n subset F`, `char(F)=p>n`, and let `R=A/C` be reduced of rational degree `B=max(deg A,deg C)`, without poles on `D`. Assume every image fiber has exactly `B` elements, so `|R(D)|=M=n/B`.

## Finding

The literature located here does **not** establish that these hypotheses force `F(X)/F(R)` to be Galois, even when `M=B=512`. Accordingly it does not justify classifying all such maps as monomial or twisted-involution maps, or asserting that one family dominates their image-domain counts. The distinction between a full projective-line value set and the image of a prescribed proper subgroup is essential.

A rigorous **conditional** classification is available: if the function-field extension is Galois, only cyclic and dihedral quotients occur, up to a Möbius change of the output. The short finite-field argument is summarized below; `structured_domains` and `gram_norm` are independently developing/reviewing its full proof.

## 1. Closest primary literature: minimal value-set rational functions

Daniele Bartoli, Herivelto Borges, and Luciane Quoos, *Rational functions with small value set*, Journal of Algebra **565** (2021), 675–690, DOI [10.1016/j.jalgebra.2020.08.039](https://doi.org/10.1016/j.jalgebra.2020.08.039), studies `R(P^1(F_q))`. Its minimum is `ceil((q+1)/B)`. Thus *minimal value-set rational function* in this source is a global projective-line notion, not the restricted-subgroup property above.

Their small-image-implies-Galois theorem has both a global image hypothesis and quantitative degree/field restrictions. In the inspected Oberwolfach preprint, Theorem 1.2 assumes `deg g=d`, `deg f=d-s`, `0<s<=d`, and

`Delta=sqrt(q)-(d-s)(d-s+1)>0`,

`|V_h| < ceil((q+1)/d)+(Delta^2+1)/[(d-1)d^2]-1`.

The preprint is an earlier version with omitted proofs explicitly noted in Remark 1.3; the published article reorganizes numbering. Use the published theorem after checking its final hypotheses before any load-bearing invocation. No such invocation is warranted from the subgroup-image hypothesis alone. [Inspected preprint](https://d-nb.info/1208741292/34).

At the proposed parameters, `q=p=2130706433`, `n=262144`, `B=512`, `M=512`. The domain is a proper subgroup of index **8128** in `F_p^*`; a bound on its 512 image values says nothing comparable about all `p+1` inputs. The global fiber-count lower bound is **4,161,537** image values. Even the preprint's auxiliary positivity condition fails when the smaller numerator degree is 256 or 511, since `sqrt(p)<46160<256*257`. A favorable normalization would still leave the missing global-image hypothesis.

For terminology, use **full degree-sized fibers on a prescribed multiplicative subgroup**, or explicitly define *relative minimal image*. Do not silently identify it with the source's global MVSRF notion.

## 2. Subgroup-intersection estimates: relevant, but not a classification here

Sergei V. Konyagin, Igor E. Shparlinski, and Ilya V. Vyugin, *Polynomial Equations in Subgroups and Applications*, [arXiv:2005.05315](https://arxiv.org/html/2005.05315), Theorem 1.2, gives a subgroup-point estimate for an irreducible bivariate polynomial of bidegree `(u,v)` whose lowest homogeneous part has at least two monomials. For a subgroup of size `t`, one scaled polynomial, and the theorem's size hypotheses, its bound is

`12*u*v*(u+v)*g*t^(2/3)`,

where `g` is the gcd of differences of total degrees of nonzero monomials. The size hypotheses include `t <= p^(3/4)/2` and an unspecified degree-dependent lower cutoff `t >= c_0(u,v)`.

The natural collision polynomial is `A(X)C(Y)-A(Y)C(X)`. Balanced fibers give exactly `n*B` ordered collision pairs in `D^2`. However the collision polynomial is reducible (it contains the diagonal), and individual components must satisfy the theorem's hypotheses. The displayed degree-dependent constant is far too large under a general bidegree-512 substitution to contradict `nB` at the target parameters. This source supplies a possible tool after discovering special low-degree components, not the desired rational rigidity theorem.

## 3. Conditional Galois classification (direct finite-field argument)

This paragraph is a derivation, not a claim that the preceding sources prove subgroup Galoisness. Suppose `n>=3` and `F(X)/F(R)` is Galois of degree `B`. Every deck transformation preserves each fiber. Since every selected fiber already has `B` distinct points, it is the complete geometric fiber; hence the deck group preserves `D`.

Every Möbius transformation `g(X)=(aX+b)/(cX+d)` preserving `D` satisfies

`(aX+b)^n-(cX+d)^n=lambda*(X^n-1)` with `lambda!=0`.

Because `p>n`, all intermediate binomial coefficients are nonzero. If all four coefficients were nonzero, the coefficients of `X` and `X^2` would force `a/b=c/d`, contradicting invertibility. If a coefficient vanishes, the same middle identities force either `g(X)=alpha X` or `g(X)=alpha/X`, with `alpha in mu_n`. Thus the stabilizer is exactly the dihedral group of order `2n`; no complex-unit-circle reasoning is used.

Its subgroups yield the following invariant fields:

- Rotation subgroup of order `B`: generator `X^B`.
- Dihedral subgroup with rotation order `d` and total order `B=2d`: generator `X^d+c/X^d`, where `c in mu_(n/d)`.

Equality of extension degrees implies that `R` differs from the relevant invariant by an output Möbius map. The full-fiber condition in the dihedral case is precisely that `c` be a nonsquare in `mu_(n/d)`: on `y=X^d`, the remaining involution is `y -> c/y`, and its fixed-point equation is `y^2=c`. Restrict the output Möbius map to avoid poles on the finite image when the setup requires all image values finite.

The same argument handles a *geometrically* Galois extension: a deck map preserving at least three points of `D subset F` is defined over `F`, so the geometric deck group descends. The unrestricted Galois hypothesis remains additional.

General finite-subgroup classification is independently available in Xander Faber, *Finite p-Irregular Subgroups of PGL_2(k)*, [arXiv:1112.1999](https://arxiv.org/html/1112.1999). That paper recovers the classical tame classification; it does not prove that the rational map in this problem has a full deck group.

## 4. What has and has not been ruled out

For `B=M=512`, the Galois branch reduces to output transforms of `X^512` and `X^256+c/X^256`, with `c` a nonsquare in `mu_1024`. No additional Galois family can evade that conclusion under the stated hypotheses.

Non-Galois maps remain outside it. The known arbitrary two-block construction has only `M=2`; it disproves an unrestricted rational classification but does not give a 512-value counterexample. Composing it with `X^d` increases fiber degree while retaining two image values. Output Möbius transformations only relabel a partition. Rational functions used to permute norm-one groups `mu_(q+1)` in quadratic extensions address different domains; they cannot be imported as maps on this prescribed split subgroup without a proved conjugacy and degree/fiber check.

No genuinely different full-fiber family with 512 image values was established by this focused search. No theorem found here excludes one. The remaining concrete question is whether full fibers on `mu_262144` force a degree-512 rational map to be Galois (or otherwise force its image statistics to obey a bound sufficient for the intended counting application).

## Citation limits

The source summaries above paraphrase only the displayed definitions/theorems and remain within 200 words per primary source, excluding this note's independently derived parameter calculations and conditional algebra. No source PDF was added to the repository. The earlier preprint's theorem numbering and incomplete-proof notice are retained to prevent it being mistaken for an audited final published proof.
