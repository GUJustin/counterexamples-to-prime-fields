"""Independently replay the C++ bank as degree-<10 F41 polynomials.

Completeness uses the documented anchor-orbit covering argument, not
this witness-only replay. This script separately verifies the orbit
cover and the scanner's expected determining-support count.
"""
from pathlib import Path
from itertools import combinations
from math import comb
import json,hashlib
folder=Path(__file__).resolve().parent
p=41;g=6;xs=[pow(g,j,p) for j in range(40)]
assert len(set(xs))==40
word=[((1+pow(x,20,p))*pow(2,-1,p)-pow(x,10,p))%p for x in xs]
assert len(set(word))==4
for c in range(4):assert len({word[c+4*j] for j in range(10)})==1
patterns={frozenset(a) for a in combinations(range(10),4)}
orbits=[]
while patterns:
 a=min(patterns,key=lambda a:sum(1<<x for x in a))
 orbit={frozenset((x+j)%10 for x in a) for j in range(10)}
 patterns-=orbit;orbits.append(orbit)
assert len(orbits)==22 and sum(map(len,orbits))==210
bank=set();reports=[]
for c in range(4):
 report=json.loads((folder/f'bank_coset{c}.log').read_text().splitlines()[0])
 assert report['complete'] and report['coset']==c and report['threshold']==15
 assert report['supports_checked']==22*comb(30,6)
 assert report['anchor_orbits']==22 and report['primitive_root']==g
 assert report['bank_size']==len(report['values'])
 bank.update(tuple(v) for v in report['values']);reports.append({k:v for k,v in report.items() if k!='values'})
counts={};coefficients=[]
for values in sorted(bank):
 c=list(values[:10])
 for h in range(1,10):
  for j in range(9,h-1,-1):c[j]=(c[j]-c[j-1])*pow(xs[j]-xs[j-h],-1,p)%p
 def evaluate(x):
  v=c[-1]
  for j in range(8,-1,-1):v=(v*(x-xs[j])+c[j])%p
  return v
 assert tuple(map(evaluate,xs))==values
 a=sum(u==v for u,v in zip(values,word));assert a>=15
 counts[a]=counts.get(a,0)+1
 coefficients.append(c)
 assert all(tuple(values[(j+4*t)%40] for j in range(40)) in bank for t in range(10))
remaining=set(bank);orbit_sizes=[]
while remaining:
 v=next(iter(remaining));orb={tuple(v[(j+4*t)%40] for j in range(40)) for t in range(10)}
 remaining-=orb;orbit_sizes.append(len(orb))
result=dict(status='passed',p=p,n=40,dimension=10,threshold=15,maximum_agreement=max(counts),list_size=len(bank),agreement_histogram=counts,orbit_sizes=sorted(orbit_sizes),anchor_pattern_orbits=len(orbits),anchor_patterns=sum(map(len,orbits)),total_supports=sum(r['supports_checked'] for r in reports),coset_reports=reports,scanner_sha256=hashlib.sha256((folder/'bank_scan.cpp').read_bytes()).hexdigest(),scope='Witnesses independently interpolated and all 40 values checked. Completeness relies on the four-coset anchor covering proof and completed C++ enumeration; not an asymptotic theorem.')
(folder/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
