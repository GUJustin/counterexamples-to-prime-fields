import sympy as s,json,time
from pathlib import Path
P=Path(__file__).parent;b,c,q,h=s.symbols('b c q h');start=time.monotonic()
bs=[0,q-b*c,q-c,q-b];S=sum(bs);E=sum(bs[i]*bs[j] for i in range(1,4)for j in range(1,i));F=s.prod(bs[1:]);D=s.expand(S*S-4*E);J3=s.factor(S*D+8*F)
N=b*c+b*q+c*q+q;J=b*c+b+c+q
M=b*b*c*c-b*b*c*q+b*b*c-b*b*q-b*c*c*q+b*c*c+b*q*q-b*q-c*c*q+c*q*q-c*q+q*q
W=-b*b*c*c*q+2*b*b*c*c-b*b*q-c*c*q+q*q*q
mh=q*M+h*W;nh=N+h*J;t=-nh/mh;k=(q-b*b)*(q-c*c)*(q-1)/mh
z=s.factor(s.cancel(k*(t*D-4)/(t*t*J3)))
out={'J3':str(J3),'z':str(z),'seconds':time.monotonic()-start};(P/'identity_leading.json').write_text(json.dumps(out,indent=2));print(out,flush=True)
