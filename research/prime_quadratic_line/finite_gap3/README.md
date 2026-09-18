# Exact finite existence certificate with gap three

Parameters: prime p=18,120,497; L=1500; q=1511; n=4,503,001; message dimension3; source/common agreement A=2998; threshold T=3001. The exact certificate proves the existence of at least **4,680,342 singleton bad challenges**, strictly more than n, on a line with both endpoint agreements and common agreement exactly A. It does not output a received word.

`certificate.py` uses only standard-library exact integers and Fractions. Runtime is about0.006 seconds. `certificate.json` saves the four lower/upper factorial moments and the resulting rational probability bound. All checks pass. No rental is required.

## Finite sharpening of the asymptotic proof

Use integer Sidon exponents b_i=2qi+(i² modq), 0≤i<L. Their largest value is4,530,122, and p−1−4max(b_i)=8>0. Thus their images under any primitive generator give the required distinct pair roots even up to sign. The usual integer Sidon proof applies; a quadratic-size pair scan is unnecessary.

Fix any t=2,254,501 fresh nodes. Draw f independently from the endpoint-blacklisted values, and put g=X³ there. For each canonical λ≠0,1 let Y count incumbents with at least d=3 fresh matches. Put Q=1/(p−2L), and write (u)_r for a falling factorial.

For k=1,2,3,4, a valid lower bound for E(Y)_k is
  (L)_k (t−6L−kd)_(kd) / [(d!)^k p^(kd)] · (1−kQ)^(t−kd).
This is the exact-support lower bound already proved in the asymptotic theorem.

For a sharper upper bound, couple the k categorical matches at every fresh coordinate to uniform categorical probabilities Q for each incumbent: the actual probabilities are each≤Q, and the residual outcome has enough mass to fill their deficits because kQ≤1. This gives stochastic domination by a multinomial(t;Q,...,Q,1−kQ).

The probability that each of these k categories has at least d occurrences is bounded above by
  (t)_(kd) Q^(kd)/(d!)^k · (1−kQ)^(t−kd)
  · [1−μ'/(d+1)]^(−k),
where μ'=tQ/(1−kQ)<d+1. To check this, write each count as d+s_i. Relative to the all-d term, bound the additional falling factorial by t^(Σs_i), and use d!/(d+s_i)!≤(d+1)^(−s_i); summing the resulting geometric series proves the bound. Multiply by (L)_k for the factorial moment.

The checker bounds (1−kQ)^(t−kd) by its odd13th and even12th binomial truncations, respectively. These are exact Bonferroni bounds. Thus the lower singleton probability
  lower(EY)−upper(E(Y)_2)+lower(E(Y)_3)/2−upper(E(Y)_4)/6
is an exact rational number greater than0.25828998.

The uniform nonbank failure probability is at most
  p^4 [3t / ((L−1)(p−2L))]^(L−1),
using binom(t,L−1)≤(3t/(L−1))^(L−1). Exact integer arithmetic verifies that p times this bound is less than1. Removing failed samples therefore costs less than1 in expected singleton count. The saved conservative integer lower bound is4,680,341 canonical singleton labels, plus the deterministic infinity singleton after the two-far-endpoint reparametrization.

The source and common agreement arguments are unchanged from the theorem. Also T²=2n−1. The first-order comparison is certified by 3n/2<2600², 3n/8<37⁴, and2600+37<T.

## Computational cost/benefit

Constructing and replaying one random realization directly would require about3.382 billion bank/fresh incidences, plus validation of every nonbank quadratic by an alternative argument. A full word has4.5 million coordinates; a label histogram has18.1 million entries. This is feasible engineering but does not improve the theorem and is far more expensive than this finite exact existence certificate. No further rental is recommended unless an explicit received-word artifact is independently valuable.

Scope: finite probabilistic existence with a rigorously positive source gap3 and more singleton bad labels than coordinates. It is not a displayed explicit word, a fixed-rate theorem, or a better.codes improvement.
