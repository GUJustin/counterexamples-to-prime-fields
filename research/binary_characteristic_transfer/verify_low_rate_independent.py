"""Independent direct finite-count replay; symbolic proof is in the audit note."""
from fractions import Fraction as F
import json
from pathlib import Path
out=[]
for p in (53,59,101,211):
 n=p**5; d=p-1; A=p**3-p**2; B=4*p*p; H=48*B
 G=sum(max(4*A-d*q+v,0) for q in range(B+1) for v in range(min(q,2)+1))
 assert G==24*p**5-24*p**4-6*p**3+18*p**2+p-3
 layers=[sum(min(4-s,max(0,min(q,s)-max(0,q-2)+1)) for q in range(6) if s+(d-1)*q<4*A) for s in range(4)]
 assert layers==[3,6,8,6]
 # Direct row test, rather than the coarser sufficient inequality.
 lhs=sum((H-q+1)*sum(max(4*A-d*q+v,0) for v in range(min(q,2)+1)) for q in range(B+1))
 rhs=n*sum((H-q+1)*sum(min(4-s,max(0,min(q,s)-max(0,q-2)+1)) for s in range(4) if s+(d-1)*q<4*A) for q in range(6))
 assert lhs>rhs
 tau=2*d-3; u=1+tau*(B-1); v=min(u,tau+d)
 freg=B*v+2*(u-v); S=max(B,3*B-4); HS=3*H
 J=H*(2*u*v-v*v)+2*(1+tau*H)*freg
 L=A//2; rat=F(n-L+1,A-L+1); lam=F(n-d,A-d)
 psi=1+(2*d-1)*(2*S-1)+2*max(S-2*d-1,0)
 ordinary=(2*S-1)*HS+rat*(S+HS*psi)+(n-L)*S
 E=ordinary+rat*lam*J+(n-L)*F(n-d,L-d)*freg
 assert E<=300000*n*n
 M=F((n-1)*(n-p),(p*p-1)*(p*p-p))
 assert M.denominator==1 and M==p**6+p**5+2*p**4+2*p**3+2*p*p+p+1
 assert (p*p-1)<A and A*A<n*d and (p**3-1)**2>n*d
 out.append(dict(p=p,source_count=G,local_layers=layers,row_surplus=lhs-rhs,bad_count=int(M),exact_E_numerator=E.numerator,exact_E_denominator=E.denominator,upper_budget=300000*n*n))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',len(out),'independent parameter replays')
