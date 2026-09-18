# Normalized genus from the Newton resource, and its precise routing scope

## A genuine genus consequence

Let K be the challenge coefficient field and work geometrically over its algebraic closure. Let A(X,Y) have Y-degree q, nonzero Y-discriminant, leading coefficient B(X), and deg_X B<=d. Assume characteristic zero or p>q. Suppose

  deg_X Disc_Y(A)<=U0,
  sum_{x in E} ord_x Disc_Y(A)>=L,

where E consists of n distinct finite coordinates. Let c be the number of geometric irreducible components of the generic degree-q algebra (equivalently, components dominating the X-line), and let g_i be their normalized genera. Vertical content factors are excluded from c. Then

  2 sum_i g_i <= U0+(q-1)(q-2)d-L+(n-1)(q-c).       (1)

This is an actual genus bound. It does not identify the normalization of a retained first-tail component with this curve.

### Monic model and finite discriminant

Set T=B Y and

  M(X,T)=B^(q-1) A(X,T/B).

M is monic in T and has polynomial coefficients in X. Its roots are B times those of A, so

  Disc_T(M)=B^((q-1)(q-2)) Disc_Y(A).

Consequently its discriminant degree is at most U=U0+(q-1)(q-2)d. Its local discriminant order at every x is at least the original forced order; extra zeros of B can only strengthen the lower bound.

The order K[X,T]/(M) is generically reduced and finite free. At a finite coordinate, the discriminant-index identity gives

  ord_x Disc(M) = diff_x + 2 index_x.

After geometric scalar extension all residue degrees are one. Every ramification index is at most q<p, so every branch is tame. Summing over the c components, the finite different at one base coordinate is at most q-c. Thus at E,

  2 index_x >= ord_x Disc(M)-(q-c).

At all other finite points the different is no larger than the polynomial discriminant order. Summing yields

  Diff_finite <= U-L+n(q-c).

The different at infinity is also at most q-c. Componentwise Riemann–Hurwitz is

  2 sum_i g_i-2c = -2q+Diff_total.

Combining proves (1). This argument handles nonmonic A, reducible A, zeros of B at the selected nodes, and infinity. No equality between polynomial-discriminant degree and normalized different is assumed.

### Binding arithmetic

The independently checked Newton/own-system bound gives

  q=43, d<=12, n=262144,
  U0=236715234, L=229763340.

Thus U<=236735898, and with c>=1,

  2 sum_i g_i <= 6972558+262143*42 =17982564,
  sum_i g_i <=8991282.

If c or the actual B-divisor is known, the displayed estimate can improve. These constants use the nonzero-discriminant branch only. The repeated-factor branch requires its own radical/contact analysis.

### Sharper treatment of the nonmonic places

The monic conversion is convenient but its degree inflation is avoidable. Outside zeros of B, division by B is an integral unit change and the original discriminant controls the different. At a zero of B outside E, bound the different directly by q-c; there are at most d such places. At the n selected coordinates use the same tame bound q-c, irrespective of B. Since all orders of the polynomial Disc A are nonnegative, dropping its unused orders at the extra B-zeros only weakens the resulting inequality. Thus

  Diff_finite <= U0-L+(n+d)(q-c),
  2 sum_i g_i <= U0-L+(n-1+d)(q-c).                 (2)

At the binding values, (2) gives

  2 sum_i g_i <=6951894+262155*42=17962404,
  sum_i g_i <=8981202.

This sharpened estimate is the preferred bound. The earlier monic proof remains a separate valid derivation with slightly worse constants.

## Why this does not yet replace the normal ledger

The curve just bounded is A_r(X,Y,Z)=0 over K=k(Z), projected to X. The retained normal component instead lies in the first-tail locus of F(X,Y,R,Z)=0 over k(X), in the remaining variables Y,R,Z. These are different curves over different coefficient fields. No morphism or degree-controlled correspondence between their normalizations has been established by the leading-coefficient argument.

The following explicit example shows that small normalized genus of A_r alone does not force small genus, or even rationality, of a regular simple first-tail component. It deliberately does NOT satisfy the high-contact/universal-kernel hypotheses and therefore does not refute a future theorem using those hypotheses.

Work in characteristic zero or p larger than all displayed degrees, with p not dividing 55*t. Let

  A(Y)=Y^43-1,
  G(Y,Z)=Y^55+Z^t+1,
  F(Y,R,Z)=A(Y) R^12+R+G(Y,Z),

where gcd(55,t)=1; the binding value t=3261 has this property.

The leading physical R coefficient is A. Its discriminant is a nonzero constant in X, and all its normalized components over the challenge field are rational. Its total normalized genus is zero.

F is irreducible: view it as Z^t+H(Y,R). At a point (c,0) with c^55=-1, H=0 and H_R=1. Hence H has an irreducible factor of multiplicity one; Eisenstein at that factor proves irreducibility over k(Y,R), and Gauss gives polynomial irreducibility. Its exact declared flags at t=3261 are R-degree12, (Y,R)-degree55, total (Y,R,Z)-degree3261, and weighted degree55w.

The curve C defined by R=0 and G(Y,Z)=0 lies on F=0 and is regular because F_R=1 there. Every point (c,z) on C supplies the constant polynomial solution P(X)=c. The normalization of C has genus

  (55-1)(t-1)/2=27(t-1),

which is 88020 at t=3261 and grows without bound with t.

It is also a simple first-tail component. On F=0 the differential equation has

  D Y=R,
  D R=-R F_Y/F_R.

At the generic point of C, F_Y=55Y^54 is a unit. Modulo R^2,

  D^j Y = (-55Y^54)^(j-1) R  (j>=1).

This follows inductively because differentiation of the coefficient contributes a factor R. Therefore the first degree-w tail D^(w+1)Y vanishes to order exactly one along C. Clearing the usual separant denominator multiplies by a unit there, preserving this multiplicity.

Thus even a squarefree, genus-zero leading coefficient can coexist with a high-genus, regular, simple first-tail component at the same declared binding flags. A routing theorem must use more than the genus of A_r: in particular, the full-kernel own-system rigidity or the distribution of high contacts must enter in an essential way. The example has no claim of positive own-system rigidity or the required primary-source contact profile.

## Remaining concrete bridge

A useful replacement theorem would have to construct a controlled correspondence from the active first-tail component to the normalized A_r curve, or charge its differential poles to the local index budget after using the full-kernel one-dimensionality. The current hypotheses give a one-dimensional own interpolation space, not such a correspondence. Passing to the radical of A_r does not fix this: it changes contact multiplicities and does not automatically make the radical vanish on nearby polynomial solutions.

The earlier failed fixed-X-to-along-P transfer is not used anywhere above. The normalized-genus estimate is new usable geometry; converting it to the mixed normal ledger remains unproved.
