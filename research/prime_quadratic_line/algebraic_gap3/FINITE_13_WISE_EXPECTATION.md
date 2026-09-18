# Monic degree-13 fresh word: exact finite feasibility

`expectation.py/json` prove an expectation guarantee; no received polynomial has yet been instantiated. No rental was used.

At the original L1500 parameters, μ=t/p=0.1244171724. The exact expected number of qualifying incumbents at one label is0.4387146319. An independent Poisson heuristic predicts singleton density0.2829116134. The rigorous13-wise lower bound is0.2795717587, or5,065,979 expected singleton labels before endpoint repair. Thus the unblacklisted profile is promising, but one must not ignore the repair cost.

A larger finite choice is certified:
L=2000, q=2003, p=32,032,061, n=8,004,001, t=4,006,001,
A=3998, T=4001, gap3.
The exact lower bound after conservative endpoint repair guarantees at least8,116,096 canonical singleton labels, plus the infinity singleton: **8,116,097>n**. This is a1.4% certified margin. L1500 andL1800 do not pass this conservative repaired bound.

## Why degree13 is enough

Choose a uniformly random monic degree-13 polynomial h. Its values on any at most13 distinct points are independent uniform field elements, by Vandermonde interpolation. On a fixed initial fresh domain set f=h and g=X³. For any incumbent and label, h+λX³−P_i is monic degree13, so its fresh match count X_i is at most13. Thus the single-incumbent tail probability is exactly recoverable from its first13 binomial moments.

For k distinct incumbents, and nonnegative r_i with total R≤13,
E[prod_i binom(X_i,r_i)]=(t)_R/[p^R prod_i r_i!].
Selected match sets must be disjoint because the incumbent values are distinct off the core. These identities hold uniformly for every label, including0 and1.

For d=3, expand the joint tail indicator using
1_{X≥d}=binom(X,d) d∫_0^1 u^(d−1)(1−u)^(X−d)du
when X≥d (and interpret both sides as zero otherwise).
The coefficient at binom(X,d+s) is(−1)^s binom(d+s−1,d−1). For several variables, truncation by total extra degree gives an upper bound at even truncation and a lower bound at odd truncation: inside the integral this is the ordinary Bonferroni bound for a product of factors1−u_i, repeated X_i−d times.

Let Y count incumbents with at least3 matches. The program computes:
- E(Y) exactly, using total degree13 and X_i≤13;
- an upper bound for E(Y)_2, using total degree12 (extra degree6);
- a lower bound for E(Y)_3, using total degree12 (extra degree3);
- an upper bound for E(Y)_4, using total degree12 (extra degree0).
All terms require at most13-wise independence. The pointwise inequality
1_{Y=1}≥Y−(Y)_2+(Y)_3/2−(Y)_4/6
then yields a rigorous singleton probability lower bound. There is no unjustified full independence or Poisson assumption in the certificate.

## Endpoint repair preserves the low-degree source

Among the initial t fresh coordinates, call x bad if h(x) equals P_i(x) or P_i(x)−x³ for any incumbent. Each coordinate has bad probability≤2L/p, so E[B]≤2Lt/p.

Remove each bad coordinate and replace it with an unused nonzero coordinate outside the core that is not bad. This is always possible: each of the2L equations is monic degree13, so at most26L coordinates in the full field are bad; the checked guard n+26L+1<p leaves enough replacements. Continue to define f=h on the replacement coordinates—no polynomial values are edited.

Changing one coordinate can alter the threshold list at at most2L labels: L labels from the removed coordinate and L from its replacement. Consequently the singleton count drops by at most2LB, deterministically. Its expected loss is at most4L²t/p. This is the repair cost subtracted by the exact certificate.

After repair both endpoints have agreement exactly A: incumbents acquire no fresh endpoint matches, while any nonbank quadratic has at most L core matches and13 fresh matches, hence at most L+13≤A. This nonbank exclusion is deterministic for ALL labels, removing the expensive validation obstacle of arbitrary random received words. Common agreement stays A by the same cubic-direction argument. The threshold remains below Johnson since T²=2n−1, and above first order by the usual finite bound.

## Cost recommendation

A successful h can be represented by13 coefficients plus the deterministic initial-domain/replacement rules. Testing it requires aboutL·t=8.012 billion bank/fresh incidences. A per-incumbent uint8 histogram of length p uses32MB and records threshold crossing at count3; a global owner counter of length p uses64–128MB. Processing banks sequentially or in CPU batches avoids an L×p dense table. Parallel partial owner counters can be reduced at the end. The low-degree nonbank bound gives a short correctness certificate once the incidence counts are replayed.

This is now a meaningful explicit-artifact target, but run a small throughput pilot before renting. The expectation proof alone does not give a success probability large enough to promise one or two random h trials; its certified repaired surplus is modest. No rental is recommended solely to reproduce the existence result.
