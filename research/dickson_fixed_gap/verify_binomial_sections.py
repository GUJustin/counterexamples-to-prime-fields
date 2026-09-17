"""Independent integer-binomial and full orbit check of section fixtures."""
from pathlib import Path
from math import comb
from collections import Counter
import json

BASE=Path(__file__).resolve().parent


def value(P,x,p):
    v=0
    for a in reversed(P):v=(v*x+a)%p
    return v


def fixture(row,c):
    r,j,k,p,g=(row[key] for key in ('r','section','k','p','generator'))
    e=r*k+j;coeff=[comb(e,r*i+j)%p for i in range(k+1)]
    assert coeff[-1]==1 and coeff[1]!=0
    h=pow(g,2*r,p);orbit=[pow(h,i,p) for i in range(k)]
    assert len(set(orbit))==k and all(pow(x,k,p)==1 for x in orbit)
    audited=[]
    for a in range(2*r):
        xs=[pow(g,a,p)*x%p for x in orbit]
        counts=Counter(value(coeff,x,p) for x in xs)
        mode=max(counts.values());symbol=min(v for v,f in counts.items() if f==mode)
        audited.append([a,mode,symbol,(symbol-pow(g,a*k,p))%p])
    audited.sort(key=lambda a:(-a[1],a[0]))
    assert audited==row['cosets']
    selected=audited[:c];domain=[];word=[]
    for a,mode,symbol,received in selected:
        xs=[pow(g,a,p)*x%p for x in orbit]
        domain+=xs;word += [received]*k
    A=sum(a[1] for a in selected);n=c*k
    candidates=[[(coeff[i]*pow(z,i,p))%p for i in range(k)] for z in orbit]
    assert len({tuple(P) for P in candidates})==k
    assert all(sum(value(P,x,p)==y for x,y in zip(domain,word))==A for P in candidates)
    below=n**n*(p-1)**(n-A)<(n-A)**(n-A)*A**A*p**(n-k)
    return dict(r=r,section=j,k=k,p=p,cosets=c,n=n,A=A,
                distinct_candidates=k,positive_gap=A>k,strict_Elias=below,
                selected_cosets=selected)


def main():
    rows=json.loads((BASE/'binomial_sections_scan.json').read_text())['cases']
    specifications=[(2,1,64,4),(2,1,97,4),(12,1,8,4),(78,0,8,8),(3,0,23,4)]
    fixtures=[fixture(next(row for row in rows if (row['r'],row['section'],row['k'])==(r,j,k)),c)
              for r,j,k,c in specifications]
    summary=[]
    for c in (4,8,16,32):
        hits=[]
        for row in rows:
            if c>2*row['r']:continue
            k,p=row['k'],row['p'];n=c*k;A=sum(x[1] for x in row['cosets'][:c])
            if A<=k:continue
            if n**n*(p-1)**(n-A)<(n-A)**(n-A)*A**A*p**(n-k):
                hits.append(dict(r=row['r'],section=row['section'],k=k,p=p,n=n,A=A))
        summary.append(dict(cosets=c,below_Elias_hits=hits,maximum_k=max((x['k'] for x in hits),default=0)))
    assert all(row['r']==2 and row['section']==1 for row in summary[0]['below_Elias_hits'])
    result=dict(status='PASS',fixtures=fixtures,summary=summary,
                scope='Independent exact coefficient/mode/orbit verification for five fixtures; exact Elias filtering of all recorded modal counts. No asymptotic claim.')
    (BASE/'binomial_sections_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='PASS',fixtures=fixtures,summary=[dict(cosets=x['cosets'],hits=len(x['below_Elias_hits']),maximum_k=x['maximum_k']) for x in summary]),indent=2))


if __name__=='__main__':main()
