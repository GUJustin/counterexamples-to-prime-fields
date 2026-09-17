"""Finite algebraic checks; the quantified argument is in README.md."""
from fractions import Fraction as F
from pathlib import Path
import json
checks=0
for D in range(2,40):
 for B in range(2,65):
  for b in range(1,B+1):
   tau=2*D-3;u=1+tau*(B-1);v=min(u,tau*(b-1)+D)
   ff=B*v+b*(u-v)
   assert ff>=F(D*B*b,4)
   for H in (0,1,17):
    J=H*(2*u*v-v*v)+2*(1+tau*H)*ff
    assert J>=F(D*D*H*B*b,4)
   checks+=1
Path(__file__).with_name('checks.json').write_text(json.dumps({'algebraic_instances':checks,'status':'passed; quantified proof is in README'},indent=2)+'\n')
print(checks)
