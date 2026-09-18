# Every monomial word has a helper in the frozen original source

September 18, 2026. Exact finite dimension certificate, following the audited 182580 one-point rank ceiling in `NTT_CONTACT_48_PROFILE_COMPRESSION_2026_09_18.md`. This closes monomial words as candidate INJECTIVITY counterinstances to the uniform source-repair gate. It does not prove that gate for arbitrary received pairs and does not improve better.codes.

Use the original parameters n=262144, w=131071, m=115, A=181275, strict weight cap W=mA=20846625, total Y/R cap 159, R cap 35, and joint Y/R/Z cap 274277, over the Koala prime 2130706433. For every exponent 0<=a<n, the received pair f(x)=x^a,g=0 has a nonzero contact-m helper satisfying ALL those caps.

## Explicit helpers outside one finite interval

If a<A, use (Y-X^a)^115. Its weight 115*max(w,a) is below W, its Y-degree is 115, and its contact at every domain node is at least 115.

If a>n+w-A=211940, use (X^(n-a)Y-1)^115. Its base factor vanishes on the received graph on mu_n and has weight w+n-a<A. Its other caps are again immediate.

Thus only the 30666 exponents 181275<=a<=211940 require a different argument. No assumption about their maximum agreement or list size enters: the tested source gate concerns arbitrary received rows. The earlier informal injectivity test at a=A was already closed by its character dimension surplus.

## Exact exhaustive dimension certificate

For each remaining a and cyclic character chi, the original column count is

    C(a,chi)=sum_(i+j<=159,j<=35)
       #{d: 0<=d<W-w(i+j)+j,
              d+a(i+j)-j == chi (mod n)}.

Every character contact image has dimension at most 182580, by the exact saturated one-point calculation. Therefore C(a,chi)>182580 proves existence of a helper over the actual Koala field without constructing or ranking a matrix.

The authorized interval check evaluated all 30666 exponents by integer endpoint sweeps, stopping if an exponent had every character count at most 182580. There was no such exponent. The exact minimax result is

    min_(181275<=a<=211940) max_chi C(a,chi)=182598.

It is attained by 28 exponents; the first is a=193328. At that exponent chi=137376 has 182598 columns, 67031 characters exceed the rank ceiling, and the summed Z-free nullity lower bound is 637598. The 18-column excess already suffices for nonzero kernel existence.

The initial 100-exponent timing was 0.016 seconds; the complete sweep takes about 6 seconds with about 36 MB peak resident memory. Each exponent also passes exact column conservation: sum_chi C(a,chi)=47859086760. No field matrix, global rank, support search, or rental is involved.

Replayable artifacts in this directory:

- `ntt_monomial_exponent_sweep.py/.json`: full event sweep, exact minimax receipt, 60-second hard cutoff, and first-survivor stop.
- `ntt_monomial_exponent_witnesses.csv`: one oversized original character for each exponent.
- `verify_ntt_monomial_witnesses.py/.json`: independent verification of every witness directly from original source exponents. It counts the residue d0=(chi-ai-(a-1)j) mod n in each original interval 0<=d<W-wi-(w-1)j. It uses neither event sorting nor transformed ceil bounds. The receipt reports PASS with 30666 checked exponents in 0.72 seconds.

Run both Python scripts with `/Users/jthaler/.local/share/research-toolchain/venv/bin/python`; the source and CSV hashes are recorded in the JSON receipts.

## Exact scalar/codeword extension

The conclusion also holds for f=cX^a+P and g=Q, with c!=0 and degP,degQ<=w. Given a monomial-word helper, substitute

    Y -> (Y-P-ZQ)/c,
    R -> (R-P'-ZQ')/c.

This is invertible. The original weights do not increase, R-degree does not increase, total Y/R degree does not increase, and replacing a Y or R by a Z-term preserves the joint Y/R/Z cap. Contact is preserved because P(a+t)-P(a)-tP'(a+t), and the corresponding expression for Q, are divisible by t^2 and can be absorbed into the free second-order variable. For c=0, the elementary helper (Y-P-ZQ)^115 suffices.

This is an exact closure of monomial-plus-codeword tests only. It says nothing about general sparse received words or genuinely arbitrary non-codeword directions. The successful special-word helper dimensions do not reduce the existing uniform local rank allowance or the separate final charge deficit 21042194961366305. No further monomial or monomial-plus-codeword rank runs are warranted for this frozen source.
