"""Independent stdlib exact check; no optimizer, no generator hull routine."""
import json
from fractions import Fraction as F
from pathlib import Path
p=Path(__file__).with_name('quartic_remainder_resource_lp.json');data=json.loads(p.read_text());n=262144;w=131071;T=3261

def polygon(co):
 d=len(co)-1;ords=[]
 for j in range(d+1):
  vals=[F(co[j])]
  for a in range(j+1):
   for b in range(j,d+1):
    if a<b:vals.append(F((b-j)*co[a]+(j-a)*co[b],b-a))
  ords.append(min(vals))
 roots=sorted(ords[j-1]-ords[j] for j in range(1,d+1))
 return roots,2*sum(ords[1:-1])
def conv(a,b):
 out=[10**9]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=min(out[i+j],x+y)
 return out

def rectangle(a,b,h):return sum(T+1-h-i-j for i in range(a) for j in range(b))
def rank(m):
 return sum(rectangle(k+1,13,0)-rectangle(max(0,k+1-(m-k)),max(0,13-(m-k)),m-k) for k in range(m))
rt={};tot=[F(0)]*11;crossG=[0]*4;crossH=[0]*3;rows=[];ranktotal=0
for row in data['profile']:
 g=row['G_coefficient_orders']+[0];h=row['H_coefficient_orders']+[0];a=[0]
 for _ in range(10):a=conv(a,g)
 a=conv(a,h);contact=min(v+j+min(v,12) for j,v in enumerate(a));assert contact==row['contact']
 vg,dg=polygon(g);vh,dh=polygon(h);res=sum(min(x,y) for x in vg for y in vh)
 eg,d,c,b=g[:4];eh,ch,bh=h[:3]
 costs=[dg,dh,res,min(c,2*b),min(d,b+c,3*b),min(eg,b+d,2*b+c,4*b),min(ch,2*bh),min(eh,bh+ch,3*bh),min(b,bh),int(b>0),int(bh>0)]
 assert list(map(F,row['costs']))==costs
 count=row['count'];tot=[x+count*y for x,y in zip(tot,costs)]
 for k in range(4):crossG[k]+=count*min(g[i]+(i-k)*bh for i in range(k,5))
 for k in range(3):crossH[k]+=count*min(h[i]+(i-k)*b for i in range(k,4))
 if contact not in rt:rt[contact]=rank(contact)
 ranktotal+=count*rt[contact];rows.append({'contact':contact,'count':count,'G_roots':list(map(str,vg)),'H_roots':list(map(str,vh))})
bud=[12*w,6*w,12*w,2*w,3*w,4*w,2*w,3*w,w,211940,211940]
assert sum(r['count'] for r in data['profile'])==n
assert all(x<=y for x,y in zip(tot,bud)) and ranktotal>=6802316684344
assert all(x<=(4-k)*w for k,x in enumerate(crossG)) and all(x<=(3-k)*w for k,x in enumerate(crossH))
out={'pass':True,'rank_sum':ranktotal,'resource_totals':list(map(str,tot)),'cross_G_at_H_centroid':crossG,'cross_H_at_G_centroid':crossH,'states':rows,'scope':'exact integer local/resource profile; no global polynomial/source existence claim'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
