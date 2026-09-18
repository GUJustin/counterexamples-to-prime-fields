import sympy as S,json,time
from pathlib import Path
from sympy.polys.matrices import DomainMatrix
start=time.time();a,b,c,d=S.symbols('a b c d');rows=[]
for u,v in ((b,c),(b,d),(c,d)):
 t=u*v;C=-(a*a-u*u)*(a*a-v*v);U=a*a*(t*t+a*a*b*c);V=-a**3*(b+c)*t
 rows.append([C*C,U*C,U*U+V*V,0,-t*V*C,-2*t*U*V])
 rows.append([0,V*C,2*U*V,-t*C*C,-t*U*C,-t*(U*U+V*V)])
M=S.Matrix(rows).applyfunc(S.expand)
det=DomainMatrix.from_Matrix(M).det().as_expr()
f=S.factor(det)
out={'paired_cleared_determinant':str(f),'elapsed_seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2));print(out)
