"""Independent candidate replay and exhaustive small optimization checks."""
from itertools import combinations,product
from math import comb,isqrt
from pathlib import Path
import json
BASE=Path(__file__).resolve().parent


def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))


def replay(row,brute=False):
    r,k,j,H,shift,p,g=(row[x] for x in ('r','k','section','H','shift','p','generator'))
    assert p==2*r*k+1 and prime(p)
    assert len({pow(g,i,p) for i in range(p-1)})==p-1
    coeff=[comb(r*k+j,r*i+j)%p for i in range(k+1)]
    def G(x):
        # Integer coefficient dot product, independently of search's Horner routine.
        powers=[1]
        for _ in range(k):powers.append(powers[-1]*x%p)
        return sum(a*b for a,b in zip(coeff,powers))%p
    full=[G(x) for x in range(p)]
    C=(p-1)//H
    subgroup=[pow(g,C*i,p) for i in range(H)]
    a=pow(g,(p-1)//k*shift,p)
    candidates=subgroup+[a*h%p for h in subgroup]
    assert len(set(candidates))==2*H and coeff[1]!=0 and coeff[-1]==1
    assert all(pow(h,k,p)==1 for h in candidates)
    cosets=[[pow(g,t,p)*h%p for h in subgroup] for t in range(C)]
    selected=row['selected_cosets']
    domain=[x for t,v,left,right in selected for x in cosets[t]]
    word=[(v-pow(x,k,p))%p for t,v,left,right in selected for x in cosets[t]]
    assert len(domain)==row['n']==len(set(domain))
    counts=[sum((full[h*x%p]-pow(x,k,p))%p==v for x,v in zip(domain,word)) for h in candidates]
    assert min(counts)==row['A'] and counts==[row['group_agreements'][0]]*H+[row['group_agreements'][1]]*H
    n,A=row['n'],row['A']
    elias=A>k and n**n*(p-1)**(n-A)<(n-A)**(n-A)*A**A*p**(n-k)
    assert elias==row['below_elias']
    out={x:row[x] for x in ('r','k','section','H','shift','p','n','L','A','below_elias')}
    if brute:
        # Enumerate every invariant-domain/word choice, without the DP or its Pareto pruning.
        vectors=[]
        for xs in cosets:
            vals={full[x] for x in xs}|{full[a*x%p] for x in xs}
            vectors.append([(sum(full[x]==v for x in xs),sum(full[a*x%p]==v for x in xs)) for v in vals])
        best=-1;checked=0
        for selected_indices in combinations(range(C),n//H):
            for choices in product(*(vectors[t] for t in selected_indices)):
                checked+=1
                best=max(best,min(sum(x[0] for x in choices),sum(x[1] for x in choices)))
        assert best==A
        out.update(brute_choices=checked,brute_optimum=best)
    return out


def main():
    census=json.loads((BASE/'scan.json').read_text())
    assert census['status']=='complete'
    expected={(r,k,j,k//4,1) for k in (32,64,128) for r in range(2,49)
              if prime(2*r*k+1) for j in {0,1,r//2,r-1}}
    assert {(x['r'],x['k'],x['section'],x['H'],x['shift']) for x in census['rows']}==expected
    checked=[replay(row) for row in census['rows']]
    small=[replay(row,True) for row in json.loads((BASE/'small_fixtures.json').read_text())]
    pilot=json.loads((BASE/'pilot.json').read_text())
    control=next(x for x in pilot['rows'] if x['shift']==2)
    old=json.loads((BASE.parent/'dickson_fixed_gap/subgroup_sections_scan.json').read_text())
    match=next(x for x in old if (x['r'],x['k'],x['section'],x['L'])==(control['r'],control['k'],control['section'],control['L']))
    assert control['A']==dict(match['agreements'])[4]
    out=dict(status='passed',cases=len(checked),positive_gap=[x for x in checked if x['A']>x['k']],below_elias=[x for x in checked if x['below_elias']],small_exhaustive=small,subgroup_control_agreement=control['A'],scope='All exhibited candidate lists replayed. DP optima independently exhausted in four small fixtures; large-instance optimality rests on the stated recurrence. No asymptotic growing short-domain list claim.')
    (BASE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
