"""Exact integer checks only; no contact matrix or numerical rank calculation."""
import json
from collections import defaultdict
from pathlib import Path
n,w,a,m,W,Q,s,L = 262144,131071,181275,115,20846625,159,35,274277

def local_rank(cap):
    return sum(max(m-max(0,d-s)-2*k,0)
               for d in range(cap+1) for k in range(min(d,s)+1))

rank = local_rank(Q)
events = defaultdict(int)
initial = 0
columns = 0
for j in range(s+1):
    for i in range(Q-j+1):
        d = i+j
        lower = a*d-j
        upper = W-1+(a-w)*d
        initial += upper//n - (-(-lower//n)) + 1
        lo_event = lower % n
        hi_event = (upper+1) % n
        if lo_event: events[lo_event] += 1
        if hi_event: events[hi_event] -= 1
        columns += (W-w*d+j)*(L-d+1)
current = initial
previous = 0
integral = surplus = surplus_characters = 0
minimum = maximum = current
for point in sorted(set(events)|{n}):
    length = point-previous
    integral += current*length
    surplus += max(current-rank,0)*length
    if current > rank: surplus_characters += length
    minimum,maximum = min(minimum,current),max(maximum,current)
    current += events[point]
    previous = point
rows = n*((L-Q+1)*rank+sum(local_rank(q) for q in range(Q)))
assert rank == 182580
assert integral == 47859086760
assert (minimum,maximum) == (182472,182687)
assert surplus == 2568270
assert surplus_characters == 98642
assert rows == 13125118926520320
assert columns == 13123663101701085
result = dict(local_rank=rank,full_local_rows=rows,full_columns=columns,
              columns_minus_rows=columns-rows,z_free_columns=integral,
              min_character_columns=minimum,max_character_columns=maximum,
              characters_above_rank_ceiling=surplus_characters,
              forced_z_free_nullity=surplus,
              forced_full_nullity=surplus*(L-Q+1),
              scope="special monomial word only; no uniform saving")
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
