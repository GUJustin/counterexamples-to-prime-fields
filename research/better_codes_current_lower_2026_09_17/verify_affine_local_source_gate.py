import json
from pathlib import Path
from affine_local_source_gate import solve,channel,coefficient_count,rank
checks=0
for w in (5,7,11):
 for D in range(w,5*w):
  for s in range(min(D//w,4)+1):
   L=max(D//w,(D+s-1)//w)
   for extra in (0,1,3):
    LL=L+extra
    brute=sum((D-(w-1)*h-w*a)*(LL+1-h-a) for h in range(s+1) for a in range(LL+1-h) if D-(w-1)*h-w*a>0)
    assert coefficient_count(D,LL,s,w)==brute,(w,D,s,LL)
    checks+=1
for Y in range(9):
 for S in range(9):
  for extra in (0,1,7):
   T=Y+extra;brute=sum(T+1-i-j for i in range(S+1) for j in range(Y+1) if i+j<=Y)
   assert channel(T,Y,S)==brute,(T,Y,S,channel(T,Y,S),brute)
   checks+=1
samples=[]
for m,s in ((1000,304),(4700,1432),(14000,4267),(64000,19840)):
 for t in (3200,3261,4000):
  got=solve(m,s,12,55,t,gate_t=9678);samples.append(got)
  if 'affine_lower_L' not in got:continue
  L0=got['affine_lower_L'];slope=got['slope'];f0=got['value_at_lower'];w=131071;delta=50205;Y=got['Y'];fuel=got['fuel']
  for L in (L0+2,L0+12345,max(L0,got['characteristic_upper_L'])):
   dc=w*55-12;Dh=max(0,w*(Y+1)-s-dc);band=0
   assert min(L//t,Y//55,s//12)==fuel
   for h in range(1,fuel+1):
    ss=s-h*12;eff=min(Y-h*55,max(0,Dh+ss-1)//w);band+=delta*channel(L-h*t,eff,ss);Dh=max(0,Dh-delta-dc)
   value=coefficient_count(181275*m,L,s)-262144*rank(m,L,s)-band
   assert value==f0+slope*(L-L0);checks+=1
out=dict(passed=True,exact_checks=checks,samples=samples,scope='Small coefficient/channel brute counts and nonadjacent exact affinity checks; explicit interval theorem in companion note.')
(Path(__file__).parent/'affine_local_source_gate_audit.json').write_text(json.dumps(out,indent=2)+'\n');print('passed',checks,'exact checks');print('feasible',[(x['m'],x['t'],x.get('minimum_L')) for x in samples if x['feasible']])
