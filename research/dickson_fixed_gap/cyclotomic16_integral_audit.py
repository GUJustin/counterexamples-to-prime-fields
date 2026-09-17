"""Integral row-lattice index certifies all exceptional characteristics for n16."""
from pathlib import Path
import json,time
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
from check_cyclotomic_lift import supports,generator,rank

R=8
zero=(0,)*R
one=(1,)+(0,)*(R-1)
def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 out=[0]*R
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   out[(i+j)%R]+=x*y*(1 if i+j<R else -1)
 return tuple(out)
def root(e):
 out=[0]*R;e%=16;out[e%R]=1 if e<R else -1;return tuple(out)
def prod(xs):
 v=one
 for x in xs:v=mul(v,x)
 return v

def main():
 start=time.monotonic();p0=17;n=16;k=4;g=generator(p0);sets=supports(p0)
 logs={pow(g,j,p0):j for j in range(n)};nodes={x:root(logs[x]) for x in range(1,n+1)}
 rows=[]
 for S in sets:
  anchors=S[:k]
  V=prod(sub(nodes[anchors[j]],nodes[anchors[i]]) for i in range(k) for j in range(i+1,k))
  for x in S[k:]:
   row=[zero]*n;row[x-1]=V
   for ai,a in enumerate(anchors):
    other=[b for b in anchors if b!=a]
    va=prod(sub(nodes[other[j]],nodes[other[i]]) for i in range(k-1) for j in range(i+1,k-1))
    coeff=mul(va,prod(sub(nodes[x],nodes[b]) for b in other))
    # row coefficient is -V/den_a * product(x-b); V/den_a sign=(-1)^(k-1-ai).
    row[a-1]=neg(coeff) if (k-1-ai)%2==0 else coeff
   rows.append(row)
 for j in range(k):
  row=[zero]*n;row[j]=one;rows.append(row)
 # Independently check every polynomial of degree<k satisfies the unnormalized rows.
 for j in range(k):
  values={x:root(logs[x]*j) for x in nodes}
  for row in rows[:-k]:
   v=zero
   for x,c in enumerate(row,1):v=add(v,mul(c,values[x]))
   assert v==zero
 integer=[]
 for row in rows:
  block=[[0]*(n*R) for _ in range(R)]
  for j,c in enumerate(row):
   for b in range(R):
    v=mul(c,root(b))
    for a in range(R):block[a][j*R+b]=v[a]
  integer.extend(block)
 # Normalize the first k word values to zero before restriction of scalars.
 A=Matrix(integer[:-k*R])[:,k*R:]
 # Choose a square cyclotomic minor using one split-prime specialization.
 q=65537;z=64;pivots={};selected=[]
 for ri,row in enumerate(rows[:-k]):
  v=[sum(a*pow(z,j,q) for j,a in enumerate(coeff))%q for coeff in row[k:]]
  for col in range(n-k):
   if not v[col]:continue
   if col in pivots:
    factor=v[col];base=pivots[col]
    v=[(x-factor*y)%q for x,y in zip(v,base)]
   else:
    inv=pow(v[col],-1,q);pivots[col]=[x*inv%q for x in v];selected.append(ri);break
  if len(selected)==n-k:break
 assert len(selected)==n-k
 square=A.extract([ri*R+j for ri in selected for j in range(R)],list(range((n-k)*R)))
 modulus=abs(int(square.det(method='domain-ge')))
 assert modulus>0
 # The row-lattice index divides this nonzero minor, enabling bounded modular HNF.
 H=hermite_normal_form(A.T,D=modulus)
 assert H.shape==((n-k)*R,(n-k)*R)
 index=1
 for i in range((n-k)*R):index*=abs(int(H[i,i]))
 assert index>0
 factors={};remaining=index
 for prime in [2,17]:
  e=0
  while remaining%prime==0:remaining//=prime;e+=1
  if e:factors[str(prime)]=e
 minor_factors={};minor_remaining=modulus
 for prime in [2,17]:
  e=0
  while minor_remaining%prime==0:minor_remaining//=prime;e+=1
  if e:minor_factors[str(prime)]=e
 assert index==2**151*17**2 and modulus==2**161*17**2
 # A nontrivial residual would require factoring before an exclusion claim.
 out=dict(status='passed',rows=A.rows,columns=A.cols,index_bit_length=index.bit_length(),
          known_prime_factors=factors,unfactored_cofactor=remaining,
          minor_modulus_bit_length=modulus.bit_length(),selected_cyclotomic_rows=selected,
          minor_known_prime_factors=minor_factors,minor_unfactored_cofactor=minor_remaining,
          only_possible_odd_exception_17=(remaining==1),seconds=time.monotonic()-start,
          scope='Integer restriction of scalars of cyclotomic16 support equations with four word values normalized to zero. HNF index gives all possible exceptional characteristics; excludes characteristic2 from distinct-root interpretation.')
 Path(__file__).with_name('cyclotomic16_integral_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
