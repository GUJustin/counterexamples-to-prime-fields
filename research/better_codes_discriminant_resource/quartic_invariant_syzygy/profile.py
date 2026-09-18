import json
from pathlib import Path
from fractions import Fraction
P=Path(__file__).parent;data=json.loads((P.parent/'verify_quartic_remainder_profile.json').read_text());raw=json.loads((P.parent/'quartic_remainder_resource_lp.json').read_text());rows=[];total=0
for r in raw['profile']:
 e,d,c,b=r['G_coefficient_orders'];alpha=min(2*c,b+d,e);beta=min(c+e,b+c+d,2*d,2*b+e,3*c);delta=int(Fraction(r['costs'][0]))
 bounds=[0,alpha+beta-1+int(3*alpha==2*beta),alpha+delta-beta-1+int(delta==3*alpha),beta+delta-2*alpha-1+int(delta==2*beta)]
 bound=max(bounds);total+=r['count']*bound;rows.append({'count':r['count'],'G_orders':r['G_coefficient_orders'],'ord_I':alpha,'ord_J':beta,'ord_Discriminant':delta,'W_bounds':bounds,'W_lower':bound})
out={'rows':rows,'W_total_lower':total,'W_degree_bound':10*131071-2,'slack':10*131071-2-total,'scope':'generic invariant orders of the archived local profile, not arbitrary cancellations'}
(P/'profile.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
