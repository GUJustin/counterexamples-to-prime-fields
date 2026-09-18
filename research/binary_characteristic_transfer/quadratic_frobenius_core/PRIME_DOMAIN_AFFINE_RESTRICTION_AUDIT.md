# Prime-domain restriction under affine evaluation changes

Independent scope audit of the Fp3 two-block / one-fiber construction. This concerns only restricting its existing words after x=a t+b, with a≠0 in E=F_(p³), to a set H⊂F_p (in particular H⊂F_p*). It is not a claim about arbitrary coordinate transformations, new words, or prime-field constructions.

Write V0=W, V1=eta W, two distinct F_p-planes in E. The original assignment is block0 when x≠0 and x²∈V0, and block1 when x≠0, x²∈V1, and x²∉V0. One-fiber surgery only removes coordinates.

## Square membership on an affine prime-field line

For each i, compose (a t+b)² with the linear projection E→E/Vi. This is a vector-valued polynomial of degree at most two over F_p. If not identically zero, some coordinate is a nonzero scalar polynomial of degree at most two, so at most two values t∈F_p satisfy square membership in Vi. If identically zero, all affine-line values satisfy membership. For odd p, the latter condition is exactly

    a², ab, b² ∈ Vi.

If both membership polynomials vanish identically, these three coefficients lie in V0∩V1, a one-dimensional space. As a≠0, both a² and ab are scalar multiples over F_p of a², giving b/a∈F_p. In this case all squares lie in the single line a²F_p, and disjointization places every nonzero evaluation in block0. No mixed block structure survives.

## Complete case split

* Neither membership polynomial vanishes identically: at most four affine-prime-line coordinates lie in the union of the two blocks. A larger domain cannot be obtained by this restriction.
* Membership in V0 is identically true: every allowed nonzero point is assigned to block0, regardless of V1. The restricted words are exactly f(t)=(a t+b)^(2p)=(a^p t+b^p)² and g(t)=0, both degree at most two in t.
* Membership in V1 is identically true but membership in V0 is not: at most two coordinates are assigned to block0; every other allowed coordinate lies in block1. Away from those at most two exceptions, f(t)=eta^(1−p)(a^p t+b^p)² and g(t)=1. Every word f+lambda*g differs from a quadratic in t at at most two coordinates.

Removing the possible zero x, applying the one-fiber deletion, or further puncturing only removes coordinates. None increases the number of exceptional coordinates in the case split. Thus on any retained domain of size h>4, every line word has agreement at least h−2 with degree-at-most-two polynomials over E. The same conclusion holds for both endpoint words and any linear combination of them. Such a restriction cannot preserve the large source distance of the original construction.

For the unshifted prime-field domain H⊂F_p*, the conclusion sharpens to exact quadratics: x²∈F_p*, so either F_p⊂Vi and all H has that membership, or Vi∩F_p={0} and none does. After disjointization all retained points lie in one block, or there are no retained points. The restricted words are x² or eta^(1−p)x², with constant direction.

## Alphabet caveat

The quadratic explanations above have coefficients in E. A naive restriction of extension-field words does not itself produce a code over F_p. If a proposed restriction is genuinely F_p-valued, then on the good coordinates these quadratics take F_p values. Provided at least three distinct good coordinates remain (e.g. h≥5), interpolation over F_p forces their coefficients to lie in F_p, so the same h−2 agreement conclusion holds for the prime-alphabet code. Applying an F_p-linear trace/projection to all word values also preserves degree at most two on the good coordinates. This audit does not analyze nonlinear alphabet maps.

Conclusion: restricting the published construction to a prime-field evaluation set, even after an arbitrary affine change over E, yields at most four usable coordinates or words within two coordinates of the quadratic code. It therefore does not transfer the far-source theorem to a prime-field benchmark domain. The claim is limited to this restriction/affine-change mechanism; no general prime-field or protocol impossibility follows.
