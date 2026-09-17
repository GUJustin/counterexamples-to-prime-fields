from fractions import Fraction as F
from pathlib import Path
import json
checks=0
for m in range(16,513):
 J=m//8;negative=F(0)
 for j in range(J+1):
  R=sum(min(min(j,ell)+1,m-ell) for ell in range(m))
  assert R>=(m-2*j)*(j+1)
  assert F(47,100)*m*(j+1)-R<=-F(m*(j+1),4)
  negative+=F(m*(j+1)*(j+2),8)
  checks+=1
 assert negative==F(m*(J+1)*(J+2)*(J+3),24)
 assert negative>F(m**4,12288)
Path(__file__).with_name('standard_checks.json').write_text(json.dumps({'degree_checks':checks,'multiplicities':497,'status':'passed'},indent=2)+'\n')
print(checks)
