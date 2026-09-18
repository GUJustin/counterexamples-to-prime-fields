# A full-contact retained source with an active multiplicity-one first-tail component

This is an explicit counterexample to a **uniform** assertion that
retained second-jet divisibility, source contact, and total-degree
avoidance force first-tail multiplicity at least two. It meets the
interpolation support and retained-stage hypotheses in the full-agreement
regime A=n. It does **not** meet the pinned benchmark ratio
A/n=181275/262144 and does not establish a benchmark lower bound.

In particular, the received line below is itself a line of codewords.
It is not an example of intrinsic ordinary correlated-agreement failure.
The stage's weaker selected-pencils predicate nevertheless holds for
the singleton selected seed set used here.

## 1. The irreducible first-order carrier

Work over an algebraically closed field k of characteristic zero, or a
prime characteristic p sufficiently large for the explicit degrees below.
Choose n distinct evaluation nodes and their monic squarefree locator
Lambda(X) of degree n. Fix integers 2<=w<n, d>=3, h>=1, and
M>h(d+2), with M>=d+4. Take the received line w_x(Z)=Z at every node.
Put

    W=Y-Z,
    T=Lambda R-Lambda' W,
    F=T^d+Lambda^(2d-2) T
        +Lambda^(d-2) W^(d+2)+Lambda^(2d) Z^M.       (1)

This is polynomial since d>=3. Over K=k(X), make the invertible
coordinate change u=W/Lambda, v=T/Lambda^2. Then

    F=Lambda^(2d) [v^d+v+u^(d+2)+Z^M].            (2)

The polynomial f(u,v)=v^d+v+u^(d+2) is squarefree when p does not
divide d+2: its u derivative is (d+2)u^(d+1), and u does not divide f.
Choose any irreducible factor pi of f in K[u,v]. It occurs to order
one. The polynomial Z^M+f is Eisenstein at pi and hence irreducible.
No primality assumption on M is needed. This proves irreducibility
over K. The X-content of (1) is one: its R^d coefficient is Lambda^d,
and its Y^d coefficient with R=Z=0 is (-Lambda')^d. Squarefreeness
of Lambda makes these coprime. Gauss's lemma gives irreducibility in
k[X,Y,R,Z] as well.

The exact cumulative carrier caps are

    r=d, y=d+2, t=M.

Indeed R^d, Y^(d+2), and Z^M all occur with nonzero coefficients.
The weighted degree for weights X=1,Y=w,R=w-1,Z=0 is at most 2dn,
so D=2dn+1 gives the primary strict weighted box. The own-shape condition
holds with cumulative flag (M-d-2,2,d).

At challenge Z=0 select the polynomial P_0=0, and let Gamma={0}.
It has n agreements, solves F=0, and is regular since

    F_R(X,0,0,0)=Lambda^(2d-1) !=0.                (3)

The exact cached NoLargeSelectedPencil predicate bounds the number of
selected seeds in each polynomial pencil by errors+1. With errors=0,
Gamma={0} satisfies it: every such intersection has size at most one.
This does not assert that the received line has no correlated agreement.

## 2. A source with genuine formal contact at every node

The second-jet variable S denotes the second HASSE derivative. Define

    delta=partial_X+R partial_Y+2S partial_R,
    Q=Lambda delta F-2d Lambda' F.                (4)

The high-degree Z^M term cancels. More explicitly, set

    Q0=2Lambda^2 S-2Lambda Lambda' R
          +(2(Lambda')^2-Lambda Lambda'')W.

Then

    Q=[d T^(d-1)+Lambda^(2d-2)]Q0
         +(d+2)Lambda^(d-2)W^(d+1)T.             (5)

This verifies both polynomiality and the complete degree bounds below.

At any domain node x, take an arbitrary formal polynomial arc P with
P(x)=Z. In the local parameter epsilon=X-x, W=P-Z has order at least
one and T=Lambda P'-Lambda'(P-Z) has order at least two. Each term
of F(P) consequently has order at least 2d. The identity

    Q(P)=Lambda^(2d+1) d/dX [F(P)/Lambda^(2d)]

shows that Q(P) has order at least 2d+1. This is stronger than checking
only the selected polynomial P_0.

It also implies the full formal source identity used in the primary
interpolation space. Take cubic arcs
P=Z+a1 epsilon+a2 epsilon^2+a3 epsilon^3. Their jets are

    R=a1+2a2 epsilon+3a3 epsilon^2,
    S=a2+3a3 epsilon,
    E=a3,
    Y=Z+epsilon R-epsilon^2 S+epsilon^3 E.

The change from (a1,a2,a3) to (R,S,E) is an invertible triangular
polynomial change over k[epsilon]. Thus the identity for all formal
cubic arcs gives, as a polynomial identity,

    Q(x+epsilon,Z+epsilon R-epsilon^2 S+epsilon^3 E,R,S,Z)
      =0 mod epsilon^(2d+1).

No density assertion over a finite field or arbitrary-realizable-jet
assumption is being used.

## 3. All interpolation flags, reserves, and avoidance

Use the source I=Q^h and parameters

    m=(2d+1)h, B=(d+1)h, s=h,
    U=L=(d+2)h, k=h-1, n0=h, A=n.                (6)

Equation (5) gives curvature degree <=h, slope/curvature flag
2 deg_S+deg_R<=B, jet degree <=U, and joint jet/challenge degree <=L.
Every monomial of Q has weighted degree at most

    2dn+w-2=m0*n-(n-w+2),  m0=2d+1.

For clarity, the three possible upper weights in (5) are
(d+1)n+dw-d-1, 2dn+w-2, and (d-1)n+(d+2)w-1;
the middle one dominates when n>w. Shifting Y to Y-Z can only
decrease the weighted degree and preserves joint degree.

For every curvature exponent j in I, the primary reserve is j if
j<h and h-1 otherwise, hence at most h-1. Therefore

    wt(monomial)+reserve*(A-(w-2))
      <=h(2dn+w-2)+(h-1)(n-w+2)
       =m*n-(n-w+2)<m*A.

Thus every strict cutoff, including the low-leading-coefficient reserve,
holds. Full formal contact has order m. The usual contact-versus-degree
argument consequently supplies the requested specialized derivatives
through k. Alternatively, with A=n and degree bound w<n, an agreeing
polynomial must equal the constant Z, at which Q and all derivatives
of Q^h through order h-1 vanish directly.

The routing side inequalities 2s<=B, s<=U,L, k<=s, s<m,
B<=U<=L, k+1<=n0, and 2(n0-k-1)<=B all hold. The special closed
rank-count hypothesis m+s<=U need NOT hold and is not claimed: this
source is constructed explicitly and does not need a dimension-count
existence proof. Factorials and the scalar two are nonzero if p>h+1.

Since the carrier's actual total weight is M>L, the primary total
avoidance condition holds strictly; this is not an example where
Q inherits a larger Z cap from F.

## 4. Retained divisibility and active leading coefficient

On F=0 the formal ODE gives the curvature root

    S=-(F_X+R F_Y)/(2F_R).

Equation (4) vanishes at this root modulo F. Hence I=Q^h has a root
of multiplicity h there. All cleared helper derivatives through
k=h-1 vanish modulo F, exactly as in the retained branch; clearing
the powers of 2F_R is legitimate over the carrier function field and
gives polynomial divisibility by its prime equation F.

Its S-leading coefficient is

    (2Lambda F_R)^h.

At the selected solution (Y,R,Z)=(0,0,0), this equals
(2Lambda^(2d))^h, nonzero over k(X). Thus the seed is good and the
component through it is active. The source's S degree is exactly h=n0,
so this is the retained-degree alternative, not the low-degree escape.

## 5. The actual first-tail component is simple

Pass to the surface over k(X), as in the generic-field construction,
and consider the point o=(Y,R,Z)=(0,0,0). Equation (3) allows the ODE
to be solved locally for R. In coordinates u,v from (2), its linear
part at o is v=0. Thus the linearized flow is

    P-Z=Lambda C,  C constant in X.

The first omitted Taylor coefficient at order w+1 has linear term

    [Lambda^[w+1]/Lambda] (Y-Z).

Here Lambda^[w+1] is a HASSE derivative, not a power. It is nonzero
for w<n and p>n. Ordinary versus Hasse normalization differs by a
nonzero factorial under the same characteristic assumption. The
cleared first-tail numerator and globalTailCut differ from this local
expression by units at o, because F_R(o)!=0 and the generic X is
nonzero.

The differentials of F and of the first-tail cut are consequently
independent: the former has a nonzero R coefficient, while the latter
is a nonzero multiple of dY-dZ. Their intersection is a smooth curve
at o. Its unique local component therefore has intersection
multiplicity ONE in the carrier/first-tail intersection. The leading
coefficient above is a unit there, so this is a genuinely active
simple component containing the selected seed.

## 6. Scope and a concrete parameter choice

For example choose d=3,h=5,M=29. Then the carrier caps are
(r,y,t)=(3,5,29), and the explicit source parameters are
(m,B,s,U,L,k,n0)=(35,20,5,25,25,4,5). Take any n>w>=2,
with p>max(2dn+1,M,h+1,d+2), and n distinct nodes.
All claims above then apply. One can use the pinned n=262144,
w=131071 and prime2130706433, with A=n rather than181275;
the small geometric caps also satisfy the old uniform characteristic
box. This is an actual retained-stage model, not just a formal germ.

At the pinned target agreement181275 the constructed source's degree
budget does not pass, so this is NOT a counterexample to a hypothetical
new lemma that additionally exploits that specific agreement ratio.
It does rule out deducing multiplicity>=2 from the retained identities,
active-leading condition, total avoidance, and full interpolation
contact alone. Any benchmark improvement requiring multiplicity four
must use an additional quantitative mechanism not present in those
hypotheses by themselves.
