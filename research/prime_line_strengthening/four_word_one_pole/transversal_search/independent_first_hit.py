"""Independent first-hit verification by Lagrange interpolation over F97."""
from pathlib import Path
import json,itertools
root=Path(__file__).parent
hit=json.loads(root.joinpath('hits.jsonl').read_text().splitlines()[0]);p=hit['p']
def trim(a):
    a=[v%p for v in a]
    while len(a)>1 and a[-1]==0:a.pop()
    return a
def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([v*c for v in a])
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return trim(out)
def ev(a,x):
    out=0
    for c in reversed(a):out=(out*x+c)%p
    return out
def div(a,b):
    a=trim(a);b=trim(b);out=[0]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        k=len(a)-len(b);c=a[-1]*pow(b[-1],-1,p)%p;out[k]=c
        a=add(a,[0]*k+scale(b,-c))
    return trim(out),a
def gcd(a,b):
    while b!=[0]:a,b=b,div(a,b)[1]
    return scale(a,pow(a[-1],-1,p))
def deriv(a):return trim([i*a[i] for i in range(1,len(a))] or [0])
def product(values):
    out=1
    for x in values:out=out*x%p
    return out

a=hit['a'];es=[sum(product(t) for t in itertools.combinations(a,j))%p for j in range(1,5)];e1,e2,e3,e4=es
alpha=e1*e4*pow(e3,-1,p)%p
assert alpha==hit['first_pole']
first_num=[-e3*e4,e2*e3-e1*e4,e3-e1*e2,e1]
# N1/(X-alpha) is the normalized original rational witness.
first_num=scale(first_num,-pow(e3,-1,p))
critical=hit['critical'];phi=[critical,0,1]
def compose(f,g):
    out=[0]
    for c in reversed(f):out=add(mul(out,g),[c])
    return out
G5=compose(first_num,phi)
baseword={}
for i,j in itertools.combinations(range(4),2):
    for sg in (1,-1):
        z=sg*a[i]*a[j]%p
        assert z not in baseword
        baseword[z]=(a[i]*a[i]+a[j]*a[j])%p
assert alpha not in baseword
core={t: ((t*t+critical-alpha)*baseword[(t*t+critical)%p])%p for t in range(p) if (t*t+critical)%p in baseword}
core.update({t:0 for t in range(p) if (t*t+critical)%p==alpha})
assert len(core)==26
beta=hit['new_pole'];ts=hit['nodes'];ws=hit['values']
assert beta not in core and len(set(ts))==12
assert all(t in core and core[t]==v for t,v in zip(ts,ws))
assert all((t*t+critical)%p==z for t,z in zip(ts,hit['base_nodes']))
# Reconstruct N ONLY from the first eight numerator interpolation values.
N=[0]
for i,t in enumerate(ts[:8]):
    basis=[1];den=1
    for j,u in enumerate(ts[:8]):
        if i!=j:basis=mul(basis,[-u,1]);den=den*(t-u)%p
    value=(t-beta)*ws[i]%p
    N=add(N,scale(basis,value*pow(den,-1,p)))
assert len(N)<=8 and ev(N,beta)!=0
matches=[t for t,v in core.items() if ev(N,t)==(t-beta)*v%p]
assert all(t in matches for t in ts)
D=add(N,scale(mul([-beta,1],G5),-1))
core_roots=[t for t in core if ev(D,t)==0]
locator=[1]
for t in core_roots:locator=mul(locator,[-t,1])
residual,rem=div(D,locator)
assert rem==[0] and len(residual)==3
corepoly=[1]
for t in core:corepoly=mul(corepoly,[-t,1])
assert gcd(residual,corepoly)==[1]
assert gcd(residual,deriv(residual))==[1]
assert ev(residual,beta)!=0
fresh=[t for t in range(p) if ev(residual,t)==0]
old_matches=[]
for ai in a:
    Hi=[ai*ai%p,0,pow(ai*ai,-1,p)]
    Gi=mul(add(phi,[-alpha]),compose(Hi,phi))
    old_matches.append(sum(ev(Gi,t)==v for t,v in core.items()))
assert old_matches==[14]*4
assert sum(ev(G5,t)==v for t,v in core.items())==12
result={'p':p,'N_coefficients_ascending':N,'G5_coefficients_ascending':G5,'all_core_matches':matches,'number_core_matches':len(matches),'selected_matches_verified':12,'proper_value_N_at_pole':ev(N,beta),'pole_off_26_core':True,'residual_D_coefficients_ascending':D,'core_roots_D':core_roots,'remaining_quadratic_ascending':residual,'remaining_discriminant':(residual[1]**2-4*residual[0]*residual[2])%p,'remaining_roots_in_Fp':fresh,'remaining_two_distinct_roots_over_closure':True,'remaining_roots_off_core_and_pole':True,'old_four_core_agreements':old_matches,'G5_core_agreements':12,'scope':'Verifies a characteristic97 finite extension witness; no characteristic-zero lift or Jacobian claim.'}
root.joinpath('independent_first_hit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
