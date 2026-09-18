"""Independent direct replay of DKT Eqs 38,54,55,60--64 for projected code."""
from fractions import Fraction as Q
from pathlib import Path
import json
out=[]
for p in [5,7,11,53,101]:
 N=2*sum(p**j for j in range(5)); A=2*p*p+p; B=2*A; H=116*B
 Gq=[sum(max(4*A-2*t+b,0) for b in range(min(t,2)+1)) for t in range(B+1)]
 Rq=[sum(min(4-s,max(min(t,s)-max(0,t-2)+1,0)) for s in range(4) if s+t<4*A) for t in range(6)]
 assert sum(Gq)==3*B*B and sum(Rq)==23
 assert 5*sum(Gq)-116*N==8*(p-5)**4+168*(p-5)**3+1148*(p-5)**2+2648*(p-5)+308
 row=sum((H-t+1)*g for t,g in enumerate(Gq))-N*sum((H-t+1)*r for t,r in enumerate(Rq))
 assert row>0
 tau=1; u=B; v=3; F=3*B+2*(B-3); S=max(B,3*B-4); HS=3*H
 J=H*(2*u*v-v*v)+2*(1+tau*H)*F
 lam=Q(N-2,A-2); L=A//2; ratio=Q(N-L+1,A-L+1)
 psi=1+3*(2*S-1)+2*max(S-5,0)
 ordinary=(2*S-1)*HS+ratio*(S+HS*psi)+(N-L)*S
 E=ordinary+ratio*lam*J+(N-L)*Q(N-2,L-2)*F
 listbound=lam*F+S
 assert B<=N and L==(B-2)//4
 assert J<=1866*B*B and E<=57943*N*N and listbound<=18*N
 out.append(dict(p=p,N=N,A0=A,Bjet=B,H=H,G=sum(Gq),Rq=Rq,row_surplus=row,list_numerator=listbound.numerator,list_denominator=listbound.denominator,E_numerator=E.numerator,E_denominator=E.denominator,published_E_bound=75000*N*N))
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: five exact direct coefficient/rank/counting replays')
