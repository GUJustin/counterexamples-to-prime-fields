# Exact arithmetic revisit of the pinned better.codes frontier

September 17, 2026. This audit uses the restored, pinned counting family,
not a newly verified live leaderboard. It supplies no new score or certificate.

The archived parameters are p=2130706433, n=262144, dimension131072,
and challenge field of size p^6. The required scalar-family count is
274980728111395088. Independent 70-digit arithmetic confirms:

| Agreement count | Unrounded score |
|---:|---:|
|139775|116.1284071162897043|
|139781|116.1204803338806496|
|139782|116.1191592365592259|

Thus seven additional coordinates would change the displayed centibit
score. This small numerical distance does not furnish those coordinates.

The exact equal-fiber scan tests B=2,4,...,131072 (and omits the infeasible
B=262144 endpoint). At the first allowed agreement at least139782, it
recomputes the known certificate

    ceil(binomial(M-1,H-1)/(M*p^max(0,H-M/2-3))), M=n/B.

Every candidate falls short. The best failed alternative is B=1024,
M=256,H=137: agreement140287 and certified count68579341025511059.
It misses the required count by 2.0034845649 bits, a factor slightly
larger than four. This is a closer combinatorial target than the
roughly27-bit loss incurred by advancing the incumbent B=512 family
one full coefficient constraint. Neither deficit is known to be recoverable.

An actual coefficient fiber may exceed its average, but these calculations
provide no lower bound showing the required fourfold excess. Similarly,
the count is a certified lower bound, not an upper bound on achievable
families. This audit does not prove a global optimum. The restored core,
partial-fiber, inverse-pair and divisor notes already exclude several
elementary ways of changing this specific counting argument.

Practical interpretation: we are close in the score's displayed units;
we do not yet have a mathematically justified improvement. The newer
asymptotic constructions on freely chosen domains and characteristics
do not bridge the fixed-domain finite counting deficit.

`frontier.py` independently recomputes the integer comparisons and writes
`frontier.json`; `resources.json` records its completed384MiB/60-second
watchdog run. The primary construction and its scope were read from the
restored `stwo_audit_2026-09-15/agents/better_codes_construction.md`,
`better_codes_divisor_search.md`, `better_codes_heterogeneous.md`, and
`better_codes_submission_ideas.md`. No protocol experiments or submission
were performed.
