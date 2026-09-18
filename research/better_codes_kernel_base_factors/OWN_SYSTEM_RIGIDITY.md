# A universal factor has a one-dimensional own interpolation system

This is a statement about a divisor of the **entire** primary kernel. It is not true for a factor of an arbitrarily selected interpolant. It supplies a new necessary condition, but no improvement of the complete better.codes ledger is claimed.

## Exact replacement lemma

Let K be a field, let the first-jet contact order at node x be the t-adic order after the injective substitution

    X=x+t, Y=f_x+Z g_x+t R+t^2 E.

These orders are additive on nonzero products. Consider the full vector space V of polynomials with specified upper bounds on contact weight, joint (Y,R,Z) degree, (Y,R) degree, and R degree, and contact at least m at every node. All four degree functions are additive on nonzero products. Assume V is nonzero.

Let an irreducible F divide every member of V. Write its exact degrees as (v,t,y,r) and its actual local contacts as a_x. Define its own interpolation system

    W_F={G: wt(G)<=v, deg_(Y,R,Z)G<=t,
             deg_(Y,R)G<=y, deg_R G<=r,
             contact_x(G)>=a_x for every x}.

Then W_F=K F, and in particular dim W_F=1.

Proof. Choose any nonzero Q in V and factor Q=F^e H with e>=1 and F not dividing H. For G in W_F, the polynomial G^e H satisfies every original degree and contact constraint, by additivity. It therefore belongs to V and is divisible by F. Primality gives F|G. Write G=F J. The weight bound forces J to have weight zero. With weights (1,w,w-1,0) and w>=2, J lies in K[Z]. The exact joint-degree bound then forces J to be constant. Conversely F itself belongs to W_F. This proof does not require a minimal choice of e, a generic member, an infinite field, or a characteristic assumption.

If the original source has additional multiplicatively additive caps, include their exact F degrees in W_F. All arguments survive scalar extension; use the full scalar-extended kernel when discussing factors over an extension field.

## An explicit necessary Hilbert-function inequality

For integers v,t,y,r, the ambient dimension of W_F is

    C_F = sum_{0<=j<=r, 0<=i, i+j<=min(y,t)}
              max(v-w*i-(w-1)*j+1,0)*(t-i-j+1).

Let R(a,t,r) be the standard unrestricted local first-jet rank bound at contact a, joint cap t, and R cap r. Ignoring the extra (Y,R) cap can only enlarge that bound. Then

    dim W_F >= C_F - sum_x R(a_x,t,r).

Consequently every universal irreducible factor must satisfy

    sum_x R(a_x,t,r) >= C_F-1.                (1)

This is an independently checkable necessary condition involving the entire contact profile. It is stronger information than merely knowing F divides one positive-dimensional source. It is not an assertion that the local constraints at different nodes are independent.

For reproducibility, if

    B(A,B,h)=A*B*(t+1-h)-B*A*(A-1)/2-A*B*(B-1)/2,

then the rank bound used here is

    R(a,t,r)=sum_{k=0}^{a-1}
       [B(k+1,r+1,0)-B(max(k+1-h,0),max(r+1-h,0),h)], h=a-k,

in the range t>=a+r. Outside that range the boxes must also be truncated by the joint cap; no untruncated formula is asserted there.

## Binding-shaped exact gate

Take n=262144,w=131071 and exact factor caps

    v=55w=7208905, y=55, r=12, t=3261.

The ambient own-system dimension is 6802316684345. Exact arithmetic in `own_system_gate.py/json` gives:

| Uniform upper bound on every a_x | C_F-n R(a_x,t,r) |
|---:|---:|
|10|6422772804665|
|39|211812576313|
|40|-163469104071|
|43|-1355181495239|

Because the rank bound is nondecreasing in a, **every universal factor with these exact caps must have at least one node of contact at least 40**. In particular the earlier binding-shaped contact-10 illustrative factors cannot be universal, now for an intrinsic full-kernel dimension reason independent of an explicitly exhibited escaping graph power.

The computation was a monotone threshold search for this one fixed shape, not a source parameter scan. It completed in 0.54 seconds with peak RSS below 8 MiB.

## Nonuniform profiles and the remaining gap

Let A_r(X,Y,Z) be the leading R coefficient, q its highest Y degree, and B(X,Z) its highest Y coefficient. The universal local contact estimate gives

    a_x <= q+2 ord_x B,
    sum_x ord_x B <= deg_X B = d,
    d <= v-r(w-1)-q w.

Here orders and degree may be taken over K(Z). This bounds both the baseline contact and the aggregate excess over that baseline. However it does not close (1) at the binding shape: q=43 and d<=12 permit the numerical profile a_x=43 everywhere, for which the own-system lower bound is already negative. This is only a profile allowed by these inequalities, not a construction of a universal factor.

Moreover R(a,t,r) is nonlinear in a. A bound on the sum of contacts cannot be substituted for a uniform contact bound when estimating the sum of ranks. Concentrated contacts require separate treatment, or a genuinely sharper global rank estimate. The own-system rigidity lemma therefore does not yet force a proper helper or lower the normal retained charge. It suggests a concrete next target: classify one-dimensional bounded-degree first-jet systems, or show that the high-contact profiles left by (1) force an additional low-cost source relation.
