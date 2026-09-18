import sympy as S,json,time
from pathlib import Path
st=time.time();X,w,z,p,q,l=S.symbols('X w z p q l');s=w+z-1;u=w/s;v=z/s;L0=p*X+q;L1=l*(X-1)-s*(p+q);L2=l*X+s*q
pairs=[((X-w)*L0-(X-v)*L1,(X-w)*L0-(X-u)*L2),((X-z)*L0-(X-u)*L1,(X-z)*L0-(X-v)*L2),(s*s*(X-u)*L0-(X-z)*L1,s*s*(X-u)*L0-(X-w)*L2),(s*s*(X-v)*L0-(X-w)*L1,s*s*(X-v)*L0-(X-z)*L2)]
out=[]
for f,g in pairs:
 f=S.Poly(S.cancel(s*f),X);g=S.Poly(S.cancel(s*g),X)
 r=S.factor(S.resultant(f,g));out.append(str(r));print(r,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'resultants':out,'seconds':time.time()-st},indent=2))
