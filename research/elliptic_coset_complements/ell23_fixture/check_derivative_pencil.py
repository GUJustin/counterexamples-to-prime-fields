#!/usr/bin/env python3
"""One verified fixture, one pencil, Newton gates only; hard 30-second cap.

No loop over all field labels, no extra-set enumeration, no curve search.
The tested error values are gamma*Phi'(x) on U, gamma=n/deg(U).
"""
import hashlib
import itertools
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import flint
from flint import nmod_poly


ROOT = Path(__file__).resolve().parent
RECEIPT = ROOT / "derivative_pencil_screen.json"
TIME_LIMIT = 30.0
FORECAST_LIMIT = 25.0
EXPECTED_FIXTURE_SHA256 = (
    "208af6edb304ae81f8a35784bd238c2e49095c8381008eeff755c4f31b679de2"
)


class TimeLimit(Exception):
    pass


def stop_for_time(signum, frame):
    raise TimeLimit("30-second computation limit")


def main():
    start = time.monotonic()
    signal.signal(signal.SIGALRM, stop_for_time)
    signal.setitimer(signal.ITIMER_REAL, TIME_LIMIT)
    counters = [
        {
            "extra_degree": d,
            "gates_factored": 0,
            "gate_roots": 0,
            "predicted_J_divides_Phi": 0,
            "coprime_to_base_pair": 0,
            "full_moment_passes": 0,
            "direct_degree_passes": 0,
            "direct_residual_degree_histogram": {},
            "first_failed_moment_histogram": {},
        }
        for d in range(6)
    ]
    hits = []
    unique_labels = set()
    per_degree_labels = [set() for _ in range(6)]
    pair_count = 0
    candidate_digest = hashlib.sha256()
    status = "RUNNING"
    failure = None
    first_pair_seconds = None
    forecast_seconds = None
    setup_seconds = None
    fixture_hash = None

    try:
        raw = (ROOT / "fixture.json").read_bytes()
        fixture_hash = hashlib.sha256(raw).hexdigest()
        assert fixture_hash == EXPECTED_FIXTURE_SHA256
        fixture = json.loads(raw)
        p, ell, n, k, threshold = (
            fixture["p"], fixture["ell"], fixture["n"],
            fixture["k"], fixture["threshold"]
        )
        redundancy = n - k
        assert (p, ell, n, k, threshold, redundancy) == (
            1657, 23, 264, 173, 213, 91
        )
        domain = fixture["domain"]
        assert len(domain) == len(set(domain)) == n
        assert len(fixture["subgroups"]) == 24
        assert p > n > 2 * ell + 5
        one = nmod_poly([1], p)
        zero = nmod_poly([], p)

        Phi = one
        for x in domain:
            Phi *= nmod_poly([-x % p, 1], p)
        f, g = Phi.derivative(), Phi.derivative().derivative()
        assert Phi.degree() == n and f.degree() == n - 1
        assert g.degree() == n - 2
        assert all(int(Phi(x)) == 0 and int(f(x)) != 0 for x in domain)

        powers = {}
        for x in domain:
            values = [1]
            for j in range(1, redundancy):
                values.append(values[-1] * x % p)
            powers[x] = values
        P = [
            sum(powers[x][j] for x in domain) % p
            for j in range(redundancy)
        ]
        H = [0] + [
            (
                sum(P[i] * P[j - 1 - i] for i in range(j))
                - j * P[j - 1]
            ) % p
            for j in range(1, redundancy)
        ]
        # Independent check of all derivative moments from actual word values.
        weighted_g = {
            x: int(g(x)) * pow(int(f(x)), -1, p) % p for x in domain
        }
        direct_H = [
            sum(weighted_g[x] * powers[x][j] for x in domain) % p
            for j in range(redundancy)
        ]
        assert direct_H == H
        assert H[0] == 0 and H[1] == n * (n - 1) % p
        assert P[0] == n

        prepared = []
        for h_index, subgroup in enumerate(fixture["subgroups"]):
            K = nmod_poly(subgroup["K"], p)
            N = nmod_poly(subgroup["N"], p)
            B = nmod_poly(subgroup["B"], p)
            product = K
            fibers = []
            for fiber in subgroup["fibers"]:
                tag = fiber["tag"]
                locator = N - tag * B
                xs = fiber["x"]
                assert len(xs) == ell
                assert locator.degree() == ell and int(locator[ell]) == 1
                assert all(int(locator(x)) == 0 for x in xs)
                product *= locator
                moments = [
                    sum(powers[x][j] for x in xs) % p
                    for j in range(redundancy)
                ]
                fibers.append((tag, locator, moments))
            assert len(fibers) == 11 and product == Phi
            prepared.append((h_index, fibers))
        total_pairs = sum(len(fs) * (len(fs) - 1) // 2 for _, fs in prepared)
        assert total_pairs == 1320
        inv_n = pow(n, -1, p)
        setup_seconds = time.monotonic() - start

        for h_index, fibers in prepared:
            for first, second in itertools.combinations(fibers, 2):
                pair_start = time.monotonic()
                tag_a, F_a, moments_a = first
                tag_b, F_b, moments_b = second
                L0 = F_a * F_b
                assert L0.degree() == 2 * ell
                Q = [(a + b) % p for a, b in zip(moments_a, moments_b)]

                for d in range(6):
                    count = counters[d]
                    u = 2 * ell + d
                    scale = u * inv_n % p
                    gamma = n * pow(u, -1, p) % p
                    # m[0] is the correctly normalized extra-root count.
                    m = [nmod_poly([d], p)] + [
                        nmod_poly(
                            [(scale * P[j] - Q[j]) % p, scale * H[j] % p],
                            p
                        )
                        for j in range(1, d + 2)
                    ]
                    coefficients = [one]
                    for j in range(1, d + 1):
                        acc = zero
                        for i in range(1, j + 1):
                            acc += coefficients[j - i] * m[i]
                        coefficients.append(-pow(j, -1, p) * acc)
                    gate = m[d + 1]
                    for i in range(1, d + 1):
                        gate += coefficients[i] * m[d + 1 - i]
                    A = u * (n - 1) % p
                    leading = (
                        pow(-1, d, p) * pow(A, d + 1, p)
                        * pow(math.factorial(d), -1, p)
                    ) % p
                    assert gate.degree() == d + 1
                    assert int(gate[d + 1]) == leading != 0
                    # FLINT factors only this polynomial of degree at most six.
                    roots = sorted(int(value) for value, mult in gate.roots())
                    assert len(set(roots)) == len(roots) <= d + 1
                    count["gates_factored"] += 1
                    count["gate_roots"] += len(roots)

                    for label in roots:
                        assert int(gate(label)) == 0
                        J = nmod_poly(
                            [int(c(label)) for c in reversed(coefficients)], p
                        )
                        assert J.degree() == d and int(J[d]) == 1
                        item = {
                            "H": h_index, "a": tag_a, "b": tag_b,
                            "d": d, "lambda": label,
                            "J": [int(c) for c in J],
                        }
                        if Phi % J:
                            item["rejection"] = "J does not divide Phi"
                        else:
                            count["predicted_J_divides_Phi"] += 1
                            if J.gcd(L0).degree() != 0:
                                item["rejection"] = "J intersects base pair"
                            else:
                                count["coprime_to_base_pair"] += 1
                                U = L0 * J
                                quotient, remainder = divmod(Phi, U)
                                assert not remainder and U.degree() == u
                                error_poly = gamma * quotient * U.derivative()
                                witness = f + label * g - error_poly
                                degree = witness.degree()
                                degree_key = str(degree)
                                hist = count["direct_residual_degree_histogram"]
                                hist[degree_key] = hist.get(degree_key, 0) + 1
                                extra_roots = sorted(
                                    int(x) for x, mult in J.roots()
                                )
                                assert len(extra_roots) == d
                                assert all(x in powers for x in extra_roots)
                                # Independent all-moment test, using actual roots.
                                first_failure = None
                                for j in range(redundancy):
                                    extra_moment = sum(
                                        powers[x][j] for x in extra_roots
                                    ) % p
                                    required = (
                                        scale * (P[j] + label * H[j]) - Q[j]
                                    ) % p
                                    if extra_moment != required:
                                        first_failure = j
                                        break
                                moments_pass = first_failure is None
                                degree_pass = degree < k
                                assert moments_pass == degree_pass
                                count["full_moment_passes"] += int(moments_pass)
                                count["direct_degree_passes"] += int(degree_pass)
                                item["direct_residual_degree"] = degree
                                item["first_failed_moment"] = first_failure
                                if not degree_pass:
                                    item["rejection"] = "remaining moment/degree"
                                    hist = count["first_failed_moment_histogram"]
                                    key = str(first_failure)
                                    hist[key] = hist.get(key, 0) + 1
                                else:
                                    agreements = sum(
                                        int(witness(x)) == int(f(x) + label*g(x))
                                        for x in domain
                                    )
                                    assert agreements == n - u >= threshold
                                    for x in domain:
                                        expected = (
                                            gamma * int(f(x)) % p
                                            if int(U(x)) == 0 else 0
                                        )
                                        assert int(error_poly(x)) == expected
                                    item["agreements"] = agreements
                                    item["gamma"] = gamma
                                    item["extra_roots"] = extra_roots
                                    item["witness"] = [int(c) for c in witness]
                                    hits.append(item.copy())
                                    unique_labels.add(label)
                                    per_degree_labels[d].add(label)
                        candidate_digest.update(
                            json.dumps(item, sort_keys=True).encode() + b"\n"
                        )

                pair_count += 1
                if pair_count == 1:
                    first_pair_seconds = time.monotonic() - pair_start
                    forecast_seconds = setup_seconds + total_pairs*first_pair_seconds
                    if forecast_seconds > FORECAST_LIMIT:
                        status = "ONE_PAIR_FORMULATION_CHECK"
                        raise TimeLimit("first-pair forecast exceeds 25 seconds")
        assert pair_count == 1320
        assert all(c["gates_factored"] == 1320 for c in counters)
        status = "PASS_COMPLETE_SCREEN"
    except TimeLimit as exc:
        if status != "ONE_PAIR_FORMULATION_CHECK":
            status = "PARTIAL_TIME_LIMIT"
        failure = str(exc)
    except Exception as exc:
        status = "FAIL"
        failure = repr(exc)
        raise
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        elapsed = time.monotonic() - start
        for d, count in enumerate(counters):
            count["distinct_qualifying_labels"] = sorted(per_degree_labels[d])
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        peak_mib = rss / (1024**2 if sys.platform == "darwin" else 1024)
        receipt = {
            "status": status,
            "scope": (
                "Only the stored ell23/F1657 fixture, the Phi',Phi'' pencil, "
                "all 1320 two-fiber base pairs and d=0..5; "
                "errors gamma*Phi' on U with gamma=n/deg(U)."
            ),
            "construction_established": False,
            "far_endpoints_established": False,
            "arbitrary_error_values_screened": False,
            "p": 1657, "ell": 23, "n": 264, "k": 173, "threshold": 213,
            "fixture_sha256": fixture_hash,
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "python_flint_version": flint.__version__,
            "computation_limit_seconds": TIME_LIMIT,
            "setup_seconds": setup_seconds,
            "first_pair_seconds": first_pair_seconds,
            "first_pair_full_screen_forecast_seconds": forecast_seconds,
            "elapsed_seconds": elapsed,
            "peak_rss_mib": peak_mib,
            "completed_base_pairs": pair_count,
            "total_base_pairs": 1320,
            "by_extra_degree": counters,
            "qualifying_witnesses": len(hits),
            "distinct_qualifying_labels": sorted(unique_labels),
            "candidate_stream_sha256": candidate_digest.hexdigest(),
            "all_derivative_moments_independently_checked": setup_seconds is not None,
            "root_method": "FLINT roots of each nonzero degree-(d+1) Newton gate",
            "all_field_labels_enumerated": False,
            "extra_sets_enumerated": False,
            "failure_or_cap_reason": failure,
            "hits": hits,
            "limitation": (
                "A negative result excludes only these prescribed scalar-Phi' "
                "error values on this single pencil and fixture. "
                "It does not exclude arbitrary errors, other received lines, "
                "other curves, or growing ell."
            ),
        }
        RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps({
            key: value for key, value in receipt.items()
            if key not in ("hits", "by_extra_degree")
        }, indent=2))
    return 0 if status in ("PASS_COMPLETE_SCREEN", "ONE_PAIR_FORMULATION_CHECK") else 1


if __name__ == "__main__":
    raise SystemExit(main())
