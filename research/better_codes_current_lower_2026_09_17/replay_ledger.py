"""Replay stored phase, prefix, and final ledger inequalities; not full receipt."""
import ast,json,re,hashlib
from pathlib import Path
from functools import lru_cache
ROOT=Path(__file__).parent
CACHE=ROOT.parents[1]/'tmp/current-lower-primary-cache'
BOUND=274980720549750805
POT=[(4248303575247,216573403547093,979597711315188),(2120670172245,138301398086505,629063470797534),(2120670172245,130746949804972,594247317012549),(1059888080375,56424395768278,255993903460056),(529932236362,28212197884139,127993778342322),(66159929185,4053574205328,18450170718773),(921366594613,113013539884289,518926361601498)]
POT+=POT[3:6]
rows={};hashes={}
for r in range(1,36):
    path=CACHE/f'MovingFiberContextData6811R{r}.lean'
    text=path.read_text();hashes[path.name]=hashlib.sha256(path.read_bytes()).hexdigest()
    refs={}
    def value(s):
        s=s.strip()
        if s in refs:return refs[s]
        return ast.literal_eval(s.replace('#[','[').replace('⟨','[').replace('⟩',']'))
    for name,raw in re.findall(r'^def (cache\w+) : .*? := (.*)$',text,re.M):refs[name]=value(raw)
    for rr,v,body in re.findall(r'def row(\d+)_(\d+) : Numbers := \{\n(.*?)\n\}',text,re.S):
        row={key:value(raw) for key,raw in re.findall(r'^  (\w+) := (.*)$',body,re.M)}
        rows[int(rr),int(v)]=row

def base(row,z):
    b=row['base']
    if z<3:return b[z+2]
    seg=b[5][0]
    for nxt in b[5][1:]:
        if nxt[0]<=z:seg=nxt
    return seg[1]+seg[2]*max(0,z-seg[0])

def basecell(row,lo,hi):
    if lo==hi:return True
    segs=row['base'][5]
    return lo>=3 and (not segs or segs[0][0]<=lo and all(s[0]<=lo or hi<s[0] for s in segs[1:]))

def potential(r,v,z,j):
    a,b,c=POT[j];return a*(r+v+z)+b*(r+v)+c*r

def line(r,v,z,witness):
    if witness==0:return base(rows[r,v],z)
    parent=rows.get((r-1,v),{}).get('prefixValues',[0]*len(POT))
    return potential(r,v,z,witness-1)+parent[witness-1]

@lru_cache(None)
def unit_coeff(y,d):
    zc=(d-1)*(3*d*131073*(1+524284*y)+4*131073*131071*y*(d-1))
    co=(d-1)*3*d*(131073+50213*80861)*y+2*50213*9000000000000
    return zc//(2*50213*d)+1,co//(2*50213*d)+1

def unit(y,z,d):
    a,b=unit_coeff(y,d);return max(9000000000000,a*z+b)

def branch(r,v,z,w,mode):
    t=9275-r-v-z;y=185-r-v;rr=min(y,40-r)
    if mode==0:comp=8728330260*t+7635583765037*y+35730343721378*rr
    elif mode==1:comp=(8728330260+7635583765037)*t+35730343721378*rr
    else:comp=(8728330260+7635583765037+35730343721378)*t
    return line(r,v,z,w)+comp+r*unit(r+v,r+v+z,r)+(40-r)*unit(185-r-v,18992-r-v-z,40-r)+18000000000000+1057030663884726

worst=[];ledger_checks=phase_checks=prefix_checks=0
for (r,v),row in sorted(rows.items()):
    assert 1<=r<=35 and r+v<=159
    for j in range(10):
        parent=rows.get((r-1,v),{}).get('prefixValues',[0]*10)
        assert parent[j]<=row['prefixValues'][j];prefix_checks+=1
        if v:
            assert rows[r,v-1]['prefixValues'][j]<=row['prefixValues'][j];prefix_checks+=1
        start=0
        for stop,w in row['phaseRuns'][j]:
            assert start<stop<=min(row['threshold'][j],9276-r-v) and w<=j
            assert w==0 or row['threshold'][w-1]<=start
            assert w!=0 or basecell(row,start,stop-1)
            for z in [start,stop-1]:
                assert line(r,v,z,w)<=potential(r,v,z,j)+row['prefixValues'][j]
                phase_checks+=1
            start=stop
        assert start==min(row['threshold'][j],9276-r-v)
    start=0;maxval=-1;loc=None
    for stop,w,mode in row['ledgerRuns']:
        assert start<stop<=9276-r-v and w<=10
        assert w==0 or row['threshold'][w-1]<=start
        assert w!=0 or basecell(row,start,stop-1)
        for z in [start,stop-1]:
            val=branch(r,v,z,w,mode)
            assert val<=BOUND,(r,v,z,val)
            ledger_checks+=1
            if val>maxval:maxval=val;loc=[r,v,z,w,mode]
        start=stop
    assert start==9276-r-v
    worst.append(dict(location=loc,upper_bound=maxval,margin=BOUND-maxval))
assert len(rows)==sum(160-r for r in range(1,36))
result=dict(rows=len(rows),phase_endpoint_checks=phase_checks,ledger_endpoint_checks=ledger_checks,
            prefix_checks=prefix_checks,worst=sorted(worst,key=lambda x:x['margin'])[:20],
            primary_hashes=hashes,scope='Stored phases, prefix monotonicity, ledger only. Excludes base/packing/threshold derivations.')
(ROOT/'ledger_replay.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ['primary_hashes','worst']},indent=2))
print(json.dumps(result['worst'][:3],indent=2))
