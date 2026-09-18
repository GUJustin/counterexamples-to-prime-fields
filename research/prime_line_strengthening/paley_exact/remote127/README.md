# Exact q127 Singer natural-twist jobs

Self-contained arithmetic script: singer127.py. Dependencies: Python3.10+
and SymPy1.14.0. Local timing used gmpy2-backed rationals; install gmpy2 for
comparable speed. No Sage, project modules, input files, network, or
numerical embeddings are used. run_bounded.py uses only Python stdlib.

Suggested environment:

    python3 -m venv venv
    venv/bin/pip install sympy==1.14.0 gmpy2

Target representatives:

    1 3 5 7 9 11 13 15 19 21 23 27 29 31 43 47 55 63

Each target is one Singer multiplier class. A complete h95 run covers18
classes. Local firstthree targets1,3,5 already have raw gcd1, but rerunning
independently is inexpensive. One target takes about16 seconds plus2.4
seconds setup locally, with peakRSS121MiB. The CLI accepts a comma list
of targets (`--targets 7,9,11`) and twists (`--h 95,96`); omitted targets
means all18. `--resume` skips completed target/twist pairs already in the
specified output JSON. Each completed target is checkpointed immediately;
`complete:false` after timeout is intentionally not a completed theorem.

Single job, hard60seconds/512MiB:

    venv/bin/python run_bounded.py --rss-mib 512 --seconds 60 --report out/h95_t7.resources.json -- venv/bin/python singer127.py --h 95 --targets 7 --output out/h95_t7.json

Eight independent workers (create out first):

    printf '%s\n' 1 3 5 7 9 11 13 15 19 21 23 27 29 31 43 47 55 63 | xargs -P8 -I{} sh -c 'venv/bin/python run_bounded.py --rss-mib 512 --seconds 60 --report out/h95_t{}.resources.json -- venv/bin/python singer127.py --h 95 --targets {} --output out/h95_t{}.json > out/h95_t{}.log 2>&1'

Alternatively, one process under a10minute/2GiB guard:

    venv/bin/python run_bounded.py --rss-mib 2048 --seconds 600 --report out/h95_all.resources.json -- venv/bin/python singer127.py --h 95 --output out/h95_all.json

Success means exit0, complete:true, and the requested target/twist row(s)
present. A positive valid_degree requires further algebraic witness and
bank-distinctness checks; it is not automatically a construction. A
negative valid_degree=0 is an exact exclusion for that support pair.
No all-h or all-difference-set-family claim follows from h95 Singer jobs.
