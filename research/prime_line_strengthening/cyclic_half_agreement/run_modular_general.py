import json,subprocess,sys
from pathlib import Path
p=Path(__file__).parent
for q in map(int,sys.argv[1:]):
 a=json.loads((p/f'profiles_q{q}.json').read_text());profiles={x['key']:x for x in a['profiles']};ds=[];index={};pairs=[]
 def add(d):
  d=tuple(d)
  if d not in index:index[d]=len(ds);ds.append(d)
  return index[d]
 ci=0;mapping=[]
 for row in a['profiles']:
  for cm in row['C_masks']:
   sid=add([i for i in range(q) if not(cm>>i&1)])
   for ti,tm in enumerate(profiles[row['target_key']]['C_masks']):
    tid=add([i for i in range(q) if tm>>i&1]);pairs.append((sid,tid,ci,ti));mapping.append({'C_mask':cm,'T_mask':tm,'source_class':ci,'relative_target':ti})
   ci+=1
 path=p/f'modular_q{q}.in'
 with path.open('w') as f:
  print(q,len(ds),len(pairs),file=f)
  for d in ds:print(len(d),*d,file=f)
  for v in pairs:print(*v,file=f)
 (p/f'modular_q{q}_mapping.json').write_text(json.dumps(mapping))
 subprocess.run(['/tmp/modular_general',str(path),str(p/f'modular_q{q}.jsonl')],check=True)
 rows=[json.loads(x) for x in (p/f'modular_q{q}.jsonl').read_text().splitlines()];assert len(rows)==len(pairs)*((q-1)//2)
 print(json.dumps({'q':q,'cases':len(rows),'accepted':sum(x['accepted'] for x in rows),'unresolved':sum(not x['accepted'] for x in rows)}),flush=True)
