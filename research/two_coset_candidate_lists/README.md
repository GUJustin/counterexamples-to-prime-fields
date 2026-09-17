# Two-coset candidate lists

September 17, 2026. Exact finite exploration of a remaining option in
the binomial-section family. No growing short-domain list is established.

Use p=2rk+1 prime and G(X)=sum_i binom(rk+j,ri+j)X^i, as in
research/dickson_fixed_gap/BINOMIAL_SECTION_SEARCH.md. Its leading
coefficient is1 and its linear coefficient is nonzero. For h in mu_k,
P_h(X)=G(hX)-X^k are distinct degree-<k candidates.

Select a subgroup H of order k/4 and two adjacent H-cosets in mu_k.
Their union has k/2 candidates and is not a subgroup. This option was
not covered by the earlier full-orbit and subgroup scans.

## Exact optimization in the invariant class

Restrict the domain to q cosets of H, and on each coordinate coset C
use a word v_C-X^k. Every candidate in the first H-coset then has
m_C(v_C) agreements on C; every candidate in the second has
m_{aC}(v_C), where m is the fiber histogram of G and a is the coset
representative ratio. Thus the problem is to select q coordinate
cosets and one value per coset, maximizing the smaller of two total
agreement counts.

After processing t coordinate cosets, the DP stores, for every number
u of selected cosets and every first agreement total b, the greatest
possible second agreement total. The next coset is either omitted or
selected with one of its available value pairs. Retaining the largest
second total at fixed u,b is valid because the objective is monotone.
Within a coset, a pair dominated in both coordinates may be discarded.
Backtracking returns actual domain cosets and received symbols.

This is an exact optimum ONLY in this specified invariant class for
the selected candidate union. It is not an optimum over every domain,
every word, every candidate subset, or every binomial section.

## Results

The census covers120 cases: k=32,64,128; r=2,...,48 whenever p is prime;
the distinct section indices0,1,floor(r/2),r-1; H of order k/4; and
n=4k. All120 exhibited lists were independently replayed.

Only four cases have agreement exceeding k:

| r | k | j | p | list size | agreement | below characteristic Elias |
|---|---|---|---|---|---|---|
|3|32|0|193|16|34|no|
|4|32|0|257|16|37|no|
|2|64|0|257|32|70|no|
|2|64|1|257|32|100|yes|

The last example has n256, rate1/4 and gap9/64. Those same32 candidates
have96 agreements with the standard full-length comparison word, so
the optimized word improves their agreement by4. This is a finite
tradeoff: the standard full-length construction has a larger list at
the lower96-agreement threshold. The field still has only257 scalar
labels. No fixed-gap superlinear line count or better.codes improvement
follows, and this example is not added to the manuscript.

## Independent validation

verify.py recomputes coefficients using integer binomial coefficients,
replays all candidate values and all asserted agreements, and checks
the exact characteristic-Elias inequality. Four smaller optimizations
are independently exhausted without the DP or its Pareto pruning:
126720,126720,20736 and16384 domain/word assignments. All agree with
the DP optimum. A two-coset union that IS a subgroup reproduces the
earlier subgroup census optimum29.

The120-case scan took14.6s at less than38MiB RSS; independent validation
took6.8s at less than22MiB. Both ran under a384MiB watchdog. The JSON
contains the selected cosets and symbols needed to reconstruct each
certificate. The search is finite evidence, not an asymptotic barrier.

## Subsequent structural bound

[BINOMIAL_BRANCH_BOUND.md](BINOMIAL_BRANCH_BOUND.md) proves a restricted
upper bound for ANY subset of the full mu_k candidate orbit, on arbitrary
domains and words of length at most c*k. For r>=3, agreement above k
forces list size at most2^20*r^3*4^r+24*c*(r*2^r+1), independently of k.
The proof separates constant radical branches, bounds residual fibers
by a norm, and applies character-sum Fourier mixing to arbitrary subsets.
The r2,j1 Dickson case is explicitly excluded.

This blocks growing candidate subsets when r is fixed and more generally
when r grows sufficiently slowly relative to log L. The exponential
dependence on r leaves the main large-prime target open. This is a
locally audited family-specific theorem, not a general RS list bound.

check_branches.py passed26 exact root-filter/mask/residual-fiber fixtures,
including all sections at r3,4,6 overF12289; it uses NumPy integer arrays.
Its Fourier numbers are floating-point diagnostics only. Separately,
check_branch_classification.py passed26104 exact sign-pattern coefficient
checks for every section and Frobenius class at r2 through8, using only
the standard library. No new manuscript appendix was added.
