from flint import fq_default_ctx
from itertools import combinations
from pathlib import Path
import json,time
start=time.time();p=5;F=fq_default_ctx(p,5,'a');a=F.gen();zero=F(0);one=F(1)
nodes=[a*a+F(u) for u in range(p)]+[a*a*a+F(u)*a for u in range(p)]
f0=[x**(p**4-1) for x in nodes];f1=[x**(p**3-1) for x in nodes];g=[x**(p*p-1) for x in nodes]
rows=[[x**j for j in range(p)]+[-gg,aa,bb] for x,gg,aa,bb in zip(nodes,g,f0,f1)]
candidates={};singular=[];inconsistent=0;tested=0
for support in combinations(range(len(nodes)),p+1):
 tested+=1;mat=[rows[i][:] for i in support];r=0
 for c in range(p+1):
  t=next((i for i in range(r,p+1) if mat[i][c]!=zero),None)
  if t is None:continue
  mat[r],mat[t]=mat[t],mat[r];scale=one/mat[r][c];mat[r]=[scale*v for v in mat[r]]
  for i in range(p+1):
   if i!=r and mat[i][c]!=zero:
    fac=mat[i][c];mat[i]=[x-fac*y for x,y in zip(mat[i],mat[r])]
  r+=1
 if any(all(v==zero for v in row[:p+1]) and any(v!=zero for v in row[p+1:]) for row in mat):inconsistent+=1;continue
 if r<p+1:singular.append({'support':support,'rank':r});continue
 sol=tuple((mat[j][p+1],mat[j][p+2]) for j in range(p+1));key=tuple(str(v) for pair in sol for v in pair)
 if key in candidates:continue
 hits=[]
 for i,row in enumerate(rows):
  vv=[sum((row[j]*sol[j][k] for j in range(p+1)),zero) for k in range(2)]
  if vv==row[p+1:]:hits.append(i)
 candidates[key]={'solution':key,'support':hits,'canonical':all(sol[j][k]==zero for j in range(1,p-1) for k in range(2))}
hist={};best=[]
for rec in candidates.values():
 n=len(rec['support']);hist[n]=hist.get(n,0)+1
 if n>=7:best.append(rec)
result={'p':p,'modulus':str(F.modulus()),'nodes':list(map(str,nodes)),'tested_six_subsets':tested,'inconsistent':inconsistent,'singular':singular,'candidate_histogram':hist,'seven_match_candidates':best,'seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2));print(json.dumps({k:v for k,v in result.items() if k not in ['nodes','seven_match_candidates']},indent=2));print('seven matches',len(best),'noncanonical',sum(not r['canonical'] for r in best))
