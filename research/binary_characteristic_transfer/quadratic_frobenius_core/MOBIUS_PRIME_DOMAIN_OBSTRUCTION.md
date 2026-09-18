# Independent audit: Möbius prime-domain obstruction

Verdict: PASS, for odd characteristic and finite prime-field parameter nodes avoiding poles. This is a restricted compiler obstruction, not a statement about arbitrary nonlinear coordinate maps or arbitrary code equivalences.

## Statement

Let E=F_{p^3}, let W be a two-dimensional F_p-subspace, and let eta be nonzero. Put
D0={x != 0: x^2 in W} and D1={x != 0: x^2 in eta W}\D0.
On D0 take f(x)=x^{2p}, g(x)=0; on D1 take f(x)=eta^{1-p}x^{2p}, g(x)=1.
Let R(z)=(az+b)/(cz+d) be a nonconstant Möbius map over E. Among distinct finite z in F_p avoiding its pole, either at most twelve have R(z) in D0 union D1, or every accepted image lies in a single block and the standard quadratic GRS transformation makes both received words polynomials of degree at most two. The same conclusion holds after any puncturing of the domain.

## Trace identity and its rigidity

Write W=ker Tr_{E/F_p}(kappa ·), with kappa nonzero. At a prime-field parameter, membership R(z)^2 in W is tested by the rational function

F(Z)=sum_{i=0}^2 kappa^{p^i} ((a^{p^i}Z+b^{p^i})/(c^{p^i}Z+d^{p^i}))^2.

Clearing the three squared linear denominators produces a polynomial of degree at most six. Thus more than six accepted finite parameters force F identically zero. The same reasoning applies to eta W by replacing kappa by kappa/eta.

If c is nonzero and d/c is not in F_p, its three conjugates are distinct: the extension degree is prime. Consequently the three summands have distinct poles. Each has a nonzero double-pole coefficient, since kappa is nonzero and ad-bc is nonzero. No cancellation is possible. An identity therefore forces c=0 or d/c in F_p.

In the first case write R=u+vZ; in the second write R=u+v/(Z+t), where t is in F_p and v is nonzero. In either case R=u+v psi for psi in PGL_2(F_p). The identity, viewed as a polynomial in the transcendental variable psi, gives

Tr(kappa u^2)=Tr(kappa uv)=Tr(kappa v^2)=0.

Here odd characteristic is used for the middle coefficient. Hence u^2, uv, v^2 all lie in W. If u/v were outside F_p, it would have degree three, and v^2 times 1,u/v,(u/v)^2 would be linearly independent over F_p. This contradicts dim W=2. Therefore R=v phi with phi in PGL_2(F_p).

All finite nonzero images now lie in v F_p^*. Their squares lie in v^2 F_p^*. Membership in each of W and eta W is all-or-none. The disjointized blocks consequently put every accepted image in just one block. If more than twelve parameters are accepted in total, one block has more than six, so this rigidity applies. Otherwise the asserted twelve-point bound is immediate.

## GRS weight

Write R=v(AZ+B)/(CZ+D) with A,B,C,D in F_p. The original denominator cZ+d is a nonzero scalar multiple of CZ+D. For z in F_p, phi(z)^p=phi(z). Therefore multiplying f(R(z)) by (cz+d)^2 gives a constant multiple of (Az+B)^2 on the occupied block. Multiplying g(R(z)) by the same weight gives either zero or a constant multiple of (Cz+D)^2. Both are degree-at-most-two polynomials. Thus the transformed received line lies in the quadratic code; this compiler cannot retain the intended source/common-agreement separation. Restricting to a punctured subset does not change these identities.

## Larger ambient-field maps

The conclusion also covers Möbius maps over F_{p^6} whose accepted images lie in E. If at least three distinct finite F_p parameters have finite images in E, the unique Möbius transformation matching these three ordered source/image points is defined over E: PGL_2(E) acts sharply transitively on ordered triples of distinct points of P^1(E). The given transformation is therefore represented over E up to a common nonzero scalar. Apply the preceding proof to this representation. Changing the representing matrix only rescales the standard quadratic GRS multiplier by a nonzero constant in F_{p^6}, so the degree-two conclusion is unchanged. In particular any proposed set exceeding twelve accepted nodes satisfies the three-point hypothesis automatically.

## Scope

The parameter nodes here are finite elements of F_p, poles are excluded, and accepted images are finite and nonzero. No assertion is made about nonlinear rational maps, arbitrary coordinate permutations, arbitrary independent coordinate multipliers, or a universal prime-alphabet impossibility. This proof concerns precisely Möbius evaluation changes with their standard degree-two GRS weight.
