"""Official-centibit endpoint arithmetic and one-coordinate source feasibility."""
import ast,json,decimal
from pathlib import Path
ROOT=Path(__file__).resolve().parent;n=262144;w=131071;A=181283
cells=[]
with decimal.localcontext() as ctx:
 ctx.prec=60
 for a in range(181284,181274,-1):
  # Supremum radius within error cell n-a is (n-a+1)/n, excluded.
  lhs=pow(a-1,12800)*pow(2,6812);rhs=pow(n,12800)
  bits=-decimal.Decimal(128)*(decimal.Decimal(a-1)/n).ln()/decimal.Decimal(2).ln()
  cells.append(dict(agreement=a,errors=n-a,score_supremum=str(bits),cell_can_reach_6812=lhs<rhs))
ns={'__file__':str(ROOT/'audit_primary_sensitivity.py')};exec((ROOT/'audit_primary_sensitivity.py').read_text().split('rows=[]')[0],ns)
C=ns['coeff'];R=ns['rank'];m=115;s=35;L=274277
gap=C(A,m,L,s)-n*R(m,L,s);slope=C(A,m,L+1,s)-n*R(m,L+1,s)-gap
req=L+(-gap)//slope+1;assert C(A,m,req,s)>n*R(m,req,s)
mainA=dict(m=m,s=s,q=(A*m)//w,oldL=L,target_gap=gap,L_slope=slope,required_L=req)
tns={'__file__':str(ROOT/'tcap_fixed_total_repair.py')};exec((ROOT/'tcap_fixed_total_repair.py').read_text().split('# Independent exact')[0].replace('181275','181283'),tns)
tcap=tns['solve'](226,70,9275);local=[]
for mm in range(210,251):
 for ss in range(60,81):
  z=tns['solve'](mm,ss,9275)
  if z is not None:local.append(z)
bestT=min([x for x in local if x['min_total_cap'] is not None],key=lambda x:x['min_total_cap'])
tree=ast.parse((ROOT/'replay_sources.py').read_text());ans={'n':n,'w':w};exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'auxcounts','exec'),ans)
c=ans['coefficients'];r=ans['rank'];aux=[]
for x in json.loads((ROOT/'source_replay.json').read_text())['sources']:
 pars=x['parameters'];oldm,B,s,U,L,k,n0=pars;g=c(A,*pars)-n*r(*pars);feasible=[]
 for mm in range(max(B,s+1),U-s+1):
  p=[mm,B,s,U,L,k,n0];p1=p.copy();p1[4]+=1
  try:g0=c(A,*p)-n*r(*p);sl=c(A,*p1)-n*r(*p1)-g0
  except AssertionError:continue
  if sl<=0:continue
  lr=max(U,mm+B+s,L+(-g0)//sl+1);p[4]=lr
  assert c(A,*p)>n*r(*p)
  feasible.append(dict(m=mm,L=lr))
 best=min(feasible,key=lambda x:x['L'])
 aux.append(dict(index=x['index'],unchanged_gap=g,oldL=L,best=best,necessary_L_increase=max(0,best['L']-L)))
out=dict(official_score_scale=100,cells=cells,one_coordinate_target=A,main_A=mainA,TCap_same_shape=tcap,TCap_local_best=bestT,TCap_local_scope='m210..250,s60..80; exact all-L strong gate within affine regime',auxiliary=aux,scope='Source arithmetic only. Smaller integer-cell progress is not a strict leaderboard score improvement unless centibit score increases.')
(ROOT/'score_cell_probe.json').write_text(json.dumps(out,indent=2)+'\n')
print('cells',[(x['agreement'],x['cell_can_reach_6812'],x['score_supremum'][:16]) for x in cells])
print('primaryA',mainA);print('TCap',tcap,'best',bestT)
print('aux passes',sum(x['unchanged_gap']>0 for x in aux),'maxLdelta',max(x['necessary_L_increase'] for x in aux));print('aux',[(x['index'],x['best'],x['necessary_L_increase']) for x in aux])
