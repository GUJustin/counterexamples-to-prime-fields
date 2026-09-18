# Full-field monomial quadratic-list probe

September 18, 2026. **Exact finite census and independent replay: PASS.**
Several cores have many more than sqrt(n) witnesses and more than two
owners per coordinate. The bounded computation does **not** establish a
family with both growing sqrt(n)-scale agreement and growing L/sqrt(n).
The balanced-factor maximum-agreement examples deteriorate in the larger
tested fields. No further scan is proposed from these results.

## Scope and prior work checked

The domain is the entire prime field F_p, the received word is `w(x)=x^e`,
and the code is ordinary RS dimension 3. We used exactly

```
p = 31, 43, 61, 101,
e = 3,...,p-1.
```

This gives 28+40+58+98=224 profiles. The objective was to count *all*
quadratics at several sqrt(p)-scale agreement thresholds and then verify
the ownership structure of promising banks. These are mechanism probes;
no small-field first-order or DKT placement claim is made.

Before running, we checked the directly relevant existing work:

- `../modular_cyclic_bank/RESULTS.md` and its scanners already exhaust all
  monomial words on every nonzero subgroup for p=17,97,193. They include
  regular banks `(n,L,a)=(16,16,5),(96,96,8),(192,192,9)` and explain their
  multiplicative-orbit mechanism. The present primes and full-field domains
  were not in that census.
- `../modular_coefficient_bank/RESULT.md` excludes the specified 4096-word
  additive-box, multiplicative-box, and paraboloid banks at p=4801 by total
  incidence capacity. It is not a census of arbitrary received words.
- `../PRIME_QUADRATIC_RICH_CORE_INCIDENCE_GATE.md` records that the available
  general prime-field incidence bound leaves room for larger rich banks.
  Neither that bound nor this finite probe excludes arbitrary prime-field
  constructions.

## Exact method and independent verification

For each quadratic/linear coefficient pair (a,b), the scanner forms the
histogram of

```
c = x^e - a*x^2 - b*x,  x in F_p.
```

Its c-bucket size is exactly the agreement of `aX^2+bX+c`. Thus one word
costs O(p^3) operations, while counting all p^3 quadratics. Every profile
checks total cardinality and the first three interpolation moments:

```
sum H_A = p^3,
sum A*H_A = p^3,
sum binom(A,2)*H_A = binom(p,2)*p,
sum binom(A,3)*H_A = binom(p,3).
```

Eleven selected word profiles are independently replayed in Python by
interpolating the unique quadratic on **every triple of coordinates**.
A quadratic with A>=3 agreements is reconstructed exactly `binom(A,3)`
times. These multiplicities recover the whole histogram for A>=3; the
remaining entries follow from the lower interpolation moments. The full
codewide histograms match the C++ census exactly. All recorded candidate
banks are also directly evaluated, with their entire coefficient lists,
agreement sets, and per-coordinate ownership retained.

The C++ kernel took approximately 0.25 seconds, and the selected independent
replay approximately 0.30 seconds. The default macOS 27 SDK linker failed;
compilation succeeded with the installed macOS 15.4 SDK. No installation,
remote compute, or enlarged search followed.

## Threshold census

The threshold is the least integer A>=c*sqrt(p). Each entry below is
`A / maximum list size`, maximized over all tested exponents in that field.

| p | c=1/2 | c=1 | c=13/10 |
| ---: | ---: | ---: | ---: |
| 31 | 3 / 4495 | 6 / 56 | 8 / 3 |
| 43 | 4 / 2870 | 7 / 13 | 9 / 3 |
| 61 | 4 / 8555 | 8 / 11 | 11 / 11 |
| 101 | 6 / 1420 | 11 / 10 | 14 / 5 |

The p=31 half-scale threshold is only 3, the interpolation dimension,
and is non-discriminating. All witnesses at the c=13/10 thresholds have
at least one zero coefficient. The p=61 threshold-11 list is a union
of lower-dimensional coefficient families; it is not a growing full-span
nearest bank.

## Balanced-factor tests

These are complete **nearest** lists, so every listed witness has exactly
the stated maximum agreement a. Coefficient rank is the rank of the
augmented rows `(a_2,a_1,a_0,1)`.

| p | exponent e | maximum a | nearest list L | ownership at 0 / each nonzero x | coefficient rank |
| ---: | ---: | ---: | ---: | --- | ---: |
| 31 | 5 | 5 | 186 | 30 / 30 | 4 |
| 31 | 6 | 6 | 56 | 6 / 11 | 4 |
| 43 | 6 | 6 | 70 | 0 / 10 | 4 |
| 43 | 7 | 7 | 13 | 7 / 2 | 3 |
| 61 | 6 | 6 | 142 | 12 / 14 | 4 |
| 61 | 10 | 10 | 6 | 0 / 1 | 2 |
| 101 | 10 | 10 | 10 | 0 / 1 | 2 |

The first two fields give genuine finite high-ownership cores. For example,
`X^6` over F_31 has 56 witnesses with six agreements, and every nonzero
coordinate belongs to eleven of them. `X^5` over F_31 has 186 witnesses
with five agreements and exactly thirty owners at every coordinate.
This is substantially more than pair or triple ownership.

However, the balanced maximum-root pattern does not persist through this
sequence. At e=10 over F_61 and F_101, the complete nearest bank consists
only of the six or ten constant values of `X^10`. These have just one
owner at each nonzero coordinate. In the already existing p=193 census,
the balanced divisors e=12 and e=16 likewise have only 16 and 12 constant
maximizers, respectively, on F_193*. We read those saved records rather
than rerunning them. Their all-nonzero-coefficient banks have only seven
agreements, though each contains 768 polynomials.

## Explicit modular orbit cores

The new census also verifies the following structured banks of quadratics
with every coefficient nonzero. The zero coordinate is unused by these
banks and can be deleted. On F_p*, all ownership counts are uniform.

| p | word exponent | agreement a | bank L | owners at every nonzero coordinate |
| ---: | ---: | ---: | ---: | ---: |
| 31 | 6 | 6 | 30 | 6 |
| 43 | 20 | 6 | 84 | 12 |
| 61 | 9 | 7 | 60 | 7 |
| 101 | 37 | 8 | 100 | 8 |

Each bank has augmented coefficient rank 4. The p=43 bank is two complete
42-element multiplicative orbits; the other three are single full orbits.
For example, over F_101 the seed

```
Q(X)=3X^2+9X+83
```

agrees with `X^37` at exactly

```
53, 59, 69, 74, 75, 91, 94, 95.
```

Its bank is the explicit family

```
Q_t(X)=3*t^35*X^2 + 9*t^36*X + 83*t^37,
t in F_101*.
```

These 100 distinct quadratics are the complete nearest list, each with
eight agreements. Every nonzero coordinate has eight owners. This is a
usable finite modular core, but the full field has only one additional
coordinate; it is not already a padded line construction.

The same orbit identity explains the earlier nonzero-subgroup census,
so this is a further explicit instance of that mechanism, not a new
general construction.

## What the scaling evidence does and does not establish

There are two rigorous elementary scope restrictions:

1. For fixed exponent e>2, `X^e-Q` has at most e roots. Hence even a rapidly
   growing list at that fixed degree has `a/sqrt(p)->0`. The large list
   at `(p,e)=(101,6)`—1420 nearest witnesses, each with six agreements—does
   not supply the requested growing-agreement family.
2. If the character-image size `r=(p-1)/e` is fixed, `X^e` has only r
   nonzero values. A nonconstant quadratic matches at most two coordinates
   at each value, plus possibly zero, so its agreement is at most `2r+1`.
   The r constant witnesses can have large agreement, but their bank size
   is fixed. This regime also fails the requested scaling.

The genuinely balanced regime `r,e` both of order sqrt(p) escapes those
two arguments. This census supplies **negative finite evidence**, not an
asymptotic theorem, for obtaining a growing-richness bank from its complete
maximum-root lists: the larger balanced examples above collapse to their
constant witnesses. The other full-coefficient orbit examples have
agreements 6,6,7,8 as p grows through 31,43,61,101; they do not certify a
positive asymptotic lower bound for `a/sqrt(p)`.

The next mathematical gate is therefore a formula for roots of
`X^e-Q(X)` in a specified growing prime/exponent family that proves
`a>=c*sqrt(p)` for a fixed c>0, together with a super-sqrt(p) bank. For the
balanced maximum-root case `a=e`, this is the exact split-locator condition

```
product_(x in S)(X-x) = X^e-Q(X),  |S|=e,
```

equivalently the first e-3 elementary symmetric coefficients of S vanish.
The finite positive instances do not establish that condition in a growing
family. No broader prime scan, compute rental, line counterexample, or
security implication is justified by this probe.

## Files and reproduction

`census.cpp` is the bounded four-prime scanner. Its rows are in `p31.jsonl`
and `p43_p61_p101.jsonl`. `verify_selected.py` is the independent
interpolation-based replay. `selected_banks.json` contains the complete
explicit candidates, and `verification.json` contains all summaries and
the selected-bank SHA256.

On the current workstation:

```sh
/usr/bin/clang++ -std=c++17 -O3 -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk census.cpp -o /tmp/rs3-full-field-monomial-census
/tmp/rs3-full-field-monomial-census 31 > p31.jsonl
/tmp/rs3-full-field-monomial-census 43 61 101 > p43_p61_p101.jsonl
python verify_selected.py
```
