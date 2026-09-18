# The known all-challenge theorem does not improve the practical benchmark

September 18, 2026. At the actual benchmark parameters p=2130706433,
q=p^6, n=262144, and strict dimension k=131072, Crites--Stewart
Corollary 1's sufficient entropy inequality holds at agreement T=132442
and fails at T=132443. Its left-minus-right residual is enclosed near
-0.232821678562 and +0.767338429386, respectively. At the desired
T=139782 it fails by more than 7344.

The certified capacity margin is therefore 1370/262144,
approximately 0.00522614, compared with the desired 8710/262144,
approximately 0.0332260. Substitution into the benchmark's score expression
-128 log2(T/n) gives approximately 126.07985, which is weaker than the
existing 116.13 upper value. This is a mathematical comparison of a
sufficient theorem, not a newly checked Lean submission.

The verifier uses 256-bit Arb intervals, so the signs do not depend on
floating-point rounding. It also certifies monotonicity of the residual
throughout T in [131074,139782]. Writing
A(T)=n H_q((n-T)/n)-(n-T), the residual is
F(T)=T-k-A(T)+sqrt(A(T))+2. The derivative A' is decreasing and already
negative at the left endpoint, while A remains greater than 1/4 through
the right endpoint. Hence F'=1-A'(1-1/(2sqrt(A)))>1 on this interval.

Failure of this sufficient condition is not an impossibility theorem.
It rules out using this particular corollary directly to improve the
target value. Nor does the asymptotic random-norm-tag theorem provide a
construction on the prescribed 262144-point multiplicative domain.

Primary input: Crites--Stewart, *On Reed--Solomon Proximity Gaps
Conjectures*, Corollary 1, https://eprint.iacr.org/2025/2046.
Run `verify_cs_benchmark.py` with python-flint to reproduce the interval
receipt in `verify_cs_benchmark.json`.
