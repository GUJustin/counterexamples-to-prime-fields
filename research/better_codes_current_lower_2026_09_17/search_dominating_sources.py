"""Bounded local search for dimension-feasible sources with no larger caps."""
import json,itertools
from replay_sources import ROOT,rank,coefficients

baseline=json.loads((ROOT/'source_replay.json').read_text())['sources']
results=[];tried=0
for row in baseline:
    m,B,s,U,L,k,n0=row['parameters']
    winners=[]
    for dm,dB,ds,dU in itertools.product(range(-2,3),[-1,0],[-1,0],[-1,0]):
        pars=[m+dm,B+dB,s+ds,U+dU,L,k,n0]
        mm,BB,ss,UU,*_=pars
        if not (2*ss<=BB<=mm and mm+ss<=UU and mm+BB+ss<=L and k<=ss<mm):continue
        tried+=1
        try:
            R=rank(*pars);C=coefficients(181275,*pars)
        except AssertionError:continue
        if C>262144*R:
            winners.append(dict(parameters=pars,surplus=C-262144*R))
    results.append(dict(index=row['index'],winners=winners))
result=dict(target_A=181275,parameter_ranges=dict(dm=[-2,2],dB=[-1,0],ds=[-1,0],dU=[-1,0],L='unchanged',k='unchanged',n0='unchanged'),
            tested=tried,results=results,
            scope='Dimension-feasible candidates only; downstream proof and complete case coverage not audited.')
(ROOT/'dominating_source_search.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(tested=tried,sources_with_candidates=sum(bool(x['winners']) for x in results),
                     winners=[(x['index'],len(x['winners'])) for x in results if x['winners']]),indent=2))
