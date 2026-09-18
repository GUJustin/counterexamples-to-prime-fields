import sympy as S,json,itertools,time
from pathlib import Path
st=time.time();root=Path(__file__).parent;data=json.loads((root/'design_orbits.jsonl').read_text().splitlines()[7]);T=data['T'];C=data['C'];X,u,v,w,z,j,k,l=S.symbols('X u v w z j k l');bs=[None,0,1,u,v,w,z];amp=[j,k,l]
Q={i:S.prod(X-bs[q] for q,cl in enumerate(C) if 1 not in cl and i not in cl) for i in range(2,8)}
# P2,P4 occur at both0 and1. P3,P6 occur at1 andinfinity. P5,P7at0andinfinity.
P=[S.Integer(0)]
for i in range(2,8):
 q=Q[i]
 if i in [2,4]:lin=(k/q.subs(X,1)-j/q.subs(X,0))*X+j/q.subs(X,0)
 elif i in [3,6]:lin=l*(X-1)+k/q.subs(X,1)
 else:lin=l*X+j/q.subs(X,0)
 P.append(S.expand(q*lin))
def pair(a,b):
 d=P[a-1]-P[b-1];common=[bb for cl,bb in zip(C,bs) if a not in cl and b not in cl]
 for bb in common:
  if bb is not None:d=S.cancel(d/(X-bb))
 return S.Poly(d,X)
bad=[-k,-j,-l,-P[1].subs(X,u),S.Poly(P[1],X).coeff_monomial(X**3)-l,j-P[2].subs(X,0),-P[2].subs(X,u)]
rows=[];forms=[];gcds=[];denoms=[]
for idx,(a,b,c) in enumerate(T):
 f=pair(a,b);g=pair(a,c)
 det=f.coeff_monomial(X)*g.coeff_monomial(1)-g.coeff_monomial(X)*f.coeff_monomial(1)
 form=S.cancel(det/bad[idx]);num,den=S.fraction(form);pp=S.Poly(num,j,k,l);assert pp.total_degree()==1
 row=[pp.coeff_monomial(aa) for aa in amp]
 gg=S.gcd_list(row);gcds.append(str(S.factor(gg)));denoms.append(str(S.factor(den)));row=[S.factor(rr/gg) for rr in row]
 forms.append(str(sum(rr*aa for rr,aa in zip(row,amp))));rows.append(row)
 print(idx,forms[-1],flush=True)
out={'variables':['u','v','w','z'],'amplitudes':['j','k','l'],'rows':[[str(x) for x in row] for row in rows],'forms':forms,'removed_row_gcds':gcds,'denominators':denoms,'first_minor':str(S.factor(S.det(S.Matrix(rows[:3])))),'seconds':time.time()-st}
print('firstminor',out['first_minor'],flush=True)
(root/'orbit7_generic.json').write_text(json.dumps(out,indent=2)+'\n')
