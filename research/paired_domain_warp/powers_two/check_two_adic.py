"""Exhaustive signed-power check of the unique lowest-valuation term."""
from itertools import product
from math import prod
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();checked=0
 m=10;bound=1<<(m*(m+1)//2+2*m+2)
 for signs in product([-1,0,1],repeat=m):
  inds=[i+1 for i,e in enumerate(signs) if e]
  if len(inds)<2:continue
  ys=[e*(1<<(i+1)) for i,e in enumerate(signs) if e];s=sum(ys)
  F=(1+s)*prod(1-y for y in ys)-(1-s)*prod(1+y for y in ys)
  assert F and abs(F)<bound
  valuation=(abs(F)&-abs(F)).bit_length()-1
  assert valuation==1+2*inds[0]+inds[1]
  checked+=1
 out=dict(status='passed',m=m,signed_vectors_checked=checked,seconds=time.monotonic()-start,
  scope='Exact integer valuation identity for all nontrivial signed supports of size at least two among the first ten powers.')
 (BASE/'two_adic_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
