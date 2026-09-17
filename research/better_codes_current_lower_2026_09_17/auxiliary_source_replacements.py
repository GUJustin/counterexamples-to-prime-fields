"""Explicit target-A auxiliary source replacement manifest; no receipt claim."""
import ast,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ns={'n':262144,'w':131071};tree=ast.parse((ROOT/'replay_sources.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'counts','exec'),ns)
rank=ns['rank'];coeff=ns['coefficients'];A=181275;n=262144;w=131071;pchar=2130706433
prev=json.loads((ROOT/'multiplicity_sensitivity.json').read_text())['rows'];out=[]
for row in prev:
 old=row['original_parameters'];new=old.copy();new[0]=row['best']['m'];new[4]=max(old[4],row['best']['minimum_feasible_L'])
 m,B,s,U,L,k,n0=new
 gates=dict(two_s_le_B=2*s<=B,B_le_U=B<=U,U_le_L=U<=L,k_le_s=k<=s,s_lt_m=s<m,k1_le_n0=k+1<=n0,reserve_le_B=2*(n0-k-1)<=B,s_lt_char=s<pchar,k_lt_m=k<m,closed_B_le_m=B<=m,closed_m_s_le_U=m+s<=U,closed_m_B_s_le_L=m+B+s<=L)
 cutoff_caps=[(m*A-(h if h<n0 else k)*(A-(w-2))+B-1)//w for h in range(s+1)]
 gates['all_cutoff_caps']=min(cutoff_caps)>=U
 C=coeff(A,*new);R=rank(*new);gates['positive_kernel']=C>n*R
 assert all(gates.values())
 oldflag=[old[4]-old[3],old[3]-old[1]+old[6],old[1]-2*(old[6]-old[5]-1)]
 newflag=[L-U,U-B+n0,B-2*(n0-k-1)]
 def pairgates(r,y,t):
  rightR=B+s*(r-1);rightY=U+s*(y-1);rightT=L+s*(t-1)
  mix=[r*rightT+t*rightR,y*rightT+t*rightY,y*rightR+r*rightY]
  assert max([r,y,t]+mix)<pchar
  return dict(left=[r,y,t],right_helper=[rightR,rightY,rightT],mixed=mix,char_margin=pchar-max(mix))
 out.append(dict(index=row['index'],old=old,replacement=new,geometry_unchanged=new[1:]==old[1:],L_increase=L-old[4],old_flag=oldflag,new_flag=newflag,flag_delta=[a-b for a,b in zip(newflag,oldflag)],coefficient_count=C,rank_bound=R,nullity=C-n*R,gates=gates,min_cutoff_cap=min(cutoff_caps),helper_gate_catalog_corner=pairgates(31,142,7501),helper_gate_expanded_corner=pairgates(36,163,9678)))
text=(ROOT/'MovingFiberCatalog6811.lean').read_text().split('def groups :')[1].split('theorem wellFormed')[0]
groups=[[int(i) for i in re.findall(r'source(\d+)',v)] for v in re.findall(r'!\[([^\[\]]+)\]',text)]
assert len(groups)==16 and all(len(g)==3 for g in groups)
group_rows=[]
for g,ids in enumerate(groups):
 group_rows.append(dict(group=g,choice=g+1,sources=ids,old_source_limit=max(out[i]['old'][4] for i in ids),new_source_limit=max(out[i]['replacement'][4] for i in ids),changed_sources=sorted(set(i for i in ids if not out[i]['geometry_unchanged']))))
result=dict(target_A=A,target_errors=n-A,target_gap=A-w,target_reserve_gap=A-(w-2),parameter_order=['m','B','s','U','L','k','n0'],sources=out,groups=group_rows,scope='Exact source dimension, all listed well-formed/cutoff gates, and helper characteristic gates; target identity checked separately in auxiliary_geometry_audit; receipt regeneration not certified.')
(ROOT/'auxiliary_source_replacements.json').write_text(json.dumps(result,indent=2)+'\n')
print('verified',len(out),'sources; maxL',max(x['replacement'][4] for x in out))
print('replacements',[(x['index'],x['replacement'][0],x['replacement'][4],x['L_increase']) for x in out])
print('limits',[(x['group'],x['old_source_limit'],x['new_source_limit']) for x in group_rows])
