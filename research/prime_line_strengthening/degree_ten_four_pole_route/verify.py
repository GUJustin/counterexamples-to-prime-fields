import json,itertools,math
from pathlib import Path
P=Path(__file__).parent

def det_mod(a,p):
 a=[row[:] for row in a];v=1
 for j in range(len(a)):
  k=next((k for k in range(j,len(a)) if a[k][j]%p),None)
  if k is None:return 0
  if k!=j:a[j],a[k]=a[k],a[j];v=-v
  q=a[j][j]%p;v=v*q%p;iv=pow(q,-1,p)
  for i in range(j+1,len(a)):
   scale=a[i][j]*iv%p
   if scale:
    a[i][j:]=[(x-scale*y)%p for x,y in zip(a[i][j:],a[j][j:])]
 return v%p
outs=[]
for D in json.loads((P/'gate.json').read_text()):
 p=D['p'];fn='fiber_patterns.json' if D['bank']=='paley' else 'orbit2_bank83.json'
 S=json.loads((P.parent/'quadratic_one_pole_route'/fn).read_text());assert D['base']==S['base'] and D['word']==S['word']
 cols=[(i,j) for j in range(10,-1,-1) for i in range(3*(10-j)+5)];assert cols==[tuple(v) for v in D['columns']]
 rows=[]
 for x,y,m in zip(S['base'],S['word'],[4]*7+[6]*7):
  for t in range(m):
   for dx in range(t+1):
    dy=t-dx
    rows.append([0 if i<dx or j<dy else math.comb(i,dx)*math.comb(j,dy)*pow(x,i-dx,p)*pow(y,j-dy,p)%p for i,j in cols])
 assert rows==D['matrix']
 det=det_mod([[row[j] for j in D['pivots']] for row in rows],p);assert det
 for v in D['kernel']:assert all(sum(a*b for a,b in zip(v,row))%p==0 for row in rows)
 lead=D['leading_Y10'];minor=None
 for js in itertools.combinations(range(5),3):
  q=det_mod([[row[j] for j in js] for row in lead],p)
  if q:minor=dict(columns=js,determinant=q);break
 assert minor
 outs.append(dict(bank=D['bank'],p=p,rank_minor=det,leading_minor=minor,status='PASS'))
 print(outs[-1],flush=True)
(P/'verify.json').write_text(json.dumps(outs,indent=2))
