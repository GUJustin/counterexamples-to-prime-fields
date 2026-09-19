# Independent affine-twist incidence audit

PASS, 2026-09-19. Actual note inspected; no corrections needed.

At every native point outside a monic divisor’s root set, G_i(x) lies in Fp*, so the exact identity forces A_i(x)=1. On the active set R, distinct parameters give at most one index solving this affine scalar equation; if its slope is zero, there are no solutions, which only strengthens the bound. The incidence inequality M(|R|−e)≤|R| and its consequence |R|≤e for M>n are valid. The union bound correctly removes at most |R| indices before obtaining a family with every point of R as a common root.

The residual identity P_i^p+A_iQ_i^(p−1)=Λ^(p−1) is exact. Since Q_i is a native monic complementary locator, it takes a nonzero prime-field value at each G_i root. Hence P_i(x)^p=−A_i(x) there; off those roots Q_i(x)=0. On D\R the unique pth root of −1 is −1 in any containing field, so the residual values are exactly restricted to {0,−1}. For a nonconstant/nonexceptional residual, P_i(P_i+1) is nonzero and yields 2degP_i≥n−|R|. The note’s constant exclusions are safe (constant −1 is in fact impossible because degG_i<n leaves a native point where P_i=0).

Crucially R may be empty. Then this argument only forces a binary-valued evaluation pattern and, for a nonzero nonconstant residual, degree at least n/2; it does not rule out a shared affine pencil or establish one. The source correctly preserves this possible escape and separately lists the missing head, label, and source-distance requirements.

Frozen source SHA256: `486c5cada81d58bc50f44f9456a9bc7a248cd7f9ed670c939859a526d828a609`.
