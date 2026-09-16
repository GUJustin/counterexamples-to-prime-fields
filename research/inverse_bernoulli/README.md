# Inverse Bernoulli equations near the characteristic cutoff

For fixed s>=2 and p>max(D,s+1), every nonzero-A equation

    P^(s-1) P' = A(X),  deg P <= D

has at most 2s polynomial solutions. The bound is sharp, including
the range p<=sD where integration leaves nonconstant Frobenius terms.
For s>=3, every distinct monic pair has an explicit rigid form:

    p=sg+1, U=X-u, V=X-v, S_0=monic(U^s-V^s),
    P=U*S_0^g, Q=V*S_0^g, degree=(s-1)g+1.

In characteristic zero or p>sD there are at most s solutions. At the
excluded boundary s=p-1, there can instead be p(p-1) solutions. The
nonzero-A family witnesses at most 2sn full-support bad labels. The
zero-A constant family also has only O(n) bad labels at fixed positive
agreement. This closes this particular first-order nonlinear route,
including a characteristic range not covered by Appendix G's general
bounded-root theorem. The general first-order conjecture remains open.

## Evidence

`appendix.tex` is Appendix K; `PROOF.md` records the derivation. The
proof is twice self-reviewed, without independent coauthor review or
a novelty claim.

Run from the repository root:

```sh
python3 research/inverse_bernoulli/verify.py
```

The exact standard-library checker exhausts 164,803 monic polynomials
in thirteen small-field fixtures. It checks the pair classification,
six examples attaining 2s solutions (56 exhibited solutions total),
and four exceptional-characteristic controls (178 solutions total).
Finite checks supplement the universal argument. The recorded run
used a sequential 384 MiB watchdog; RSS is sampled process-group use.
No better.codes gain or quadratic MCA lower bound is claimed.
