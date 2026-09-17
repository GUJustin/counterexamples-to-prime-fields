"""Check the exact integer weighted-intersection threshold, not a grid claim."""
import json
checks=0
for D in range(1,41):
 for u in range(31):
  for s in range(31):
   N=u+s
   k=min(N,(D+2*u+2*s)//3,(D+5*u+4*s)//6)
   for b in range(N+1):
    misses=3*(N-b)
    weight=max(0,N-misses)+max(0,s-misses)
    assert (weight>D)==(b>k),(D,u,s,b,k,weight)
    checks+=1
   if u==0:assert k==min(s,(2*s+D//2)//3)
print(json.dumps(dict(weighted_threshold_checks=checks,passed=True),indent=2))
