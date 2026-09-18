import sympy as S,json,itertools,time
from pathlib import Path
start=time.monotonic();root=Path(__file__).parent
q,X=S.symbols('q X');f=q**3-10*q**2+3*q+1
u,v,z,d=S.symbols('u v z d');env={'u':u,'v':v,'z':z,'d':d,'Poly':S.Poly}
def red(a):
 n,den=S.fraction(S.cancel(a));n=S.rem(n,f,q);den=S.rem(den,f,q)
 return S.rem(n*S.invert(den,f,q),f,q).expand()
def pr(a):return sum(red(cc)*X**i for i,cc in enumerate(reversed(S.Poly(S.expand(a),X).all_coeffs())))
data=json.loads((root/'nonfano2_branchII_reduce.json').read_text())
gb=S.sympify(data['groebner_basis'][1],locals=env).as_expr()
vv=red((-gb.subs(v,0)/S.expand(gb).coeff(v)).subs(z,q))
uu=red(vv*q*q*(vv-q)/(vv*vv*q-vv*vv-vv*q**3+2*vv*q*q-vv*q+vv-q*q))
dd=red(uu+q*(uu-vv)/(vv*(q-1)))
sub={u:uu,v:vv,z:q,d:dd}
raw=json.loads((root/'nonfano2_projective.json').read_text());M=[[red(S.sympify(a,locals=env).subs(sub,simultaneous=True)) for a in row['primitive_row']] for row in raw['rows']]
amp=None
for a,b in itertools.combinations(M,2):
 cr=[red(a[(i+1)%3]*b[(i+2)%3]-a[(i+2)%3]*b[(i+1)%3]) for i in range(3)]
 if any(cr):amp=cr;break
assert amp is not None
assert all(red(sum(a*b for a,b in zip(row,amp)))==0 for row in M)
lead=next(a for a in amp if a!=0);amp=[red(a/lead) for a in amp]
entry=json.loads((root/'design_orbits.jsonl').read_text().splitlines()[2]);T=entry['T'];C=entry['C'];bs=[None,S.Integer(0),S.Integer(1),uu,vv,q,dd]
W=sum(amp[i]*X**(i+3) for i in range(3));P=[]
for i in range(1,8):
 L=S.prod(X-bs[h] for h,c in enumerate(C) if i not in c and h!=0)
 P.append(pr(S.rem(W,S.expand(L),X)))
def val(P,x):return red(S.Poly(P,X).coeff_monomial(X**3) if x is None else P.subs(X,x))
triples=[];tm=[]
for cl in T:
 a,b=next((a,b) for a,b in itertools.combinations(cl,2) if sum(a not in c and b not in c for c in C)==2)
 R=pr(P[a-1]-P[b-1]);qq=[x for cc,x in zip(C,bs) if a not in cc and b not in cc]
 for x in qq:
  if x is None:continue
  Q,Rr=S.div(R,X-x,X);assert pr(Rr)==0;R=pr(Q)
 assert S.degree(R,X)<=1
 aa=red(R.coeff(X));bb=red(R.subs(X,0));node=None if aa==0 else red(-bb/aa)
 triples.append(node);target=val(P[cl[0]-1],node)
 tm.append([i+1 for i,pp in enumerate(P) if red(val(pp,node)-target)==0])
qm=[]
for cc,node in zip(C,bs):
 target=val(P[next(i for i in range(7) if i+1 not in cc)],node)
 qm.append([i+1 for i,pp in enumerate(P) if red(val(pp,node)-target)==0])
nodes=bs+triples
collisions=[(i,j) for i in range(14) for j in range(i+1,14) if (nodes[i] is None and nodes[j] is None) or (nodes[i] is not None and nodes[j] is not None and red(nodes[i]-nodes[j])==0)]
passed=tm==T and qm==[[i for i in range(1,8) if i not in cc] for cc in C] and not collisions
out={'verdict':'PASS' if passed else 'FAIL','minimal_polynomial':str(f),'node_parameters':{str(k):str(a) for k,a in sub.items()},'amplitudes':list(map(str,amp)),'polynomials':list(map(str,P)),'quad_nodes':[None if x is None else str(x) for x in bs],'triple_nodes':[None if x is None else str(x) for x in triples],'triple_matches':tm,'quad_matches':qm,'node_collisions':collisions,'seconds':time.monotonic()-start}
(root/'orbit2_number_field.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
