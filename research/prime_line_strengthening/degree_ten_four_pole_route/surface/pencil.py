import json,math
from pathlib import Path
from flint import nmod_mat,nmod_mpoly_ctx
P=Path(__file__).parent;out=[]
for B in json.loads((P.parent/'gate.json').read_text()):
 p=B['p'];cols=[(i,3-j) for j in range(4) for i in range(3*j+3)];M=[]
 for t,(x,y) in enumerate(zip(B['base'],B['word'])):
  m=2 if t<7 else 1
  for d in range(m):
   for dx in range(d+1):
    dy=d-dx;M.append([math.comb(i,dx)*math.comb(j,dy)*pow(x,i-dx,p)*pow(y,j-dy,p)%p if i>=dx and j>=dy else 0 for i,j in cols])
 R,r=nmod_mat(M,p).rref();A=[[int(R[i,j]) for j in range(len(cols))] for i in range(r)];piv=[next(j for j,a in enumerate(row) if a) for row in A];free=[j for j in range(len(cols)) if j not in piv];K=[]
 for f in free:
  v=[0]*len(cols);v[f]=1
  for row,j in zip(A,piv):v[j]=-row[f]%p
  assert all(sum(a*b for a,b in zip(row,v))%p==0 for row in M);K.append(v)
 C=nmod_mpoly_ctx.get(['X','Y'],p);polys=[C.from_dict({ij:a for ij,a in zip(cols,v) if a}) for v in K];g=polys[0]
 for f in polys[1:]:g=g.gcd(f)
 rec=dict(bank=B['bank'],p=p,columns=cols,matrix=M,rank=r,pivot_columns=piv,rank_minor=int(nmod_mat([[row[j] for j in piv] for row in M],p).det()),kernel=K,common_gcd=str(g),polynomials=[str(f) for f in polys],degrees=[list(map(int,f.degrees())) for f in polys]);out.append(rec)
 print(B['bank'],r,len(K),'gcd',g,'degrees',rec['degrees'],flush=True)
(P/'pencil.json').write_text(json.dumps(out,indent=2))
for B,rec in zip(json.loads((P.parent/'gate.json').read_text()),out):
 p=rec['p'];cols=[tuple(v) for v in rec['columns']]
 cmax=max(i-3*(3-j) for v in rec['kernel'] for (i,j),a in zip(cols,v) if a)
 assert cmax==2
 ords=[]
 for t,(x,y) in enumerate(zip(B['base'],B['word'])):
  m=2 if t<7 else 1
  val=[]
  for v in rec['kernel']:
   val.append([sum(a*math.comb(i,dx)*math.comb(j,m-dx)*pow(x,i-dx,p)*pow(y,j-m+dx,p) for (i,j),a in zip(cols,v) if i>=dx and j>=m-dx)%p for dx in range(m+1)])
  assert any(a for row in val for a in row);ords.append(val)
 assert any(a for v in rec['kernel'] for (i,j),a in zip(cols,v) if j==3)
 rec['boundary_no_fixed_component']=dict(max_coefficient_excess=cmax,exceptional_leading_jets=ords,negative_section_not_fixed=True)
(P/'pencil.json').write_text(json.dumps(out,indent=2))
print('All compactification boundary and exceptional fixed components excluded in both reductions')
