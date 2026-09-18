from fractions import Fraction as Q
from math import sqrt,floor
import json,pathlib

def evaluate(L,s):
 n=s*(2*L*L-2*L+1);D=2*s;T=s*(2*L-1);B=4*L-2
 G=3*s*B*B-(s-1)*(3*B-2)
 W=s*B**3+Q(3,2)*B*B+(Q(3,2)-3*s)*B+2*s-2
 surplus=G-23*n
 assert surplus>0
 H=max(B,(W-43*n)//surplus)
 assert (H+1)*surplus>W-43*n
 tau=2*D-3;u=1+tau*(B-1);v=min(u,tau+D)
 F=B*v+2*(u-v);S=3*B-4;Hs=3*H
 J=H*(2*u*v-v*v)+2*(1+tau*H)*F
 lam=Q(n-D,T-D)
 ar=lam*J*(n-T);br=(n-D)**2*F
 center=D+(T+1-D)*sqrt(float(br))/(sqrt(float(ar))+sqrt(float(br)))
 candidates={max(D+1,min(T,floor(center)+j)) for j in range(-2,4)}
 def regular(r):return Q(n-r+1,T-r+1)*lam*J+Q((n-r)*(n-D)*F,r-D)
 r=min(candidates,key=regular)
 # Convexity proves the minimum lies at floor/ceil of the displayed center.
 r0=D+1;psi=1+(2*D-1)*(2*S-1)+2*max(S-2*D-1,0)
 ordinary=(2*S-1)*Hs+Q(n-r0+1,T-r0+1)*(S+Hs*psi)+(n-r0)*S
 E=regular(r)+ordinary
 cs=(sqrt(5120-6912/s+2304/s**2)+sqrt(28-18/s))**2
 return dict(L=L,s=s,n=n,k=D+1,T=T,source_gap=s,B=B,G=G,H=int(H),regular_threshold=r,ordinary_threshold=r0,exceptional_upper=[str(E.numerator),str(E.denominator)],upper_over_n_squared=float(E/n**2),limiting_coefficient=cs,upper_over_L_cubed=float(E/L**3),ordinary_upper=[str(ordinary.numerator),str(ordinary.denominator)],list_upper=[str((lam*F+S).numerator),str((lam*F+S).denominator)])
rows=[evaluate(10000,s) for s in [1,10,100]]
pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows:print({k:row[k] for k in ['L','s','n','H','upper_over_n_squared','limiting_coefficient']})
