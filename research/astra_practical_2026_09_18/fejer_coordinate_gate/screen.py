from pathlib import Path
import json,math
from decimal import Decimal,localcontext
base=Path(__file__).parent
raw=json.loads((base/'coefficients.json').read_text());p=raw['p'];target=274980728111395088
nh=list(map(int,json.loads((base.parents[1]/'better_codes_revisit_2026_09_17/product_distribution.json').read_text())['counts']))
assert len(nh)==256 and sum(nh)==math.comb(255,136)
H={(r['direction'],r['harmonic']):r['values'] for r in raw['coefficients']}
zeroerr=max(abs(H[0,0][h][0]-float(nh[h]))/float(nh[h]) for h in range(256))
rows=[]
for ell in range(1,7):
 ratios=[];amplitudes=[]
 for h in range(256):
  excess=2*sum((1-t/9)*math.hypot(*H[ell,t][h]) for t in range(1,9))
  ratios.append((nh[h]+excess)/p**6/target);amplitudes.append(excess/nh[h])
 rows.append({'direction':ell,'maximum_all_center_triangle_ratio_to_target':max(ratios),'argmax_product_class':ratios.index(max(ratios)),'maximum_relative_fourier_excess':max(amplitudes),'maximum_single_harmonic_relative_amplitude':max(math.hypot(*H[ell,t][h])/nh[h] for h in range(256) for t in range(1,9))})
with localcontext() as ctx:
 ctx.prec=70
 exactbase=str(Decimal(max(nh))/Decimal(p**6)/Decimal(target))
out={'status':'floating-point screening only; no certified error bound','target':str(target),'exact_maximum_mean_to_target':exactbase,'zero_frequency_relative_replay_error':zeroerr,'directions':rows,'center_search_performed':False}
(base/'screen.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
