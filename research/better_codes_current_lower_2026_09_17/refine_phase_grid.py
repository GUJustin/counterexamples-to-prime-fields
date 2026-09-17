"""Refine new-source filter with explicit ancestor contexts, no certificate claim."""
import ast,json
import replay_ledger as q
import replay_phase_kernels as ker
for filename,names in [('repeat_phases.py',{'pieces','candidates'}),('search_new_phase.py',{'channel','threshold','potential'})]:
    tree=ast.parse((q.ROOT/filename).read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in names],type_ignores=[]),filename,'exec'))
A=181275;n=262144;w=131071;delta=A-w+1
state=json.loads((q.CACHE/'target31_state.json').read_text());q.POT=[tuple(x) for x in state['pot']];q.rows={(r,v):row for r,v,row in state['rows']}
contexts=[(34,124),(27,79),(25,75),(29,75),(27,70),(27,90),(30,100),(20,75),(30,50),(20,100),(15,100),(10,124)]
envelopes={}
for r,v in contexts:
    row=q.rows[r,v];cuts=sorted(pieces(r,v,row,9276-r-v,len(q.POT)));points=set()
    for lo,stop in zip(cuts,cuts[1:]):
        if lo<stop:points.update(candidates(r,v,row,lo,stop-1,len(q.POT))[0])
    def cap(z):return min(q.line(r,v,z,j) for j in range(len(q.POT)+1) if j==0 or row['threshold'][j-1]<=z)
    envelopes[r,v]={z:cap(z) for z in points}
results=[];tested=0
for m in [125,150,175,200,225,250,275,300,350,400,600,800,1000]:
 for sr in [280,290,300,308,315,325,335,350]:
  for lr in [50000,55000,60000,65000,70000,75000,80000,85000,88902,95000,100000]:
    L=(m*lr+999)//1000;s=m*sr//1000;Y=(A*m+s-1)//w
    tested+=1
    if L<9249 or Y<159 or s<35:continue
    gap=ker.count(A*m,L,s)-n*ker.rank(m,L,s)
    if gap<=0 or threshold(L,Y,s,gap,35,124)>9090:continue
    a,b,c=potential(L,Y,s);prefix=0;origin=None
    for r,v in contexts:
        th=threshold(L,Y,s,gap,r,v);values=envelopes[r,v]
        pts=[(z,val) for z,val in values.items() if z<th]
        if th:
            z=th-1;row=q.rows[r,v]
            val=values.get(z)
            if val is None:val=min(q.line(r,v,z,j) for j in range(len(q.POT)+1) if j==0 or row['threshold'][j-1]<=z)
            pts.append((z,val))
        needed=max([0]+[val-a*(r+v+z)-b*(r+v)-c*r for z,val in pts])
        if needed>prefix:prefix=needed;origin=[r,v]
    results.append(dict(m=m,L=L,s=s,Y=Y,gap=gap,potential=[a,b,c],necessary_local_prefix=prefix,filter_origin=origin,optimistic_binding_source_charge=prefix+a*9249+b*159+c*35))
results.sort(key=lambda x:x['optimistic_binding_source_charge'])
out=dict(tested=tested,feasible=len(results),contexts=contexts,scope='Necessary prefix over12 selected ancestors; excludes other ancestors and full ledger. Ranking only.',best=results[:40])
(q.ROOT/'new_phase_refined_grid.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['best'][:3],indent=2))
