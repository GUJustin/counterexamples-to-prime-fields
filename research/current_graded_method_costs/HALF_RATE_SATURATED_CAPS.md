# Half-rate graded costs for saturated standard caps

September17,2026. Restricted method theorem, not a better.codes gain.

## Scope and result

Let n be even, D=n/2-1>=2, D+1<A<=n, and use the complete jet cap
S={(u,v):v<=b,u+v<=Q}, with all X coefficients of degree
x+Du+(D-1)v<mA. Require

    0<=b<=min(Q,m/2), Q>=m+b-1, Q<=2m-2,
    L_Q=mA-(D-1)Q>=max(m,Q+1).

The first Q condition means every derivative column reaches height m.
The L_Q condition ensures full, locally saturated coefficient prefixes.
Assume characteristic zero or greater than max(D,Q), covering both local
rank and current reconstruction. Define

    a0=(1+sqrt(6))/5,
    a*=(An-4)/(n(n-4)), epsilon=a*-a0,

and assume 0<epsilon<=1/500. If the source has positive dimension surplus
G>nR and passes current Eq63 at height H, then

    m>1/(16epsilon), b>m/8,
    H+1>m/(4055040epsilon).

Thus current squarefree list and regular-MCA numerical ledgers have
necessary orders Omega(D/epsilon²) and Omega(D²/epsilon⁴) in this
restricted class. This does NOT prove the half-rate statement for all
standard caps: the nonsaturated case Q<m+b-1 is not handled.

## Exact finite multiplicity cost

For a derivative column v with height h=Q-v+1>=m, the exact saturated
rank marginal sums to

    R_v=m²/2+m/2-mv+v²,

in either parity of m. This follows from
floor((m+1)²/4)+floor((m-2v)_+²/4) when v<=m/2.
The restriction b<=m/2 is used here; for larger derivative columns the
positive-part term truncates. The reported benchmark support b47,m152
satisfies the restriction.

At normalized leading agreement a, the benefit of column v is
(Q-v+1)(ma-(Q+v)/4). Its maximum over real Q occurs at Q=2ma-1/2.
Summing this maximum minus R_v, and then optimizing b continuously,
yields the upper bound

    (b+1)[m² F(a)-(3/4)m(1-a)+1/8],
    F(a)=(5a²-2a-1)/4.                              (1)

Before optimizing b, the bracket is

    m²(a²-1/2)+m(1-a)(b-1)/2-b(b+1)/4+1/16.         (2)

Since L_Q>=m, the exact-to-leading comparison bounds G/n by the leading
benefit at a*. The half-rate correction follows by using
q<=m(A-1)/(D-1), v<=q in

    (mA-Dq+v)/n =m(A/n)-q/2+(q+v)/n.

At a0, F(a0)=0. On [a0,a0+1/500], a<.695 and
F(a)<=5epsilon/4. Positive surplus and (1) imply
mF(a)>(3/4)(1-a)-1/(8m)>.103, so m>1/(16epsilon).
In particular m>31. On b<=m/8 expression(2) increases with b; evaluating
at b=m/8 and a=.695 gives a strictly negative value. Thus b>m/8.

## Bounding positive prefix surpluses with a finite Riemann error

Every total-degree prefix is still a standard cap, though generally not
saturated in its individual columns. Its compressed exact rank is the
sum over its jet cells of

    g(u,v)=max(0,m-u-v,ceil((m-u)/2)).

For real x,y>=0 put g_c(x,y)=max(0,m-x-y,(m-x)/2). On each unit square
[u,u+1]x[v,v+1], g_c<=g(u,v). Integrating the benefit on that square
lowers it from its value at (u,v) by1/2. Therefore the discrete leading
surplus is at most the integral of

    w(x,y)=ma-(x+y)/2-g_c(x,y)

over the union of the squares, plus half their number.

For a prefix endpoint q<=Q and b'=min(b,q), compare this union with the
continuous cap T={0<=y<=b'+1,0<=x,x+y<=q+1}. The union contains T and
has only an extra upper strip of area (b'+1)/2<=m. Since q+2<=2m,
|w|<=3m there. There are at most2m² cells. Thus the total discrepancy
is at most4m².

Every continuous standard cap has nonpositive surplus at a0. This follows
also by continuity from the audited high-rate shape theorem: a positive
half-rate cap would remain positive after first slightly decreasing its
agreement and then taking rho>1/2 sufficiently close to1/2, below that
theorem's continuously limiting threshold. Increasing a to a0+epsilon adds at most
2epsilon m³, since area(T)<=2m². Consequently every normalized exact
prefix surplus obeys

    P_j<=2epsilon m³+4m²<66epsilon m³.              (3)

The last step uses m>1/(16epsilon). No sign claim for each discrete
critical prefix is needed.

## Negative area and the graded height

For q<=floor(m/8), all q+1 jets occur. Their rank is at least
(m-2q)(q+1)>=3m(q+1)/4, whereas their normalized source contribution is
at most ma*(q+1)<.695m(q+1). Hence the degree surplus is at most
-m(q+1)/20. If J=floor(m/8),

    P_j<=-m(j+1)(j+2)/40, 0<=j<=J,
    -sum_(j=0)^J P_j>m⁴/61440.

Eq63 is precisely sum_(j=0)^H P_j>0. It forces H>J, and (3) therefore
gives 66epsilon m³(H+1)>m⁴/61440, proving the height bound. The current
Eq54/55 reconstruction inequalities then give the stated powers, exactly
as in the quarter-rate standard-support proof.

## Benchmark interpretation

For n262144,A181284, the corrected epsilon is about0.001656182765.
The exact inequality(1) already forces m>=114 for this saturated subclass;
the best support in our bounded numerical scan has m152,b47,Q210 and
satisfies these saturation hypotheses. This helps explain the large
finite interpolation degrees near the pinned incumbent.

The explicit height constant proved above is far too weak to exclude a
competitive finite certificate at those parameters. It establishes an
asymptotic method cost, NOT an all-support obstruction or a better.codes
improvement. Extending the finite multiplicity argument to nonsaturated
caps remains the missing step for a full half-rate standard-support theorem.
