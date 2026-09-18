from pathlib import Path
import json
from functools import lru_cache
P=Path(__file__).parent;s=(P/'fixed_c_faces.py').read_text();exec(s[:s.index('# C0*d')])
rows=[];desc=[]
for a in range(3):
 for b in range(a+1,3):
  k=3-a-b
  for bit in range(2):
   v=bit<<k;cycle=[v,v^(1<<a),v^(1<<a)^(1<<b),v^(1<<b),v];row=[zero]*6
   for i,j in zip(cycle,cycle[1:]):
    axis=(i^j).bit_length()-1;dif=sub(c[i],c[j])
    for t in range(3):
     if t!=axis:
      idx=2*t+((i>>t)&1);row[idx]=add(row[idx],dif)
   rows.append(row);desc.append([a,b,bit])
A=[r[:] for r in rows];r=0;pivs=[]
for j in range(6):
 z=next((z for z in range(r,len(A)) if A[z][j]!=zero),None)
 if z is None:continue
 A[z],A[r]=A[r],A[z];iv=inv(A[r][j]);A[r]=[mul(x,iv) for x in A[r]]
 for z in range(len(A)):
  if z!=r:
   cf=A[z][j];A[z]=[sub(x,mul(cf,y)) for x,y in zip(A[z],A[r])]
 pivs.append(j);r+=1
out=dict(rank=r,rows=[[code(x) for x in row] for row in rows],rref=[[code(x) for x in row] for row in A],pivots=pivs,cycles=desc)
(P/'edge_cycle_gate.json').write_text(json.dumps(out,indent=2));print(out)
# RREF leaves face4,face5 free; translation permits face5=0,
# and any nonconstant solution scales to face4=1.
node=[zero]*6;node[4]=one
for i,j in enumerate(pivs):node[j]=neg(A[i][4])
const=[]
for a,b,bit in desc:
 k=3-a-b;v=bit<<k;cy=[v,v^(1<<a),v^(1<<a)^(1<<b),v^(1<<b),v];value=zero
 for i,j in zip(cy,cy[1:]):
  axis=(i^j).bit_length()-1;inds=[2*t+((i>>t)&1) for t in range(3) if t!=axis]
  value=add(value,mul(sub(c[i],c[j]),mul(node[inds[0]],node[inds[1]])))
 const.append(value)
out.update(normalized_nodes=list(map(code,node)),constant_cycle_values=list(map(code,const)),nonconstant_impossible=any(x!=zero for x in const));(P/'edge_cycle_gate.json').write_text(json.dumps(out,indent=2));print('constant cycle values',list(map(code,const)))
