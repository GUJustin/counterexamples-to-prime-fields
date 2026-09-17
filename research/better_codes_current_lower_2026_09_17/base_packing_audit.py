"""Independent baseline carrier, singleton, base, and Bellman arithmetic replay."""
import ast,re,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent;CACHE=ROOT.parents[1]/'tmp/current-lower-primary-cache'
ns={'__file__':str(ROOT/'replay_ledger.py')};exec((ROOT/'replay_ledger.py').read_text().split('worst=[]')[0],ns)
rows,base,basecell,potential=ns['rows'],ns['base'],ns['basecell'],ns['potential']

def mix(p,q,r):
 a,b,c=p;d,e,f=q;g,h,i=r
 return c*f*i+(a*f*i+d*c*i+g*c*f)+(b*f*i+e*c*i+h*c*f)+(c*e*h+f*b*h+i*b*e)+(a*e*i+a*h*f+d*b*i+d*h*c+g*b*f+g*e*c)

def cost(r,v,z):
 f=(z,v,r)
 if r>=3 and v>=2:
  a,b,s=z,v-1,r-2
  reduced=(2*a*131072,1+(2*b+2)*131072,(2*s+2)*131072)
  rational=(131074*a,131074*b+2,131074*s+3)
  normal=(rational[0],rational[1],rational[2]+131071)
  moving=(a,b+1,s+3);cut=(rational[0],rational[1]+131072,rational[2]+262144)
  return mix(f,reduced,normal)+65539*mix(f,moving,cut)
 S=max(r,2);Y=max(v+r,S+1);T=max(z+v+r,Y)
 def tail(d):return(2*(T-Y)*d,1+2*(Y-S)*d,2*(S-1)*d)
 return mix(f,tail(131072),tail(131073))

def safe(r,y):
 b=max(0,y-r-1);s=max(0,r-2);ps=s+2;pys=b+s+3
 return r*(1+2*(pys-ps)*131072)+y*(2*ps-2)*131072<2130706433 and r*(1+(2*(pys-ps)-1)*131071)+y*(2*ps-1)*131071<2130706433

arith={}
for suffix in 'ABCD':
 path=ROOT/f'MovingFiberArithmetic6811{suffix}.lean'
 if not path.exists():path=CACHE/path.name
 text=path.read_text()
 for idx,body in re.findall(r'namespace ProximityPrize.SubmissionLower.MovingFiberArithmetic6811.G(\d+)\n(.*?)(?=\nend ProximityPrize|\Z)',text,re.S):
  den=int(re.search(r'def denominator : ℕ := (\d+)',body)[1]);cfg=[int(a) for a in re.search(r'def cfg .*? := !\[(.*?)\]',body)[1].replace('source','').split(',')]
  funcs={}
  for name in ['slope','intercept']:
   expr=re.search(r'def '+name+r' \(a b : ℕ\) : ℕ :=\s*(.*?)(?=\ndef )',body,re.S)[1]
   assert re.fullmatch(r'[0-9ab*+^\s]+',expr)
   funcs[name]=compile(expr.replace('^','**').replace('\n',' ').strip(),'<primary-polynomial>','eval')
  arith[int(idx)]=(den,funcs,cfg)
assert len(arith)==16
sourcepars=json.loads((ROOT/'source_replay.json').read_text())['sources'];sourceL={a['index']:a['parameters'][4] for a in sourcepars}
limits={i:max(sourceL[j] for j in a[2]) for i,a in arith.items()}

def root(which,r,v,z):
 den,f,_=arith[which-1];env={'a':max(0,r-3),'b':max(0,v-2)}
 return(eval(f['slope'],{},env)//den+1)*z+eval(f['intercept'],{},env)//den+1

def carrier(c,z):return c[z] if z<3 else c[3]+max(0,c[4]-c[3])*(z-3)
def choice(row,which,r,v,z):
 if which==0:return carrier(row['carrier'],z)
 if which<=16:return root(which,r,v,z)
 return potential(r,v,z,which-17)
def active(row,which,r,v,lo,hi):
 if which==0:return r<=32 and r+v<=149 and r+v+hi<=8121 and safe(r,r+v)
 if which<=16:return 3<=r<=31 and v>=2 and lo>=3 and limits[which-1]<r+v+lo and r+v<=142 and r+v+hi<=7501
 j=which-17;return j<7 and row['threshold'][j]<=lo

sheets=[]
for j in range(8):
 text=(CACHE/f'MovingFiberPackingData6811S{j}.lean').read_text()
 slope=int(re.search(r'def slope : Nat := (\d+)',text)[1]);own={};packed={}
 for typ,r,nums in re.findall(r'def (own|packed)(\d+) : Array Nat := #\[([^\]]*)\]',text):
  (own if typ=='own' else packed)[int(r)]=[int(a) for a in nums.split(',')]
 assert all(len(own[r])==160-r for r in range(1,36));assert all(len(packed[r])==160-r for r in range(36))
 sheets.append((slope,own,packed))
counts=dict(carrier=0,singleton_endpoints=0,base_endpoints=0,bellman_pairs=0)
for(r,v),row in rows.items():
 for z in range(5):assert row['carrier'][z]==cost(r,v,z),(r,v,z);counts['carrier']+=1
 for slope,own,packed in sheets:
  lo=0
  for stop,who in row['singletons']:
   assert lo<stop<=9276-r-v and (lo>=3 or stop==lo+1)
   assert active(row,who,r,v,lo,stop-1),(r,v,lo,stop,who)
   for z in [lo,stop-1]:assert choice(row,who,r,v,z)<=slope*z+own[r][v],(r,v,z,who);counts['singleton_endpoints']+=1
   lo=stop
  assert lo==9276-r-v
 lo=0
 for stop,j in row['baseChoices']:
  assert lo<stop<=9276-r-v and j<8 and basecell(row,lo,stop-1)
  slope,own,packed=sheets[j]
  for z in [lo,stop-1]:assert slope*z+packed[r][v]<=base(row,z),(r,v,z,j);counts['base_endpoints']+=1
  lo=stop
 assert lo==9276-r-v
print('carriers/singletons/base pass',counts,flush=True)
for j,(slope,own,packed) in enumerate(sheets):
 maxv=max(max(a) for a in packed.values());assert maxv<2**62
 arrays={r:np.array(a,dtype=np.int64) for r,a in packed.items()}
 for R in range(1,36):
  out=arrays[R]
  for r in range(1,R+1):
   left=own[r];right=arrays[R-r]
   for u,a in enumerate(left[:len(out)]):
    count=min(len(right),len(out)-u)
    assert np.all(a+right[:count]<=out[u:u+count]),(j,R,r,u)
    counts['bellman_pairs']+=count
 print('sheet',j,'Bellman pass',flush=True)
(ROOT/'base_packing_audit.json').write_text(json.dumps(dict(passed=True,rows=len(rows),counts=counts,scope='Baseline carrier,SingleValid/BaseValid and directBellman arithmetic; not all source-provider geometric theorems or updated-target receipt.'),indent=2)+'\n')
