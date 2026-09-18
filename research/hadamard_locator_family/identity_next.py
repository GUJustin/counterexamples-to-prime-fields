import sympy as s,json,time
from sympy.polys.fields import field
from sympy.polys.domains import QQ
from pathlib import Path
P=Path(__file__).parent;start=time.monotonic();K,b,c,q,h=field('b,c,q,h',QQ)
beta=[K.zero,q-b*c,q-c,q-b];S=sum(beta);E=sum(beta[i]*beta[j]for i in range(1,4)for j in range(1,i));F=beta[1]*beta[2]*beta[3];D=S*S-4*E;J3=S*D+8*F
N=b*c+b*q+c*q+q;J=b*c+b+c+q
M=b*b*c*c-b*b*c*q+b*b*c-b*b*q-b*c*c*q+b*c*c+b*q*q-b*q-c*c*q+c*q*q-c*q+q*q
W=-b*b*c*c*q+2*b*b*c*c-b*b*q-c*c*q+q*q*q;mh=q*M+h*W;nh=N+h*J;t=-nh/mh;k=(q-b*b)*(q-c*c)*(q-1)/mh;pp=-(2*h*N+(h*h+q)*J)/nh;z=k*(t*D-4)/(t*t*J3)
a=[1+t*v*(S-2*v)for v in beta];edges={(0,1):h+1,(0,2):h+b,(0,3):h+c,(1,2):h+q/c,(1,3):h+q/b,(2,3):h+q};ee=lambda i,j:edges[tuple(sorted((i,j)))];cs=[-sum(ee(i,j)for j in range(4)if j!=i)for i in range(4)]
# Leading two coefficients of Bhat=z*B/sigma, degree2.
b2=[k*beta[i]+z*(1-a[i])for i in range(4)]
b1=[k*beta[i]*(pp-(ee(0,i)if i else 0))+z*(cs[0]-a[i]*cs[i]-k*beta[i]-pp*(1-a[i]))for i in range(4)]
# Hhat=Y Bi Bj(Bi-Bj)-z Bj(Ai²-A0²)+z Bi(Aj²-A0²).
i,j=1,2
H7=b2[i]*b2[j]*(b2[i]-b2[j])-z*(b2[j]*(2*a[i]*a[i]*cs[i]-2*cs[0])+b1[j]*(a[i]*a[i]-1))+z*(b2[i]*(2*a[j]*a[j]*cs[j]-2*cs[0])+b1[i]*(a[j]*a[j]-1))
print('computed',time.monotonic()-start,flush=True)
num=s.factor(H7.numer.as_expr());den=s.factor(H7.denom.as_expr());out={'H7_numerator':str(num),'H7_denominator':str(den),'seconds':time.monotonic()-start};(P/'identity_next.json').write_text(json.dumps(out,indent=2));print(out,flush=True)
