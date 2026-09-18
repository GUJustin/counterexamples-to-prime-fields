"""Reconstruct verifier input independently from original profile supports."""
import argparse,json
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('--profiles',required=True);ap.add_argument('--certificates',required=True);ap.add_argument('--output',required=True);a=ap.parse_args()
data=json.load(open(a.profiles));q=data['q'];r=(q-1)//2
rows=[json.loads(line) for line in open(a.certificates) if line.strip()]
domains=[];domain_ids={};pairs=[];pair_ids={}
def domain(xs):
 key=tuple(sorted(xs))
 if key not in domain_ids:domain_ids[key]=len(domains);domains.append(key)
 return domain_ids[key]
expected=set()
for ci,c in enumerate(data['unit_classes']):
 C=set(c['C']);S=set(range(q))-C
 assert S==set(c['S']) and len(C)==r and len(S)==r+1
 for ti,mask in enumerate(c['compatible_T_orbit_masks']):
  T={x for j,O in enumerate(data['doubling_orbits']) if mask>>j&1 for x in O}
  assert len(T)==r
  # Check actual correlations directly, independently of stored profile values.
  for t in range(1,q):assert len(C&{(x+t)%q for x in C})+len(T&{(x+t)%q for x in T})==r-1
  pair_ids[ci,ti]=len(pairs);pairs.append((domain(S),domain(T)))
  for h in range(r+1,q):expected.add((ci,ti,h))
accepted=set();records=[];seen=set()
for i,row in enumerate(rows):
 key=(row['source_class'],row['relative_target'],row['h'])
 assert key in expected
 if row['accepted']:accepted.add(key)
 seen.add(key)
 records.append((i,pair_ids[key[:2]],key[2],row['p'],row['zeta'],int(row['accepted'])))
with open(a.output,'w') as f:
 f.write(f'{q} {len(domains)} {len(pairs)} {len(records)}\n')
 for d in domains:f.write(str(len(d))+' '+' '.join(map(str,d))+'\n')
 for p in pairs:f.write(' '.join(map(str,p))+'\n')
 for row in records:f.write(' '.join(map(str,row))+'\n')
summary={'q':q,'domains':len(domains),'pairs':len(pairs),'rows':len(rows),'expected_cases':len(expected),'seen_cases':len(seen),'accepted_cases':len(accepted),'missing_cases':len(expected-seen),'uncertified_cases':len(expected-accepted)}
Path(a.output+'.summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary))
