#!/usr/bin/env python3
"""Exact modular norm-power obstruction; records a square nonzero minor."""
import json,math,hashlib
from pathlib import Path
P=Path(__file__).resolve().parent
raw=(P.parent/'gate.json').read_bytes();bank=next(z for z in json.loads(raw) if z['bank']=='paley');p=29
receipts=[]
for t in [2,5,10]:
 cols=[(i,j) for j in range(10//t+1) for i in range(34//t-3*j+1)]
 rows=[];labels=[]
 for k,(x,y) in enumerate(zip(bank['base'],bank['word'])):
  m=((4 if k<7 else 6)+t-1)//t
  for d in range(m):
   for b in range(d+1):
    a=d-b;labels.append([k,a,b]);rows.append([math.comb(i,a)*math.comb(j,b)*pow(x,i-a,p)*pow(y,j-b,p)%p if i>=a and j>=b else 0 for i,j in cols])
 M=[r[:] for r in rows];ids=list(range(len(rows)));selected=[];rank=0
 for c in range(len(cols)):
  z=next((z for z in range(rank,len(M)) if M[z][c]),None)
  if z is None:continue
  M[rank],M[z]=M[z],M[rank];ids[rank],ids[z]=ids[z],ids[rank];selected.append(ids[rank]);iv=pow(M[rank][c],-1,p)
  M[rank]=[(v*iv)%p for v in M[rank]]
  for z in range(rank+1,len(M)):
   v=M[z][c]
   if v:M[z]=[(u-v*w)%p for u,w in zip(M[z],M[rank])]
  rank+=1
 assert rank==len(cols)
 # Recompute determinant of the selected ORIGINAL rows, with independent elimination.
 A=[rows[z][:] for z in selected];det=1
 for c in range(len(cols)):
  z=next(z for z in range(c,len(A)) if A[z][c]);
  if z!=c:A[c],A[z]=A[z],A[c];det=-det
  q=A[c][c];det=det*q%p;iv=pow(q,-1,p)
  for z in range(c+1,len(A)):
   v=A[z][c]*iv%p
   for j in range(c+1,len(cols)):A[z][j]=(A[z][j]-v*A[c][j])%p
   A[z][c]=0
 assert det%p
 receipts.append(dict(intermediate_degree=t,columns=cols,row_labels=labels,rows=len(rows),rank=rank,selected_rows=selected,minor_determinant=det%p,weighted_cap=34//t,Y_cap=10//t,contacts=[(4+t-1)//t,(6+t-1)//t]))
out=dict(status='PASS',input_sha256=hashlib.sha256(raw).hexdigest(),prime=p,cases=receipts)
(P/'nonprimitive_norm_gate.json').write_text(json.dumps(out,indent=2)+'\n')
print([(r['intermediate_degree'],r['rows'],len(r['columns']),r['minor_determinant']) for r in receipts])
