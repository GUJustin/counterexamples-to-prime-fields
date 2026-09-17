# Exact local lists via absence of signed relations (development notes)

The relation and histogram checks passed independently. The exact local-list
result is integrated in `finite.tex`; see `../UNIQUE_PROOF_AUDIT.md`.

For n62,K31,D16, a nearby codeword must match both padding positions
and exactly32 core coordinates, by saturation of the two-coordinate bound.
Thus H=w-Q is the monic locator of a32-element core subset. Since Q has
degree<=30, its root sum is zero. Matching both±1 also givesH(1)=H(-1).

Cancel the core sign-orbits whose two elements are roots ofH. The remaining
single roots correspond to a nonzero ternary vector epsilon in{-1,0,1}^30.
Its sum is sum epsilon_i a_i=0. Its count is even becauseHdegree32 iseven.
Writing R_i=(1-a_i)/(1+a_i), the padding equality says
 prod R_i^epsilon_i=1.
Therefore, if the only ternary vector mapping to(0,1) inFp x Fp* is zero,
ALL nearby codewords are exactly the paired locators already enumerated.

This relation check is feasible by meeting two halves of15variables:
3^15=14,348,907 keys each, encoded in62bits, total219MiB. The sets are
closed under inversion; their intersection should consist only of the
single empty key. Sorted multiplicities handle any internal duplicate keys.
No independence/randomness is needed after exact replay.

If the check passes, compute the full product-fiber histogram with a byte
counter array for one eighth ofFp at a time (256MiB), rescan all145million
supports eight times, and assert no byte overflows. This gives exact local
list sizes, uniquely nearby count, and total nearby count. The histogram
can be checked against the independent bitmap image count and total support
count. This does not establish a global maximum list size over all received
words. Do not promote until relation and histogram replays pass.
