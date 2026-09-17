"""Symbolic baseline domination: generated max4 envelope vs primary own receipts."""
import json,re
from pathlib import Path
import sympy as sp
import repaired_auxiliary_roots as R
ROOT=Path(__file__).resolve().parent;CACHE=ROOT.parents[1]/'tmp/current-lower-primary-cache'
a,b,c=sp.symbols('a b c',nonnegative=True);r=a+3;y=a+b+5;t=y+c;v=b+2
old=[x['old'] for x in R.MANIFEST['sources']];checks=[]
for suffix in 'ABCD':
 p=ROOT/f'MovingFiberArithmetic6811{suffix}.lean'
 if not p.exists():p=CACHE/p.name
 for idx,body in re.findall(r'namespace ProximityPrize.SubmissionLower.MovingFiberArithmetic6811.G(\d+)\n(.*?)(?=\nend ProximityPrize|\Z)',p.read_text(),re.S):
  g=int(idx);den=int(re.search(r'def denominator : ℕ := (\d+)',body)[1]);parts=[]
  for name in ['slope','intercept']:
   expr=re.search(r'def '+name+r' \(a b : ℕ\) : ℕ :=\s*(.*?)(?=\ndef )',body,re.S)[1]
   assert re.fullmatch(r'[0-9ab*+^\s]+',expr)
   parts.append(sp.sympify(expr.replace('^','**').replace('\n',' '),locals={'a':a,'b':b}))
  full=parts[0]*c+parts[1];params=[old[i] for i in R.GROUPS[g]];helpers=[];co=0
  for P in params:
   m,B,s,U,L,k,n0=P
   helpers.append((R.pair_numerator(r,y,t,B+s*(r-1),U+s*(y-1),L+s*(t-1),181284),50213))
   co+=R.pair_numerator(r,y,t,B,U,L,181284)
  graph,scale=R.graph_value(params,r,v,c)
  candidates=helpers+[(50213*graph+scale*co,50213*scale)]
  for j,(num,d) in enumerate(candidates):
   diff=sp.Poly(d*full-den*num,a,b,c)
   coeffs=[int(x) for x in diff.coeffs()]
   assert min(coeffs)>=0,(g,j,min(coeffs))
   checks.append(dict(group=g,alternative=j,minimum_coefficient=min(coeffs),terms=len(coeffs)))
assert len(checks)==64
(ROOT/'root_semantic_match_audit.json').write_text(json.dumps(dict(passed=True,checks=checks,conclusion='At baseline parameters, generated max4 affine envelope is pointwise <= primary rounded rootUpper for every a,b,c>=0; coefficientwise slope/intercept domination proves this globally, not just at sampled points.',scope='Root candidate arithmetic/semantics only; does not compare global singleton option inventories or packing algorithms.'),indent=2)+'\n')
print('64 symbolic baseline domination inequalities pass; generated root envelope never worse than primaryrootUpper')
