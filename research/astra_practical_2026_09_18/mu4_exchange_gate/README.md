# Exact four-packet modular exchange gate

September 18, 2026. Bounded positive-search test at the actual benchmark prime p=2130706433, completed locally. No random search or rental.

Take supports consisting of four whole mu4 cosets inside mu256, avoiding the coset containing1. Their tags are four-subsets of mu64 minus1. There are C(63,4)=595665 such supports, each containing16 roots.

For a mu4 coset tagged by a, its moments of orders1,2,3,5,6 vanish, its fourth moment is4a, and its root product is -a. Therefore two four-packet supports have equal six-moment-plus-product signatures exactly when their tag sums and tag products agree. The test enumerates ALL595665 tag subsets, computes the key `(sum mod p, exponent-sum mod64)`, and sorts. This is exhaustive for this structured family only.

`gate.cpp` uses primitive generator3 and tag root1548376985. Its memory is one vector of16-byte records (about9.6 MB), plus negligible sorting stack. Build with the available MacOSX15.4 SDK; the default installed SDK had an incompatible linker metadata format. The successful build and run together took under one second.

## Result

`result.json` records:

- 3150 unordered equal-signature pairs;
- all3150 pairs have disjoint tag supports;
- zero genuinely characteristic-specific pairs;
- maximum signature fiber15.

To distinguish modular from lifted collisions, write the difference of tag indicator vectors d_j. Equality over Q(zeta64) holds iff d_j=d_(j+32), by Phi64=X32+1. The code checks this exact signed condition for every collision, not merely numerical complex approximations. Every collision passes it.

An independent small integer count confirms3150: a disjoint lifted exchange must consist of two opposite-tag pairs on either side. There are31 available opposite pairs; group their two-element subsets by exponent sum modulo32. The product-fiber sizes are15 in17 classes and14 in15 classes. Hence the collision count is17*C(15,2)+15*C(14,2)=3150. Distinct members of one such product class cannot share an opposite pair. This independently reproduces both the pair count and disjointness.

## Exact completion contribution

These pairs certify6300 ordered t=16 exchanges in the original255-root problem. Their weighted collision contribution is

    6300*C(223,120).

`contribution.json` computes it exactly and compares it with the sufficient target

    C(255,136)*(274980728111395088-1)+1.

The contribution is about2^(-77.3311) of that target. Dividing by C(255,136), its contribution to the second-moment lower bound on a fiber is only0.000001446535..., not a useful count increase. These are already lifted packet exchanges, so this is not a new source of the baseline's large modular concentration.

## Scope and next discriminator

This test does not enumerate all t16 exchanges, all t8 exchanges, or larger packet exchanges. It closes only the smallest four-mu4-packet route capable of satisfying the reduced sum/product constraints. A larger test should be justified by a mechanism producing genuinely modular collisions and a completion-weight estimate; merely finding a few low-t exchanges would not approach the missing factor four. No additional scan is recommended solely on this negative gate.
