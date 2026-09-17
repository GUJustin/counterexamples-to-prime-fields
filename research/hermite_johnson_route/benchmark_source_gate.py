"""Small derivative caps: exact finite source gates plus a global full-box slope bound."""
import sys,json
from pathlib import Path
from fractions import Fraction
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'better_codes_current_lower_2026_09_17'))
from capped_source_count import count
from restricted_rank_probe import rank
N=262144;W=131071;A=181275

def gate(m,S,Y,A=A):
 D=m*A;L=max(Y,m+S-1)
 C=count(D,L,Y,S);R=rank(m,L,S,Y)
 v=C-N*R
 slope=count(D,L+1,Y,S)-C-N*(rank(m,L+1,S,Y)-R)
 return dict(m=m,S=S,Y=Y,L_lower=L,margin_at_lower=v,slope=slope,feasible=v>0 or slope>0,minimum_L=(L if v>0 else L+(-v)//slope+1) if v>0 or slope>0 else None)

if __name__=='__main__':
 rows=[];best=[]
 for S in range(4):
  top=None;tested=0;positive=0
  for m in range(1,65):
   for Y in range((m*A+S-1)//W+1):
    g=gate(m,S,Y);tested+=1;positive+=g['feasible']
    # normalized slope is only a ranking diagnostic, not a certificate.
    if top is None or Fraction(g['slope'],m*m*(S+1))>Fraction(top['slope'],top['m']**2*(S+1)):top=g
  rows.append(dict(S=S,tested=tested,positive=positive,best_normalized_slope=top))
 # Locate the exact best untrimmed affine-L threshold for a small analytic neighborhood.
 thresholds=[]
 for S in [1,2,3]:
  for m in range(max(1,2*S),65):
   lo=A;hi=190000
   while lo<hi:
    mid=(lo+hi)//2;Y=(m*mid+S-1)//W
    if gate(m,S,Y,mid)['slope']>0:hi=mid
    else:lo=mid+1
   g=gate(m,S,(m*lo+S-1)//W,lo)
   thresholds.append(dict(A=lo,**g))
 thresholds.sort(key=lambda r:(r['A'],r['minimum_L']))
 out=dict(n=N,w=W,target_A=A,finite_restricted_support_gates=rows,best_full_box_thresholds=thresholds[:8],scope='All m1..64,S0..3,YS caps0..automatic cap; exact affine-L regime L>=max(Y,m+S−1). Finite failure does not assert no kernel. Threshold comparison uses untrimmed support only.')
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
