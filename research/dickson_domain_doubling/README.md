# First quadratic-extension domain-doubling test

September 17, 2026. Complete finite result, not an asymptotic statement.

Over F_(17^2)=F17[T]/(T^2-3), take the32 distinct roots of X^32-1 and
W=(X^8-1)^2/2. For degree-<8 polynomials the maximum agreement is exactly12.
Thus doubling the F17 source domain and dimension in this case preserves
the3/8 agreement fraction; it does not improve it. The characteristic17
still exceeds the message degree7. The family remains below the
quarter-rate first-order curve.

A lower witness is P=9+16X^2+7X^4+2X^6, obtained by composing a known
F17 witness with X^2. It agrees on12 of32 points.

For the upper bound suppose a degree-<8 nonconstant polynomial has at
least13 agreements. W is constant on each of four mu_8 cosets, with four
distinct values. Some coset contains at least4 matches. There are at most7
matches in that coset by the root bound, leaving at least6 outside.
Choose4 matches in the coset, with locator Z. Then P=v+ZQ with deg Q<4.
The chosen four-subset can be rotated to one of10 representatives of the
70 four-subsets under mu_8. Four outside matches determine Q. Enumerating
all four cosets,10 representatives, and binomial(24,4) outside supports
therefore covers every candidate with13 or more agreements.

`scan.cpp` completes all425,040 determining supports and finds none.
Its early termination condition only discards candidates whose current
agreement plus every remaining coordinate is less than13. The field
operations use exact tables; all nonzero inverse identities are asserted.
The independent Python replay uses coefficient tuples, verifies field
irreducibility, all288 inverse identities, the complete domain, the lower
witness, and the anchor orbit cover. The upper bound relies on the completed
C++ enumeration, not on witness checks alone.

Compile as C++17 with -O2 and assertions enabled; the local run used the
Zig wrapper targeting aarch64-macos.14.0. Run sequentially under the384MiB,
60-second repository watchdog. Logs, resource reports, and verifier are
stored alongside the sources. This result does not establish a general
nearestness-preservation theorem under polynomial composition, nor exclude
other domain enlargements.
