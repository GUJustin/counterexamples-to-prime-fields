import json, pathlib, subprocess
here=pathlib.Path(__file__).resolve().parent
src=here.parent/'cyclic_half_agreement'
summary=[]
for q in [5,7,9,13,15,17,19,21,23]:
 lines=(src/f'modular_q{q}.in').read_text().splitlines()
 qq,nd,np=map(int,lines[0].split());assert qq==q and len(lines)==1+nd+np
 pairs=[list(map(int,s.split())) for s in lines[1+nd:]]
 rows=[json.loads(s) for s in (src/f'modular_q{q}.jsonl').read_text().splitlines()]
 assert len(rows)==np*((q-1)//2)
 seen=set()
 out=[f'{q} {nd} {np} {len(rows)}']+lines[1:1+nd]+[f'{p[0]} {p[1]}' for p in pairs]
 for i,r in enumerate(rows):
  key=(r['pair_id'],r['h']);assert key not in seen;seen.add(key)
  p=pairs[r['pair_id']];assert p[2:]==[r['source_class'],r['relative_target']]
  out.append(f"{i} {r['pair_id']} {r['h']} {r['p']} {r['zeta']} {int(r['accepted'])}")
 assert seen=={(j,h) for j in range(np) for h in range((q+1)//2,q)}
 inp=here/f'modular_q{q}_independent.in';op=here/f'modular_q{q}_independent.out'
 inp.write_text('\n'.join(out)+'\n')
 r=subprocess.run([str(here/'verify_modular'),str(inp),str(op)],capture_output=True,text=True)
 assert r.returncode==0,(q,r.stderr)
 vals=[list(map(int,s.split())) for s in op.read_text().splitlines()]
 summary.append(dict(q=q,pairs=np,rows=len(rows),certified=sum(x[1] for x in vals),claimed=sum(r['accepted'] for r in rows),diagnostic=r.stderr))
(here/'SMALL_Q_MODULAR_AUDIT.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
