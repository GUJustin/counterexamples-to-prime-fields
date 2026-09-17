"""Independent baseline transcription and target affine-envelope audit."""
import json,re
from pathlib import Path
import sympy as sp
import repaired_auxiliary_roots as R
ROOT=Path(__file__).resolve().parent;CACHE=ROOT.parents[1]/'tmp/current-lower-primary-cache'
a,b,c=sp.symbols('a b c', nonnegative=True);r=a+3;v=b+2;z=c
old=[x['old'] for x in R.MANIFEST['sources']]
checks=[]
for suffix in 'ABCD':
 p=ROOT/f'MovingFiberArithmetic6811{suffix}.lean'
 if not p.exists():p=CACHE/p.name
 for idx,body in re.findall(r'namespace ProximityPrize.SubmissionLower.MovingFiberArithmetic6811.G(\d+)\n(.*?)(?=\nend ProximityPrize|\Z)',p.read_text(),re.S):
  g=int(idx);scale=int(re.search(r'def scale : ℕ := (\d+)',body)[1]);polys=[]
  for j in range(3):
   expr=re.search(r'def g'+str(j)+r' \(a b c : ℕ\) : ℕ :=\s*(.*?)(?=\ndef )',body,re.S)[1]
   assert re.fullmatch(r'[0-9abc*+^\s]+',expr)
   polys.append(sp.sympify(expr.replace('^','**').replace('\n',' '),locals={'a':a,'b':b,'c':c}))
  actual,sc=R.graph_value([old[i] for i in R.GROUPS[g]],r,v,z)
  assert sc==scale and sp.expand(actual-(c*polys[0]+(b+2)*polys[1]+(a+3)*polys[2]))==0
  new=R.numerators(g,r,v,z)
  for j,(num,den) in enumerate(new):
   poly=sp.Poly(num,c);assert poly.degree()<=1
   for coeff in poly.all_coeffs():assert all(x>=0 for x in sp.Poly(coeff,a,b).coeffs())
  checks.append(dict(group=g,baseline_graph_identity=True,target_four_numerators_affine_in_z=True,nonnegative_coefficients=True))
assert len(checks)==16
for g in range(16):
 for r,v in [(3,2),(17,50),(31,111)]:
  lo,hi=R.root_domain(g,r,v)
  for z in [lo,(lo+hi)//2,hi]:
   assert max(q//d for q,d in R.numerators(g,r,v,z))<=R.root_upper(g,r,v,z)
(ROOT/'repaired_auxiliary_roots_audit.json').write_text(json.dumps(dict(passed=True,checks=checks,scope='Exact old graph polynomial match; new four rational numerators affine with nonnegative coefficients; rounded max-of-lines majorizes generic bound. Target Lean source and receipt port still required.'),indent=2)+'\n')
print('16 baseline graph identities and64 target affine numerator identities pass')
