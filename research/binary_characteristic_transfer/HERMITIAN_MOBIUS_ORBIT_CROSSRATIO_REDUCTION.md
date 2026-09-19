# Exact cross-ratio test for all native Möbius subgroup competitors

2026-09-19. Analytic necessary-and-sufficient reduction, with no coverage assertion or scan.

Let B=Fp², E=Fp4, q=p², and bar denote the qth-power involution. Assume 2≤e<p and m=p+e divides q−1. Fix beta∈E\B and Λ(beta)=beta^q−beta. Start from R0(X)=X^(−e). For M∈PGL2(B), the appropriate Frobenius-twisted conjugate is

    R_M=M^sigma ∘ R0 ∘ M^(−1), sigma(a)=a^p.

Restrict to maps whose input pole a=M^(−1)(infinity) is outside mu_m. The pole a=infinity is allowed: it is simply an affine map. This guard is essential, since otherwise one split support point maps to infinity and the intended degree-p+e finite locator is lost.

## Connection to the compiler and the label

Write M(X)=(aX+b)/(cX+d), using these coefficients only in this paragraph. Put U=dY−b, V=a−cY. The transformed locator is a scalar normalization of U^m−V^m. Its Y^p block has coefficient

    F_raw=d^p U^e+c^p V^e,
    A_raw=−b^p U^e−a^p V^e.

The coefficient-row determinant is nonzero and U,V are coprime, so F_raw,A_raw are coprime. The pole guard makes the locator monic of degree p+e after scaling, and F monic of degree e. Its roots are the finite native set M(mu_m), and −A/F equals R_M. Thus P=ΛF/G gives a degree<k competing witness with exactly D−e native matches, with label

    z=P(beta)=Λ(beta)/(beta^p−R_M(beta)).             (1)

If R_M(beta)=infinity, interpret (1) as z=0. The denominator cannot vanish for an allowed M, because that would make beta a root of the native-split G. Thus no infinite compiler label occurs.

For a prescribed nonzero finite z, put

    v=beta^p−Λ(beta)/z,  w=v^(p³).

Set t=M^(−1)(beta), necessarily in E\B, and u=t^(−e p³). Applying p³-Frobenius to R_M(beta)=v gives exactly

    M(t)=beta, M(u)=w.                              (2)

For z=0, the same equivalence holds with w=infinity. Conversely any M,t satisfying (2) and the pole guard gives the required compiler label and witness. No assumption of even e is needed for this reduction.

## Exact two-point orbit invariant

For exterior t define the projective coordinate

    phi_t(x)=(x−t)/(x−bar(t)), phi_t(infinity)=1.

Every B-Möbius map with M(t)=beta has a unique representation

    phi_beta(M(x))=c*phi_t(x),  c in E*, c*bar(c)=1.  (3)

Indeed a B-map also sends bar(t) to bar(beta), so this conjugated map fixes zero and infinity and is scalar multiplication. Commuting with bar forces norm(c)=1. Conversely that norm condition makes (3) descend to B.

Suppose first u is different from t and bar(t). Then (2) is possible only if w differs from beta and bar(beta). In that case define

    c=phi_beta(w)/phi_t(u).

There exists a B-map satisfying (2) if and only if

    norm_E/B(phi_t(u))=norm_E/B(phi_beta(w)).         (4)

When it exists the map is UNIQUE. For finite generic u, the left side is the cross-ratio expression

    ((u−t)(bar(u)−bar(t))) / ((u−bar(t))(bar(u)−t)).

Projective evaluation handles u or w at infinity. In our input u is finite and nonzero, but w=infinity is useful for the zero label. Equation (4) includes native-point cases correctly: norm(phi_t(u))=1 if and only if u∈P1(B), and similarly on the target side. Thus it does not silently identify native and exterior second points.

The map's input pole is explicit:

    a=(c*t−bar(t))/(c−1) if c≠1, and a=infinity if c=1. (5)

The norm condition guarantees a∈P1(B). Accept the candidate only if a∉mu_m. The invariant equality alone does not enforce this necessary finite-root guard.

## Degeneracies

If u=t, condition (2) requires w=beta; if u=bar(t), it requires w=bar(beta). In either matched case every norm-one c in (3) is possible. The poles in (5) run bijectively over P1(B), so exactly q+1−m maps survive the pole guard. A mismatched case is impossible. Generic u cannot map to either beta or bar(beta), and there are no further degeneracies.

For a finite nonzero compiler label, w=beta never occurs. The case w=bar(beta) occurs exactly at c*, where c*^p=Λ(beta)^(p−1). Hence the c* orbit test collapses to

    t^(p³+e)=1 with t exterior.

The pole guard can always be met once such t exists, since q+1>m. At p=e²−e−1 with even e, gcd(p³+e,p⁴−1)=p+e; all roots of this equation are native, excluding saturation in this particular Möbius orbit. In contrast the fifth-root Dirichlet construction provides exterior t and hence does reach c* on its different prime progression.

## What remains to decide coverage

For each generic target z the exact question is whether there exists t∈E\B such that (4) holds for u=t^(−e p³), and the uniquely reconstructed pole (5) avoids mu_m. This is an explicit cross-ratio value problem, not a free choice of a Möbius map after matching both points. The invariant lies in B, but that alone does not prove surjectivity or justify treating its values as random. Both failure of the invariant equation and failure of the pole guard can obstruct a label.

The reduction characterizes all members of this orbit and includes its zero and c* cases. It neither asserts that generic endpoints escape nor that the orbit covers all nonbank labels. Rational competitors outside this Möbius orbit also remain possible. No large enumeration is proposed or performed.
