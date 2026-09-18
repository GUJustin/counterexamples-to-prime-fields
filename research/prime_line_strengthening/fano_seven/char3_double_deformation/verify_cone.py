"""Replay eleven cone identities using independent univariate field arithmetic."""
import json
from pathlib import Path
from functools import lru_cache
P=Path(__file__).parent
source=(P.parent/'char3_deformation/verify.py').read_text()
exec(source[source.index('def padd'):source.index('z=decode(3)')])
d=json.loads((P/'solve.json').read_text());c=json.loads((P/'cone.json').read_text())
Q=[list(map(decode,row[:78])) for row in d['quadratic_projection']]
M=[list(map(decode,row)) for row in c['active_map']]
T=[list(map(decode,row)) for row in c['row_combinations']]
pairs=[(i,j) for i in range(12) for j in range(i,12)]
def product(a,b):
 return [mul(a[i],b[j]) if i==j else add(mul(a[i],b[j]),mul(a[j],b[i])) for i,j in pairs]
target=[]
for i in range(5):
 target.append([sub(a,b) for a,b in zip(product(M[i],M[i]),product(M[5],M[5]))])
 target.append(product([sub(a,b) for a,b in zip(M[i],M[5])],M[6]))
target.append(product(M[6],M[6]))
for n,t in enumerate(T):
 out=[zero]*78
 for a,row in zip(t,Q):
  if a!=zero:
   for j,b in enumerate(row):
    if b!=zero:out[j]=add(out[j],mul(a,b))
 assert out==target[n],n
# Centering subtracts the same quantity from all marked velocities.
K=[list(map(decode,row)) for row in d['kernel_complement']]
for i in range(6):
 for j in range(6):
  assert [sub(a,b) for a,b in zip(M[i],M[j])]==[sub(v[138+i],v[138+j]) for v in K]
(P/'verify_cone.json').write_text(json.dumps({'pass_all':True,'independent_field':True,'exact_polynomial_identities':11,'original_variables':12,'coefficients_per_identity':78,'velocity_differences_preserved':True,'consequence':'Every geometric point of the homogeneous quadratic cone has at most two distinct marked velocities; later cluster splitting remains open.'},indent=2))
print('PASS: 11 exact identities in all 12 original variables; marked velocity differences preserved')
