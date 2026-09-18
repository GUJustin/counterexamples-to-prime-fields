"""Independent exact Newton interpolation in Q[z]/(z^16-z^8+1).
Optional --input accepts JSON candidates with support or finite_field_support.
No generator imports. All supports are exponents of the chosen primitive root.
"""
import argparse,json,time
from pathlib import Path
from flint import fmpq_poly
P=Path(__file__).parent
F=fmpq_poly([1]+[0]*7+[-1]+[0]*7+[1]);zero=fmpq_poly([]);one=fmpq_poly([1]);z=fmpq_poly([0,1])
def mul(a,b):return (a*b)%F
def inv(a):
 g,s,t=a.xgcd(F);assert g==one
 return s%F
xs=[one]
for i in range(1,48):xs.append(mul(xs[-1],z))
assert mul(xs[-1],z)==one
word=[(one+xs[(24*i)%48])/2-xs[(12*i)%48] for i in range(48)]
def evaluate(coeff,x):
 v=zero
 for a in reversed(coeff):v=mul(v,x)+a
 return v

def interpolate(S):
 assert len(S)>=12 and len(set(S))==len(S)
 S=list(reversed(S[-12:]));coef=[zero]*12;basis=[one]
 for i in S:
  t=mul(word[i]-evaluate(coef,xs[i]),inv(evaluate(basis,xs[i])))
  for j,b in enumerate(basis):coef[j]+=mul(t,b)
  nxt=[zero]*(len(basis)+1)
  for j,b in enumerate(basis):nxt[j]-=mul(xs[i],b);nxt[j+1]+=b
  basis=nxt
 return coef

def key(c):return tuple(tuple(str(v) for v in a) for a in c)
def rotation(c,t):return [mul(a,xs[(4*t*j)%48]) for j,a in enumerate(c)]
def support(c):return [i for i in range(48) if evaluate(c,xs[i])==word[i]]
def modvalue(a,p,root):
 val=0
 for q in reversed(list(a)):val=(val*root+int(q.numerator)*pow(int(q.denominator),-1,p))%p
 return val

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input');ap.add_argument('--output',default=str(P/'exact_replay.json'));args=ap.parse_args();start=time.monotonic()
 known=json.loads((P.parent/'structured_search.json').read_text())['fixtures'][-1]
 assert (known['n'],known['k'])==(48,12)
 knownbank={}
 for row in known['candidates']:
  c=interpolate(row['finite_field_support']);assert support(c)==row['finite_field_support']
  for t in range(12):knownbank[key(rotation(c,t))]=rotation(c,t)
 assert len(knownbank)==9 and all(len(support(c))==16 for c in knownbank.values())
 rows=[];full={}; data={}
 if args.input:
  data=json.loads(Path(args.input).read_text())
  for row in data['candidates']:
   S=row.get('support',row.get('finite_field_support'));assert S is not None
   c=interpolate(S);hits=support(c)
   p=data.get('p',data.get('split_prime'));root=data.get('root',data.get('primitive_nth_root'))
   if p is not None and root is not None:
    coeff=[modvalue(a,p,root) for a in c]
    for i in S:
     x=pow(root,i,p);v=sum(a*pow(x,j,p) for j,a in enumerate(coeff))%p
     assert v==((1+pow(x,24,p))*pow(2,-1,p)-pow(x,12,p))%p
   orbit={key(rotation(c,t)):rotation(c,t) for t in range(12)}
   if len(hits)>=16:full.update(orbit)
   rows.append({'modular_support':S,'exact_support':hits,'qualifies':len(hits)>=16,'orbit_size':len(orbit),'known_composition':key(c) in knownbank,'coefficients':key(c)})
 out={'field_modulus_ascending':[1]+[0]*7+[-1]+[0]*7+[1], 'known_bank_size':9,'known_supports':[support(c) for c in knownbank.values()], 'candidates':rows,'exact_full_orbit_count':len(full),'full_bank':[{'coefficients':key(c),'support':support(c)} for c in full.values()],'agreement_histogram':{str(m):sum(len(support(c))==m for c in full.values()) for m in sorted({len(support(c)) for c in full.values()})},'seconds':time.monotonic()-start,'scope':'Exact lifting of supplied representatives; completeness requires separately certified exhaustive modular search.'}
 Path(args.output).write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items() if k not in ('candidates','known_supports','full_bank')})
if __name__=='__main__':main()
