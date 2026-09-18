import json,subprocess
from pathlib import Path
P=Path(__file__).parent;old=json.loads((P.parent/'better_codes_current_lower_2026_09_17/primary_A_small_quotients.json').read_text());want={(160,116,35),(160,116,36),(160,117,35),(160,117,36),(161,117,35),(161,117,36),(163,118,36)};out=[]
for r in old:
 if(r['qcap'],r['m'],r['s'])not in want:continue
 L=-1 if r['required_L'] is None else r['required_L']-1;name='nearby_q%d_m%d_s%d'%(r['qcap'],r['m'],r['s']);subprocess.run(['/tmp/primary_gate',str(P/name),str(r['m']),str(L),str(r['qcap']),str(r['s']),str(r['D'])],check=True)
 subprocess.run(['python3',str(P/'verify_receipt.py'),name],check=True)
 out.append({'name':name,'rectangle':r,'tested_L':L,'optimum':json.loads((P/(name+'.json')).read_text())['maximum_surplus']})
(P/'nearby_a.json').write_text(json.dumps(out,indent=2))
