# Finite-characteristic subgroup boundary search

September 17, 2026. Exact finite experiments; no asymptotic claim.

The first census enumerated every 8-subset of mu_16 in 22 split prime
fields, comparing all seven positive surplus values with the exact
characteristic-zero maximum. No maximum-size violation satisfied
the strict characteristic-Elias inequality in those fields.

The second census enumerated every 8-subset of mu_32 over p=97,193,
257,353,449: 52,591,500 supports in total. One lexicographic sort of
all seven-moment keys gives every prefix class size. Peak memory per
process was below 384 MiB. At s=1,...,7 the maxima were:

    p97:  108508,1260,44,4,4,4,4
    p193: 54876,348,28,4,4,4,4
    p257: 40975,252,28,4,4,4,4
    p353: 31484,144,28,4,4,4,4
    p449: 24700,156,28,4,4,4,4.

The characteristic-zero maxima are 1820,28,28,4,4,4,4. Again none
of the maximum-size violations lies strictly below Elias. The Elias
test is exact integer arithmetic:

    n^n (p-1)^(n-A) < (n-A)^(n-A) A^A p^(n-K).

## A genuine below-Elias classification exception

The absence of a maximum-size violation does NOT mean all support
classes are the characteristic-zero classes. On mu_32 in F_97, take
dimension K=4, threshold A=8, and

    W(X)=X^8+23 X^4.

Its ENTIRE nearby list is

    75,   8+16 X^2,   8-16 X^2.

Each agrees at exactly eight coordinates. The exact rate and gap are
both 1/8, and the radius is strictly below the characteristic-based
Elias bound. The support difference between a quadratic candidate and
the constant is not 4-periodic, contradicting the characteristic-zero
support classification at these parameters. Its list size three is
still below the characteristic-zero UNIFORM maximum four, so it does
not contradict that numerical upper bound or the whitepaper's bound.

Independent verification enumerates every one of the 35,960 determining
four-subsets, yielding 28,833 distinct interpolants, and checks every
one against the full domain. The two quadratic witnesses form only a
two-element orbit under mu_4; they are fixed by mu_2. Thus this is not
an example of a growing orbit. Scaling it by composition in fixed
characteristic97 cannot give a growing-length prime-field family with
n<p. No transfer to unbounded characteristics has been proved.

## Reproduction

* scan_subgroup_exceptions.py: full 16-point census.
* subgroup32_census.cpp: exact 32-point moment-prefix census; compile
  with assertions enabled and run separately at each recorded prime.
* subgroup32_census.json: aggregate counts and exact Elias comparisons.
* verify_subgroup_exception.py: independent full interpolation check.

This search identifies real finite-characteristic effects below Elias,
but currently only bounded lists and bounded witness orbits. The next
asymptotic construction would need growing orbit complexity or a
different received-word/domain structure. No better.codes improvement
or new manuscript claim follows from this experiment.
