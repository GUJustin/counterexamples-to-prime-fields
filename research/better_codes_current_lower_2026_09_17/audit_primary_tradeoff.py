import ast,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parent
T=ast.parse((ROOT/'audit_primary_sensitivity.py').read_text());ns={'math':math,'w':131071,'n':262144}
exec(compile(ast.Module(body=[x for x in T.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'primary_arithmetic','exec'),ns)
rank,coeff=ns['rank'],ns['coeff'];out=[]
for name,m0,L0,s0 in [('A',115,274277,35),('B',134,18992,40),('TCap',226,9281,70)]:
 rows=[]
 for m in range(m0,m0+9):
  for s in range(s0-2,s0+3):
   try:
    gap=coeff(181275,m,L0,s)-262144*rank(m,L0,s)
    slope=coeff(181275,m,L0+1,s)-coeff(181275,m,L0,s)-262144*(rank(m,L0+1,s)-rank(m,L0,s))
   except AssertionError:continue
   if slope<=0:continue
   q=(181275*m)//131071;L=max(m+s-1,q,L0+(-gap)//slope+1)
   assert coeff(181275,m,L,s)>262144*rank(m,L,s)
   rows.append(dict(m=m,s=s,q=q,L=L))
 pareto=[a for a in rows if not any(all(b[k]<=a[k] for k in ['s','q','L']) and any(b[k]<a[k] for k in ['s','q','L']) for b in rows)]
 out.append(dict(name=name,range_m=[m0,m0+8],range_s=[s0-2,s0+2],pareto=pareto))
 print(name,pareto,flush=True)
(ROOT/'primary_tradeoff.json').write_text(json.dumps(out,indent=2)+'\n')
