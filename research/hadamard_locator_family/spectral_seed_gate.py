"""One exact nonsymmetric seed, one spectral-derivative ansatz, no scan."""
import itertools,json,time
from pathlib import Path
import sympy as s
X,z=s.symbols('X z');us=[1,2,4,8]
P=[s.Poly(u*X**2+u*u*X+u**3,X,domain=s.QQ) for u in us]
diff=[P[i]-P[j] for i in range(4) for j in range(i)]
locator=s.Poly(1,X,domain=s.QQ)
for f in diff:locator*=f.monic()
assert locator.degree()==12 and s.gcd(locator,locator.diff()).degree()==0
D=[s.prod(P[i]-P[j] for j in range(4) if i!=j) for i in range(4)]
C=[int(f.LC()) for f in D]
assert len(set(C+[-c for c in C]))==8
out={'seed_parameters':us,'seed_polynomials':[str(f.as_expr()) for f in P],
     'spectral_leading_coefficients':C,'old_locator':str(locator.as_expr()),
     'old_locator_squarefree':True,'ansatz':'P_i + sign_i*z*product_(j!=i)(P_i-P_j)',
     'patterns':[]}
for tail in itertools.product([-1,1],repeat=3):
    signs=(1,)+tail
    aa=[signs[i]*D[i]-D[0] for i in range(1,4)]
    bb=[P[i]-P[0] for i in range(1,4)]
    minors=[aa[i]*bb[j]-aa[j]*bb[i] for i in range(3) for j in range(i)]
    g=s.Poly(0,X,domain=s.QQ)
    for f in minors:g=s.gcd(g,f)
    raw=g
    assert g # No positive-dimensional coincidence family in this seed.
    while True:
        h=s.gcd(g,locator)
        if h.degree()==0:break
        g=g.exquo(h)
    rec={'signs':signs,'minor_degrees':[f.degree() for f in minors],
         'raw_gcd':str(raw.as_expr()),'off_domain_gcd':str(g.monic().as_expr())}
    if g.degree()>0:
        rec['lambda_resultants']=[str(s.resultant(g.as_expr(),a.as_expr()*z+b.as_expr(),X)) for a,b in zip(aa,bb)]
    out['patterns'].append(rec)
out['off_domain_root_degrees']=[s.Poly(r['off_domain_gcd'],X).degree() for r in out['patterns']]
out['scope']='Complete sign-pattern coincidence gate for this single seed and common spectral scale; no general gluing exclusion.'
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
