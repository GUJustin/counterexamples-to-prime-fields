"""Exact conditional integer moments; no finite-field or protocol operations."""
from math import comb
from pathlib import Path
import json
import time


def moments(n, t, qmax, degree):
    rows = [{} for _ in range(t + 1)]
    rows[0][0] = [1] + [0] * degree
    updates = 0
    for a in range(n):
        b = comb(a, 2)
        shift = [[comb(r, j) * b ** (r-j) for j in range(r+1)]
                 for r in range(degree+1)]
        for size in range(min(t, a+1), 0, -1):
            for q, old in rows[size-1].items():
                target = q + a
                if target > qmax:
                    continue
                added = [sum(coef * old[j] for j, coef in enumerate(line))
                         for line in shift]
                current = rows[size].get(target)
                rows[size][target] = added if current is None else [
                    x+y for x, y in zip(current, added)]
                updates += 1
    return rows[t], updates


def centered(raw, center):
    return [sum(comb(r, j) * (-center)**(r-j) * raw[j]
                for j in range(r+1)) for r in range(len(raw))]


if __name__ == '__main__':
    start = time.perf_counter()
    rows, updates = moments(64, 34, 1071, 20)
    raw = rows[1071]
    result = dict(n=64, t=34, q=1071, center=22138, degree=20,
                  raw_moments=raw, centered_moments=centered(raw, 22138),
                  updates=updates, seconds=time.perf_counter()-start)
    Path(__file__).with_name('exact_moments.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
