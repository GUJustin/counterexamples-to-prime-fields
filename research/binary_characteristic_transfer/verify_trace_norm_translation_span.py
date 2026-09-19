"""Exact Hasse-derivative rank; no field-label or codeword enumeration."""
import json
from math import comb
from pathlib import Path
p=3
G={30:1,10:1,0:1}
rem={81:1,1:2}; quotient={}
while rem and max(rem)>=30:
    d=max(rem)-30; c=rem[max(rem)]; quotient[d]=c
    for j,v in G.items():
        i=d+j; rem[i]=(rem.get(i,0)-c*v)%p
        if not rem[i]: del rem[i]
assert not rem
P={i+3:c for i,c in quotient.items()}
assert P=={54:1,34:2,24:2,14:1,4:2}
rows=[[P.get(j+l,0)*comb(j+l,l)%p for j in range(55)] for l in range(1,55)]
rank=0
for j in reversed(range(55)):
    pivot=next((i for i in range(rank,len(rows)) if rows[i][j]),None)
    if pivot is None: continue
    rows[rank],rows[pivot]=rows[pivot],rows[rank]
    inv=pow(rows[rank][j],-1,p)
    rows[rank]=[x*inv%p for x in rows[rank]]
    for i in range(len(rows)):
        if i!=rank:
            c=rows[i][j]
            rows[i]=[(x-c*y)%p for x,y in zip(rows[i],rows[rank])]
    rank+=1
basis=[{str(j):v for j,v in enumerate(row) if v} for row in rows[:rank]]
assert rank==15 and basis[-1]=={'0':1}
receipt=dict(status='PASS',p=3,Q=9,n=81,k=34,P=P,translation_difference_rank=rank,witness_difference_rank=rank-1,basis=basis,method='Exact polynomial division and Lucas/Hasse coefficient elimination over F3; rank unchanged over extension fields.')
Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
