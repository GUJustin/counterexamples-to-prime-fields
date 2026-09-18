import json,time
from pathlib import Path
from flint import nmod_mpoly_ctx
P=Path(__file__).parent;outs=[]
for D in json.loads((P/'gate.json').read_text()):
 C=nmod_mpoly_ctx.get(['X','Y'],D['p']);polys=[C.from_dict({tuple(kl):a for kl,a in zip(D['columns'],v) if a}) for v in D['kernel']]
 g=polys[0]
 for f in polys[1:]:g=g.gcd(f)
 out=dict(bank=D['bank'],p=D['p'],common_gcd=str(g),factors=[])
 print(D['bank'],'gcd',g,flush=True)
 for i,f in enumerate(polys):
  start=time.monotonic();a,fs=f.factor();rec=dict(index=i,unit=int(a),factors=[dict(polynomial=str(g),exponent=int(e),degrees=[int(x) for x in g.degrees()]) for g,e in fs],seconds=time.monotonic()-start)
  out['factors'].append(rec);print('basis',i,[(q['degrees'],q['exponent']) for q in rec['factors']],rec['seconds'],flush=True)
 outs.append(out);(P/'factors.json').write_text(json.dumps(outs,indent=2))
