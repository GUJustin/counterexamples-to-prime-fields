# Bounded dependent-incidence pilot: all 24 prescribed seeds obstructed

September 17, 2026. This executes the finite feasibility gate proposed
in strategy_review/STRATEGY_PRIME_FIELDS_2026_09_17.md. The stopping rule
was fixed before the run: 24 patterns, at most two deeper analyses if
compatible, and no larger random census after universal failure.

The source is the complete 210-member nearest bank over F41 for the
40-node Dickson word, dimension 10 and maximum agreement 15. Every
pattern contains 16 distinct candidates and at least one candidate
outside the original twenty-member Dickson subbank. There are eight
broad seeded samples, eight greedily overlap-clustered patterns, and
eight greedily balanced-incidence patterns. They are all distinct.
The selection algorithm and seed are recorded in pilot.py.

At these parameters L*eta=16*(5/40)=2, exceeding the full-row smoothness
threshold 2-rho=1.75. The experiment therefore tests first-order
COMPATIBILITY with dependent equations, rather than expecting full row
rank. Nodes, all candidate coefficients, and received symbols are free;
received values are eliminated by pairwise differences against one
reference at each occupied node. Gauge freedoms are retained in the
matrix because they do not change compatibility. The standard gauge
kernel explains why full rank is impossible, but is not used to infer
an obstruction.

Every one of the 24 first correction systems is inconsistent modulo41.
The reported matrix ranks range from181 to186. Each saved certificate
is a left-kernel vector annihilating every Jacobian column with nonzero
pairing against the canonical mod41² correction residual. The independent
stdlib verifier reconstructs all incidence equations and their residuals,
checks all200 column identities, and confirms all24 nonzero pairings.
It also checks that the reconstructed polynomial bank matches the
existing complete census and every selected candidate has15 agreements.
The rank numbers are generator diagnostics, not needed by the verifier.

The generator completed in2.97 seconds with peak sampled RSS below37MiB.
The independent certificate verifier completed in0.56 seconds. Both used
the384MiB/60-second repository guard. Files results.json and
verification.json contain the full evidence, with resource reports.

These certificates exclude lifts with these prescribed reductions to
Z/41², and corresponding unramified extensions. They do NOT exclude
ramified characteristic-zero lifts, unrelated characteristic-zero
incidence patterns, or all sixteen-candidate subsets of the bank.
Nor do they constitute a general barrier to dependent incidence designs.

No pattern passed, so no higher-order analysis was run and this design
rule is now stopped. Further work should require a new exact syzygy or
construction mechanism, rather than more random subsets of this bank.
