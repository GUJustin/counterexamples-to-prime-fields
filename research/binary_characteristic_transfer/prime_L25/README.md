# Exact prime-field instance: n=1201, K=3

The certificate uses the prime **2,000,003**, with L=25 bank quadratics, 600 core nodes and 601 fresh nodes. Both individual source agreements and common agreement are 48. At threshold 49 there are exactly **15,026 nonzero bad challenges**, each with a singleton list.

Files:

* `generate.py`: deterministic standard-library generator; starts just above 2,000,000 and verifies primality by trial division.
* `certificate.json`: 377,524-byte compact field/domain/source/label/witness certificate.
* `check.py`: separate replay implementation, using independently sieved primes, Horner evaluation and direct modular reconstruction. It does not import the generator.
* `verified.json`: PASS receipt, including 736,225 checked designated witness equations.
* `generate.resources.json`, `check.resources.json`: bounded-run receipts, each below 0.6 seconds under 60 seconds/384 MiB. Their RSS numbers are the runner's sampled values, not an exact process high-water measurement.

The first 25 primes a_i define P_i=X²/a_i²+a_i². Pair intersections are ±a_i a_j. Every core coordinate is explicitly checked to match exactly its designated two bank quadratics, and every bank has 48 core matches.

The certificate stores the **final both-far sources**. On the core both equal the intersection word; on fresh coordinates they are x⁴ and x⁴+x³. Each finite label row is

    [canonical_label, final_label, bank_index, fresh_index].

The designated witness coefficient vector, in increasing degree order, is

    (1+final_label) * bank_coefficients[bank_index] modulo p.

The additional label p-1 has witness 0 and exactly 600 matches. There are 15,025 finite rows; the corresponding canonical labels are all distinct and avoid 0,1.

## Why the verification is complete without enumerating p³ quadratics

Every non-bank quadratic has at most 25 core matches: each core match contributes two intersections with bank quadratics, while each of 25 nonzero quadratic differences contributes at most two. It has at most four fresh matches on a canonical line word, because the fresh residual is a quartic with nonzero leading coefficient. Thus it has at most29<49 total matches. Global distinctness of the bank/fresh labels ensures each incumbent gets at most one fresh match. This proves exact finite-label supports and singleton lists.

At the extra label, the word is zero on the core and -x³ on the fresh set. Any nonzero quadratic has at most two core and three fresh matches; only zero reaches 49, with 600 matches. The same degree bound applied to the difference of simultaneous source witnesses proves common agreement at most 48. Taking the same bank quadratic for both sources attains 48 on the core. The excluded canonical labels 0,1 and the degree bounds likewise prove both individual source agreements are exactly 48.

The checker also independently reconstructs the finite first-order support counts: m=4, derivative cap 2, total cap 98, challenge cap 4704, coefficient count 28812, local layers 3,6,8,6. It verifies 49²=2·1201-1 and the exact finite counting budget.

Certificate SHA256:

    9e93845cc51689c298e30631e625531420ed0bf61aea2a46a002a12c2fcd2522

Reproduce from the repository root with `python3 research/binary_characteristic_transfer/prime_L25/generate.py`, then `python3 research/binary_characteristic_transfer/prime_L25/check.py`. The bounded wrapper command is recorded verbatim in each resource receipt.
