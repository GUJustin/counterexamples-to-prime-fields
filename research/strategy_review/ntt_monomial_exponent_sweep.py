"""Exact character-dimension gate; no field/contact matrices or ranks.

Run with /Users/jthaler/.local/share/research-toolchain/venv/bin/python.
Stops at the first exponent passing the NECESSARY dimension condition.
"""
import hashlib
import csv
import json
from pathlib import Path
import resource
import struct
import sys
import time

import numpy as np

N, WCODE, CAP, Q, S, M = 262144, 131071, 20846625, 159, 35, 115
FIRST, LAST = 181275, 211940
RANK_CEILING = sum(
    max(M - max(0, q - S) - 2 * k, 0)
    for q in range(Q + 1) for k in range(min(q, S) + 1)
)
PAIRS = np.array([(q, j) for q in range(Q + 1)
                  for j in range(min(S, q) + 1)], dtype=np.int64)
T, J = PAIRS[:, 0], PAIRS[:, 1]
DEGREES = np.arange(Q + 1, dtype=np.int64)
UPPER_MULT = np.minimum(DEGREES, S) + 1
DELTAS = np.concatenate((np.ones(len(T), dtype=np.int64), -UPPER_MULT))
SOURCE_COLUMNS = sum(CAP - WCODE * q + j for q, j in PAIRS.tolist())


def profile(a):
    lower = (a * T - J) % N
    upper = (CAP + (a - WCODE) * DEGREES) % N
    initial = int(np.maximum(
        0, (CAP - 1 + (a - WCODE) * T) // N
        - (a * T - J + N - 1) // N + 1
    ).sum())
    keys = np.concatenate((lower, upper))
    active = keys != 0
    keys, deltas = keys[active], DELTAS[active]
    order = np.argsort(keys, kind="stable")
    keys, deltas = keys[order], deltas[order]
    starts = np.r_[0, np.flatnonzero(keys[1:] != keys[:-1]) + 1]
    endpoints = np.r_[0, keys[starts], N]
    counts = np.r_[initial, initial + np.cumsum(np.add.reduceat(deltas, starts))]
    lengths = np.diff(endpoints)
    assert int(np.dot(lengths, counts)) == SOURCE_COLUMNS
    top = int(np.argmax(counts))
    return {
        "a": a,
        "min_columns": int(counts.min()),
        "max_columns": int(counts[top]),
        "first_max_character": int(endpoints[top]),
        "forced_kernel_characters": int(lengths[counts > RANK_CEILING].sum()),
        "Z_free_nullity_lower_bound": int(np.dot(
            lengths, np.maximum(counts - RANK_CEILING, 0))),
    }


def main():
    start = time.monotonic()
    digest = hashlib.sha256()
    best = None
    improvements = []
    ties = 0
    processed = 0
    survivor = None
    status = "complete"
    witness_path = Path(__file__).with_name("ntt_monomial_exponent_witnesses.csv")
    witness_file = witness_path.open("w", newline="")
    witnesses = csv.writer(witness_file)
    witnesses.writerow(["a", "character", "columns"])
    for a in range(FIRST, LAST + 1):
        if time.monotonic() - start > 60:
            status = "timeout"
            break
        row = profile(a)
        witnesses.writerow([a, row["first_max_character"], row["max_columns"]])
        processed += 1
        digest.update(struct.pack("<6q", *row.values()))
        if best is None or row["max_columns"] < best["max_columns"]:
            best = row
            ties = 1
            improvements.append(row)
        elif row["max_columns"] == best["max_columns"]:
            ties += 1
        if row["max_columns"] <= RANK_CEILING:
            survivor = row
            status = "necessary_gate_survivor"
            break
    witness_file.close()
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = rss if sys.platform == "darwin" else 1024 * rss
    result = {
        "scope": "character dimensions only; no matrices or ranks",
        "status": status,
        "first_exponent": FIRST, "last_exponent": LAST,
        "processed": processed, "local_rank_ceiling": RANK_CEILING,
        "Z_free_source_columns": SOURCE_COLUMNS,
        "minimum_max_columns_record": best, "minimizer_count_in_processed_range": ties,
        "record_improvements": improvements, "necessary_gate_survivor": survivor,
        "all_processed_records_sha256": digest.hexdigest(),
        "seconds": time.monotonic() - start, "peak_rss_bytes": rss_bytes,
        "numpy_version": np.__version__,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "witness_csv": witness_path.name,
        "witness_csv_sha256": hashlib.sha256(witness_path.read_bytes()).hexdigest(),
    }
    target = Path(__file__).with_suffix(".json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "record_improvements"}, indent=2))


if __name__ == "__main__":
    main()
