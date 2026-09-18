import json,math
from pathlib import Path
from flint import nmod_mpoly_ctx
from sympy import symbols,Poly,factor_list
P=Path(__file__).parent;d=json.loads((P.parent.parent/'gate.json').read_text())[0];p=29;pars=[1,8,15]
f={tuple(kl):sum(a*v[j]for a,v in zip(pars,d['kernel']))%p for j,kl in enumerate(d['columns'])};f={k:c for k,c in f.items()if c}
C=nmod_mpoly_ctx.get(['X','Y'],p);ff=C.from_dict(f);fac=ff.factor();print('factors',[(g.degrees(),e)for g,e in fac[1]],flush=True)
def shift(f,x,y):
 out={}
 for(k,l),c in f.items():
  for a in range(k+1):
   for b in range(l+1):out[a,b]=(out.get((a,b),0)+c*math.comb(k,a)*math.comb(l,b)*pow(x,k-a,p)*pow(y,l-b,p))%p
 return{k:c for k,c in out.items()if c}
f=shift(f,1,1);m=min(k+l for k,l in f);T=symbols('T');cone=sum(c*T**l for(k,l),c in f.items()if k+l==m);print('multiplicity',m,'cone',factor_list(cone,T,modulus=p),flush=True)
(P/'resolve.json').write_text(json.dumps({'parameters':pars,'irreducible_mod29':len(fac[1])==1 and fac[1][0][1]==1,'local_polynomial':[[k,l,c]for(k,l),c in f.items()],'multiplicity':m,'tangent_factorization':str(factor_list(cone,T,modulus=p))},indent=2))
