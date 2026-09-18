import sympy as S,json
from pathlib import Path
root=Path(__file__).parent;w,X=S.symbols('w X');f=w**3+2*w**2-w-1
def red(a):
 n,d=S.fraction(S.cancel(a));return S.rem(S.rem(n,f,w)*S.invert(S.rem(d,f,w),f,w),f,w).expand()
def pr(a):return sum(red(c)*X**i for i,c in enumerate(reversed(S.Poly(S.expand(a),X).all_coeffs())))
d=json.loads((root/'orbit7_number_field.json').read_text());ps=list(map(S.sympify,d['polynomials']));ts=list(map(S.sympify,d['triple_nodes']))
ys=[red(ps[mask[0]-1].subs(X,t)) for mask,t in zip(d['triple_matches'],ts)]
P=S.Integer(0)
for i,(t,y) in enumerate(zip(ts,ys)):
 numerator=S.prod(X-x for j,x in enumerate(ts) if j!=i)
 denominator=red(S.prod(t-x for j,x in enumerate(ts) if j!=i))
 P=pr(P+pr(numerator)*red(y/denominator))
assert all(red(P.subs(X,t)-y)==0 for t,y in zip(ts,ys))
out={'interpolant':str(P),'degree':int(S.degree(P,X)),'coefficients_ascending':[str(red(P.coeff(X,i))) for i in range(7)],'is_eighth_cubic':bool(S.degree(P,X)<=3)}
print(json.dumps(out,indent=2),flush=True)
(root/'orbit7_eighth.json').write_text(json.dumps(out,indent=2)+'\n')
