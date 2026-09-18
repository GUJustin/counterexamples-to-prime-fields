# F_(p³) overlap does not restore a linear source gap in the pure two-block model

Independent exact audit, September 18, 2026. Let p be odd, E=F_(p³), W a two-dimensional F_p subspace, and eta=s² outside F_p. Set

    D0={x!=0:x² in W*},
    D1={x!=0:x² in eta W*} minus D0.

On D0 use f=x^(2p), g=0. On D1 use f=eta*(x²/eta)^p, g=1. This note concerns these two blocks only; it makes no assertion about arbitrary additional coordinates or noncanonical witnesses.

## Canonical maps and labels

For a projective direction [u] in W put `a_u=u^(p-1)` and `L_u(y)=y^p-a_u y`. The kernel on W is F_p u, so its image I_u has dimension one. Choose an ordered basis w1,w2 of W and set `delta=w1*w2^p-w1^p*w2 !=0`. The alternating-bilinear identity

    u L_u(y)=u y^p-u^p y

shows `I_u=(delta/u) F_p`. Thus a canonical quadratic `Q=a_u X²+b` has core fiber `L_u(y)=b`, and fresh fiber `L_u(y)=v` when `lambda=b-eta v`, with b,v in I_u.

The previous plane-incidence lemma applies after scaling labels by delta. Every nonzero lambda has at least one representation; exceptional labels with all p+1 directions are exactly those with `lambda W=delta span(1,eta)`.

## Square-root counts on affine fibers

For an affine F_p-line `C=y0+u F_p` not containing zero, let alpha=y0/u. Then alpha is not in F_p; because E/F_p has prime degree three, its minimal polynomial has degree three and is separable. The polynomial `Norm_(E/Fp)(t+alpha)` is consequently a separable cubic with no F_p roots.

The quadratic character satisfies `chi_E(z)=chi_p(Norm(z))`. The number of physical x with x² in C is therefore

    p + chi_E(u) sum_(t in F_p) chi_p(Norm(t+alpha)).

The curve `Y²=Norm(t+alpha)` is a smooth genus-one double cover with one rational point at infinity. Hasse's elliptic-curve bound gives absolute value at most `2 sqrt(p)` for the displayed character sum. Thus every nonzero affine fiber supplies between `p-2 sqrt(p)` and `p+2 sqrt(p)` physical points. Multiplication by eta does not change these counts because eta is a square.

For a zero fiber `F_p u`, after excluding zero, exactly half of its p-1 nonzero values are squares in E, because chi_E restricted to F_p* is chi_p. Its physical count is exactly p-1. Hence every canonical fiber, including a zero fiber, has physical count between `p-2 sqrt(p)` and `p+2 sqrt(p)`.

This argument uses the standard Hasse bound for the explicitly identified smooth cubic curve, not an unverified full-fiber count of 2p.

## The completely deleted fresh fiber is on the exceptional label line

Write `F_p u0=W intersect eta^(-1)W`. The intersection is one-dimensional since eta cannot stabilize W. Then u0 and eta u0 are independent and

    W=u0 span(1,eta).

The removed fresh coordinates correspond exactly to the zero line F_p u0 in the normalized variable y=x²/eta. An affine fresh fiber is wholly deleted ONLY when its direction is [u0] and v=0. All other affine fresh fibers meet this line in at most one point, so lose at most two physical x coordinates.

For a nonzero label whose [u0] representation has v=0, one has `lambda in I_u0*=(delta/u0)F_p*`. These labels satisfy `lambda W=delta span(1,eta)`: they are EXACTLY the all-directions exceptional labels. Each has p-1 other representations with both b,v nonzero, in addition to its one v=0 and one b=0 representation. Choosing any both-nonzero representation avoids the completely deleted fiber.

Every other nonzero label already has a representation whose fresh fiber is not completely removed. At lambda=0 choose any direction other than [u0]. Both fibers are zero lines, and the fresh zero line intersects the removed zero line only at zero, which was already omitted. This gives exactly 2p-2 matches.

## Uniform consequence for source separation

Every finite label lambda has a canonical quadratic with at least

    2p-4 sqrt(p)-2

matches on D0 union D1. Every individual canonical quadratic at any label has at most

    2p+4 sqrt(p)

matches, since deleting overlap cannot increase the two full-block counts. Therefore a threshold witnessed by this canonical bank can exceed the nearest agreement of ANY chosen finite endpoint by at most `8 sqrt(p)+2`. In particular deleting/assigning the shared zero fiber cannot create a Theta(p) source-to-target gap within the pure canonical two-block construction.

The conclusion is a lower bound on every source agreement and an upper bound only on CANONICAL bank witnesses. It neither classifies all quadratic competitors nor prohibits adding a new mechanism that changes their agreement pattern. Arbitrary padding, a different source on the overlap, or a different bank requires a separate analysis. The root count and the all-direction exceptional geometry together close the specific proposed zero-fiber loophole.

Scope clarification: this bounds separation above the INDIVIDUAL nearest agreements of the chosen endpoints. It does not prove a lower bound on their ordinary COMMON agreement; individually close words can have different witnesses. Accordingly no obstruction to an ordinary-CA-only counterexample follows. The parent supplied an exact small-field census in `check_fp3_overlap.py/json`; that census was not rerun in this independent algebraic audit. A primary exposition of the Hasse theorem used above is MIT 18.783 (2021), Lecture 7: https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/resources/mit18_783s21_notes7/ .
