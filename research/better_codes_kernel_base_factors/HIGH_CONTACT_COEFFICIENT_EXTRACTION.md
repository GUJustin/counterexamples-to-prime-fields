# What own-system rigidity forces at the leading R coefficient

This note separates a valid coefficient-extraction lemma from the quantitative gap in applying it to the complete benchmark ledger.

## Exact extraction, including challenge dependence

Write F=sum_{j=0}^r A_j(X,Y,Z)R^j, and let A=A_r. At node x with received line u(Z)=f_x+Zg_x, suppose F has first-jet contact a:

    F(x+t,u(Z)+tR+t^2E,R,Z)=0 mod t^a.

For every integer k<a, the coefficient of t^k R^(k+r) E^0 in this expression is exactly

    (partial_Y^[k] A)(x,u(Z),Z).              (1)

Here the derivative is Hasse, so the identity holds in every characteristic. A summand with original R-degree j<r needs at least k+r-j>k copies of tR to produce that R-power and cannot contribute. For j=r, exactly k copies are required; any X-variation or E-term would raise t-degree. Therefore (1) is zero. Equivalently,

    (Y-u(Z))^a divides A(x,Y,Z)

unless A(x,Y,Z) is identically zero, in which case the assertion remains true. This is a polynomial identity in Z, not an assertion obtained by specializing Z first.

At the binding-shaped caps wt(F)<=55w, deg_R F=12, deg_(Y,R)F<=55, put q=deg_Y A. When q=43, write

    A=B(X,Z)Y^43+C(X,Z)Y^42+...,
    deg_X B<=12, deg_X C<=w+12.

For a>=43, (1) with k=42 gives the linear graph equation

    43 B(x,Z)(f_x+Zg_x)+C(x,Z)=0.

The intended prime is larger than43. Where B(x,Z) is nonzero as a polynomial, this is the rational graph -C/(43B) over k(Z).

For a>=40, the universally valid equation is instead

    G_4(x,f_x+Zg_x,Z)=0,
    G_4=partial_Y^[39] A.

It has Y-degree4, weighted (X,Y) degree at most4w+12, and joint (Y,Z) degree at most3261-12-39=3210. These degree bounds account for the possible dependence of every coefficient on Z.

## A genuine conditional helper consequence

Let H be the set of nodes with a>=43 and B(x,Z) nonzero. If a polynomial P(X) of degree at most w agrees with the received word at A0 nodes and

    |H|+A0-n>w+12,

then 43 B(X,Z)P(X)+C(X,Z) is identically zero in X (over k(Z), or at a specialization where the graph coefficients and degrees behave as stated). This follows by the degree bound w+12 and the size of the intersection of the two agreement sets. At the target A0=181275, this requires |H|>=211953.

This is a conditional reduction to an R-free linear graph. Specializations where B or graph coefficients vanish must be separated before a challenge-label counting claim; none is asserted here.

## Why the existing two inequalities do not force that hypothesis

Own-system rigidity gives

    sum_x R(a_x,3261,12)>=6802316684344.

The leading-coefficient contact estimate gives, in the q43 case,

    a_x<=43+2 ord_x B,   sum_x ord_x B<=12.

The constant numerical profile a_x=40 at all262144 nodes satisfies both inequalities: n R(40)=6965785788416, which already exceeds the required rank sum. It also obeys the scalar primary contact-resource allowance, since the factor charge would be15w. This is an admissible profile for these inequalities, not an exhibited universal factor.

Thus these proved inequalities cannot by themselves force even one node with a>=41. In particular they cannot force the >211952 linear-graph nodes required by the conditional helper argument. The lower-order quartic equation is genuinely available on a forced high-contact subset, but its degree is4w+12; a degree-w candidate's181275 agreements do not by themselves force that quartic to vanish identically along the candidate.

A new bridge would have to rule out the intermediate contact regime40--42 using more of the full kernel or exploit the quartic equation with an additional rank/routing theorem. Merely replacing a nonuniform profile by its average would be invalid and does not supply this bridge.

## Exact size of the currently forced subset

In the q43 case let h=#{x:a_x>=40}. Separate the baseline rank contribution at contacts39 and43, and bound the exceptional contribution using the integer orders of B. The exact finite recurrence

    E(0)=0,
    E(d)=max_{1<=v<=d}[E(d-v)+R(43+2v)-R(43)]

for0<=d<=12 gives E(12)=49897120 (attained by one node of order12). Therefore

    sum_x R(a_x)<=n R(39)+h[R(43)-R(39)]+49897120.

Combining with own-system rigidity yields h>=35426. The target candidate may disagree at80869 coordinates, so this guaranteed subset can be disjoint from its agreement set. No unsupported convexity assumption enters the recurrence; it enumerates the13 integer resource totals, not source shapes.

The stronger numerical profile a_x=40 everywhere would give factor charge15w=1966065. Three such factors consume5898195, still below the primary strict resource budget5924072. Thus even the possibility of three binding-shaped factors is not removed by combining this profile test with the scalar additive resource.

The exact arithmetic and resource report are `high_contact_subset_gate.py/json/resources.json` (0.56seconds, peak RSS below7MiB).
