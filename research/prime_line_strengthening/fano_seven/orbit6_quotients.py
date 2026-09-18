import sympy as S,json,time
from pathlib import Path
st=time.time();X,u,w,z,K=S.symbols('X u w z K');v=w*z*(1-u)/(w*z+u*(1-w-z));Q=[None,None,(X-w)*(X-z),(X-u)*(X-v),(X-v)*(X-z),(X-u)*(X-w),(X-v)*(X-w),(X-u)*(X-z)]
L=S.factor(K/((1-v)*(1-z))-1/(u*z))
P=[S.Integer(0)]*8
for i in [2,3]:P[i]=S.cancel(Q[i]*((K/Q[i].subs(X,1)-1/Q[i].subs(X,0))*X+1/Q[i].subs(X,0)))
for i in [4,5]:P[i]=S.cancel(Q[i]*(L*(X-1)+K/Q[i].subs(X,1)))
for i in [6,7]:P[i]=S.cancel(Q[i]*(L*X+1/Q[i].subs(X,0)))
extra=S.factor(-L+K/((1-u)*(1-w))-1/(v*w));print('through1',extra,flush=True)
triples=[(2,4,5,1,z,1,w),(2,6,7,0,w,0,z),(3,4,6,1,v,0,v),(3,5,7,1,u,0,u)]
out={'through1':str(extra),'determinants':[]}
for i,j,k,a,b,c,d in triples:
 f=S.Poly(S.cancel((P[i]-P[j])/((X-a)*(X-b))),X);g=S.Poly(S.cancel((P[i]-P[k])/((X-c)*(X-d))),X)
 assert f.degree()<=1 and g.degree()<=1
 det=S.factor(S.cancel(f.nth(1)*g.nth(0)-f.nth(0)*g.nth(1)))
 out['determinants'].append(str(det));print((i,j,k),det,flush=True)
out['seconds']=time.time()-st;Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
