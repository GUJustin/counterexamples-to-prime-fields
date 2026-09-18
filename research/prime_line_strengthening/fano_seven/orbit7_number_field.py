import sympy as S,json,itertools
from pathlib import Path
root=Path(__file__).parent;w,X=S.symbols('w X');f=w**3+2*w**2-w-1
def red(a):
 n,d=S.fraction(S.cancel(a));n=S.rem(n,f,w);d=S.rem(d,f,w)
 return S.rem(n*S.invert(d,f,w),f,w).expand()
def pr(a):return sum(red(c)*X**i for i,c in enumerate(reversed(S.Poly(S.expand(a),X).all_coeffs())))
u=w*w;v=w*w+w-1;z=w*w+w;sub={'u':u,'v':v,'w':w,'z':z}
data=json.loads((root/'orbit7_generic.json').read_text());M=[[red(S.sympify(a).subs(sub)) for a in row] for row in data['rows']]
amp=None
for a,b in itertools.combinations(M,2):
 cr=[red(a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3]) for i in range(3)]
 if any(cr):amp=cr;break
assert amp is not None
assert all(red(sum(a*b for a,b in zip(row,amp)))==0 for row in M)
amp=[red(a/amp[0]) for a in amp];j,k,l=amp
qs=[(X-w)*(X-z),(X-v)*(X-z),(X-u)*(X-v),(X-u)*(X-z),(X-u)*(X-w),(X-v)*(X-w)]
ps=[S.Integer(0)]
for i,Q in enumerate(qs,2):
 if i in[2,4]:L=(k/Q.subs(X,1)-j/Q.subs(X,0))*X+j/Q.subs(X,0)
 elif i in[3,6]:L=l*(X-1)+k/Q.subs(X,1)
 else:L=l*X+j/Q.subs(X,0)
 ps.append(pr(Q*L))
design=json.loads((root/'design_orbits.jsonl').read_text().splitlines()[7]);T=design['T'];C=design['C'];bs=[None,S.Integer(0),S.Integer(1),u,v,w,z]
def val(P,x):return red(S.Poly(P,X).coeff_monomial(X**3) if x is None else P.subs(X,x))
triples=[];matches=[]
for cl in T:
 a,b,c=cl
 P=pr(ps[a-1]-ps[b-1]);quad=[x for cc,x in zip(C,bs) if a not in cc and b not in cc]
 for x in quad:
  if x is None:continue
  q,r=S.div(P,X-x,X);assert pr(r)==0;P=pr(q)
 assert S.degree(P,X)<=1
 aa=red(P.coeff(X));bb=red(P.subs(X,0));x=None if aa==0 else red(-bb/aa)
 triples.append(x)
 target=val(ps[a-1],x);actual=[i+1 for i,p in enumerate(ps) if red(val(p,x)-target)==0];matches.append(actual)
nodes=bs+triples
def eq(a,b):return a is None and b is None if a is None or b is None else red(a-b)==0
collisions=[(i,jj) for i in range(14) for jj in range(i+1,14) if eq(nodes[i],nodes[jj])]
quadmatches=[]
for cc,x in zip(C,bs):
 want=[i for i in range(1,8) if i not in cc];target=val(ps[want[0]-1],x)
 quadmatches.append([i+1 for i,p in enumerate(ps) if red(val(p,x)-target)==0])
assert matches==T
assert quadmatches==[[i for i in range(1,8) if i not in cc] for cc in C]
assert collisions==[]
assert all(sum(i in mask for mask in matches+quadmatches)==7 for i in range(1,8))
out={'minimal_polynomial':str(f),'amplitudes':list(map(str,amp)),'polynomials':list(map(str,ps)),'quad_nodes':[None if a is None else str(red(a)) for a in bs],'triple_nodes':[None if a is None else str(a) for a in triples],'triple_matches':matches,'quad_matches':quadmatches,'node_collisions':collisions}
print(json.dumps(out,indent=2),flush=True)
(root/'orbit7_number_field.json').write_text(json.dumps(out,indent=2)+'\n')
