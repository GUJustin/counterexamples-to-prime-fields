# Exact q127, all six cyclic difference-set source families

Dependencies: Python3.10+, sympy==1.14.0, gmpy2. No other project files.

    python3 -m venv venv
    venv/bin/pip install sympy==1.14.0 gmpy2

The independent multiplier census supplies80 normalized target difference
sets in6 unit-equivalence classes. Source class4 is the native Singer
support, source class5 is Paley QR; classes0,1,2,3 are distinct additional
families. See source_mapping.json. Source received support is always
S=complement(−D), not D itself. The six target representative indices are
0,1,2,3,4,36 (NOT0..5).

The adapter regression source4,target4 matches the earlier native Singer
h95,target1 exact computation, including source coefficients and gcd1.
It completed in22.3sec/76MiB locally. The bounded script checkpoints each
completed target. A per-job90s/512MiB guard is in run_one.sh; change the
seconds limit if desired before deployment. This does not replace the
rental's external hard-deadline shutdown.

Priority36 jobs (one representative target per family, each source):

    xargs -P8 -n2 ./run_one.sh < priority36.tsv

After reviewing timing, remaining444 relative orientations:

    xargs -P8 -n2 ./run_one.sh < remaining444.tsv

The36 priority jobs are NOT a complete family classification: relative
unit-multiplier orientations matter. All480 completed negative jobs are
needed to exclude all difference-set support pairs at h95. They still do
not exclude other twists or non-difference-set complementary profiles.

Standalone CLI examples:

    venv/bin/python difference_set127.py --census multiplier_census.json --source-class 4 --target-indices 4 --h 95 --output one.json
    venv/bin/python difference_set127.py --census multiplier_census.json --source-class 0 --target-start 0 --target-stop 80 --h 95 --output family0.json

Target intervals are half-open. --target-indices accepts comma lists.
--h accepts comma lists. --resume skips completed target/twist pairs from
the output JSON; complete:false after a watchdog limit is not success.
Positive valid_degree requires subsequent candidate verification.
A successful negative job has exit0, complete:true, and valid_degree0
for its requested h95,target row.
