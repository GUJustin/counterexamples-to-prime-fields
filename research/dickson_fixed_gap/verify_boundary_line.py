"""Exact anchored line transfer of the complete p=41 boundary fixture.

Relies on the complete interpolation census for the maximum-agreement
upper bound; independently checks all explicit selected witnesses.
"""
from pathlib import Path
from math import comb
import json

BASE=Path(__file__).resolve().parent
def require(ok,message):
    if not ok: raise AssertionError(message)
def value(poly,x,p):
    v=0
    for a in reversed(poly):v=(v*x+a)%p
    return v
def quotient(poly,tau,c,p):
    a=list(poly);a[0]=(a[0]-c)%p
    out=[0]*(len(a)-1);out[-1]=a[-1]
    for j in range(len(out)-2,-1,-1):out[j]=(a[j+1]+tau*out[j+1])%p
    require((a[0]+tau*out[0])%p==0,'anchor divisibility')
    return out

seed=json.loads((BASE/'three_coset_scan.log').read_text().splitlines()[0])
p=seed['p'];k=seed['r'];domain=sorted(seed['domain']);M=seed['maximum_agreement']
polys=seed['witnesses'];spare=sorted(set(range(1,p))-set(domain))
require(seed['complete'] and seed['interpolation_subsets']==comb(len(domain),k),'complete determining-subset census')
require(len(polys)==seed['maximizing_polynomials']==len({tuple(P) for P in polys}),'distinct maximizing witnesses')
w={x:((1+pow(x,2*k,p))*pow(2,-1,p)-pow(x,k,p))%p for x in domain}
for P in polys:require(sum(value(P,x,p)==w[x] for x in domain)==M,'seed witness agreement')
K=k-1;q=M-K
require(q<=len(spare) and q>0,'enough padding points')
choices=[]
for tau in domain:
    anchored=[quotient(P,tau,w[tau],p) for P in polys if value(P,tau,p)==w[tau]]
    maps={x:{value(P,x,p):i for i,P in enumerate(anchored)} for x in spare}
    chosen=sorted(spare,key=lambda x:(-len(maps[x]),x))[:q]
    choices.append((sum(len(maps[x]) for x in chosen),tau,anchored,maps,chosen))
J,tau,anchored,maps,chosen=max(choices,key=lambda row:(row[0],-row[1]))
full_diversity=sum(len({value(P,x,p) for P in polys}) for x in chosen)
anchor_diversity_sum=sum(sum(len(row[3][x]) for x in chosen) for row in choices)
require(anchor_diversity_sum >= M*full_diversity,'boundary value-diversity averaging')
guaranteed=(M*full_diversity+len(domain)-1)//len(domain)
require(J>=guaranteed,'chosen anchor retains guaranteed diversity')
old=[x for x in domain if x!=tau]
f={x:(w[x]-w[tau])*pow(x-tau,-1,p)%p for x in old}
labels=set();records=[]
for x in chosen:
    for v,i in maps[x].items():
        P=anchored[i];z=(v,-x%p)
        require(z not in labels,'distinct labels in independent basis (1,theta)')
        labels.add(z)
        core=[y for y in old if value(P,y,p)==f[y]]
        extra=[y for y in chosen if (value(P,y,p),0)==(v,(y-x)%p)]
        require(len(core)==M-1 and extra==[x],'exact threshold agreement')
        records.append(dict(label=z,witness=P,agreement=core+extra))
N=len(old)+q
require(J==len(labels),'label count')
require((K-1)+q<M,'nonzero direction cannot have correlated agreement')
# Zero direction: a core witness with M agreements would lift at tau to
# a degree<k seed witness with M+1 agreements, forbidden by the census.
errors=N-M
below_elias=(p-1)**errors*N**N < p**(N-K)*errors**errors*M**M
result=dict(status='PASS',p=p,alphabet='any extension of F_p of degree at least two',
            n=N,k=K,agreement=M,anchor=tau,anchored_list_size=len(anchored),
            padding_points=chosen,distinct_values=[len(maps[x]) for x in chosen],
            nearby_labels=J,no_correlated_agreement_at_threshold=True,
            total_unanchored_value_diversity=full_diversity,
            averaged_anchor_label_guarantee=guaranteed,
            strictly_below_characteristic_elias=below_elias,
            maximum_selected_concurrency_bound=N-M+1,witnesses=records)
(BASE/'boundary_line_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({key:v for key,v in result.items() if key!='witnesses'},indent=2))
