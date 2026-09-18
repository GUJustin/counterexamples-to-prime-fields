import p2,json
from pathlib import Path

def span(rows):
 s={0}
 for r in rows:s|={v^r for v in s.copy()}
 return s
checks=[]
for key,rr in p2.G.items():
 if len(rr)!=15:continue
 ss=[span(r['rows']) for r in rr];intersection=set.intersection(*ss)
 assert len(intersection)==8
 assert len(set.union(*ss))==128
 assert all(len(a&b)==8 for i,a in enumerate(ss) for b in ss[i+1:])
 assert len({r['locator'][2] for r in rr})==1
 checks.append({'head_line':key,'common_three_space':sorted(intersection),'constant_X4_coefficient':rr[0]['locator'][2]})
assert len(checks)==127
Path(__file__).with_suffix('.json').write_text(json.dumps({'verified_pencils':127,'checks':checks},indent=2))
print('All 127 maximal groups are complete common-three-space pencils.')
