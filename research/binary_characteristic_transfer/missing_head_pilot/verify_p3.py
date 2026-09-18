import json
from pathlib import Path
p=Path(__file__).parent;data=json.loads((p/'p3.json').read_text());q=2187

def ds(a):
 r=[]
 for _ in range(7):r.append(a%3);a//=3
 return r
def encode(a):return sum(v*3**i for i,v in enumerate(a))
def add(a,b):return encode([(x+y)%3 for x,y in zip(ds(a),ds(b))])
def neg(a):return encode([(-x)%3 for x in ds(a)])
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 aa,bb=ds(a),ds(b);c=[0]*13
 for i,x in enumerate(aa):
  for j,y in enumerate(bb):c[i+j]=(c[i+j]+x*y)%3
 for k in range(12,6,-1):
  c[k-7]=(c[k-7]-2*c[k])%3;c[k-5]=(c[k-5]-c[k])%3
 return encode(c[:7])
def power(a,k):
 r=1
 while k:
  if k&1:r=mul(r,a)
  a=mul(a,a);k//=2
 return r
def inv(a):return power(a,q-2)
verified=[]
for group in data['best']:
 line=group['line_id']
 if line<q*q:u,v,k=1,line//q,line%q
 else:u,v,k=0,1,line-q*q
 pairs=[];rootsets=[]
 for E,C,B,A,one in group['locators']:
  assert one==1
  roots=[]
  for x in range(q):
   r=0;y=x
   for c in [E,C,B,A,1]:r=add(r,mul(c,y));y=power(y,3)
   if r==0:roots.append(x)
  assert len(roots)==81
  rootsets.append(set(roots))
  uu=sub(power(C,3),mul(B,power(A,3)))
  kk=add(sub(sub(power(E,9),mul(power(A,9),power(C,3))),power(B,10)),mul(B,power(A,12)))
  scale=inv(uu or B)
  assert (mul(uu,scale),mul(B,scale),mul(kk,scale))==(u,v,k)
  z1=sub(power(B,3),power(A,4));z0=add(sub(sub(power(C,9),mul(power(A,9),power(B,3))),mul(A,power(B,9))),power(A,13))
  if v:pair=(sub(z1,mul(A,mul(u,inv(v)))),sub(z0,mul(A,mul(k,inv(v)))))
  else:pair=(A,sub(z0,mul(z1,mul(k,inv(u)))))
  pairs.append(pair)
 assert len(set(pairs))==2
 verified.append({'line':line,'labels':pairs,'root_counts':[81,81],'intersection_size':len(rootsets[0]&rootsets[1])})
assert data['subspaces']==925771 and data['maximum_distinct_labels']==2
(p/'p3.selected_verified.json').write_text(json.dumps({'arithmetic':'independent polynomial convolution modulo X7+X2+2','verified':verified},indent=2));print('All six saved locators and three double-label groups independently verified.')
