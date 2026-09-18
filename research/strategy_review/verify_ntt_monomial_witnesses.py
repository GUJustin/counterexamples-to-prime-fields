"""Independently count ORIGINAL source exponents; no event/ceil-bound logic."""
import csv
import hashlib
import json
from pathlib import Path
import time

import numpy as np

start = time.monotonic()
base = Path(__file__).parent
path = base / "ntt_monomial_exponent_witnesses.csv"
n, w, W, rank_ceiling = 262144, 131071, 20846625, 182580
pairs = np.array([(i, j) for j in range(36)
                  for i in range(160 - j)], dtype=np.int64)
i, j = pairs[:, 0], pairs[:, 1]
d_lengths = W - w * i - (w - 1) * j
checked = 0
minimum_witness = None
for row in csv.DictReader(path.open()):
    a, character, claimed = (int(row[k]) for k in ("a", "character", "columns"))
    assert a == 181275 + checked
    assert 0 <= character < n
    residue = (character - a * i - (a - 1) * j) % n
    actual = int(np.maximum(0, 1 + (d_lengths - 1 - residue) // n).sum())
    assert actual == claimed and actual > rank_ceiling, (a, character, claimed, actual)
    if minimum_witness is None or actual < minimum_witness["columns"]:
        minimum_witness = {"a": a, "character": character, "columns": actual}
    checked += 1
assert checked == 30666
result = {
    "status": "PASS", "checked_exponents": checked,
    "scope": "one exact oversized character in original source coordinates for every remaining exponent",
    "minimum_recorded_witness": minimum_witness,
    "seconds": time.monotonic() - start,
    "witness_csv_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
    "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
