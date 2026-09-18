import itertools,json,time
import sympy as s
from pathlib import Path
start=time.time()
K=s.QQ.algebraic_field(s.sqrt(3)/2+s.I/2)
z=K.from_sympy(s.sqrt(3)/2+s.I/2)
xs=[z**j for j in range(12)]
us=[z**(2*j) for j in (0,1,2,4)]
Hs=[[u*x*x+K.one/u for x in xs] for u in us]
word=[]
for j,x in enumerate(xs):
 pairs=[(a,b) for a,b in itertools.combinations(range(4),2) if Hs[a][j]==Hs[b][j]]
 assert len(pairs)==1
 word.append(Hs[pairs[0][0]][j])
w=[word[j]-Hs[3][j] for j in range(12)]
zeros=[j for j in range(12) if not w[j]]
nonzeros=[j for j in range(12) if w[j]]
assert len(zeros)==len(nonzeros)==6
hits={};tested=0;proper=0;hist={}
for Z in itertools.combinations(zeros,3):
 def F(x):
  out=K.one
  for j in Z:out*=x-xs[j]
  return out
 for i,j in itertools.combinations(nonzeros,2):
  tested+=1
  yi,yj=F(xs[i])/w[i],F(xs[j])/w[j]
  b=(yi-yj)/(xs[i]-xs[j]);d=yi-b*xs[i]
  if not b:continue
  a=-d/b
  if a in xs or not F(a):continue
  proper+=1
  matches=[k for k,x in enumerate(xs) if F(x)==(b*x+d)*w[k]]
  hist[len(matches)]=hist.get(len(matches),0)+1
  if len(matches)>=6:
   key=(str(a),str(b),Z)
   hits[key]={'zero_indices':Z,'nonzero_pair':(i,j),'a':str(K.to_sympy(a)),'numerator_scale':str(K.to_sympy(K.one/b)),'matches':matches}
result={'field':'Q(zeta_12), zeta_12=sqrt(3)/2+i/2','old_u_exponents_of_zeta6':[0,1,2,4],'translated_old_index':3,'zero_indices':zeros,'tested':tested,'proper_candidates_with_repetitions':proper,'agreement_histogram':hist,'hits':list(hits.values()),'elapsed_seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
