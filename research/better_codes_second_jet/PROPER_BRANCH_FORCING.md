# Proper-branch forcing in the restored helper framework

## All-low curvature coefficients reduce to first-order helpers

Let Q be a nonzero restored second-jet interpolant with curvature cap s, contact m>s, and n0=s+1. Assume the characteristic exceeds s, so h! is nonzero for h<=s. Let h be the actual curvature degree and C_h its nonzero leading coefficient. Since h<n0, its support reserves h units of the derivative cost delta=A−(w−2).

The existing differentiation lemma gives contact order at least m−h to partial_V^h Q=h! C_h. Specializing the curvature contact variables V=−E1,E3=0 recovers the first-jet contact identity for C_h. Its coefficient weight is strictly bounded by

    mA−h delta−h(w−2)=(m−h)A.

The coefficient flags are

    slope <= B−2h,
    jet total <= U−h,
    jet plus challenge total <= L−h.

Thus C_h is an ordinary first-jet interpolation polynomial at multiplicity m−h, with the same agreement threshold. For an irreducible target factor F with total degree t>L, C_h cannot be divisible by F. It is therefore a proper first-order helper directly, using its actual reduced caps. No retained/prolongation branch is needed.

This is a constructive existence reduction. It does not by itself say that a particular first-order coefficient-count-minus-rank sufficient test must discover C_h: sufficient dimension inequalities are not converses. It does say that all-low forcing introduces no new class of helper equations. Its potential benefit would have to be a stronger proof of existence of an ordinary first-order helper under these caps.

## What combining high-curvature sources can and cannot force

Fix F and the source cap s. Each original cleared helper operator

    Q -> helper Q F (s−d) d mod F,  0<=d<=k,

is linear in Q. Let U be an available linear subspace of interpolants. A proper helper exists by these derivative operators exactly when at least one of these restricted linear maps is nonzero. If U is contained in their common kernel, every scalar linear combination stays in that common kernel. This is the derivative-congruence part of the restored retained alternative, but it does not alone preclude the separate low-curvature branch.

Lowering curvature degree by cancelling leading coefficients IS a legitimate additional escape mechanism: a nonzero combination of degree h<n0 yields a proper leading-coefficient helper by the low-coefficient lemma and L<t, even if every requested derivative helper remains zero. Thus the complete sufficient escape criterion is

    some requested helper map is nonzero on U,
    OR U intersects {curvature degree<n0} nontrivially.

Only when both fail does every nonzero element of U have curvature degree at least n0. In that case the leading-coefficient map on the minimal nonzero degree stratum is injective. Let High be the linear map extracting all curvature coefficients numbered n0 through s. Then low-degree escape is exactly ker(High|U)!=0. A dimension argument dim(U)>dim(image High|U) would suffice. The available ambient coefficient-space dimensions are far too large to establish that inequality from the present source nullity alone; a useful theorem needs a sharper image bound incorporating contact or the derivative-helper congruences. These observations neither prove such an escape for the full kernel nor rule it out.

## Explicit obstruction to source-wise or bank-wise automatic forcing

The following example satisfies the relevant source/support/contact properties and has nonzero leading coefficient modulo F, but all requested helper operators vanish modulo F. It is not a claim that the ENTIRE interpolation kernel for this received line lacks other proper sources.

Use the pinned field, w131071,A181275, any262144 distinct nodes, and the full-support received line w_x(Z)=Z. Take

    m20, s3, B6, U23, L23, k1, n03,
    Q=(Y−Z)^20 V^3,
    F=R−Z^24.

The source flags hold, and its maximum weighted degree plus reserved cost is

    23w−6 + [A−(w−2)] = 3064833 < 20A=3625500.

The curvature degree3 is in the high-coefficient branch, so reserve=k1. At every received coordinate Y−Z becomes tR−t²V+t³E, giving contact at least20. Both Q and partial_V Q vanish on every degree<=w polynomial agreeing with the constant word Z at at least A>w coordinates, since such a polynomial is identically Z and has curvature zero.

The irreducible factor F has total degree24>L and slope derivative1. Its differential prolongation is delta F=2V. The source and its first curvature derivative retain respectively powers V^3 and V^2, so substitution along delta F=0 makes both cleared helpers zero modulo F. Its leading coefficient (Y−Z)^20 is nevertheless nonzero and not divisible by F. The two-dimensional available bank span(Q,XQ) cannot lower curvature degree or produce a proper helper by scalar combinations: its leading-coefficient map is injective. Multiplying by X preserves the total/jet flags and the contact order, and the displayed strict weighted inequality has more than one unit of slack. Thus even two scalar-linearly-independent sources do not force the desired cancellation.

This counterexample uses a full-support line but makes no assertion of a large bad-label set; indeed it is intended only to refute automatic algebraic forcing. The complete interpolation kernel here contains other sources. Any universal full-kernel escape theorem must exploit additional information about that full kernel, rather than just nonzero leading coefficients, scalar dimension greater than one, or a collection of high-curvature interpolants.
