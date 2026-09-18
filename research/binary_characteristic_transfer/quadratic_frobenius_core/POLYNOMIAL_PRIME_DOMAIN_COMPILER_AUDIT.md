# Polynomial evaluation compiler: a conic improves the minority-block bound

Let p be odd, E=F_(p³), and let W,V=eta W be distinct two-dimensional F_p-subspaces of E. Consider the existing two-block words, with priority to D0={x≠0:x²∈W} and D1={x≠0:x²∈V}\D0. Let P(Z)∈E[Z] have degree D, and let H⊂F_p consist of h distinct parameters. No injectivity assumption on P|H is needed below. The inherited compiler requires each P(z) to be an allowed evaluation coordinate.

**Result.** If h>4D and P(z)≠0 on H, then either all compiled line words are degree-at-most-2D polynomials on H, or every compiled line word differs from such a polynomial at at most floor(D/2) coordinates. In particular the proposed D≤65535, h=262144 compiler cannot preserve far sources for code dimension 131072 and agreement threshold 181275.

## 1. At least one trace-quadric identity is forced

Choose nonzero kappa_i with Wi=ker Tr_(E/Fp)(kappa_i x), where W0=W,W1=V. Square membership is the zero condition for

    q_i(P(Z))=Tr_(E/Fp)(kappa_i P(Z)²) ∈ F_p[Z].

Here trace applies to coefficients; on Z∈F_p this equals the trace of the evaluated value. Each polynomial has degree at most 2D. If neither vanishes identically, the union of the two blocks can contain at most 4D parameters. Thus h>4D forces at least one identity.

If q_0(P)≡0, every nonzero evaluation is assigned to D0. On F_p parameters, write P^[p] for coefficientwise Frobenius. Then f(P(z))=P^[p](z)² and g(P(z))=0. Every compiled line word is a degree-at-most-2D polynomial.

It remains to consider q_1(P)≡0 and q_0(P) not identically zero.

## 2. The two planes select just one rational point on the conic

The quadratic form q_1(x)=Tr(kappa_1 x²) on the three-dimensional F_p-space E is nondegenerate: its polar form is 2Tr(kappa_1 xy), and the trace pairing is nondegenerate. Thus q_1=0 is a nonsingular projective conic.

Let J=W∩V, a one-dimensional F_p-space. There is r∈E* with r²∈J: on each nonzero F_p-line exactly half the elements are squares, because the quadratic character of the odd-degree extension restricts to the character of F_p. If x²∈J and x≠0, then (x/r)²∈F_p*. But x/r lies in the cubic extension E and has degree at most two over F_p, hence actually belongs to F_p. Conversely every x∈rF_p has square in J.

Therefore simultaneous membership in W and V selects exactly ONE F_p-rational projective point [r] on the conic, not a general four-point intersection. The remaining geometric intersection points need not be rational; counting them as independent prime-field branches loses the key information.

## 3. Polynomial parametrization gives at most D/2 minority coordinates

A nonsingular conic with a rational point is carried by an F_p-linear coordinate change to AC=B². Express the three coefficient polynomials of P in such coordinates and remove their greatest common divisor. The remaining primitive triple has the form

    (U²,UV,V²)

up to a common nonzero constant, with coprime U,V∈F_p[Z]. This follows directly from unique factorization: in a primitive triple AC=B², A and C are relatively prime, so both are squares up to constants, and those constants can be absorbed in the common scalar and one parameter. The cases A=0 or C=0 give a constant projective map and satisfy the same conclusion.

Hence, for a fixed invertible linear map M over F_p,

    P(Z)=h0(Z) M(U(Z)²,U(Z)V(Z),V(Z)²),
    D=deg(h0)+2 max(deg U,deg V).

The equality of degrees follows because an invertible constant linear map preserves the maximum degree of a polynomial vector. The unique rational point [r] corresponds to a unique [u0:v0]∈P¹(F_p). Away from zeros of h0, the minority block D0 occurs precisely when

    v0 U(Z)−u0 V(Z)=0.

This polynomial has degree at most max(deg U,deg V)≤floor(D/2). It is not identically zero: otherwise P has constant projective value [r], forcing q_0(P)≡0 contrary to the remaining case. Consequently at most floor(D/2) retained parameters lie in D0.

On every other parameter the line word is

    eta^(1−p) P^[p](Z)² + lambda,

of degree at most 2D. The values on the minority coordinates may differ, but their number is at most floor(D/2). This proves the result. Any linear combination of the two sources has the same bound.

## 4. Zero parameters and alphabet scope

The inherited domain excludes P(z)=0. If one instead extends the compiler by assigning arbitrary values at its zero parameters, these occur only at roots of h0, since U,V are coprime. Counting those as additional exceptions gives at most

    deg(h0)+max(deg U,deg V) <=D

exceptions in the remaining conic case. Thus even arbitrary zero-value patching still leaves agreement at least h−D. Arbitrary patching of other missing/deleted coordinates is a different construction and is not covered by the inherited restriction claim.

The approximating polynomial has coefficients in E. If the compiled received word is actually F_p-valued and has more than 2D good coordinates, coefficientwise projection or interpolation forces its approximating polynomial to lie in F_p[Z]. A common F_p-linear trace/projection of alphabet values also preserves its degree and agreement. Nonlinear alphabet maps are not addressed.

## 5. Numerical benchmark ledger

With h=262144 and D≤65535, we have 4D≤262140<h and 2D≤131070<131072. Therefore every compiled word has at least

    h−floor(D/2) >=229377

matches with the code, well above threshold 181275. Even arbitrary patching of P=0 parameters leaves at least

    h−D >=196609 >181275

matches. Thus this polynomial evaluation substitution, including nonconstant degree-two parametrizations of the isotropic conic, cannot retain the required far endpoints on the fixed prime-field domain. The conclusion does not use injectivity of P, nor does dropping injectivity evade it.

This is a bound for this specific two-block inherited compiler under polynomial evaluation changes. It is not a general obstruction to half-rate prime-field lines, independently chosen piecewise words, or higher-degree substitutions whose composed witnesses no longer meet the stated code-degree budget. No computation or manuscript edit was needed.
