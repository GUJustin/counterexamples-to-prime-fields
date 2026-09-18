"""A five-point obstruction to an eighth cubic, using independent field arithmetic."""
import runpy,json
from pathlib import Path
r=Path(__file__).parent
s=runpy.run_path(str(r/'orbit7_independent_field_audit.py'));K=s['K'];P=s['P'];nodes=s['nodes'];ev=s['ev'];masks=s['masks']
# The first three triple targets are zero. A cubic meeting them is a scalar
# times their locator; its fourth prescribed value determines that scalar.
roots=nodes[7:10]
def loc(x):
 z=K(1)
 for a in roots:z=z*(x-a)
 return z
x4=nodes[10];v4=ev(P[masks[10][0]-1],x4);lam=v4/loc(x4)
x5=nodes[11];v5=ev(P[masks[11][0]-1],x5);error=lam*loc(x5)-v5
assert error
out={'pass':True,'test':'first five triple nodes','locator_roots':[a.out() for a in roots],'scale':lam.out(),'fifth_point_error':error.out(),'conclusion':'No cubic meets all seven triple targets; the degree-at-most-three list at agreement seven is exactly seven.'}
(r/'orbit7_eighth_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
