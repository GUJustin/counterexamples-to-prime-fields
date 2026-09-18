#!/usr/bin/env python3
"""Independent all-triples replay of selected small prime-field RS(3) cores."""
import hashlib
import json
import math
from collections import Counter
from itertools import combinations
from pathlib import Path
from time import monotonic

HERE = Path(__file__).resolve().parent


def matrix_rank(rows, p):
    rows = [list(row) for row in rows]
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][col], -1, p)
        rows[rank] = [v*inverse % p for v in rows[rank]]
        for i in range(len(rows)):
            if i != rank:
                factor = rows[i][col]
                rows[i] = [(a - factor*b) % p for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def primitive_root(p):
    value, factors, divisor = p - 1, set(), 2
    while divisor*divisor <= value:
        while value % divisor == 0:
            factors.add(divisor)
            value //= divisor
        divisor += 1
    if value > 1:
        factors.add(value)
    return next(g for g in range(2, p) if all(pow(g, (p-1)//d, p) != 1 for d in factors))


def replay(row):
    p, e = row["p"], row["e"]
    domain, word = list(range(p)), [pow(x, e, p) for x in range(p)]
    inverse = [0] + [pow(x, -1, p) for x in range(1, p)]
    determined = Counter()
    for x, y, z in combinations(domain, 3):
        xy_slope = (word[y] - word[x])*inverse[y-x] % p
        xz_slope = (word[z] - word[x])*inverse[z-x] % p
        a = (xz_slope - xy_slope)*inverse[z-y] % p
        b = (xy_slope - a*(x+y)) % p
        c = (word[x] - a*x*x - b*x) % p
        determined[(a, b, c)] += 1
    counts_to_agreement = {math.comb(a, 3): a for a in range(3, p+1)}
    agreement = {coeff: counts_to_agreement[count] for coeff, count in determined.items()}
    hist = Counter(agreement.values())
    hist[2] = math.comb(p, 2)*p - sum(math.comb(a, 2)*count for a, count in hist.items())
    hist[1] = p**3 - sum(a*count for a, count in hist.items())
    hist[0] = p**3 - sum(hist.values())
    hist = {a: count for a, count in hist.items() if count}
    assert hist == {int(a): count for a, count in row["histogram"].items()}
    full_hist = Counter(a for coeff, a in agreement.items() if all(coeff))
    expected_full = {int(a): count for a, count in row["full_coefficient_histogram"].items() if int(a) >= 3}
    assert dict(full_hist) == expected_full
    return domain, word, agreement


def bank_record(p, e, domain, word, agreement, threshold, full_only):
    bank = sorted(coeff for coeff, a in agreement.items() if a >= threshold and (all(coeff) or not full_only))
    assert bank
    supports = [[x for x in domain if (a*x*x+b*x+c-word[x]) % p == 0] for a,b,c in bank]
    assert all(len(support) == agreement[coeff] for coeff, support in zip(bank, supports))
    ownership = [sum(x in support for support in supports) for x in domain]
    assert sum(ownership) == sum(map(len, supports))
    g = primitive_root(p)
    multipliers = [pow(g, e-j, p) for j in (2,1,0)]
    remaining, orbits = set(bank), []
    while remaining:
        seed, orbit = min(remaining), []
        current = seed
        while not orbit or current != seed:
            assert current in remaining
            remaining.remove(current)
            orbit.append(current)
            current = tuple(a*b % p for a,b in zip(current, multipliers))
        assert (p - 1) % len(orbit) == 0
        orbits.append({"representative_coefficients_descending": seed, "size": len(orbit)})
    return {
        "p": p, "e": e, "domain": domain, "received_word": word,
        "coefficient_order": "quadratic, linear, constant", "all_coefficients_nonzero": full_only,
        "threshold": threshold, "bank_size": len(bank), "bank_coefficients": bank,
        "supports": supports, "bank_agreement_histogram": dict(Counter(map(len, supports))),
        "coordinate_ownership": ownership, "ownership_histogram": dict(Counter(ownership)),
        "augmented_coefficient_rank": matrix_rank([list(coeff)+[1] for coeff in bank], p),
        "L_over_sqrt_n": len(bank)/math.sqrt(len(domain)),
        "minimum_agreement_over_sqrt_n": min(map(len, supports))/math.sqrt(len(domain)),
        "maximum_ownership": max(ownership), "coordinates_with_at_least_three_owners": sum(a >= 3 for a in ownership),
        "primitive_generator": g, "multiplicative_orbits": orbits}


def main():
    started = monotonic()
    rows = [json.loads(line) for name in ("p31.jsonl", "p43_p61_p101.jsonl")
            for line in (HERE/name).read_text().splitlines()]
    assert len(rows) == 224
    indexed = {(row["p"],row["e"]): row for row in rows}
    balanced = [(31,5),(31,6),(43,6),(43,7),(61,6),(61,10),(101,10)]
    full_candidates = [(31,6),(43,20),(61,9),(101,37)]
    extra_fixed_degree = [(101,6)]
    chosen = sorted(set(balanced + full_candidates + extra_fixed_degree))
    records, replay_summary = [], []
    for key in chosen:
        row = indexed[key]
        domain, word, agreement = replay(row)
        record = bank_record(*key, domain, word, agreement, row["maximum"], False)
        record["selection_reason"] = "balanced factor" if key in balanced else "selected complete nearest list"
        records.append(record)
        if key in full_candidates:
            full = bank_record(*key, domain, word, agreement, row["full_coefficient_maximum"], True)
            full["selection_reason"] = "full-coefficient rich bank"
            records.append(full)
        replay_summary.append({"p": key[0], "e": key[1], "triples_reconstructed": math.comb(key[0],3),
                               "complete_histogram_matches": True, "full_coefficient_histogram_ge3_matches": True})
    threshold_maxima = []
    for p in (31,43,61,101):
        subset = [row for row in rows if row["p"] == p]
        for j in range(3):
            best = max(row["threshold_profiles"][j]["list_size"] for row in subset)
            winners = [row["e"] for row in subset if row["threshold_profiles"][j]["list_size"] == best]
            example = subset[0]["threshold_profiles"][j]
            threshold_maxima.append({"p": p, "A": example["A"],
                                    "c_numerator": example["c_numerator"], "c_denominator": example["c_denominator"],
                                    "maximum_list_size": best, "attaining_exponents": winners,
                                    "L_over_sqrt_n": best/math.sqrt(p)})
    encoded = (json.dumps(records, indent=2)+"\n").encode()
    (HERE/"selected_banks.json").write_bytes(encoded)
    summary_records = [{key: value for key, value in record.items()
                        if key not in ("domain","received_word","bank_coefficients","supports","coordinate_ownership")}
                       for record in records]
    output = {"status": "PASS: bounded full-field census and independent all-triples selected replay",
              "profile_count": len(rows), "prime_exponent_counts": dict(Counter(row["p"] for row in rows)),
              "threshold_maxima": threshold_maxima, "selected_bank_summaries": summary_records,
              "independent_replays": replay_summary,
              "selected_banks_sha256": hashlib.sha256(encoded).hexdigest(),
              "scope": "Fixed small fields only; no asymptotic scaling or finite DKT placement claim.",
              "elapsed_seconds": monotonic()-started}
    (HERE/"verification.json").write_text(json.dumps(output,indent=2)+"\n")
    print(json.dumps(output,indent=2))


if __name__ == "__main__":
    main()
