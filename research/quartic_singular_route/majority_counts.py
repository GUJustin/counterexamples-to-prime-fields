"""Exact majority-pair probability via binomial sums, never sign-vector enumeration."""
from math import comb,sqrt,pi
from fractions import Fraction
from pathlib import Path
import json

def probability(L):
 return Fraction(1,4)+Fraction(comb(2*L,L),2*4**L)

def tails(L):
 # Candidate (++): other sum >= -2, including tie; (--): other sum <2.
 N=2*L-2
 plus=sum(comb(N,k) for k in range(N+1) if 2*k-N>=-2)
 minus=sum(comb(N,k) for k in range(N+1) if 2*k-N<2)
 return Fraction(plus+minus,4*2**N)

def abs_moment(L):
 return Fraction(sum(comb(2*L,k)*abs(2*k-2*L) for k in range(2*L+1)),4**L)

if __name__=='__main__':
 checks=0
 for L in range(1,101):
  p=probability(L);central=Fraction(comb(2*L,L),4**L)
  assert p==tails(L)
  assert abs_moment(L)==2*L*central
  # Square both nonnegative sides to check the uniform lower bound exactly.
  assert central*central>=Fraction(1,4*L)
  checks+=1
 rows=[]
 for L in [1,2,3,4,5,8,10,16,25,50,100,1000]:
  p=probability(L);gain=p-Fraction(1,4)
  rows.append(dict(L=L,probability=str(p) if L<=100 else None,probability_float=float(p),gain_float=float(gain),sqrtL_times_gain=float(gain)*sqrt(L),uniform_lower_gain=1/(4*sqrt(L))))
 out=dict(exact_checks=checks,formula='p_L=1/4+binom(2L,L)/(2*4^L)',absolute_moment='E|S_(2L)|=2L*binom(2L,L)/4^L',uniform_gain_lower_bound='p_L−1/4>=1/(4sqrt(L))',asymptotic_gain='(1−1/(8L)+O(L^−2))/(2sqrt(pi L))',asymptotic_constant=1/(2*sqrt(pi)),rows=rows,scope='Independent uniform Rademacher signs. Transfer to finite-field character patterns requires the separately audited equidistribution/error bound.')
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
