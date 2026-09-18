# Exact nonuniform gap for total-jet-linear regular carriers

**Proved bounded result.** Let the domain consist of n distinct nodes, received
symbols r_x arbitrary in a coefficient field K, and weights (1,w,w-1) with
w>=2 and n>=2w. Suppose

    F(X,Y,R)=A(X)Y+B(X)R+C(X),   B!=0.

Let V=wt(F), and let a_x be its ACTUAL formal contacts under
F(x+t,r_x+tR+t^2E,R). Then, in every characteristic,

    V-(w/n)sum_x a_x >= w-1.                     (1)

No uniformity or integrality assumption on the average contact is required.
The conclusion applies to arbitrary coefficients in K=k(Z) as well. It is
sharp, since F=R has weight w-1 and zero contact at every node.

## Proof

At a fixed node put beta_x=ord_(X-x) B. The coefficient of R in the
local substitution is B(x+t)+t A(x+t); that of E is t^2 A(x+t).
If beta_x=0, the R coefficient is a unit and a_x=0.
If beta_x>=1, then

    a_x<=beta_x+1.                               (2)

Indeed, a_x>=beta_x+2 would force ord A>=beta_x via the E coefficient.
But then t A has order at least beta_x+1 and cannot cancel the order-beta_x
leading term of B in the R coefficient. This contradicts that contact.
The case A=0 is included by interpreting its order as infinity. The
constant coefficient involving r_x and C can only lower the contact.

Write d=deg B and h=#{x:B(x)=0}. Since sum beta_x<=d and h<=d,

    sum a_x<=d+h<=2d.

Also V>=d+w-1. Consequently

    V-(w/n)sum a_x
       >=w-1+(1-w/n)d-(w/n)h
       >=w-1+(1-2w/n)d >=w-1,

as claimed. The stronger expression involving d and h is retained when
useful. All steps are characteristic-free.

## Sharp nonuniform family and its primary-factor interpretation

Take the zero received word and a squarefree polynomial B whose h roots
are domain nodes, with degree h. Then

    F=B R-B'Y

has actual contact exactly two at those h nodes and zero elsewhere. At a
simple root, the R coefficient B(x+t)-tB'(x+t) has order at least two,
and the E coefficient -t^2B'(x+t) has order exactly two. Its weight is
h+w-1. It is primitive and irreducible over K[X,Y,R], since gcd(B,B')=1
and it is linear over K(X) in the jet variables. Its derivative F_R=B
is nonzero.

At n=2w+2 its exact charge is

    w-1+h/(w+1).

Thus this natural nonuniform construction cannot evade a gap of order w.
Multiplication by a zero-charge graph power Y^a increases every contact
by a and the weight by aw, preserving the charge. Such a product is no
longer irreducible; it is only a useful check on additive accounting.

These examples are genuine source-factor/contact models, not a claimed
counterexample satisfying every retained-routing or benchmark hypothesis.
The theorem covers TOTAL JET DEGREE AT MOST ONE. It does not cover merely
R-degree one with nonlinear Y-dependence, nor general higher-jet-degree
regular carriers. The requested general nonuniform gap remains open.
