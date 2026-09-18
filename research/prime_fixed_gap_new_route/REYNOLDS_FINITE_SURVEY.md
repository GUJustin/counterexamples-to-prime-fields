# Exact finite Reynolds survey and optimal complete-bank word

The script `check_reynolds_surplus.py` checks the prime values
`p=4dr+1`, for the fourteen primes `3<=r<=47` and `2<=d<=100`.
There are 377 such cases. Arithmetic, polynomial coefficients, and
agreement counts are exact in the prime field.

No case gives more than `r` agreements with the original word `W_r`.
The largest additive surplus is `-1`. This finite result does not
prove that the proposed asymptotic surplus lemma is false.

We also optimize the received word for agreement with every member of
the complete bank of `r` rotations. On each of the four cosets of
`mu_r` in `mu_(4r)`, let `m_C` be the largest multiplicity of a value
of `V_1`. Then the optimal minimum agreement with all `r` candidates is
exactly `sum_C m_C`:

* At a coordinate in coset C, the bank values are the evaluations of
  `V_1` throughout C, permuted. The largest agreement bucket is `m_C`.
  Summing over coordinates bounds the average candidate agreement by
  `sum_C m_C`, and hence bounds the minimum by the same quantity.
* Choose the word constant on each coset, equal to a modal value.
  Every rotated candidate visits each coset once under permutation,
  and agrees at exactly `m_C` of its coordinates. The bound is attained
  simultaneously by every bank member.

In the survey, even this optimal word gives no surplus over `r` for
any tested `r>=5`. The 44 surplus cases all have `r=3`; they do not
provide an unbounded bank. Repeated modal values can also make a
constant polynomial a better nearest candidate, so surplus alone
would not certify the intended nearest-orbit construction.

Independent checks in `REYNOLDS_MODAL_AUDIT.md` verify the coefficient
formula against integer binomial coefficients, the actual Reynolds
average, the root-of-unity filter, and every rotation in five fixtures.
The scan covers complete banks only. Proper subbanks and other
parameters remain outside its scope. The evidence makes this specific
complete-bank averaging proposal a lower priority than finding a new
short-domain source.
