"""Independent small-field checks of averaging, filtering, and modal bank bound."""
from math import comb
from collections import Counter
from pathlib import Path
import json

def ev(c,x,p):
    return sum(v*pow(x,j,p) for j,v in enumerate(c))%p

rows=[]
for p,r,d in [(37,3,3),(41,5,2),(61,3,5),(89,11,2),(101,5,5)]:
    k=d*r;e=2*k+1
    mu_d=[z for z in range(1,p) if pow(z,d,p)==1]
    mu_2d=[z for z in range(1,p) if pow(z,2*d,p)==1]
    mu_r=[z for z in range(1,p) if pow(z,r,p)==1]
    domain=[z for z in range(1,p) if pow(z,4*r,p)==1]
    H=[comb(e,2*j+1)%p for j in range(k)]
    V=[comb(e,2*d*j+1)%p for j in range(r)]
    assert len(mu_d)==d and len(domain)==4*r and V[-1]!=0
    for x in range(1,p):
        averaged=sum(ev(H,z*x%p,p) for z in mu_d)*pow(d,-1,p)%p
        assert averaged==ev(V,pow(x,d,p),p)
    for s in range(1,p):
        x=s*s%p
        filtered=sum(pow(z,-1,p)*pow(1+z*s,e,p) for z in mu_2d)*pow(2*d*s,-1,p)%p
        assert filtered==(ev(V,pow(x,d,p),p)+pow(x,k,p))%p
    cosets={u:[y for y in domain if pow(y,r,p)==u] for u in {pow(y,r,p) for y in domain}}
    word={};M=0
    for ys in cosets.values():
        frequencies=Counter(ev(V,y,p) for y in ys)
        mode,peak=max(frequencies.items(),key=lambda q:(q[1],q[0]))
        M+=peak
        for y in ys:word[y]=mode
    agreements=[sum(ev(V,y*pow(a,-1,p)%p,p)==word[y] for y in domain) for a in mu_r]
    assert set(agreements)=={M}
    # Direct double count for unrelated arbitrary words.
    for t in range(5):
        w={y:(y*y+t*y+t)%p for y in domain}
        counts=[sum(ev(V,y*pow(a,-1,p)%p,p)==w[y] for y in domain) for a in mu_r]
        assert sum(counts)<=r*M
    stored=json.loads(Path(__file__).with_name('reynolds_surplus_checks.json').read_text())
    original=next(z for z in stored['rows'] if (z['p'],z['r'],z['d'])==(p,r,d))
    assert original['optimal_bank_agreement']==M
    W={y:((1+pow(y,2*r,p))*pow(2,-1,p)-pow(y,r,p))%p for y in domain}
    assert original['agreement']==sum(ev(V,y,p)==W[y] for y in domain)
    rows.append(dict(p=p,r=r,d=d,optimal_bank_agreement=M,checks='passed'))
out=dict(fixtures=rows,scope='Independent averaging on every nonzero x; filter on every square x; all rotation candidates and five arbitrary-word double counts.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
