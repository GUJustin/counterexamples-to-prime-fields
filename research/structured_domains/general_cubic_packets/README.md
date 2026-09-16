# Exact complete-fiber maximum for rational cubics on the pinned subgroup

Every degree-three rational map over any extension of F_2130706433 has
at most **three complete three-point fibers** in its 256-element
multiplicative subgroup. Three are attained. This is a computer-assisted
finite theorem; `PROOF.md` explains the exhaustive reduction.

The general search examined 29,715,666,375 pairs across all 10,795
normalized anchors, using 172.1 MiB sampled peak process-group RSS.
The constant-product case separately examines 58,260,615 pairs.
All 85 chunk witnesses were checked in Python. Independent all-pencil
enumerations over F_97 and F_193 agree with both C++ implementations.

Composing a fixed cubic with X^1024 therefore supplies at most three
complete degree-3072 packets on the pinned 262144-point domain. Its
at most eight packet unions cannot supply the required counterexample
bank. This excludes that fixed-map construction route; it does not
improve the score, or exclude varying maps or partial fibers.

## Reproduce

From the repository root, with Python 3 and a C++17 compiler:

```sh
python3 research/structured_domains/general_cubic_packets/verify.py
```

This checks the archive's source hash and disjoint coverage, evaluates
all chunk witnesses, exhausts the small independent fixtures, reruns
the full pinned constant-product search, and checks the strengthened
dyadic coverage arithmetic. It takes about seven seconds on the
recorded machine. To repeat the entire general enumeration as well:

```sh
python3 research/structured_domains/general_cubic_packets/verify.py --full
```

The original general run took about nine minutes, in sequential chunks.
`full_search_resources.json` records its bounded execution; the default
check's report is `check_resources.json`. Sampled RSS can miss brief
peaks. Archived computations supplement, rather than replace, the
proof that the enumerated cases exhaust all coefficient fields.
