import sympy as S,json,itertools,time
from pathlib import Path
st=time.time();root=Path(__file__).parent;data=json.loads((root/'design_orbits.jsonl').read_text().splitlines()[7]);T=data['T'];C=data['C'];X=S.symbols('X');a,b,c=S.symbols('a b c');amp=[a,b,c];bs=list(range(7));W=a*X**4+b*X**5+c*X**6
Ps=[]
for i in range(1,8):
 L=S.prod(X-bs[j] for j,Cj in enumerate(C) if i not in Cj)
 Ps.append(S.rem(W,L,X))
lin={}
for i,j in itertools.combinations(range(1,8),2):
 common=[bs[z] for z,Cj in enumerate(C) if i not in Cj and j not in Cj];assert len(common)==2
 l=S.div(Ps[i-1]-Ps[j-1],S.prod(X-t for t in common),X);assert l[1]==0
 lin[i,j]=S.Poly(l[0],X)
quad=[]
for i,j,k in T:
 f=lin[min(i,j),max(i,j)];g=lin[min(i,k),max(i,k)]
 quad.append(S.factor(f.coeff_monomial(X)*g.coeff_monomial(1)-g.coeff_monomial(X)*f.coeff_monomial(1)))
mon=[a*a,a*b,a*c,b*b,b*c,c*c]
M=S.Matrix([[S.Poly(q,a,b,c).coeff_monomial(mm) for mm in mon] for q in quad]);rank=M.rank()
print('rank',rank,'quadrics',quad,flush=True)
ns=M.nullspace();out={'orbit':7,'b_nodes':bs,'polynomials':list(map(str,Ps)),'quadrics':list(map(str,quad)),'monomial_matrix':list(map(list,M.tolist())),'matrix_rank':rank,'kernel':[list(map(str,v)) for v in ns],'seconds':time.time()-st}
(root/'orbit7_fixed.json').write_text(json.dumps(out,indent=2,default=int)+'\n')
