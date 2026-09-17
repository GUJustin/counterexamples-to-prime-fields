"""All-codeword checks after reducing the code dimension within an orbit."""
from pathlib import Path
from array import array
import json,time
from check_exhaustive import audit,replay_line
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 start=time.monotonic();rows=[]
 # Reuse a fully audited extra-coordinate fixture, then classify the
 # smaller code independently via its own interpolation pencils.
 source=json.loads((BASE/'negative_verification.json').read_text())
 line=next(r['exhaustive_line'] for r in source['rows'] if r['p']==1009 and r['d']==3 and r['D']==2)
 roots=line['core_roots']+line['extra_roots']+[line['padding_radical']]
 rows.append(replay_line(1009,3,3,2,1,line['q'],roots,line['omega'],2))
 p=65521;d=5;inv=array('I',[0])*p;inv[1]=1
 for i in range(2,p):inv[i]=p-(p//i)*inv[p%i]%p
 source=audit(p,d,2,1,0,inv,False);line=source['exhaustive_line'];assert line
 roots=line['core_roots']+[line['padding_radical']]
 for s in (2,3,4):rows.append(replay_line(p,d,2,1,0,line['q'],roots,line['omega'],s))
 out=dict(status='passed',rows=rows,seconds=time.monotonic()-start,source_scan=source,
  scope='Every potentially nearby codeword classified in reduced-dimension toy fixtures. No numerical prescription violation claimed for these small domains.')
 (BASE/'tradeoff_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
