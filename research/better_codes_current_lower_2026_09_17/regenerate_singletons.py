"""Exact target singleton envelopes on a bounded r chunk, using repaired roots."""
import ast,json,sys
import replay_ledger as q
import repaired_auxiliary_roots as roots
for filename,names in [('base_packing_audit.py',{'mix','cost','safe'}),('search_new_phase.py',{'channel','threshold'})]:
 tree=ast.parse((q.ROOT/filename).read_text().replace('9275','9678').replace('9276','9679'))
 exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
A=181275;n=262144;w=131071;delta=A-w+1
lo_r,hi_r=map(int,sys.argv[1:3])
source=json.loads((q.ROOT/'target_thresholds_1_7.json').read_text())['sources']
new=json.loads((q.ROOT/'new_phase_refined_finalist_0.json').read_text())['candidate']
source.append([new['L'],new['Y'],new['s'],new['gap']])
pot=json.loads((q.ROOT/'expanded_total_all_contexts.json').read_text())['potentials'];pot=pot[:7]+pot[-1:]
old={}
for ll,hh in [(1,7),(8,14),(15,21),(22,28),(29,35)]:
 for row in json.loads((q.ROOT/f'target_thresholds_{ll}_{hh}.json').read_text())['rows']:old[row['r'],row['v']]=row['threshold'][:7]
slopes=[320000000000000,160000000000000,80000000000000,40000000000000,20000000000000,10000000000000,4000000000000,0]
# Read actual sheet order rather than relying on list above.
import re
slopes=[int(re.search(r'def slope : Nat := (\d+)',(q.CACHE/f'MovingFiberPackingData6811S{j}.lean').read_text())[1]) for j in range(8)]
results=[];checks=0;segment_count=0
for r in range(lo_r,hi_r+1):
 for v in range(164-r):
  y=r+v;finish=9679-y
  previous=old.get((r,v));ts=[]
  for j,(L,Y,S,g) in enumerate(source):
   z=previous[j] if previous and j<7 and previous[j]<9276-y else threshold(L,Y,S,g,r,v)
   ts.append(z)
  segments=[]
  for j,(a,b,c) in enumerate(pot):
   if ts[j]<finish:segments.append((ts[j],finish-1,a,(a+b)*y+c*r))
  if r<=32 and y<=149 and safe(r,y):
   end=min(finish-1,8121-y)
   for z in range(min(2,end)+1):segments.append((z,z,0,cost(r,v,z)))
   if end>=3:
    a=cost(r,v,4)-cost(r,v,3);segments.append((3,end,a,cost(r,v,3)-3*a))
  for group in range(16):
   domain=roots.root_domain(group,r,v)
   if domain is None:continue
   lo,hi=domain;hi=min(hi,finish-1)
   if lo>hi:continue
   lines=roots.root_lines(group,r,v);cuts={lo,hi+1}
   for k,(a,b) in enumerate(lines):
    for aa,bb in lines[:k]:
     if a!=aa:
      cross=(bb-b)//(a-aa)
      cuts.update(x for x in [cross,cross+1] if lo<x<=hi)
   cuts=sorted(cuts)
   for left,stop in zip(cuts,cuts[1:]):
    a,b=max(lines,key=lambda ab:ab[0]*left+ab[1]);segments.append((left,stop-1,a,b))
  points={0,finish-1}
  for k,(lo,hi,a,b) in enumerate(segments):
   points.update(x for x in [lo-1,lo,hi,hi+1] if 0<=x<finish)
   for ll,hh,aa,bb in segments[:k]:
    if a==aa:continue
    left,right=max(lo,ll),min(hi,hh)
    if left>right:continue
    cross=(bb-b)//(a-aa)
    points.update(x for x in [cross,cross+1] if left<=x<=right)
  own=[0]*8
  for z in points:
   options=[a*z+b for lo,hi,a,b in segments if lo<=z<=hi]
   assert options,('uncovered',r,v,z)
   bound=min(options)
   for j,slope in enumerate(slopes):own[j]=max(own[j],bound-slope*z)
   checks+=1
  results.append(dict(r=r,v=v,threshold=ts,own=own));segment_count+=len(segments)
 print('r',r,'done',flush=True)
out=dict(A=A,total=9678,r_range=[lo_r,hi_r],slopes=slopes,rows=results,critical_point_checks=checks,segments=segment_count,scope='Regenerated target singleton envelopes: repaired27auxiliary sources,8phase sources, unchanged conservative carrier domain. Arithmetic for target port, not complete certificate.')
(q.ROOT/f'regenerated_singletons_{lo_r}_{hi_r}.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(rows=len(results),critical_points=checks,segments=segment_count)))
