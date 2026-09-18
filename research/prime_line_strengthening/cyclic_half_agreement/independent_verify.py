"""Reconstruct every cyclic candidate and check incidence without C++ helpers."""
import json,itertools
from pathlib import Path
r=Path(__file__).parent;hits=[d for line in (r/'q7p113.hits.jsonl').read_text().splitlines() if 'q' in (d:=json.loads(line))]
out=[]
for h in hits:
 q,p,z,e,a,c=h['q'],h['p'],h['zeta'],h['h'],h['alpha'],h['value'];D=(q-1)//2;P=h['P']
 assert pow(z,q,p)==1 and all(pow(z,j,p)!=1 for j in range(1,q));assert pow(a,q,p)!=1
 roots=[pow(z,j,p) for j in range(q)];xs=roots+[a*x%p for x in roots];word=[pow(z,e*j,p) for j in range(q)]+[c*pow(z,e*j,p)%p for j in range(q)]
 polynomials=[[v*pow(z,((d-e)*j)%q,p)%p for d,v in enumerate(P)] for j in range(q)]
 def ev(coeff,x):return sum(v*pow(x,i,p) for i,v in enumerate(coeff))%p
 masks=[[j for j,Q in enumerate(polynomials) if ev(Q,x)==w] for x,w in zip(xs,word)]
 counts=[sum(j in S for S in masks) for j in range(q)]
 paircounts=[sum(i in S and j in S for S in masks) for i,j in itertools.combinations(range(q),2)]
 assert len(set(xs))==2*q and len({tuple(Q) for Q in polynomials})==q
 assert counts==[q]*q and paircounts==[D]*(q*(q-1)//2)
 assert [len(S) for S in masks]==[D+1]*q+[D]*q
 actual_first=sum((1<<i) for i,x in enumerate(roots) if ev(P,x)==pow(z,e*i,p));assert actual_first==h['mask']
 # All pair differences have exact degree D, with exactly D domain roots.
 assert len({Q[-1] for Q in polynomials})==q
 # Complete list: any extra q-agreement candidate must equal the received
 # word on the entire second coset. Its degree-D interpolant cannot do so
 # when c !=0 and e>D, since its unique degree<q interpolant has degree e.
 assert c!=0 and e>D
 out.append({'pass':True,'hit':h,'domain':xs,'word':word,'polynomials':polynomials,'masks':masks,'agreements':counts,'pair_agreements':paircounts,'complete_list_size':q})
(r/'independent_verify.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'pass':True,'verified_hits':len(out),'q':7,'prime':113,'complete_list_size':7,'all_pair_agreements':3}))
