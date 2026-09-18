"""Independent DFT degree/support verification of retained finite candidates."""
import json
from pathlib import Path
P=Path(__file__).parent
a=json.loads((P/'survivors.json').read_text());p=a['p'];z=a['root']
assert pow(z,48,p)==1 and pow(z,24,p)!=1 and pow(z,16,p)!=1
word=[(pow(z,12*i,p)-1)**2*pow(2,-1,p)%p for i in range(48)]
allv=set();out=[]
for row in a['candidates']:
 v=row['values']; coeff=[sum(v[i]*pow(z,(-i*j)%48,p) for i in range(48))*pow(48,-1,p)%p for j in range(48)]
 assert not any(coeff[12:]); assert [i for i in range(48) if v[i]==word[i]]==row['support']; assert len(row['support'])==16
 for t in range(12):allv.add(tuple(v[4*t:]+v[:4*t]))
 out.append({'coefficients':coeff[:12],'support':row['support'],'nonzero_degrees':[j for j,c in enumerate(coeff) if c]})
assert len(allv)==9
(P/'survivors.verified.json').write_text(json.dumps({'passed':True,'total':len(allv),'orbits':out},indent=2)+'\n')
print(out)
