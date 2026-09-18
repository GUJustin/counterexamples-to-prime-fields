# Correlated heads: collision audit and nonconstant-b shared-core reduction

September 18, 2026. This is an exact reduction, not a claimed large population or a universal odd-characteristic bound.

## Collision identity independently checked

Use `CORRELATED_HEAD_FOURSPACE_TARGET.md` notation. Put J=L^p+(w-a^p)L, t=b^p-a^(p+1)+wa, q=u+w^(p+1). The two B-components R0,Rtheta of the complete outer residual satisfy

    R0+w^p Rtheta-Rtheta^p=(q-t^p)L.

Hence z=(q-t^p)a+(theta-w^p)t is injective on the admissible locators except when t^p=q. That unique t-fiber maps to a single label. A positive nondegenerate component would therefore yield genuinely distinct challenges, rather than merely many coincident locator presentations.

Independent head parameters instead force missing coefficients b=c=v=0; they cannot solve this target. The known constant-b pencil uses a three-plane trinomial locator X^(p³)+B X^p+C X on F_(p7), which is characteristic-two-only by Santonastaso–Zullo Theorem 1.3(c), or upper's elementary composition calculation. It does not supply an odd-characteristic component.

## Extensions of an arbitrary common three-plane

Let a three-plane U have locator

    J_U=X^(p³)+A X^(p²)+B X^p+C X,  C≠0,

and assume A≠0. Every four-plane containing U has locator

    L_gamma=J_U^p-gamma J_U,

where gamma=y^(p-1) for a nonzero y in Im(J_U). Thus

    a=A^p-gamma,
    b=B^p-gamma A,
    c=C^p-gamma B,
    v=-gamma C.

Fix correlated heads u,w and define

    k=A^(p²)-w,
    l=(k B^p-C^(p²))/A,
    r=(u-B^(p³)+w A^(p³))/A.

Substitution into the two missing-coefficient equations gives exactly

    gamma^(p+1)-k gamma+l=0,
    gamma^(p²+p+1)=r(B^p-gamma A).

Equivalently, admissible nonzero y belong to the F_p-linear intersection

    Im(J_U) intersect ker K2 intersect ker K3,
    K2(Y)=Y^(p²)-kY^p+lY,
    K3(Y)=Y^(p³)+r A Y^p-r B^pY.

No b=0 solution was lost in rewriting: the second displayed equation would then force nonzero gamma to be zero, which is impossible. Distinct F_p-lines in this intersection correspond to distinct gamma and distinct four-planes.

Because K2 has degree p², this intersection has dimension at most two. Consequently a common-core family has 0,1, or p+1 admissible four-planes. In particular an isolated pair of distinct four-planes cannot be the full fixed-head fiber through this core.

For all these gamma, the theta residual is the SAME polynomial

    Rtheta=K2 composed with J_U.

Hence t is constant throughout the family. If t^p≠q, the labels are distinct (z is affine with nonzero coefficient in gamma). If t^p=q, all labels collapse to one. This explicitly preserves the exceptional chart.

## Necessary condition for a nonconstant-b pencil

If the intersection has dimension two, K2 is its monic squarefree locator and K3 vanishes on that same space. Thus

    K3=K2^p+k^p K2.

Coefficient comparison gives

    l^p-k^(p+1)=rA,
    k^p l=-r B^p.

Eliminating r yields B*l=k*C^p, and therefore

    k(B^(p+1)-A C^p)=B C^(p²).

The remaining geometric condition is ker K2 contained in Im(J_U). These explicit equations are a smaller target for a composition/trace argument. They do not by themselves prove that such a pencil is impossible in odd characteristic, especially on a non-field additive domain.

## Scope

The full-field p=3 census reportedly has at most two admissible locators per head pair. If a double lies in the nonexceptional label chart, the reduction above implies its two four-planes cannot share a three-dimensional core (unless another constraint of the census differs). Checking their intersection dimension is a useful diagnostic, not a proof for other primes.

The source-domain field hypothesis is crucial to the known constant-b no-go: it uses Frobenius^7=identity, or divisibility into X^(p7)-X. A seven-dimensional additive domain in a larger field has a general locator, so that argument cannot simply be reused. The collision identity and shared-core reduction do remain valid there. No new positive nonconstant-b component or general bound of two is asserted.
