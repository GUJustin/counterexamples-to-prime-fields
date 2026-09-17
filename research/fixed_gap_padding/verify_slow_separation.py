"""Audit the slow-separation parameters and one exact prime-field instance."""
from fractions import Fraction as F
from pathlib import Path
import json,time
from verify_multi_match_finite import certificate


def icbrt(n):
 lo,hi=0,1
 while hi**3<=n:hi*=2
 while lo+1<hi:
  m=(lo+hi)//2
  if m**3<=n:lo=m
  else:hi=m
 return lo


def audit_parameters():
 rows=[]
 for ell in (32,64,128,256,512,1024,2048):
  b=1<<ell;s=ell;r=icbrt(s);log_s=s.bit_length()-1
  # c=2, rho=1/2. Replace log_2 s by its floor in h;
  # for this power-of-two schedule it is already exact.
  n=2*((s*b)//4);K=n//2
  h=-(-(3*(r+1)*b)//log_s);D=K+s;N=D+h;q=n-N
  assert 0<K<D<N<n
  m=N+1
  ratio=N//h;support_log_floor=ratio.bit_length()-1
  # binom(N,h)>=(N/h)^h >=2^(h*floor(log_2(N/h))).
  support_bits=h*support_log_floor
  # Each binomial-moment range has at most 2*m^(j+1) values.
  # Bit length gives an integer upper bound without giant exponentiation.
  moment_bits=s+(s*(s+3)//2)*m.bit_length()
  list_bits=support_bits-moment_bits
  assert list_bits>r*b
  off_h=h-r;off_s=s+r-1
  off_bits=off_h*((N//off_h).bit_length()-1)
  off_moment_bits=off_s+(off_s*(off_s+3)//2)*(N+1).bit_length()
  assert off_bits-off_moment_bits>b
  e=h-s-1;assert e>0 and 2*D>N
  exponent=F(r*r*e,q-r+1)
  # A finite consistency bound, not the asymptotic theorem itself.
  assert exponent*log_s<48
  h1=-(-(2*b)//log_s);N1=K+s+h1;q1=n-N1
  single_support=h1*((N1//h1).bit_length()-1)
  single_moments=s+(s*(s+3)//2)*(N1+1).bit_length()
  assert single_support-single_moments>b
  single_scale=F(q1,h1*s*log_s)
  assert F(1,16)<single_scale<F(1,8)
  rows.append(dict(single_match_exponent_scale=str(single_scale),log2_b=ell,s=s,r=r,log2_s=log_s,
                   log2_list_over_p_to_r_lower=str(list_bits-r*b),
                   collision_exponent_times_log2_s=str(exponent*log_s),
                   relative_far_fraction=str(F(r,s+r))))
 return rows


def main():
 start=time.monotonic();b=9689;s=b.bit_length()-1;r=icbrt(s);log_s=s.bit_length()-1
 n=2*((s*b)//4);K=n//2;h=-(-(3*(r+1)*b)//log_s);D=K+s
 row=dict(n=n,K=K,A=D+r,m=D+h+1,s=s,r=r)
 finite=certificate(b,row,5000)
 out=dict(status='passed',parameter_audit=audit_parameters(),finite_certificate=finite,
          seconds=time.monotonic()-start,
          scope='Exact sufficient parameter inequalities and a prime-field instance. The all-prime slowly varying schedule is justified by the written proof, not finite testing.')
 Path(__file__).with_name('slow_separation_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
