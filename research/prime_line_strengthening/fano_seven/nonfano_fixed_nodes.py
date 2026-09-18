#!/usr/bin/env python3
"""Exact fixed-node diagnostic, not a global obstruction."""
import sympy as s, json, pathlib, time, sys
start=time.monotonic(); base=pathlib.Path(__file__).resolve().parent
orb=int(sys.argv[1]) if len(sys.argv)>1 else 0
entry=[json.loads(l) for l in (base/'design_orbits.jsonl').read_text().splitlines()][orb]
x=s.Symbol('X'); amps=s.symbols('a b c'); a,b,c=amps
nodes=[0,1,3,7,11,17,23]
W=a*x**4+b*x**5+c*x**6
P={}; L={}
for i in range(1,8):
    L[i]=s.prod(x-nodes[j] for j,C in enumerate(entry['C']) if i not in C)
    P[i]=s.rem(W,s.expand(L[i]),x).expand()
def primitive(f):
    p=s.Poly(f,*amps,domain=s.QQ)
    if p.is_zero:return s.Integer(0)
    return p.monic().as_expr()
bad={}
for i in range(1,8):
    for j in range(i+1,8):
        f=primitive(s.Poly(P[i]-P[j],x).coeff_monomial(x**3))
        bad.setdefault(str(f),[]).append(['pair_degree',i,j])
for j,C in enumerate(entry['C']):
    for i in C:
        f=primitive((P[i]-W).subs(x,nodes[j]))
        bad.setdefault(str(f),[]).append(['extra_quad_match',i,j])
rows=[]; necessary=[]
for T in entry['T']:
    i,j,k=T
    common=[h for h,C in enumerate(entry['C']) if all(v not in C for v in T)]
    divisor=s.prod(x-nodes[h] for h in common)
    f=s.div(P[i]-P[j],divisor,x);g=s.div(P[i]-P[k],divisor,x)
    assert f[1]==0 and g[1]==0
    resultant=s.resultant(f[0],g[0],x)
    factors=s.factor_list(resultant,*amps)[1]
    fs=[]; good=s.Integer(0) if resultant == 0 else s.Integer(1)
    for fac,mult in factors:
        norm=primitive(fac); reason=bad.get(str(norm))
        fs.append({'factor':str(norm),'multiplicity':int(mult),'forbidden_reason':reason})
        if not reason:good*=norm**mult
    rows.append({'triple':T,'common_quad_indices':common,'degrees':[int(s.degree(f[0],x)),int(s.degree(g[0],x))],'factors':fs,'retained_equation':str(s.expand(good))})
    necessary.append(s.expand(good))
out={'scope':'One exact rational quadruple-node specialization only','orbit':orb,'nodes':nodes,'polynomials':{i:str(p) for i,p in P.items()},'forbidden_linear_forms':bad,'triples':rows,'seconds':time.monotonic()-start}
(base/f'nonfano_fixed_nodes_{orb}.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'orbit':orb,'rows':rows,'seconds':out['seconds']},indent=2))
