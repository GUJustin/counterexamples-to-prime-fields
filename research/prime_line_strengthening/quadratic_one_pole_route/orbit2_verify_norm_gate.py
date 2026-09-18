"""Independent census/matrix rebuild/Bareiss replay plus polynomial Bezout certificate."""
import json,itertools
from fractions import Fraction
from pathlib import Path
P=Path(__file__).parent;d=json.loads((P.parent/'fano_seven/orbit2_independent_field_audit.json').read_text());p=83;q=4
assert (q**3-10*q*q+3*q+1)%p==0
def reduce(v):return sum(Fraction(x).numerator*pow(Fraction(x).denominator,-1,p)*pow(q,j,p) for j,x in enumerate(v))%p
xs=list(map(reduce,d['affine_nodes']));ys=list(map(reduce,d['affine_word']));polys=[list(map(reduce,row)) for row in d['affine_polynomials']]
masks=[{i for i,row in enumerate(polys) if sum(c*pow(x,j,p) for j,c in enumerate(row))%p==y} for x,y in zip(xs,ys)]
assert len(set(xs))==14 and [sorted(x) for x in masks]==[[j-1 for j in row] for row in d['agreement_masks']]
# Reuse only the independent verifier's generic integer-polynomial and determinant code.
s=(P/'verify_norm_gate.py').read_text();s=s[s.index('expected=set()'):]
s=s.replace("'all_fiber_norm_gate.json'","'orbit2_norm_gate.json'").replace('len(actual)==302','len(actual)==332').replace("v[:2]==[0,0]","v[:2]!=[0,0]").replace("'norm_gate_independent_verification.json'","'orbit2_norm_independent_verification.json'").replace("'minor_mod29'","'minor_mod83'").replace('minor_mod29=','minor_mod83=').replace('302 exact integer Bareiss minors, unique linear f0 kernel','332 exact integer Bareiss minors, unique quadratic f0 kernel')
exec(s)

def trim(a):
 a=[v%p for v in a]
 while a and a[-1]==0:a.pop()
 return a

def plus(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([x*c for x in a])
def times(a,b):
 c=[0]*max(0,len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return trim(c)
def divrem(a,b):
 a=trim(a);out=[0]*max(0,len(a)-len(b)+1)
 while a and len(a)>=len(b):
  k=len(a)-len(b);c=a[-1]*pow(b[-1],-1,p)%p;out[k]=c
  a=plus(a,[0]*k+scale(b,-c))
 return trim(out),a
v=json.loads((P/'orbit2_norm_gate.json').read_text())[0]['kernel'][0];A=v[:2];B=v[2:7];C=v[7:]
D=plus(times(B,B),scale(times(A,C),-4));Dp=trim([i*D[i] for i in range(1,len(D))]);r0,r1=D,Dp;s0,s1=[1],[];t0,t1=[],[1]
while r1:
 quotient,rr=divrem(r0,r1);r0,r1=r1,rr;s0,s1=s1,plus(s0,scale(times(quotient,s1),-1));t0,t1=t1,plus(t0,scale(times(quotient,t1),-1))
assert len(D)==9 and len(r0)==1
S=scale(s0,pow(r0[0],-1,p));T=scale(t0,pow(r0[0],-1,p));assert plus(times(S,D),times(T,Dp))==[1]
(P/'orbit2_discriminant_certificate.json').write_text(json.dumps(dict(p=p,field_root=q,relation=v,discriminant=D,derivative=Dp,bezout_S=S,bezout_T=T,degree=8,squarefree=True,geometric_genus=3),indent=2));print('PASS: degree8 discriminant and exact Bezout(S*D+T*Dprime=1), genus3')
