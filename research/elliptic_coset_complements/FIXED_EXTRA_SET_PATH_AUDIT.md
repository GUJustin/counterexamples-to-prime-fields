# Three-edge-path audit and a fixed set of extra errors

September 18, 2026. Independent bounded algebraic review. No search or manuscript edit.

**Result.** The strict two-fiber linear bound passes. A fixed set of \(d\le5\) extra coordinates changes the four-fiber kernel dimension and cannot be removed by puncturing without that cost. After discarding only \(O(n)\) possible labels, every surviving subgroup with a nonempty 3-core forces the received plane into a generalized weighted-tag space of dimension at most \(4d+3\le23\). These spaces all contain a common \(d\)-dimensional residue space whose nonzero points are entirely far; its common planes are not constructions. The quotient dimension is at most \(3d+3\le18\), but no useful intersection theorem or construction for those quotients is proved here.

## 1. Independent check of the strict two-fiber argument

Keep \(n=(\ell^2-1)/2\), \(k=n-4\ell+1\), \(t=(\ell-1)/2\), and assume a far endpoint so that each two-fiber support determines at most one projective syndrome point. Adjacent graph edges determine distinct points: otherwise their error difference would be a nonzero codeword supported on three fibers, fewer than the code's minimum weight \(4\ell\).

On a simple path \(a-b-c-d\), the three syndrome points are linearly dependent. Both leaf-edge coefficients in a dependence are nonzero, since setting either to zero would make two adjacent syndrome points proportional. The middle coefficient may be zero; nothing requires otherwise. The corresponding error combination is nonzero on a leaf fiber and is a codeword supported on the four fibers. Their union has exactly \(4\ell\) coordinates, so this codeword is a scalar multiple of

\[
\frac{\Phi}{L_aL_bL_cL_d}.
\]

Each leaf restriction is therefore proportional to the canonical weight \(C_H=K_HB_H^{t-4}\). In a graph of minimum degree at least three, every oriented edge extends to a simple three-edge path: after choosing the next neighbor, its degree leaves a final neighbor outside the two previously used vertices. Applying this to both orientations makes both restrictions of every 3-core edge canonical. Two adjacent such edges span the received plane, placing it in \(V_H\).

The audited intersection bound \(\dim(V_H\cap V_{H'})\le1\) allows at most one subgroup with a nonempty 3-core. Every other graph is 2-degenerate, hence has at most \(2t-3\) edges. Adding the at-most-one single-fiber point per subgroup gives

\[
\binom t2+\ell(2t-3)+(\ell+1)
=\frac{9\ell^2-28\ell+11}{8}<\frac94 n.
\]

This agrees with [TWO_FIBER_LINEAR_RESOURCE_BOUND.md](TWO_FIBER_LINEAR_RESOURCE_BOUND.md). It permits arbitrary error values and partial coordinate support inside the two fibers.

## 2. Puncturing a fixed extra set changes the rank

Now fix one set \(Z\subset\mathcal D\), \(|Z|=d\le5\), permitted as additional errors for every witness. Assume one original endpoint has maximum agreement strictly below \(T=n-2\ell-5\). Its punctured agreement is then also strictly below \((n-d)-2\ell\), which supplies the far-endpoint premise used below. Let \(J_Z\) be its monic locator. Puncturing gives an ordinary RS code of length \(n-d\), the same dimension \(k\), and redundancy

\[
R_Z=4\ell-1-d.
\]

Consider four tag fibers with union \(U_4\), and put \(e_4=|Z\cap U_4|\). The restricted parity-check kernel on \(U_4\setminus Z\) has dimension

\[
(4\ell-e_4)-R_Z=d+1-e_4.
\]

Equivalently, every original code polynomial whose punctured support is contained in those four fibers has the form

\[
q(X)=\frac{\Phi(X)}{L_aL_bL_cL_d\,J_{Z\setminus U_4}(X)}A(X),
\qquad \deg A\le d-e_4.
\tag{1}
\]

The original scalar minimum-weight word is recovered only when \(e_4=d\). If all extra coordinates lie outside the four fibers, the path relation has \(d+1\) polynomial degrees of freedom instead of one.

Puncturing therefore does not restore the strict theorem. Multiplying by \(J_Z\) moves the same degree cost into the witness space. Shortening could remove this cost only under an additional constraint on witness values at \(Z\), such as a common affine dependence on the challenge that can first be subtracted. Arbitrary errors on \(Z\) do not impose that constraint.

## 3. Clean fibers and the generalized weighted space

Assume henceforth \(\ell\ge23\), as in the corrected threshold window. For a subgroup whose kernel is disjoint from \(Z\), call a tag clean if its entire fiber is disjoint from \(Z\). At most \(d\) tags are not clean. On a path using four clean fibers, (1) becomes

\[
q=\frac{\Phi}{J_ZL_aL_bL_cL_d}A
=\frac{C_H}{J_Z}\,
\prod_{z\in\mathcal A_H\setminus\{a,b,c,d\}}(Y_H-z)\,A,
\qquad\deg A\le d.
\]

On any one of its four fibers the tag product is a nonzero scalar. Thus every leaf restriction lies in the \((d+1)\)-dimensional local space

\[
\left.\frac{C_H}{J_Z}\mathbb F_p[X]_{\le d}\right|_{\text{fiber}}.
\]

As before, adjacent edge syndromes in the punctured code are distinct because \(3\ell<R_Z\). Consequently every oriented edge of a clean 3-core extends to a suitable path, and its two restrictions lie in these local spaces.

Define \(\mathcal W_{H,Z}\) to be the space of words on \(\mathcal D\setminus Z\) of the form

\[
\frac{C_H(X)}{J_Z(X)}
\sum_{j=0}^{d}X^j q_j(Y_H(X)),
\qquad\deg q_j<t,
\tag{2}
\]

off the kernel, and zero on the kernel. Polynomial interpolation on the \(t\) distinct tags shows that every error with the preceding local form on two selected fibers, and zero on the other fibers, belongs to this word space. Therefore a nonempty clean 3-core forces the punctured received syndrome plane to lie in the image \(V_{H,Z}\) of \(\mathcal W_{H,Z}\) modulo the punctured code.

If the punctured syndrome image has dimension at most one, a far endpoint allows at most one qualifying challenge unless all points are close: any nonzero qualifying image spans that entire one-space. Thus the two-plane assumption loses no growing bank.

## 4. The dimension bound is at most \(4d+3\)

Space (2) has at most \((d+1)t\) parameters. Restrict to \(\deg q_j\le t-4\); the numerator

\[
F=C_H\sum_{j=0}^{d}X^j q_j(Y_H)
\]

is then a polynomial of degree at most \(k-1+d\).

The \((d+1)(t-3)\) numerator parameters are linearly independent. Indeed rewrite a possible relation as
\(\sum_{i=0}^{m}p_i(X)Y_H^i=0\), where \(\deg p_i\le d<t\). Multiply by \(B_H^m\) and evaluate at all roots of \(K_H\). Since \(N_H\) is nonzero there, the highest coefficient \(p_m\) vanishes on all \(t\) roots. Its degree is less than \(t\), so it is zero. Induction removes every coefficient. This proves independence without assuming a dimension count for a rational-function presentation.

The condition \(J_Z\mid F\) imposes at most \(d\) linear equations. Hence a subspace of dimension at least

\[
(d+1)(t-3)-d
\]

gives polynomials \(F/J_Z\) of degree at most \(k-1\). They agree with (2) also at kernel coordinates: \(J_Z\) has no kernel roots, and every such numerator has the factor \(K_H\). These are independent codewords, since evaluation is injective below degree \(k\). It follows that

\[
\boxed{\quad\dim V_{H,Z}
\le(d+1)t-\big((d+1)(t-3)-d\big)=4d+3\le23.\quad}
\]

For \(d=0\), this recovers the old three-dimensional weighted-tag space.

## 5. A common residue space that supplies no nearby words

For \(d\ge1\), define the following subspace in the quotient of punctured words by the punctured code:

\[
\mathcal R_Z=
\left\{\left[\frac{R(X)}{J_Z(X)}\right]:\deg R<d\right\}.
\]

For every subgroup with kernel disjoint from \(Z\), one has
\(\mathcal R_Z\subset V_{H,Z}\). Indeed, \(C_H\) is nonzero on \(Z\), so interpolate a polynomial \(P\) of degree less than \(d\) with

\[
C_HP\equiv R\pmod{J_Z}.
\]

The word \(C_HP/J_Z\) belongs to (2), using constant tag polynomials. Its difference from \(R/J_Z\) is the polynomial \((C_HP-R)/J_Z\), of degree at most \(k-1\). This also holds at the kernel coordinates: \(C_HP\) vanishes there and \(J_Z\) does not. Thus the claimed containment is valid for the actual zero-extended words.

The residue subspace has dimension exactly \(d\). For nonzero \(R\) of degree less than \(d\), its difference from a code polynomial \(h\) has numerator

\[
R-J_Zh,
\]

which is nonzero and has degree at most \(k+d-1\). Hence every nonzero residue class has punctured maximum agreement at most \(k+d-1\), below the required two-fiber agreement \((n-d)-2\ell\) by \(2\ell-2d>0\). Even granting all \(d\) deleted coordinates as additional matches, every extension to the original domain has agreement at most

\[
k+2d-1<T=n-2\ell-5,
\]

because \(T-(k+2d-1)=2\ell-2d-5>0\). In particular a common two-plane inside \(\mathcal R_Z\), available whenever \(d\ge2\), has no nonzero qualifying point.

Removing this common space gives the sharper dimension bound

\[
\boxed{\quad\dim(V_{H,Z}/\mathcal R_Z)\le3d+3\le18.\quad}
\]

There is an exact code interpretation of this quotient. On the punctured domain, coordinatewise multiplication by \(J_Z\) is invertible. It sends the original code to \(J_Z\operatorname{RS}_k\) and the residue words to \(\operatorname{RS}_d\). Euclidean division gives the direct sum identity

\[
J_Z\operatorname{RS}_k\oplus\operatorname{RS}_d
=\operatorname{RS}_{k+d}.
\]

Thus quotienting out the residue space becomes an ordinary RS quotient of length \(n-d\) and dimension \(k+d\), after this coordinate multiplier. Its minimum distance is \(4\ell-2d\), not \(4\ell\). This accounting does not restore the strict two-fiber theorem. For \(d=0\), the residue space is zero and the interpretation reduces to the original code.

## 6. Precise remaining fixed-set target

The discarded cases cost only \(O(n)\) possible labels when \(d\le5\) is fixed. A point of \(Z\) belongs to the kernel of exactly one order-\(\ell\) subgroup, so at most \(d\) subgroups have a contaminated kernel; each has at most \(\binom t2\) pair supports. For every other subgroup, edges incident to the at-most-\(d\) contaminated tags number at most \(dt\). Graphs with an empty clean 3-core contribute at most \(2t-3\) further edges each. The far-endpoint condition makes each support determine at most one projective point, and single-fiber cases add at most one point per subgroup.

Thus a superlinear bank with one common fixed extra set would require a common punctured syndrome two-plane \(L\) contained in \(V_{H,Z}\) for a growing number of subgroups \(H\), with \(L\not\subset\mathcal R_Z\), and actual qualifying error representations at many distinct points of \(L\). The exclusion of \(\mathcal R_Z\) is essential: mere common-plane containment already occurs there and supplies no near points.

The image of \(L\) in the quotient by \(\mathcal R_Z\) may have dimension one or two. In the one-dimensional case, many distinct projective challenge points upstairs can have the same projective image; their error representations and labels must still be checked separately. Thus even a common nonzero quotient intersection is not a construction or a label count. The previous pairwise-intersection theorem for the three-dimensional spaces gives no corresponding result for these quotients. The extra polynomial factors alter both the kernel-pole orders and the degree-versus-roots calculation.

This is the exact surviving fixed-set algebraic target. It is stronger than treating the five positions as unconstrained new parameters, and weaker than a closure or construction. Extra sets that vary with the witness remain governed by [FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md](FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md), not by one common punctured code. No numerical search is proposed without an identity predicting a qualifying shared plane beyond the common residue space.
