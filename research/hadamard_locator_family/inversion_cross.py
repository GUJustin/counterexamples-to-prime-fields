"""Exact cross-pattern equations over Q(b,c,q), with z=sigma^2."""
import json,time,sympy as s
from pathlib import Path
from sympy.polys.rings import ring
P=Path(__file__).parent;start=time.monotonic();b,c,q,z,V=s.symbols('b c q z V');loc={str(v):v for v in [b,c,q,z,V]};d=json.loads((P/'inversion_gate.json').read_text());e=json.loads((P/'inversion_parameters.json').read_text());aa=[s.sympify(v,locals=loc)for v in d['leading']];pp=s.sympify(e['p'],locals=loc);kk=s.sympify(e['sigma_tau'],locals=loc)
K=s.QQ.frac_field(b,c,q);R,vv,zz=ring('V,z',K);cv=lambda e:K.convert(e);a=[cv(v)for v in aa];p=cv(pp);k=cv(kk);bs=list(map(cv,[0,q-b*c,q-c,q-b]));xs={(0,1):cv(1),(0,2):cv(b),(0,3):cv(c),(1,2):cv(q/c),(1,3):cv(q/b),(2,3):cv(q)};x=lambda i,j:xs[tuple(sorted((i,j)))];Cs=[]
for i in range(4):
 f=R.one
 for j in range(4):
  if j!=i:f*=vv**2-x(i,j)*zz
 Cs.append(f)
out={'variables':['b','c','q','z'],'z':'sigma^2 nonzero','partitions':[]}
def save():out['seconds']=time.monotonic()-start;(P/'inversion_cross.json').write_text(json.dumps(out,indent=2))
save()
for i in range(1,4):
 j,l=[j for j in range(1,4)if j!=i]
 hij=(a[0]*x(0,j)*x(0,l)-a[i]*x(i,j)*x(i,l))/(a[0]-a[i]);ri=(bs[0]-bs[i])/(a[0]-a[i]);L=vv**2+k*ri*vv+zz*hij/p
 N=(vv**2+p*zz-vv*zz)*Cs[0]+(vv**2+p*zz+vv*zz)*a[j]*Cs[j]-vv*k*bs[j]*((vv**2+p*zz)**2-vv**2*zz**2)*(vv**2-x(0,j)*zz)
 rem=N.rem(L);rec={'i':i,'j':j,'L':str(L.as_expr()),'terms':len(rem),'remainder':str(rem.as_expr())};out['partitions'].append(rec);save();print('partition',i,'terms',len(rem),'seconds',time.monotonic()-start,flush=True)
out['status']='complete';save()
