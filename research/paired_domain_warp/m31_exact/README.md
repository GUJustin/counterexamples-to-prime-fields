# Deterministic M31 banks and exact local lists

Four paired-coordinate domains over `2^31-1` are stored in `instances.json`.
`verify.py` compiles two independent C++17 subset-product enumerators, compares
their counts, verifies the integer inequalities and distances, and recovers
explicit witnesses. The largest replay uses about285MiB and all four rows
run sequentially in about a minute on the restored laptop.

For n62,K31, `verify_local_lists.py` additionally excludes every nonpaired
nearby polynomial, using the signed-relation criterion in `../unique.tex`.
It then computes the complete local-list histogram by two independent methods.
There are exactly140,916,078 nearby parameters;136,494,714 are uniquely nearby;
the maximum list size on this line is5. The unique count alone exceeds the
prescribed bound below103,199,661. These are not global list-size bounds.

The relation check uses two sorted ternary half-images with3^15 keys each.
The histogram replays use one field segment at a time, keeping memory below
384MiB. No bitmap or large dataset needs to be retained. The small fingerprint
in the count records is a noncryptographic debugging check, not a proof hash.
