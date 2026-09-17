import ast,json,sys
from pathlib import Path
from fractions import Fraction
from exact_slab import slab,thin
ROOT=Path(__file__).parent
OTHER=ROOT.parent/'better_codes_current_lower_2026_09_17'
sys.path.insert(0,str(OTHER));from fast_firstjet_count import coefficient_count
source=ast.parse((OTHER/'replay_phase_kernels.py').read_text());exec(compile(ast.Module(body=[x for x in source.body if isinstance(x,ast.FunctionDef) and x.name=='rank'],type_ignores=[]),'rank','exec'))
m=28000;s=8529;A=181275;w=131071;n=262144;D=A*m;Y=(D+s-1)//w;width=A-w+1
rows=[]
for lam in [130,260,520]:
 L=lam*m;gap=coefficient_count(D,L,s)-n*rank(m,L,s)
 for z in [2950,3206]:
  old=thin(D,L,Y,s,12,43,z,width,exact=False);new=thin(D,L,Y,s,12,43,z,width,exact=True)
  rows.append(dict(m=m,s=s,L=L,Y=Y,z=z,gap=gap,old_exactD_thin=old,slab_thin=new,saved=old-new,old_margin=float(Fraction(gap-old,w*m**4)),exact_slab_margin=float(Fraction(gap-new,w*m**4)),passes=new<gap))
out=dict(scope='Exact arithmetic gate only; no characteristic/helper/full-certificate claim',rows=rows)
(ROOT/'exact_slab_evaluations.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
