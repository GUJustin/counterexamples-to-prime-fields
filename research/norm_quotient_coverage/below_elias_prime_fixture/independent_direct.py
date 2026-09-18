"""Replay every fixed-cardinality product without discrete logarithms."""
from array import array
from itertools import combinations
from pathlib import Path
import json
import struct
import time

folder = Path(__file__).resolve().parent
tags = json.loads((folder / "canonical_tags.json").read_text())["tags"]
p = 65537
factors = [(3-a) % p for a in tags]
counts = array("I", [0]) * p
start = time.monotonic()
for support in combinations(range(len(tags)), 13):
    value = 1
    for i in support:
        value = value * factors[i] % p
    counts[value] += 1
assert counts[0] == 0 and all(counts[1:])
assert sum(counts) == 1144066
# Producer bins are indexed by logarithm base 3; replay bins are field values.
producer = struct.unpack("<65536I", (folder / "product_counts_u32le.bin").read_bytes())
value = 1
for multiplicity in producer:
    assert counts[value] == multiplicity
    value = value * 3 % p
result = {
    "status": "PASS",
    "method": "direct field multiplication of every 13-subset; no logarithms",
    "subsets": sum(counts),
    "min_multiplicity": min(counts[1:]),
    "max_multiplicity": max(counts),
    "missing_nonzero_products": 0,
    "all_producer_counts_match": True,
    "elapsed_seconds": time.monotonic() - start,
}
(folder / "independent_direct.verified.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result))
