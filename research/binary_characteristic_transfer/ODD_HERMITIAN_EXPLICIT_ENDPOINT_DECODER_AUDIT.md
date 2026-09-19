# Explicit outside endpoint and constant-dimensional Hermitian decoder

2026-09-19. Independent audit: **PASS**. This is an exact algebraic decoder, not an implementation benchmark. No manuscript edits or scan.

Use B=Fp²⊂E=Fp4, beta∈E\B, Λ=X^(p²)−X, and the full monic Hermitian bank from ODD_HERMITIAN_COMPLETE_LIST_CLASSIFICATION_AUDIT.md. Put A=Λ(beta)^(p−1)≠0.

## Explicit second far endpoint

Let c*=A^(p³), the unique pth root of A in E. It is nonzero. Every bank label z=P_G(beta) obeys

    z^p=A(1−G(beta)^(1−p)).

Since G(beta)≠0, its right side is never A. Therefore c* is outside the bank. The explicit endpoints f and f+c*g are both outside, and their affine line λ=c*t retains the exact full bank without chart loss. This replaces the previous existence choice without changing source or common-agreement bounds.

## The evaluation isomorphism

Consider the Fp-vector space

    H={bX^(p+1)+sX^p+s^pX+d : b,d∈Fp, s∈B}.

It has dimension four, since the displayed degrees are distinct for p≥5. Evaluation at beta is injective. For b≠0, dividing by b gives a monic norm-circle polynomial, possibly with zero radius; all roots lie in B. For b=0,s≠0 the polynomial is a nonzero affine trace polynomial and has p roots, all in B. For b=s=0,d≠0 it has none. Thus no nonzero member vanishes at beta. Since E also has dimension four over Fp, this evaluation map is an isomorphism, with an invertible 4×4 matrix after fixing bases.

## Exact membership and witness recovery

Given z∈E, set u=1−z^p/A.

1. If u=0, reject: no bank value can have this parameter.
2. Solve the Fp-linear equation v−u*v^p=0 in E. If its kernel is zero, reject. Otherwise choose any nonzero solution v.
3. Invert the evaluation isomorphism to obtain H=bX^(p+1)+sX^p+s^pX+d with H(beta)=v.
4. If b=0, reject. Otherwise divide by b and set s0=s/b, c0=d/b. Reject if c0−Norm(s0)=0.
5. The surviving monic G=H/b belongs to the bank. Form P_G=(X+s0)Λ/G and the already proved divided-difference witness.

For u≠0, a nonzero solution exists exactly when Norm_(E/Fp)(u)=1. Indeed the equation is v^(p−1)=u^(−1), whose solvability condition in E* is u^(1+p+p²+p³)=1. All nonzero solutions differ by an Fp* scalar, so the kernel is exactly one-dimensional. This is also immediate from taking the ratio of two solutions and noting that it is fixed by p-Frobenius. Thus the arbitrary choice of v in step 2 scales H by the same base-field scalar and has no effect on the normalized G or on the rejection tests.

If the tests pass, v=u*v^p gives G(beta)^(1−p)=u, and therefore P_G(beta)^p=A(1−u)=z^p. Frobenius injectivity implies P_G(beta)=z, proving sufficiency. Conversely a true bank label supplies v=G(beta), and every step recovers its unique monic G. The zero input is correctly rejected: then u=1, the kernel consists of Fp, and its inverse evaluations are constants with b=0. The explicit c* is rejected at step 1.

The decoder uses only two 4-dimensional base-field linear systems (the evaluation inverse can be precomputed), field operations, and the explicit witness formula. Norm one alone is NOT a membership test: the b≠0 and nonzero-radius conditions are essential. Producing the dense witness coefficient array still costs at least its output length; the constant-dimensional claim concerns label membership and recovery of the compact Hermitian parameters, not outputting a length-Theta(p²) polynomial in constant time.

No singleton or completeness claims beyond the separately proved threshold classification are assumed in this derivation. Combined with that classification, rejection means the threshold list is empty, and acceptance supplies its unique member.
