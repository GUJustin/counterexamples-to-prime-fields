# Index-three subgroup branch: authorized bounded test

The exact Fourier common-root criterion is in
`SUBGROUP_REDUCTION_GATE.md`. Here the subgroup index is three modulo
four, so the native monomial X^k reduces to X^(3n/4). The earlier
quarter-rate proof for index one modulo four does not apply.

Before numerical work, two simple symbolic cases can be closed. Write
n=4q and k=((p-1)/n)q.

* Index three: k=3q<n, so no reduction occurs at all. The nonzero
  coefficient of X^(k-1) gives reduced degree exactly 3q-1.
* Index seven: n<=k-1<2n-1, so the reduced coefficient of X^(n-1)
  has exactly one summand, binom(2k+1,2n-1)t^(k-n+1). It is nonzero
  for every nonzero t because the binomial indices are below p.
  Thus the reduced degree is exactly n-1.

These already exclude a quarter-rate reduction in the two smallest
index-three classes. They do not exclude index eleven and larger.

## Complete bounded survey

With the numerical slot coordinated, ran the parent-authorized single
survey over every prime p<=500, every n divisible by four with
n|(p-1) and index three modulo four, and every nonzero square parameter
t. The script is `subgroup_index_three_probe.py`; exact output and
watchdog data are the accompanying JSON files.

Results:

* 53 admissible (p,n) cases;
* 7,280 nonzero-square parameter cases;
* zero reduced polynomials of degree <n/4.

The output records the entire degree histogram for each case, not only
the minimum. It also records example parameters attaining the minimum,
and the zero-parameter candidate's native-word agreement. The script
would record coefficients and exact agreements for every quarter-rate
candidate; that list is empty. Distinct parameter representations of
the zero candidate are not counted as additional codewords.

All index-three cases have degree 3n/4-1, and all index-seven cases
have degree n-1, as the symbolic arguments predict. Among the remaining
tested cases, reductions have degree n-1 or n-2. The only degree-drop
cases there are (p,n)=(157,4),(317,4),(409,8),(433,16), with respectively
2,4,4,8 parameters of degree n-2. Even these do not approach degree n/4.
This last observation is finite evidence, not a general n-2 theorem.

The watchdog reports 0.565 seconds and 13,824 KiB peak RSS, well below
the 60-second/384-MiB guard. No larger-prime survey or nearest-list
enumeration was run. No positive source or prime-field lower bound was
found. The remaining algebraic target is a simultaneous zero of the
high-residue Fourier polynomials for index at least eleven; this
experiment supplies no general obstruction to such a zero.
