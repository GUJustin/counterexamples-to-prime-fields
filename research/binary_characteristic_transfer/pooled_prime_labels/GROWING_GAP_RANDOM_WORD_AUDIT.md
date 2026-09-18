# Independent random-word proof: growing gap and superlinear singleton labels

This audits the new route proposed by the frontier agent. It uses no further rental or scan. All asymptotics are along arbitrary primes p tending to infinity.

## Parameters

Let d=floor(sqrt(log(p)/2)) and
L=floor((p^d d!)^(1/(2d+1))). Put A=2L−2, T=A+d,
n=ceil((T²+1)/2), N0=L(L−1), t=n−N0.
Then t=L²+O(Ld+d²), d~sqrt(log L),
L(t/p)^d/d!→1, μ=t/p→0, dμ→0, and p/n→infinity.
Indeed log(p/L²)=(log p−2log(d!))/(2d+1)+o(1), which dominates log log L. In particular p>2a_L² eventually for the first L primes a_i, so the usual pair-core construction is valid. Also t<p−N0−1 eventually, allowing t distinct nonzero fresh nodes outside the core.

The adjustment of t is essential: keeping t=L(L−1)+1 would put the growing-gap threshold above Johnson. Here T²<2n exactly. The first-order threshold for K=3 is (sqrt(3/2)+o(1))sqrt(n), whereas T=(sqrt(2)+o(1))sqrt(n), so T is above it.

## Random source with exact far endpoints

On the core use the standard intersection word f and g=0. Fix any t distinct fresh nodes outside core and zero, set g(x)=x³, and choose f(x) independently uniformly from F_p excluding the at most 2L values
{P_i(x),P_i(x)−g(x):1≤i≤L}.
This prevents any bank polynomial from acquiring fresh matches at canonical labels0 or1.

For λ≠0,1 and incumbent i, let X_iλ be its fresh match count with f+λg. At each permitted coordinate its match probability is between 1/p and 1/(p−2L). At most6(L−1) fresh coordinates are not permitted: an excluded target requires
P_i−P_j=λX³ or P_i−P_j=(λ−1)X³,
and each nonzero cubic has at most3 roots. At any fresh coordinate the targets of different incumbents are distinct.

## Uniform factorial moments and singleton labels

Let Yλ=# {i:X_iλ≥d}. For every fixed positive integer k,
E[(Yλ)_k]→1 uniformly over λ≠0,1.
For clarity, here is a direct sandwich proving that assertion. For k fixed distinct incumbents, an upper bound on their simultaneous event is
(t)_(kd)/(d!)^k · (p−2L)^(−kd),
by selecting d disjoint matches per incumbent. A lower bound is
(t−6L−kd)_(kd)/(d!)^k · p^(−kd)
  ·(1−k/(p−2L))^(t−kd).
Choose only permitted disjoint supports and forbid additional matches to these k incumbents elsewhere. These exact-support events are disjoint. Multiplying both bounds by (L)_k tends to1: kd²/t, kdL/t, kdL/p, and kμ all tend to zero, while L(t/p)^d/d!→1.

The pointwise Bonferroni inequality
1_{Y=1} ≥ Y−(Y)_2+(Y)_3/2−(Y)_4/6
therefore gives P(Yλ=1)≥1/3−o(1), uniformly. Higher fixed even truncations yield the stronger limit inferior1/e, but the constant1/3 needs only these four moments.

## Uniform exclusion of all nonbank quadratics

Every nonbank quadratic has at most L core matches. At a fixed label and for a fixed nonbank polynomial, its probability of at least L−1 fresh matches is at most
binom(t,L−1)/(p−2L)^(L−1).
Union over at most p⁴ polynomial/label pairs gives failure probability at most
p⁴ binom(t,L−1)/(p−2L)^(L−1)=o(1).
Thus, except on an event of probability o(1), EVERY nonbank quadratic at EVERY finite canonical label has agreement at most A. This stronger cutoff, rather than merely T, proves both endpoints have agreement exactly A.

The expected number of singleton threshold labels is at least (1/3−o(1))p. Removing all failed samples costs at most p·o(1). Therefore some realization simultaneously has the uniform nonbank exclusion and at least (1/3−o(1))p singleton threshold labels.

## Common agreement and final line

A nonzero quadratic direction agrees with g at at most two core zeros and three fresh points, hence contributes at most5 simultaneous matches. Zero direction restricts simultaneous matches to the core, where the maximum is A. Thus common agreement is exactly A, independently of random f.

Apply the usual two-endpoint reparametrization from f,g to f,f+g. Both endpoints have agreement A; common agreement stays A. Canonical singleton labels avoid0,1 and map injectively to nonzero finite labels. The additional infinity word −g has singleton threshold list {0}, since it matches zero on N0 core points and every nonzero quadratic at at most5 points.

Conclusion: for all sufficiently large primes p there exist K=3 prime-field lines with n=p^(1−o(1)), p/n→infinity, agreement gap d~sqrt(log(n)/2), and at least (1/3−o(1))p singleton bad challenges at a threshold above first order and below Johnson. Thus the bad count is superlinear in n and the absolute source gap grows. The rate still tends to zero and the relative gap still tends to zero; this is not a fixed-rate or fixed-relative-gap result.

## Stronger parameter choice with the SAME first-prime core

The proof above also applies with d=floor(log p/(6 log log p)) and the same formula for L. Stirling gives
p/L² ~ 6e (log p)² log log p,
p/n ~ 3e (log p)² log log p,
d ~ log n/(6 log log n).
Indeed log(p/L²)=log p/(2d)−log d+1+o(1). The floor error contributes o(1) to this identity. This ratio dominates log²L, so p>2a_L² still follows for the first-prime bank. Also dμ→0, d²/L→0, and every factorial-moment/union-bound estimate above holds unchanged. Thus the nearly-logarithmic gap does NOT require a new core construction.

A proposed d=floor(log p/(4 log log p)) or /(2 log log p) is not justified with the first-prime core: its p/L² ratio need not dominate log²L. Such sharper choices require a separate multiplicative Sidon core with p≥constant·L². They should not be silently substituted in the first-prime proof. The frontier agent independently caught this distinction while auditing the original proof.
