"""Exact squarefree residual discriminant costs and surviving profiles.

No optimizer, search, or global polynomial realization is asserted.
"""
from collections import defaultdict
from math import comb
from pathlib import Path
import json

n, w, C, t, cap = 262144, 131071, 6802316684345, 3261, 12


def box(a, b, h):
    return a*b*(t+1-h)-b*a*(a-1)//2-a*b*(b-1)//2


def rank(a):
    return sum(box(k+1, cap+1, 0)
               - box(max(0, 2*k+1-a), max(0, cap+1-a+k), a-k)
               for k in range(a))


def nu(s):
    return max(0, (s+1)//2, s-cap)


def disc_cost(b):
    extra = max(b-2*cap, 0)
    return comb(b, 2)+comb(extra, 2)


def multiply(f, g):
    out = defaultdict(int)
    for (u, j), a in f.items():
        for (v, k), b in g.items():
            out[u+v, j+k] += a*b
    return {key: value for key, value in out.items() if value}


def cluster(b):
    assert b >= 24
    f = {(0, 0): 1}
    for c in range(1, 13):
        f = multiply(f, {(0, 2): 1, (1, 0): -c})
    for d in range(1, b-24+1):
        f = multiply(f, {(0, 1): 1, (1, 0): -d})
    # Factor discriminants plus twice pairwise resultant orders:
    s = b-24
    exact_disc = 12+4*comb(12, 2)+24*s+2*comb(s, 2)
    assert exact_disc == disc_cost(b)
    assert min(u+j+min(u, cap) for u, j in f) == b
    return f


rows = []
for e in range(13, 17):
    h = 43-e
    budget = h*(h-1)*w+24*(h-1)
    high, low = disc_cost(h), disc_cost(h-1)
    original_disc = (60000+131071)*high+71073*low
    excess = original_disc-budget
    shift = max(0, -(-excess//(high-low)))
    c42, c43 = 71073+shift, 131071-shift
    assert c42+c43+60000 == n
    total_disc = (60000+c43)*high+c42*low
    assert total_disc <= budget
    total_rank = 60000*rank(h)+c42*rank(42)+c43*rank(43)
    assert total_rank >= C-1
    coefficient_slacks = [
        k*w+12-c42*nu(k-1)-c43*nu(k) for k in range(1, h+1)]
    assert min(coefficient_slacks) >= 0
    weights = {q: q*w+60000*h+c42*max(42-q, 0)+c43*max(43-q, 0)
               for q in range(56)}
    minimum = min(weights.values())
    assert minimum > 55*w
    assert c42+c43 < 211941
    # Squarefree local residual models: cluster(h), or (Y-1)*cluster(h-1).
    full_cluster = cluster(h)
    for a in (42, 43):
        residual = cluster(a-e)
        if a == 42:
            residual = multiply(residual, {(0, 1): 1, (0, 0): -1})
        leading = multiply({(0, e): 1}, residual)
        assert min(u+j+min(u, cap) for u, j in leading) == a
    nongraph = multiply({(0, j): comb(e, j) for j in range(e+1)}, full_cluster)
    assert min(u+j+min(u, cap) for u, j in nongraph) == h
    rows.append(dict(
        e=e, h=h, local_disc_contact_h=high, local_disc_contact_h_minus_1=low,
        discriminant_budget=budget, original_profile_discriminant=original_disc,
        original_excess=excess, graph43_to_graph42_shift=shift,
        profile=[dict(type="nongraph", contact=h, count=60000),
                 dict(type="graph", contact=42, count=c42),
                 dict(type="graph", contact=43, count=c43)],
        discriminant_total=total_disc, discriminant_slack=budget-total_disc,
        rank_total=total_rank, rank_surplus=total_rank-(C-1),
        minimum_graph_coefficient_slack=min(coefficient_slacks),
        graph_count=c42+c43, routing_required=211941,
        best_helper_weight=minimum, own_weight=55*w,
        helper_excess=minimum-55*w,
        minimizing_graph_powers=[q for q, weight in weights.items() if weight == minimum],
    ))

out = dict(
    status="PASS: all four squarefree-residual resource relaxations remain feasible",
    n=n, w=w, own_rank_required=C-1, rows=rows,
    local_squarefree_models="12 distinct factors (Y^2-c*t), with distinct (Y-d*t); one unit root for contact h-1",
    scope="Necessary-resource profiles with squarefree local models; no global H or universal F is constructed. Non-squarefree H is outside the discriminant argument. No benchmark gain.",
)
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
