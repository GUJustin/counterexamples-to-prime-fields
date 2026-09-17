"""Exhaust a quadratic tower at a degree cap outside the old fixed-k profile."""
from itertools import combinations
from pathlib import Path
from math import comb
import json
from verify_profile import roots,profile
from verify import interpolate,evaluate


def main():
 p=1000000007;t1=63;t2=1556
 middle=[];mw=[]
 for a,w in zip([-2,-1,0,1,2],[2,1,0,1,2]):
  middle+=roots(t1+a,p);mw +=[w]*2
 nodes=[];word=[]
 for a,w in zip(middle,mw):
  nodes+=roots(t2+a,p);word +=[w]*2
 hist,high,total=profile(nodes,word,5,p)
 residual={interpolate([middle[i] for i in I],[mw[i] for i in I],p)
           for I in combinations(range(10),3)}
 descended=set()
 for c,h in high.items():
  assert c[1]==c[3]==0 and h%2==0
  q=((c[0]+t2*c[2]+t2*t2*c[4])%p,(c[2]+2*t2*c[4])%p,c[4])
  assert sum(evaluate(q,x,p)==y for x,y in zip(middle,mw))*2==h
  descended.add(q)
 assert descended==residual and len(high)==70
 out=dict(status='passed',p=p,t1=t1,t2=t2,n=20,degree_cap=4,dimension=5,
  determining_supports=comb(20,5),distinct_interpolants=total,
  agreement_histogram=dict(sorted(hist.items())),complete_list_at_six=70,
  all_candidates_descend_one_step=True,residual_determining_supports=comb(10,3),
  residual_distinct_interpolants=len(residual),
  scope='One finite specialization, exhaustively verified. Uniform tower-height bound follows from the separate algebraic descent proof.')
 Path(__file__).with_name('variable_degree_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
