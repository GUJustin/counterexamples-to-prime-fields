# Independent algebra check of the retained/simple-tail model

Status: independent audit PASS of RETAINED_SIMPLE_COMPONENT_MODEL.md, including
the exact cached global-tail definitions and the source/contact/reserve conditions.
This is an A=n local-stage example, NOT the pinned A/n approximately .6915 case,
and NOT an intrinsic ordinary-CA counterexample.

Let Lambda be squarefree of degree n, with all its roots used as evaluation
coordinates. Take 2<=w<n, d>=3, h>=1, and M>h(d+2), M>=d+4. Work in
characteristic zero or sufficiently large positive characteristic (in particular
p>n,h,M,d+2, and all desired geometric characteristic budgets).
Put W=Y-Z and over k(X) set

    u=W/Lambda,
    v=(Lambda R-Lambda'W)/Lambda^2,
    F=Lambda^(2d)(v^d+v+u^(d+2)+Z^M),
    delta=partial_X+R partial_Y+2V partial_R,
    Q=Lambda delta F-2d Lambda' F,   Source=Q^h.

## Polynomiality, irreducibility, flags

The four summands of F are

    (Lambda R-Lambda'W)^d,
    Lambda^(2d-2)(Lambda R-Lambda'W),
    Lambda^(d-2)W^(d+2),
    Lambda^(2d)Z^M.

Thus F is polynomial. Over k(X), the change (Y,R,Z) to (u,v,Z) is an invertible
linear change. The polynomial v^d+v+u^(d+2) has a simple irreducible factor:
at the origin its v derivative is 1. Eisenstein at this factor proves
Z^M+v^d+v+u^(d+2) irreducible. Clearing denominators introduces no common
X factor: the Z^M coefficient is Lambda^(2d), whereas the W^d coefficient
includes (-Lambda')^d, coprime to Lambda. Thus F is primitive and irreducible.
Its slope, combined Y/R, and total Y/R/Z caps are d,d+2,M respectively.

The Z^M summand cancels from Q. Direct differentiation gives source caps

    deg_V Q<=1,
    max(2*Vexp+Rexp)<=d+1,
    max(Vexp+Yexp+Rexp)<=d+2,
    max(Vexp+Yexp+Rexp+Zexp)<=d+2.

Raising to h gives the proposed flags s=h,B=(d+1)h,U=L=(d+2)h.

With weights (X,Y,R,V,Z)=(1,w,w-1,w-2,0), the three surviving pieces of Q
have upper weights

    d(n+w-1)+n-1,
    2dn+w-2,
    (d-1)n+(d+2)w-1.

Since n>w, their maximum is at most 2dn+w-2. With m=(2d+1)h,
k=h-1,n0=h, the restored reserve is at most h-1 for every curvature exponent.
Therefore

    wt(Source)+reserve*(n-w+2)
       <=h(2dn+w-2)+(h-1)(n-w+2)
       =mn-(n-w+2)<mn.

This checks the strict weighted source cutoff with A=n and reserve gap n-w+2.

## Actual source contact

At a node x use t=X-x and the restored endpoint substitution

    Y=Z+tR-t^2 V+t^3 E.

Since Lambda has a simple zero at x, u and v are regular in the local ring
k[[t]][R,V,E,Z]. The identity delta u=v holds. Moreover

    delta v=[2V Lambda^2-2 Lambda Lambda' R
                +(2(Lambda')^2-Lambda Lambda'')W]/Lambda^3.

Substitution cancels all terms below order t^3 in this numerator. For example,
writing Lambda=a t+b t^2+O(t^3), the numerator's t and t^2 coefficients vanish
identically. Hence delta v is regular as well. It follows that

    Q=Lambda^(2d+1) delta(v^d+v+u^(d+2)+Z^M)

has contact at least 2d+1, and Q^h has contact at least m.

## Regular selected seed and retained power

Take Gamma={0}, selected P=0, and received word w_z(x)=z. Then F(P,0)=0,
all n coordinates agree, and F_R at this seed is Lambda^(2d-1), nonzero in
k(X). Also Q_V=2 Lambda F_R, so the leading V coefficient of Q^h is nonzero
there. Modulo F, Q=Lambda delta F; thus Source modulo F is a scalar multiple
of the hth power of the cleared prolongation factor. This gives a root of
multiplicity h in the component curvature polynomial and therefore vanishing
of its derivatives of orders 0 through h-1. This is the retained-helper
mechanism, with factorials invertible under the characteristic assumption.

The EXACT restored predicate NoLargeSelectedPencil holds for Gamma={0}, e=0:
every intersection with the one-element selected set has size at most e+1=1.
The entire received line nevertheless consists of codewords. The example must
not be described as an ordinary-CA construction.

## Simple first-tail geometry

At the seed, the equation in (u,v,Z) has linearization v=0. Along actual jets,
u'=v, so the linearized solution is P=Z+c Lambda. Since w<n and
characteristic exceeds n, Lambda's derivative of order w+1 is nonzero.
The first degree-w tail condition linearizes to

    c Lambda^{(w+1)}=0,

where the superscript denotes a DERIVATIVE, not a power. Equivalently its
coefficient in W is Lambda^{(w+1)}/Lambda, nonzero in k(X). Thus the gradients
of F and the first tail are independent at the selected point: the local
intersection is a smooth reduced curve, and its component multiplicity is 1.
The global-tail denominator clearing is by powers of the regular separant,
which is a unit at this point; it does not change this conclusion.

This establishes the algebraic mechanism preventing a blanket implication
from arbitrary retained curvature multiplicity to first-tail multiplicity >=2.
A claim specialized to the pinned agreement ratio or with additional source
structure is not decided by this example. It also does not prove that the
existing numerical normal budget is sharp: it refutes only this proposed
multiplicity shortcut in unrestricted stage generality.

## Exact primary tail cross-check

Cached LowerFoundation.lean around lines4557--4576 defines numerator by repeated
contact derivation and proves `iterate_Y_eq_numerator`: the iterated derivative
of Y equals numerator times the inverse separant to power 2j. Around lines32234--32261,
`globalTailCut_eq` multiplies this numerator by the nonzero generic scalar
(-X)^j. At the selected point the separant is nonzero. Thus both conversions
are by units and the transversality calculation applies to the ACTUAL
first-tail cut in the restored stage, not merely a proposed replacement.
Ordinary/Hasse derivative normalization is a nonzero scalar when p>n.

The originating note's concrete d=3,h=5,M=29 example also checks. The primary
source framework has the harmless standing w>=2 requirement for nonnegative
second-jet weight; choose w>=2 in this audit. The pinned n,w,p satisfy that
and the required large-characteristic bounds, but agreement is A=n.
