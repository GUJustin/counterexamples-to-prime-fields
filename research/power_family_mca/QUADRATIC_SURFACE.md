# A third-order family with genuinely quadratic solution-variety degree

September 16, 2026. Self-reviewed algebraic observation, not an MCA
counterexample. The accompanying self-reviewed Wronskian proof bounds this family by
O(n) full-MCA labels in the stated large-characteristic asymptotic regime.

Fix e>=1 and work in characteristic zero or p>2e. Among nonzero
polynomials of degree at most 2e, the solutions of

    e^2 P^2 P''' + 3e(1-e) P P' P''
                  + (1-e)(1-2e) (P')^3 = 0              (1)

are exactly P=c H^e with deg H<=2. Thus (1) has fixed derivative order
three and fixed total jet degree three, independently of e.

To prove necessity, take a root of P of multiplicity m. The coefficient
at the lowest possible order 3m-3 in (1), after removing a nonzero
leading local scalar, is

    m(m-e)(m-2e).

Since 1<=m<=2e<p, every root has multiplicity e or 2e. Hence P=cH^e
for a polynomial H of degree at most two. Constants are included. The
converse follows by substituting P=cH^e, or by differentiating a local
e-th root three times: equation (1) is the denominator-cleared form of
(P^(1/e))'''=0. Over a non-algebraically-closed base field the monic H
descends, since its root multiplicities and its normalized e-th power
determine it uniquely. Its scalar coefficient can be kept as c.

## The projective solution surface has degree e^2

The map from projective quadratic polynomials [H] to [H^e] is injective,
has no base points, and is given by homogeneous forms of degree e. Its
image therefore has degree e^2. One can see the degree directly from
two evaluation hyperplanes. Choose three distinct points a,b,c and cut by

    P(a)=P(b),   P(c)=P(b).

There is no projective solution with H(b)=0: it would also have H(a)=H(c)=0,
which is impossible for a nonzero quadratic. Normalize H(b)=1. Then
H(a) and H(c) can independently be any e-th root of unity. Quadratic
interpolation gives exactly e^2 distinct points. Their intersections are
reduced because the derivatives of U^e-1 and V^e-1 are nonzero there.

For fixed positive RS rate with D=2e, this is a Theta(n^2)-degree actual
solution variety at fixed derivative order. It supplies no nearby received
line and no quadratic exceptional-label count. In fact, fixed-word lists
for bounded-root polynomials are constant at fixed positive agreement
when p/n tends to infinity, so ordinary list-to-line padding cannot use
this family to reach the desired lower bound.

The remaining question was direct line incidence. The new working note
`PROOF.md` gives an O(n) argument
for all P=cH^e with fixed deg H, including this family. Its finite checks pass, but
no independent mathematical review is claimed. The degree classification
and ten reduced sections were also checked exactly: 156,194 monic
polynomials, 278 solutions, and sections through e=24.
