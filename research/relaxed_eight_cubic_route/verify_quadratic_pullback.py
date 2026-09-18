#!/usr/bin/env python3
"""Independent forward elimination and necessary coefficient checks for norm gate."""
import json,itertools,hashlib,time,collections
from pathlib import Path
P=Path(__file__).resolve().parent;raw=(P/'local_search.json').read_bytes();d=json.loads(raw);reference_raw=(P/'quadratic_pullback_gate.json').read_bytes();reference=json.loads(reference_raw);p=17
x=d['nodes'];w=d['word'];rows=[]
# Independent order: C0..C6, then B0..B3, unlike generator.
for xx,ww in zip(x,w):rows.append([pow(xx,j,p) for j in range(7)]+[ww*pow(xx,j,p)%p for j in range(4)]+[-ww*ww%p])
start=time.time();hist=collections.Counter();solutions=set();rank_deficient_consistent=[]
for omitted in itertools.combinations(range(16),4):
 I=[i for i in range(16) if i not in omitted];A=[rows[i][:] for i in I];piv=[];r=0
 for j in range(11):
  k=next((k for k in range(r,12) if A[k][j]),None)
  if k is None:continue
  A[r],A[k]=A[k],A[r];iv=pow(A[r][j],-1,p)
  for k in range(r+1,12):
   t=A[k][j]*iv%p
   if t:
    for h in range(j+1,12):A[k][h]=(A[k][h]-t*A[r][h])%p
    A[k][j]=0
  piv.append(j);r+=1
 inconsistent=any(not any(row[:11]) and row[11] for row in A)
 hist[f'rank{r}_'+('inconsistent' if inconsistent else 'consistent')]+=1
 if inconsistent:continue
 if r<11:rank_deficient_consistent.append(I);continue
 sol=[0]*11
 for k in range(r-1,-1,-1):
  j=piv[k];sol[j]=(A[k][11]-sum(A[k][h]*sol[h] for h in range(j+1,11)))*pow(A[k][j],-1,p)%p
 # Store canonical B then C order for exact comparison.
 solutions.add(tuple(sol[7:]+sol[:7]))
assert not rank_deficient_consistent and len(solutions)==84
assert dict(hist)==reference['rank_counts']
assert solutions=={tuple(r['B']+r['C']) for r in reference['records']}
failures=[]
for sol in sorted(solutions):
 B=sol[:4];C=sol[4:];E=[-a*pow(2,-1,p)%p for a in B]
 j0=(E[0]**2-C[0])%p;j6=(E[3]**2-C[6])%p
 assert j0 or j6
 failures.append(dict(B=B,C=C,constant_obstruction=j0,degree6_obstruction=j6))
out=dict(status='PASS',input_sha256=hashlib.sha256(raw).hexdigest(),reference_sha256=hashlib.sha256(reference_raw).hexdigest(),method='reordered columns, omitted-four enumeration, forward elimination/back substitution',all_subsets=1820,rank_counts=dict(hist),consistent_norms=84,consistent_lower_rank=0,all_rejected_before_square_test=True,obstructions=failures,seconds=time.time()-start,scope='No non-even degree6 candidate reaches14 agreements over algebraic closure of F17; coefficient guards suffice')
(P/'quadratic_pullback_gate.verified.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='obstructions'}))
