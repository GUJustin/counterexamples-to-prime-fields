# Explicit algebraic fresh-word certificate

Both pilots are successful finite computed constructions. The larger instance
passed a separately structured replay: `pilot_d3.verified.json` compares all
counts and the domain hash, with input and code hashes. Replay used 31.80
seconds wall time and approximately 163 MiB sampled process-group RSS.

## Successful gap-three instance

`pilot_d3.json` supplies the exact polynomial and domain rule.

- L=1,500, p=18,120,497, message dimension 3, monic fresh degree 13.
- Core size 2,248,500; fresh size 2,254,501; n=4,503,001.
- Both endpoint and common agreements A=2,998; threshold T=3,001; gap 3.
- **5,127,684 transformed singleton labels**, exceeding n by 624,683.
- **6,437,753 transformed nonempty labels**.
- Canonical counts are one smaller; the additional label is the singleton
  infinity word −g.
- All nonbank agreements are at most 1,513, strictly below A.
- T²=9,006,001<2n=9,006,002. The first-order bound is less than
  sqrt(3n/2)+(3n/8)^(1/4)<2600+37=2637<T.
- Of the first 2,254,903 noncore candidates, 402 were blacklisted; the last
  retained fresh coordinate is 2,574,933.

The run took 41.32 seconds and 182,714,368 bytes peak RSS (about 174.25 MiB),
within the authorized 60-second/384-MiB limit. The degree argument excludes
all nonbanks and no exhaustive quadratic decoder is required.

## Stable small instance

`pilot_d2.json` records the monic degree-13 fresh polynomial, primitive root,
Sidon exponents, deterministic fresh-domain rule, and exact owner histogram.

- Prime p=1,000,003; bank size L=293; message dimension 3.
- Core n0=85,556; fresh t=86,143; total n=171,699.
- Both source and common agreement A=584; threshold T=586; gap d=2.
- Canonical singleton labels: 369,518; canonical nonempty labels: 643,471.
- After changing endpoints to f and f+g, the extra infinity parameter gives
  **369,519 singleton labels** and **643,472 nonempty labels**.
- All nonbank quadratic agreements are at most L+13=306, uniformly in labels.
- T²=343,396<2n=343,398. The low-rate first-order bound is less than
  sqrt(3n/2)+(3n/8)^(1/4)<508+16=524<T.

The bank is P_i(X)=X²/a_i²+a_i². Its core consists of the distinct points
±a_i a_j, assigned their common bank value. The direction g is zero on the
core and X³ on fresh coordinates. The fresh received word is the saved monic
h(X). On fresh coordinates, h is forbidden to equal any P_i or P_i−X³.
Coordinates are retained in increasing integer order until there are t.

The program counts hits separately for each bank polynomial. A label's owner
counter increases exactly when that bank reaches d hits. It is not an
incidence-occupancy approximation. The owner histogram is the exact finite
threshold-list-size histogram because all nonbank witnesses are harmless.

For any nonbank quadratic Q, its core agreement is at most L and the fresh
equation h+lambda X³−Q has degree exactly 13. This proves the nonbank cap
without a polynomial decoder. It also covers extension-field witnesses:
three matched prime-field coordinates force any quadratic witness to have
prime-field coefficients. The usual direction argument proves common
agreement A, and blacklisting fixes both endpoint agreements at A.

## Runtime and reproducibility

The original run took 0.957 seconds internally, 1.24 seconds wall time,
and 11.1 MB peak RSS. Updating hit histograms incrementally avoids scanning
every label for each bank. The optimized replay took 0.241 seconds and
matched every exact output field, including the fresh-domain hash.
The two receipts and resource logs are retained separately.

Build on the current Mac toolchain:

```sh
clang++ -O3 -std=c++17 -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk pilot.cpp -o pilot
./pilot 293 1000003 2 20260918
```

The gap-three run processed 3,381,751,500 retained bank-coordinate incidences.
`verify.cpp` is a separately structured checker: it forms core nodes from
direct products, obtains inverses by batch inversion rather than a field-wide
inverse table, rewrites each label as an affine combination of 1/x and 1/x³,
processes banks in reverse order, and updates owner counters only after each
bank's complete histogram has been formed. It does not call or import the
generator. `prepare_verify.py` copies only the numerical certificate input to
a C++ header. `run_bounded.py` enforces 60 seconds and 384 MiB on the entire
replay process group.

To reproduce the larger replay and all receipt comparisons:

```sh
python3 prepare_verify.py pilot_d3.json
clang++ -O3 -std=c++17 -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk verify.cpp -o verify
python3 run_bounded.py verify_d3 ./verify
python3 compare_verify.py
```
