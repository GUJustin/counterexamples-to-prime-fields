# Mixed linearized-square core: independent classification

PASS with one necessary geometric-irreducibility qualification. Let p>2, E=F_{p³}, W=span_{F_p}(w1,w2) with independent w1,w2, and s in E. On the full plane W put F(x)=(x^p−sx)^2. Write Q=aX²+cX+b.

**Conclusion.** Every Q with more than four matches on W is either even (c=0) or a polynomial square over E. There are at most p(p+1) polynomial-square witnesses having more than two matches. The square family need not lie in a two-dimensional coefficient subspace; the conclusion is a union of an even family and a separately bounded nonlinear square family.

## Nonsquare quadratics

For U,V in F_p introduce the invertible E-linear change

 X=w1 U+w2 V,
 Y=(w1^p−s w1)U+(w2^p−s w2)V.

Its determinant w1 w2^p−w2 w1^p is nonzero, independently of s. Matching points lie on the conic C:Y²−Q(X)=0.

A nonsquare polynomial Q over E need not give a geometrically irreducible conic. If Q=k(ell X+m)^2 with nonsquare k in E, equality Y²=Q(X) at an E-point forces Y=ell X+m=0, so there is at most one point; a nonsquare constant gives none. These cases are harmless but must be removed before invoking Bezout. Every other nonsquare polynomial Q of degree at most two gives a geometrically irreducible conic.

For this remaining case, more than four F_p-points are common to C and its coefficientwise Frobenius conjugate. Bezout forces them to be proportional. Equivalently their common projective coefficient vector is Frobenius-fixed, so scaling one nonzero coefficient to one makes every coefficient lie in F_p. In the U,V coordinates the linear part is exactly −c(w1 U+w2 V). If c!=0, both linear coefficients are nonzero and their ratio w2/w1 is not in F_p, contradiction. Thus a nonsquare Q with c!=0 has at most four matches.

## Square quadratics

Write Q=(uX+v)^2, allowing constant and zero squares. Matching is equivalent to one of

 x^p−(s+u)x=v,   x^p−(s−u)x=−v.

On W each is an affine F_p-linear equation. Its kernel has dimension at most one: a nonzero kernel is contained in the roots of X^{p−1}=s±u, which form one F_p-direction. Hence each solution set is empty, a singleton, or an affine F_p-line. If there are more than two matches, at least one full line occurs.

A full line ell=x0+h F_p determines Q uniquely. Since p>2, equality at its p distinct x-values determines a quadratic. Explicitly the forced square is

 Q_ell(X)=((h^p−s h)/h · X + (x0^p−s x0)−((h^p−s h)/h)x0)^2.

There are p(p+1) affine lines in W. Assigning any rich square witness one of its full matching lines is injective after choosing one per witness, because a line determines only one Q. Thus the number of square witnesses with more than two matches is at most p(p+1). Each has at most 2p matches; no assertion that all these upper bounds are attained is needed.

## Scope and relation to earlier gates

The identity X^{2p}+tX^{p+1}=(X^p+(t/2)X)^2−(t²/4)X² transfers this classification to that mixed word on W by a common even quadratic shift. Its rich witnesses are therefore an even coefficient plane plus a translated square family of size at most p(p+1). This is a core classification, not a global received-line or amplification impossibility theorem.

The scalar-nonsquare exception is already distinguished in `../fp3_quadratic_roots/PROOF.md`; it is handled explicitly here rather than silently assuming geometric irreducibility. Full-line matching is also the mechanism behind the earlier fresh-line explorations. No new finite-field scan or fresh-block claim is made: any follow-up would need a genuinely new synchronization identity for the bounded square family, rather than treating its three coefficient slots as independently free.


## Sharpening: the remaining even nonsquare family has at most p members

This additional argument passes independently. Retain the linear forms X=w1U+w2V and L=(w1^p−s w1)U+(w2^p−s w2)V. They are independent. In the projective plane of binary homogeneous quadratic forms, their squares determine the line

    ell=P(span_E{X²,L²}).

This line is not defined over F_p. Indeed, if it were, containing [X²] would force it to contain all three distinct Frobenius conjugates of [X²]. These lie on the nonsingular Veronese conic of squares. They are distinct because w2/w1 has degree three over F_p. A line cannot meet this conic in three distinct geometric points. This uses p>2, as assumed throughout.

Consequently ell contains at most one F_p-rational point: two distinct such points would define ell over F_p. For an even nonsquare Q=aX²+b with more than four matches, the preceding conic argument says that Y²−aX²−b, expressed in U,V, becomes F_p-defined after a scalar multiplication. In particular its nonzero homogeneous quadratic part L²−aX² represents an F_p-rational point of ell. The map a→[L²−aX²] is injective, since L² and X² are independent. Thus there is at most one possible a.

For that a, choose a scalar k!=0 making k(L²−aX²) an F_p-coefficient quadratic form. The remaining constant coefficient forces k b in F_p, giving at most p choices of b. Changing the normalizing scalar by an F_p* factor does not change this allowed scalar line. The geometrically reducible nonsquare cases already have at most one match and contribute nothing here.

Combining the at-most-p even nonsquares with the at-most-p(p+1) square witnesses proves the uniform bound

    #{Q in E[X]: deg Q<=2, agr_W(F,Q)>4} <= p²+2p.

For p=3 the threshold exceeds some fiber counts, but the same bound and proof remain valid. After the common quadratic shift this also bounds the rich quadratic bank for X^{2p}+tX^{p+1} on W. It excludes a p³-sized rich core bank within this model; it does not bound the number of fresh labels generated by an additional received-line construction.


## Sharp bound and an explicit extremal plane (p>=5)

The preceding upper bound improves by one. In the even nonsquare family, b=0 gives Q=aX². If it is nonsquare, the scalar-square argument gives at most one matching point. It therefore does not qualify. Hence, for every s and W,

    #{quadratics with more than four matches} <= p(p+1)+(p−1)=p²+2p−1.

This bound is attained for every odd p>=5. Choose t in E\F_p, a nonsquare d in F_p*, and W=span_{F_p}(1,t). Set

    s=(t^(p+1)−d)/(t²−d),
    k=(1−s)/t=(t−t^p)/(t²−d),
    a0=k²d,   kappa=k²(t²−d).

All displayed denominators and k,kappa are nonzero: t has degree three, and t^p!=t. With x=U+tV, U,V in F_p, direct substitution gives

    L=x^p−sx=k(tU+dV),
    L²−a0 x²=kappa(U²−dV²).

Thus each c in F_p* gives the even quadratic Q_c=a0X²+kappa c, whose matching equation is U²−dV²=c. The quadratic norm from F_{p²} to F_p has exactly p+1 preimages of each nonzero c. These p−1 polynomials are nonsquares over E, since their leading and constant coefficients are nonzero and their linear coefficient is zero; a polynomial square of degree two with nonzero leading coefficient has zero linear coefficient only when its constant coefficient is zero (odd characteristic).

Every affine F_p-line in W supplies a square Q_line agreeing at all p points, as above. These p(p+1) polynomials are pairwise distinct. Suppose two distinct lines supplied the same square Q. The nonzero degree-two polynomial L²−Q(X), in U,V, vanishes identically on both lines, and hence is a nonzero scalar times their two affine linear equations. Its homogeneous quadratic part would therefore be an F_p-defined split (possibly repeated-factor) form after scaling. But that homogeneous part lies on the pencil ell, whose unique F_p-rational point is the exhibited anisotropic form U²−dV². This is impossible. The same reasoning includes parallel lines, whose homogeneous product is a repeated linear factor.

Because p>=5, all p-point line witnesses and all (p+1)-point norm witnesses have more than four matches. Their coefficient-square statuses separate the two families. The upper bound is therefore attained exactly:

    maximum possible number of >4-match quadratics on such a plane core
    = p²+2p−1.

This is a sharp local core classification/construction. It is not a received-line exception count, a first-order-threshold crossing, or a manuscript claim. The supplied p=5 census is compatible with the proof (30 square witnesses plus four even nonsquares), but is not needed for it and was not independently rerun here.
