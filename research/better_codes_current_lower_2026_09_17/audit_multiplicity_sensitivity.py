"""Complete multiplicity optimization within the existing closed-rank regime."""
import ast,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
# Load only arithmetic definitions, without rerunning or rewriting source replay.
tree=ast.parse((ROOT/'replay_sources.py').read_text());body=[x for x in tree.body if isinstance(x,ast.FunctionDef)]
ns={'n':262144,'w':131071};exec(compile(ast.Module(body=body,type_ignores=[]),'audited_source_formulas','exec'),ns)
rank,coefficients=ns['rank'],ns['coefficients'];src=json.loads((ROOT/'source_replay.json').read_text())['sources'];rows=[]
for row in src:
 old,B,s,U,L,k,n0=row['parameters'];tested=[]
 for m in range(max(B,s+1),U-s+1):
  pars=[m,B,s,U,L,k,n0]
  if m+B+s>L:continue
  try:
   R=rank(*pars);C=coefficients(181275,*pars)
   higher=pars.copy();higher[4]+=1
   slope=coefficients(181275,*higher)-C-262144*(rank(*higher)-R)
  except AssertionError:continue
  surplus=C-262144*R;minimum=max(U,m+B+s)
  # Linear dependence on L holds on this interval; zero/negative slopes cannot repair upward.
  required=max(minimum,L+((-surplus)//slope+1)) if slope>0 else None
  if required is not None:
   candidate=pars.copy();candidate[4]=required
   assert coefficients(181275,*candidate)-262144*rank(*candidate)>0
   if required>minimum:
    candidate[4]-=1;assert coefficients(181275,*candidate)-262144*rank(*candidate)<=0
  tested.append(dict(m=m,surplus_at_old_L=surplus,L_slope=slope,minimum_feasible_L=required))
 best=min((a for a in tested if a['minimum_feasible_L'] is not None),key=lambda a:a['minimum_feasible_L'])
 winners=[a for a in tested if a['surplus_at_old_L']>0]
 rows.append(dict(index=row['index'],original_parameters=row['parameters'],tested=tested,best=best,nonworsening=winners))
 print(row['index'], 'best m',best['m'],'L',best['minimum_feasible_L'],'oldL',L,'winners',len(winners),flush=True)
 (ROOT/'multiplicity_sensitivity.json').write_text(json.dumps(dict(A=181275,complete=len(rows)==27,scope='All m in B<=m<=U-s satisfying existing closed-rank formula; fixed B,s,U,k,n0.',rows=rows),indent=2)+'\n')
