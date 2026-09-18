"""Exact Singer q15 test; all twists and both multiplier classes."""
import json,time
import sympy as s
X,T=s.symbols('X T');eta=(1+s.sqrt(-15))/2;bar=1-eta
K=s.QQ.algebraic_field(s.sqrt(-15))
def poly(f,x=X):return s.Poly(f,x,domain=K)
C=poly(X**4-eta*X**3-2*X**2-bar*X+1)
Cn=poly(X**4-bar*X**3-2*X**2-eta*X+1)
assert C*Cn==poly(s.cyclotomic_poly(15,X))
A=poly(X**3-1)*C;An=poly(X**3-1)*Cn
B=poly(sum(X**i for i in range(5)))*C
assert B*An==poly(X**15-1)
# independently verify the F16 trace support and full period of primitive2
mod=0b10011
def mul(a,b):
 c=0
 while b:
  if b&1:c^=a
  b>>=1;a<<=1
  if a&16:a^=mod
 return c
powers=[];a=1
for _ in range(15):powers.append(a);a=mul(a,2)
assert len(set(powers))==15 and a==1
def trace(a):
 out=0
 for _ in range(4):out^=a;a=mul(a,a)
 assert out in [0,1]
 return out
D=[j for j,a in enumerate(powers) if trace(a)==0]
assert D==[0,1,2,4,5,8,10]
S=sorted(set(range(15))-{(-j)%15 for j in D})
assert S==[1,2,3,4,6,8,9,12]
assert all(sum((a-b)%15==j for a in D for b in D)==3 for j in range(1,15))
rows=[];start=time.time()
for h in range(8,15):
 P=s.rem(poly(X**h),B)
 for name,Q in [('D',A),('-D',An)]:
  powersQ=[s.rem(poly(X**j),Q) for j in range(15)]
  v=[powersQ[h].nth(i) for i in range(7)]
  R=[poly(sum(P.nth(j)*powersQ[j].nth(i)*T**j for j in range(8)),T) for i in range(7)]
  pivot=next(i for i,a in enumerate(v) if a!=0)
  fs=[R[i].mul_ground(v[pivot])-R[pivot].mul_ground(v[i]) for i in range(7) if i!=pivot]
  G=poly(0,T)
  for f in fs:G=s.gcd(G,f)
  G=G.monic();valid=G;forbid=poly(T*(T**15-1),T)
  while valid.degree()>0:
   d=s.gcd(valid,forbid)
   if d.degree()==0:break
   valid=s.exquo(valid,d)
  rows.append({'h':h,'target':name,'P':str(P.as_expr()),'raw_gcd':str(G.as_expr()),'valid_gcd':str(valid.monic().as_expr()),'valid_degree':int(valid.degree())})
result={'q':15,'D':D,'S':S,'eta_relation':'eta^2-eta+4=0','unit_period_polynomial':str(C.as_expr()),'rows':rows,'elapsed':time.time()-start}
with open('research/prime_line_strengthening/paley_exact/q15.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps({'q':15,'elapsed':result['elapsed'],'survivors':[(r['h'],r['target'],r['valid_gcd']) for r in rows if r['valid_degree']>0]}))
