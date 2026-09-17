import json
from pathlib import Path
import sympy as S
from repaired_auxiliary_roots import mixed
ROOT=Path(__file__).resolve().parent
a,b,s=S.symbols('a b s',nonnegative=True);units=[(1,0,0),(0,1,0),(0,0,1)]
def identity(f,a,b,s):
 z,y,r=f;return z*(393219+262146*s)+y*(786438+524292*s)+r*(1048586+262146*a+524292*b+524292*s)
def high(f,a,b,s):
 red=(2*a*131072,1+2*(b+1)*131072,2*(s+1)*131072)
 normal=(131074*a,131074*b+2,131074*s+3+131071)
 mf=(a,b+1,s+3);cut=(131074*a,131074*b+2+131072,131074*s+3+262144)
 return mixed(f,red,normal)+65539*mixed(f,mf,cut)
def low(f,a,b,s):
 tail=lambda d:(2*a*d,1+2*(b+1)*d,2*(s+1)*d)
 return mixed(f,tail(131072),tail(131073))
rows=[]
for kind,func,B,T in [('high',high,b+1,s+1),('low',low,b,s)]:
 for j,f in enumerate(units):
  slack=S.Poly(50204*func(f,a,B,T)-131073*80870*identity(f,a,B,T),a,b,s)
  coeffs=[int(x) for x in slack.coeffs()];assert min(coeffs)>=0
  rows.append(dict(branch=kind,flag_coordinate=j,smallest_nonzero_coefficient=min(coeffs)))
assert 80870<=131076 and 80870<=262147
(ROOT/'carrier_target_audit.json').write_text(json.dumps(dict(passed=True,identity_checks=rows,high_tangent_min=131076,low_tangent_min=262147,scope='Target identity absorption and error-dependent tangent gates; unchanged domain/characteristic conditions from original carrier proof retained, no Lean port.'),indent=2)+'\n')
print('6 carrier identity polynomial gates and2 tangent gates pass')
