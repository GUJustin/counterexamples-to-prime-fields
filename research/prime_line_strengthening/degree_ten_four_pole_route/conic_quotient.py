"""Exact F29 conic-parameter discriminant quotient and factorization."""
import json,time
from pathlib import Path
from flint import nmod_poly,nmod_mpoly_ctx
P=Path(__file__).parent;p=29
D=next(d for d in json.loads((P/'gate.json').read_text()) if d['bank']=='paley')
old=json.loads((P/'residual_discriminant'/'old_graph_lines.json').read_text())
zero=nmod_poly([],p)
forms=[]
for v in D['kernel']:
 forms.append([nmod_poly([sum(a for (i,l),a in zip(D['columns'],v) if i==k and l==j)%p for k in range(35-3*j)],p) for j in range(11)])
H=[zero for _ in range(21)]
for i in range(11):
 for j in range(11):H[i+j]=H[i+j]+forms[1][i]*forms[1][j]-20*forms[0][i]*forms[2][j]
for row in old['lines']:
 f=nmod_poly(row['cubic'],p);d=len(H)-1;Q=[zero for _ in range(d)];Q[-1]=H[-1]
 for j in range(d-1,0,-1):Q[j-1]=H[j]+f*Q[j]
 assert H[0]+f*Q[0]==zero
 for j in range(d+1):assert H[j]==(Q[j-1] if j else zero)-(f*Q[j] if j<d else zero)
 H=Q
assert len(H)==14
ctx=nmod_mpoly_ctx.get(['X','Y'],p);terms={(i,j):int(c[i]) for j,c in enumerate(H) for i in range(c.degree()+1) if c[i]}
g=ctx.from_dict(terms);assert max(i+3*j for i,j in terms)==47
tick=time.monotonic();unit,factors=g.factor()
rebuild=ctx.constant(int(unit))
for h,e in factors:rebuild*=h**e
assert rebuild==g
out={'status':'PASS','p':p,'kappa':5,'seven_exact_divisions':True,'quotient_terms':[[i,j,c] for (i,j),c in sorted(terms.items())],
 'weighted_degree':47,'Y_degree':13,'factor_seconds':time.monotonic()-tick,'unit':int(unit),
 'factors':[{'terms':[[int(i),int(j),int(c)] for (i,j),c in h.to_dict().items()],'exponent':int(e),'degrees':list(map(int,h.degrees()))} for h,e in factors]}
assert len(factors)==1 and factors[0][1]==1
x,y=1,23
assert sum(c*pow(x,i,p)*pow(y,j,p) for (i,j),c in terms.items())%p==0
gradient=[sum(c*i*pow(x,i-1,p)*pow(y,j,p) for (i,j),c in terms.items() if i)%p,
          sum(c*j*pow(x,i,p)*pow(y,j-1,p) for (i,j),c in terms.items() if j)%p]
assert gradient==[3,17]
out.update(smooth_F29_point=[x,y],gradient=gradient,
           absolute_irreducibility_certificate='Irreducible over F29 plus a smooth F29-rational point')
(P/'conic_quotient.json').write_text(json.dumps(out,indent=2));print({'factors':[(list(map(int,h.degrees())),int(e)) for h,e in factors],'seconds':out['factor_seconds']})
