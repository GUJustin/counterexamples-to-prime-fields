"""Exact tiny-field checks, independent of symbolic solution counting."""
import json
p=7; S=set(range(4)); D=1; A=5
rows=[]; solutions=0
for z in range(p):
 for a in range(p):
  for c in range(p):
   h=(a-z)%p
   # Q=h*(h+R0(X)*(X-z)); leading coefficient h rules out h!=0.
   if h: continue
   solutions+=1
   matches=[x for x in range(p) if (a*x+c- (z*x if x in S else z*x+z-x))%p==0]
   if len(matches)<A: continue
   common=any(all((b*x+d-(x if x in S else x+1))%p==0 for x in matches) for b in range(p) for d in range(p))
   regular=[]
   for x in matches:
    r=1
    for y in S:r=r*(x-y)%p
    if (r*(x-z)+2*h)%p:regular.append(x)
   assert not common and not regular
   rows.append(dict(z=z,a=a,c=c,matches=matches,nonsingular=regular))
assert solutions==49 and [r['z'] for r in rows]==[4,5,6]
xs=[0,1,2,4]; f=[6,0,0,0]; g=[1,4,2,4]
polys=[(0,0),(1,0),(0,1)]
counts=[sum((a*x+c-fv-z*gv)%p==0 for x,fv,gv in zip(xs,f,g)) for z,(a,c) in enumerate(polys)]
assert counts==[3,3,3]
assert tuple((polys[2][i]-2*polys[1][i]+polys[0][i])%p for i in range(2))!=(0,0)
result=dict(polynomial_label_pairs=343,solutions=solutions,nearby_bad_pairs=rows,triple_boundary_counts=counts,passed=True)
print(json.dumps(result,indent=2))
