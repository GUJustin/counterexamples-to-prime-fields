# Complete nearest-list census over F41

September 17, 2026. For the word

    W(x)=(1+x^20)/2-x^10, x in F41*,

among polynomials of degree less than10, the maximum agreement is exactly15.
Exactly210 polynomials attain it, forming21 multiplicative orbits of size10.
This upgrades the earlier sampled210-element bank to a complete nearest
list. It does not prove the analogous maximum3k/2 for unbounded k.

## Why the enumeration is complete

Let g=6, a primitive root of F41. The four cosets
C_c={g^(c+4j): 0<=j<10}, c=0,...,3, each have10 points; W is constant
on each, with four distinct values. Every constant polynomial therefore
has at most10 agreements.

Suppose a nonconstant degree-<10 polynomial P has at least15 agreements.
Some coset C_c contains at least4 of them. In any one coset P can agree
at most9 times, by applying the root bound to P minus the constant
received value v_c. There are therefore at least6 agreements outside C_c.

Choose four agreements A in C_c. Multiplication of the input by an element
of mu_10 preserves W and rotates the ten positions within each coset.
The210 four-subsets of a coset form22 rotation orbits. After such a
rotation, A is one of the22 canonical representatives used by the scanner.
For its locator Z_A we necessarily have

    P = v_c + Z_A Q, deg Q < 6.

On the30 points outside C_c, Q must agree with (W-v_c)/Z_A in at least6
places. Every such Q is determined by some six-subset of these30 points.
The scanner interpolates all binomial(30,6)=593,775 choices for each
anchor representative, tests all relevant remaining agreements, and
retains every candidate reaching15. Early termination of a candidate
only occurs when its current count plus ALL untested coordinates is
less than15. It then restores all ten rotations of every retained word.
The four cosets exhaust all possible candidates with at least15 agreements.

Total determining supports: 4*22*593775=52,252,200. No candidate reaches16.
The union consists of210 distinct evaluation vectors. The independent
Python replay interpolates each from its first ten values and verifies
all40 coordinates, its15 agreements, and the complete orbit decomposition.
It separately enumerates the four-subset orbit cover and checks all
support counts. The completeness assertion uses the covering argument
above together with the completed C++ enumeration, not witness checking
alone.

## Files and reproduction

- `bank_scan.cpp`: complete threshold15 census, one coset per invocation.
- `bank_coset{0,1,2,3}.log`: full evaluation banks and watchdog reports.
- `verify.py`, `verification.json`: independent arithmetic replay.
- `threshold_scan.cpp`, `coset{0,1,2}.log`: preliminary threshold16 checks;
  the complete four-coset bank census supersedes them.

Compile with C++17, optimization enabled, assertions retained. The run used
`zig c++ -target aarch64-macos.14.0 -std=c++17 -O2 -UNDEBUG` and output
`tmp/dickson-nearest-bank`. Invoke it with one argument c=0,1,2,3,
sequentially under the repository's384MiB/60-second watchdog; store each
stdout in its corresponding bank_coset log. Run `verify.py` after all four
complete. Each census used under2MiB measured process-group RSS and less
than11 seconds. No floating-point arithmetic enters either implementation.
