"""Exact restricted second-jet rank over the pinned prime, not a routing receipt."""
import json
from math import comb
from pathlib import Path
P=2130706433;N=262144;W=131071;A=181275

def rank(columns):
    pivots={}
    for column in columns:
        v={k:x%P for k,x in column.items() if x%P}
        while v:
            k=min(v)
            if k not in pivots:
                inv=pow(v[k],-1,P)
                pivots[k]={r:x*inv%P for r,x in v.items()}
                break
            t=v[k]
            for r,x in pivots[k].items():
                y=(v.get(r,0)-t*x)%P
                if y:v[r]=y
                else:v.pop(r,None)
    return len(pivots)

def columns(m,S,K,J,only_ell=None):
    for k in range(K+1):
      for j in range(S+1):
       for i in (range(max(0,J-j-k+1)) if only_ell is None else [only_ell-j-k]):
        if i<0:continue
        ell=i+j+k
        for a in range(m):
          out={}
          for b in range(i+1):
            for v in range(i-b+1):
              r=a+i+v+2*b
              if r>=m:break
              out[(r,b,v+k,ell-b-v-k)]=comb(i,b)*comb(i-b,v)*(-1)**v
          if out:yield (ell,a+i-k),out

def local_rank(m,S,K,J,blocked=True):
    if not blocked:return rank([v for _,v in columns(m,S,K,J)])
    result=0
    for ell in range(J+1):
        blocks={}
        for key,v in columns(m,S,K,J,ell):blocks.setdefault(key,[]).append(v)
        result+=sum(rank(v) for v in blocks.values())
    return result

def count(m,S,K,J):
    return sum(max(m*A-W*i-(W-1)*j-(W-2)*k,0)
               for k in range(K+1) for j in range(S+1)
               for i in range(max(0,J-j-k+1)))

checks=0
for m in range(1,5):
 for K in (0,1):
    J=m+1;S=min(2,m)
    assert local_rank(m,S,K,J)==local_rank(m,S,K,J,False)
    checks+=1
rows=[]
for m in (4,8,12,16,32,64):
 S=max(1,round(.31*m))
 for K in (0,1):
    J=(m*A+S+2*K-1)//W
    R=local_rank(m,S,K,J);C=count(m,S,K,J)
    if K==0:
        assert 6*R==(S+1)*(3*m*m+3*(1-S)*m+S*(2*S+1))
    rows.append(dict(m=m,S=S,curvature_cap=K,J=J,
                     local_rank=R,coefficient_slope=C,
                     dimension_slope=C-N*R,rank_ratio=R/C))
out=dict(p=P,n=N,w=W,A=A,independent_unblocked_checks=checks,rows=rows,
 scope='Exact scalar local rank in the ambient translated jet box; C−nR is sufficient global scalar kernel bound and large-challenge slope test. No routing/factor certificate.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
