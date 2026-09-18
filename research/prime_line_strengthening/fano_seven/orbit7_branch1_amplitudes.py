import sympy as S,json
from pathlib import Path
root=Path(__file__).parent;u,v,w,z,X=S.symbols('u v w z X');j,k,l=S.symbols('j k l')
d=json.loads((root/'orbit7_generic.json').read_text());M=S.Matrix([[S.sympify(a) for a in row] for row in d['rows']])
U=v*w*(v-w)/((w-1)*(z-v));cross=M.row(0).cross(M.row(1))
sub={a:S.factor(b.subs(u,U)) for a,b in zip([j,k,l],cross)}
qs=[(X-w)*(X-z),(X-v)*(X-z),(X-u)*(X-v),(X-u)*(X-z),(X-u)*(X-w),(X-v)*(X-w)]
ps=[S.Integer(0)]
for i,Q in enumerate(qs,2):
 if i in[2,4]: L=(k/Q.subs(X,1)-j/Q.subs(X,0))*X+j/Q.subs(X,0)
 elif i in[3,6]:L=l*(X-1)+k/Q.subs(X,1)
 else:L=l*X+j/Q.subs(X,0)
 ps.append(Q*L)
out={'cross':[str(x) for x in sub.values()],'bad':[],'row_residuals':[]}
for f in [-k,-j,-l,-ps[1].subs(X,u),S.Poly(ps[1],X).coeff_monomial(X**3)-l,j-ps[2].subs(X,0),-ps[2].subs(X,u)]:
 out['bad'].append(str(S.factor(f.subs(u,U).subs(sub))))
for row in M.tolist():out['row_residuals'].append(str(S.factor(sum(a*sub[b] for a,b in zip(row,[j,k,l])).subs(u,U))))
print(json.dumps(out,indent=2),flush=True)
(root/'orbit7_branch1_amplitudes.json').write_text(json.dumps(out,indent=2)+'\n')
