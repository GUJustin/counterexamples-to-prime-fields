"""Exact graph-factor lines, with independent interpolation and synthetic division."""
import json,time
from pathlib import Path
from flint import nmod_poly,nmod_mpoly_ctx
P=Path(__file__).parent
D=next(d for d in json.loads((P.parent/'gate.json').read_text()) if d['bank']=='paley')
B=json.loads((P.parents[1]/'quadratic_one_pole_route'/'fiber_patterns.json').read_text())
p=29;X=nmod_poly([0,1],p);one=nmod_poly([1],p);zero=nmod_poly([],p)
def pol(v):return nmod_poly(v,p)
def arr(f):return [int(f[i]) for i in range(f.degree()+1)]
forms=[]
for v in D['kernel']:
    forms.append([pol([sum(a for (i,l),a in zip(D['columns'],v) if i==k and l==j)%p
                      for k in range(35-3*j)]) for j in range(11)])
out={'p':p,'lines':[]}
for label in range(7):
    support=[j for j,m in enumerate(B['masks']) if label in m]
    assert len(support)==7
    f=zero
    for j in support[:4]:
        L=one;den=1
        for k in support[:4]:
            if k!=j:L*=X-B['base'][k];den=den*(B['base'][j]-B['base'][k])%p
        f+=L*(B['word'][j]*pow(den,-1,p)%p)
    actual=[j for j,(x,y) in enumerate(zip(B['base'],B['word'])) if int(f(x))==y]
    assert actual==support and f.degree()==3
    locator=one
    for j in support:locator*=(X-B['base'][j])**(4 if j<7 else 6)
    assert locator.degree()==34
    lam=[]
    for coeff in forms:
        value=zero
        for c in reversed(coeff):value=value*f+c
        scalar=int(value[34]);assert value==locator*scalar;lam.append(scalar)
    pivot=next(i for i,a in enumerate(lam) if a)
    normalized=[a*pow(lam[pivot],-1,p)%p for a in lam]
    linebasis=[];quotients=[]
    for free in range(3):
        if free==pivot:continue
        v=[0]*3;v[free]=1;v[pivot]=-lam[free]*pow(lam[pivot],-1,p)%p
        coeff=[sum((forms[i][j]*v[i] for i in range(3)),zero) for j in range(11)]
        quotient=[zero for _ in range(10)];quotient[9]=coeff[10]
        for j in range(9,0,-1):quotient[j-1]=coeff[j]+f*quotient[j]
        assert coeff[0]+f*quotient[0]==zero
        # Replay every coefficient of (Y-f)*quotient.
        for j in range(11):
            rebuilt=(quotient[j-1] if j else zero)-(f*quotient[j] if j<10 else zero)
            assert rebuilt==coeff[j]
        linebasis.append(v);quotients.append([arr(c) for c in quotient])
    out['lines'].append({'label':label,'cubic':arr(f),'support':support,
                         'lambda':lam,'normalized_lambda':normalized,
                         'line_basis':linebasis,'quotient_basis':quotients})
assert len({tuple(v['normalized_lambda']) for v in out['lines']})==7
(P/'old_graph_lines.json').write_text(json.dumps(out,indent=2))
print('All seven distinct graph-factor lines and fourteen divisions verified',flush=True)
# One generic line over F29(z), represented as a primitive trivariate polynomial.
C=nmod_mpoly_ctx.get(['X','Y','z'],p);terms={}
for zexp,coeffs in enumerate(out['lines'][0]['quotient_basis']):
    for j,coeff in enumerate(coeffs):
        for i,a in enumerate(coeff):
            if a:terms[i,j,zexp]=a
g=C.from_dict(terms);tick=time.monotonic();unit,factors=g.factor()
out['generic_first_line_quotient_factorization']={'unit':int(unit),'seconds':time.monotonic()-tick,
    'factors':[{'polynomial':str(h),'exponent':int(e),'degrees':list(map(int,h.degrees()))}
               for h,e in factors]}
(P/'old_graph_lines.json').write_text(json.dumps(out,indent=2))
print('Generic quotient factors:',[(list(map(int,h.degrees())),int(e)) for h,e in factors],flush=True)
