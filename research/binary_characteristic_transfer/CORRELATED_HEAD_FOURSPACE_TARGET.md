# A four-space target with a missing witness coefficient

This is a concrete new-family target, not an asserted superlinear construction. Let B=F_(p^7), let theta lie outside B, and write a four-space locator as

    L=X^(p^4)+aX^(p³)+bX^(p²)+cX^p+vX,  v!=0.

Seek an outer additive polynomial L^(p²)+A L^p+B0 L whose X^(p²) coefficient vanishes. After division by X, its witness then has degree at most p-1 rather than p²-1. The intended parameters are N=p^7, K=p, agreement p^4-1, and a raw Gaussian population [7 choose 4]_p~p^12=N^(12/7).

## Independent fixed heads give no solutions

Fix the X^(p^5), X^(p^4) coefficients to theta1,theta2. Necessarily

    A=theta1-a^(p²),
    B0=theta2-b^(p²)-A a^p.

The missing coefficient is

    v^(p²)+A c^p+B0 b.

If 1,theta1,theta2 are B-linearly independent, its theta2 coefficient forces b=0, its theta1 coefficient then forces c=0, and the constant coefficient forces v=0. This is incompatible with a subspace locator. Thus independent exterior parameters cannot simply be reused from the standard compiler.

## The correlated-head chart

Take theta1=theta and theta2=u+w theta, with u,w in B. The missing coefficient vanishes exactly when

    c^p=(a^p-w)b,
    v^(p²)=b^(p²+1)-(u+w a^(p²))b.                 (1)

In particular b!=0. These equations determine c,v uniquely from a,b. Put

    t=b^p-a^(p+1)+wa,   q=u+w^(p+1).

The X^(p³) coefficient, which is the affine challenge label, simplifies to

    z=(q-t^p)a+(theta-w^p)t.                       (2)

For fixed u,w, a label determines t by its theta coordinate. If t^p!=q, it then determines a, hence b,c,v. All collision possibilities are confined to the single exceptional t satisfying t^p=q; that chart collapses to one label. Any search must preserve this exceptional chart, but it cannot itself generate many distinct labels.

There is also a useful composition identity. Set

    J=L^p+(w-a^p)L.

Its X^(p²) coefficient is zero by (1). The complete outer expression is

    L^(p²)+A L^p+B0 L
       =J^p+(theta-w^p)J+(q-t^p)L.                (3)

Away from t^p=q, its roots in B are exactly ker L: the theta component forces J=0, then the B component forces L=0. The witness constant is automatically nonzero: if B0=0, its theta component gives a^p=w; (1) then gives c=0, and the missing-coefficient equation forces v=0, a contradiction. Thus after dividing by X the agreement count is p^4-1. On the exceptional chart roots instead come from J; this needs separate accounting, and is not used to claim a new population.

## An explicit small component: subspace pencils

Suppose U is a three-dimensional subspace whose locator has a missing X^(p²) term:

    J_U=X^(p³)+B1 X^p+C1 X,  B1!=0, C1!=0.

For every four-space W containing U,

    L_W=J_U^p-gamma J_U,

where gamma ranges over the (p^4-1)/(p-1) projective values arising from the image of J_U. Here

    a=-gamma, b=B1^p, c=C1^p+a B1, v=a C1.

All these locators satisfy (1) for the SAME correlated heads

    u=B1^(p³),   w=-C1^(p²)/B1^p.

Thus the constraints do have nonempty structured components whenever such a U exists. This is conditional on that explicitly stated locator property, not a proof of their existence at every p. The bounded full-field p=2 pilot finds precisely such components among its maximal groups.

The subspace count is p³+p²+p+1, only N^(3/7) in scale. Labels are injective away from the exceptional t, and that exceptional t can occur for at most p+1 values of a (from the degree-p+1 equation defining t). Hence, when it exists, the component supplies order p³ distinct labels, not the superlinear population sought.

### On the full field this component is characteristic-two only

There is a short elementary certificate, consistent with the known maximum-kernel trinomial restriction. Suppose J_U=X^(p³)+B1 X^p+C1 X is a three-space locator in F_(p7). Its image has dimension four. Composing with that image's monic locator gives

    Q composed with J_U = X^(p7)-X,

where Q has p-degree four. Write its coefficients as 1,q3,q2,q1,q0 in descending p-degree. Coefficient comparison successively gives

    q3=0, q2=-B1^(p4), q1=-C1^(p4), q0=B1^(p4+p2),
    B1^(p4) C1^(p2)+C1^(p4) B1^p=0,
    B1^(p4+p2+1)=C1^(p4+p),
    B1^(p4+p2) C1=-1.

Here p4 denotes p^4, and similarly for the exponent shorthand in this display. The last two equations imply B1=-C1^(p4+p+1). Substituting this into the preceding equation and using Frobenius^(7)=identity on F_(p7) gives

    -2 C1^(p5+p4+p2+p)=0.

Since C1!=0, necessarily p=2. Thus the maximal pencil seen in the p=2 pilot is unavailable for every odd characteristic on the full field. This does not exclude a similar configuration on a non-field additive domain in a larger ambient field.

Nonconstant-b components remain the substantive open locus. The exhaustive p=3 full-field pilot finds at most two labels per correlated head line, but this observation is not a theorem for other odd primes.

## Uniform DKT admissibility if a stronger component exists

More generally, for r>=3 consider N=p^(2r-1), K=p, actual target p^r-1 and advertised threshold

    A0=p^(r-1)(p-1).

For p>=53 the same fixed multiplicity/derivative support works:

    m=4, S=2, Bjet=4p^(r-1), H=48Bjet.

Its local rank is 23 and exact coefficient count

    G=(p-1)(3Bjet²-3Bjet+2)/2+3Bjet-2
      =24p^(2r-1)-24p^(2r-2)-6p^r+18p^(r-1)+p-3
      >(47/2)N.

The same challenge inequality therefore holds. Substitution in the finite counting formulas gives the same conservative constants 68N for lists and 300000N² for MCA. Thus the four-space target faces no new derivative-cap or low-rate-uniformity obstruction: the unresolved issue is the size of the correlated-head locus and its distinct label population.
