"""Exact prime-field certificates for multiple-coordinate far points."""
from fractions import Fraction as F
from math import comb,prod
from pathlib import Path
import json,time
from verify_average_padding import h,c


def fall(x,a):return prod(x-j for j in range(a)) if a<=x else 0


def certificate(b,row,bits):
 p=h.lucas_lehmer(b);U=p-1
 n,K,A,m,s,r=(row[key] for key in ['n','K','A','m','s','r'])
 D=A-r;t=D+1;N=m-1;q=n-N;R=p-N;d=K-1
 assert n==2*K and s==D-K and K<D<N<n<p and 1<=r<=q
 L0,_,_=h.gram_bound(m,t,s);L=h.ceil(F(t*L0,m))
 # The selected subset can have exactly this certified lower-bound size.
 T=d*comb(L,2)-h.pairs(L*D,N);assert T>=0
 e=d-max(0,2*D-N);assert e>=1
 B=F(0);uniform=F(0)
 for a in range(r+1):
  if not 0<=r-a<=q-r:continue
  v=F(comb(r,a)*comb(q-r,r-a),comb(q,r))
  B+=v if a==0 else v*U**a*(F(1,L)+F(2*T*fall(e-1,a-1),L**2*fall(R,a)))
  uniform+=v*U**a*(F(1,L)+F((L-1)*fall(e,a),L*fall(R,a)))
 B=min(B,uniform);assert B>=1
 J=h.ceil(F(U)/B);assert 0<J<=U
 assert p**(A-K)*A**A*(n-A)**(n-A)>n**n
 assert n**(A-K)*2**(n+bits*(A-K))<p**(A-K)
 assert J**(A-K)>n**(A-K)*2**n
 return dict(prime_exponent=b,n=n,K=K,A=A,far_coordinates=r,exact_far_agreement=D,
             seed_length=m,seed_moments=s,padding=q,outside_pair_cap=e,
             nearby_fraction_lower=c.decimal_lower(F(J,p),8),
             prescription_fraction_less_than_power_two=-bits,
             list_lower_bound_sha256=c.digest_integer(L),
             label_lower_bound_sha256=c.digest_integer(J),strict_elias=True)


def main():
 start=time.monotonic()
 data=json.loads(Path(__file__).with_name('multi_match_search.json').read_text())['best']
 rows=[]
 for b,bits in [(61,10),(127,40),(521,100),(1279,100)]:
  for r in [2,3]:
   candidates=data[str(b)][str(r)+':'+str(bits)]
   assert candidates
   rows.append(certificate(b,candidates[0],bits))
 out=dict(status='passed',certificates=rows,seconds=time.monotonic()-start,
          scope='Exact finite certificates on arbitrary padded interval domains. All counts, Elias, primality and numerical-prescription comparisons are exact; floating search only chooses integer parameters. No prescribed-domain or protocol-security claim.')
 Path(__file__).with_name('multi_match_finite_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
