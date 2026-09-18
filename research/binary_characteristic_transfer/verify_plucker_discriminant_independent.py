"""Exact sparse integer-polynomial replay; no finite-field search."""
import json
from pathlib import Path
N=8
zero=(0,)*N
one={zero:1}
def const(c):return {} if c==0 else {zero:c}
def add(*args):
 out={}
 for a in args:
  for k,v in a.items():out[k]=out.get(k,0)+v
 return {k:v for k,v in out.items() if v}
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}
def mul(a,b):
 out={}
 for ka,va in a.items():
  for kb,vb in b.items():
   k=tuple(x+y for x,y in zip(ka,kb));out[k]=out.get(k,0)+va*vb
 return {k:v for k,v in out.items() if v}
def prod(args):
 out=one
 for a in args:out=mul(out,a)
 return out
def var(i):
 k=list(zero);k[i]=1;return {tuple(k):1}
z=[var(i) for i in range(4)];t=[var(i+4) for i in range(4)]
Z=prod(z);T=prod(t);delta=add(one,scale(Z,-1))
D=[add(t[(i+1)%4],scale(prod([t[(i+3)%4],z[(i+1)%4],z[(i+2)%4]]),-1)) for i in range(4)]
U=prod([add(one,scale(mul(z[1],z[3]),-1)),D[1],D[3]])
V=prod([add(mul(z[0],z[2]),scale(one,-1)),D[0],D[2]])
P=add(*(prod([z[i],D[i],D[(i+1)%4]]) for i in range(4)),scale(mul(delta,delta),-1))
l=[prod([t[(i+1)%4],t[(i+2)%4],z[i]]) for i in range(4)]
L=add(*l);E2=add(*(mul(l[i],l[j]) for i in range(4) for j in range(i+1,4)))
C=add(*(prod([t[(i+1)%4],t[(i+2)%4]]+[z[j] for j in range(4) if j!=(i+2)%4]) for i in range(4)))
lead=add(Z,scale(L,-1),one)
F=add(mul(lead,lead),scale(add(mul(add(T,scale(one,-1)),Z),T,C,scale(E2,-1)),4))
assert not add(mul(P,P),scale(mul(U,V),-4),scale(prod([delta,delta,F]),-1))
# Independently multiply the four recovered A-coordinate vectors.
A=[(scale(mul(z[1],D[1]),-1),D[0]),(scale(D[1],-1),scale(mul(z[2],D[2]),-1)),(mul(z[3],D[3]),scale(D[2],-1)),(D[3],mul(z[0],D[0]))]
def pairprod(a,b):return (mul(a[0],b[0]),add(mul(a[0],b[1]),mul(a[1],b[0])),mul(a[1],b[1]))
a02=pairprod(A[0],A[2]);a13=pairprod(A[1],A[3])
assert not add(a02[0],scale(a13[0],-1),scale(U,-1))
assert not add(a02[1],scale(a13[1],-1),scale(mul(delta,delta),-1),scale(P,-1))
assert not add(a02[2],scale(a13[2],-1),scale(V,-1))
# Homogeneous pieces in z, with t held as coefficients.
pieces={k:{a:b for a,b in F.items() if sum(a[:4])==k} for k in range(9)}
assert pieces[8]==mul(Z,Z) and not pieces[7] and not pieces[6]
assert pieces[5]==scale(mul(Z,L),-2) and pieces[3]==scale(C,4)
# Scalar slice z_i=z_0 and t_i=t_0.
def collapse(a):
 out={}
 for k,v in a.items():
  key=(sum(k[:4]),0,0,0,sum(k[4:]),0,0,0);out[key]=out.get(key,0)+v
 return {k:v for k,v in out.items() if v}
z2=mul(z[0],z[0]);t2=mul(t[0],t[0]);a=add(z2,scale(one,-1));b=add(z[0],scale(t2,-1))
expected=mul(mul(a,a),add(mul(a,a),scale(mul(b,b),4)))
assert collapse(F)==expected
receipt={'status':'PASS','method':'sparse integer polynomial arithmetic in eight independent variables','F_terms':len(F),'checks':['four A conjugate vectors give U,P,V','P^2-4UV=(1-Z)^2 F','degree8,7,6,5,3 homogeneous pieces','scalar theta,z slice']}
Path(__file__).with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
