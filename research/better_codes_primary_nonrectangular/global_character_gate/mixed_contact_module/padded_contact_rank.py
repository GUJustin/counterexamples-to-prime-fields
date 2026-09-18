"""Exact full weighted-box contact ranks; restriction of scalars over Q(sqrt d)."""
import json,time
from pathlib import Path
from flint import fmpq as Q,fmpq_mat
P=Path(__file__).parent;root=P.parents[2];seed=root/'relaxed_eight_cubic_route';d=json.loads((seed/'rational_seed.json').read_text());fr=json.loads((seed/'pair_padding_gate.json').read_text())['candidates'];start=time.monotonic();cols=[(a,i,j) for j in range(7) for i in range(5) for a in range(max(14-3*i-2*j,0))];assert len(cols)==123
out=[]
for bank in ['ten','eleven']:
 t0,t1=(Q(25,358),Q(-125,358)) if bank=='ten' else (Q('-4525/15304'),Q('-4175/3826'))
 z=(Q(0),Q(0));one=(Q(1),Q(0))
 def add(a,b):return a[0]+b[0],a[1]+b[1]
 def mul(a,b):return a[0]*b[0]+a[1]*b[1]*t0,a[0]*b[1]+a[1]*b[0]+a[1]*b[1]*t1
 def sc(a,n):return a[0]*n,a[1]*n
 def powers(a,n):
  ans=[one]
  for _ in range(n):ans.append(mul(ans[-1],a))
  return ans
 def ev(c,x):
  r=z
  for a in reversed(c):r=add(mul(r,x),(Q(a),Q(0)))
  return r
 xs=[(Q(a),Q(0)) for a in d['affine_nodes']];ws=[(Q(a),Q(0)) for a in d['affine_word']]
 if bank=='ten':
  new=[(Q(0),Q(1)),(t1,Q(-1))];xs+=new;ws.extend(ev(fr[0]['coefficients'],x) for x in new)
 else:
  new=[(Q('-80/163'),Q(0)),(Q('-135/262'),Q(0)),(Q(0),Q(1))];xs+=new;ws.extend([ev(fr[0]['coefficients'],new[0]),ev(fr[0]['coefficients'],new[1]),ev(fr[2]['coefficients'],new[2])])
 for control in [False,True]:
  yy=ws[:]
  if control:yy[0]=add(yy[0],one)
  rows=[]
  for x,y in zip(xs,yy):
   xp,yp=powers(x,13),powers(y,4)
   for typ in [0,1]:
    for rdeg in range(7):
     vals=[]
     for a,i,j in cols:
      v=z
      if typ==0 and rdeg==j:v=mul(xp[a],yp[i])
      if typ==1:
       if rdeg==j and a:v=add(v,sc(mul(xp[a-1],yp[i]),a))
       if rdeg==j+1 and i:v=add(v,sc(mul(xp[a],yp[i-1]),i))
      vals.append(v)
     arow=[];brow=[]
     for u,v in vals:arow.extend([u,v*t0]);brow.extend([v,u+v*t1])
     rows.extend([arow,brow])
  A,r=fmpq_mat(rows).rref();assert r%2==0
  result={'bank':bank,'control_word_first_value_plus_one':control,'n':len(xs),'m':2,'strict_weight_cap':14,'columns':len(cols),'local_rows':14,'global_rows':14*len(xs),'rank_over_quadratic_field':r//2,'nullity':len(cols)-r//2};out.append(result);print(result,flush=True)
result={'cases':out,'columns':cols,'seconds':time.monotonic()-start};(P/'padded_contact_rank.json').write_text(json.dumps(result,indent=2))
