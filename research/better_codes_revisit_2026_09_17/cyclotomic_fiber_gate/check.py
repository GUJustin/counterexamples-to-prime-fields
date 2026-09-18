import math,json
from pathlib import Path
M,k=32,17
D=[[0]*M for _ in range(k+1)];D[0][0]=1
for j in range(1,M):
 for h in range(k,0,-1):
  for s in range(M):D[h][s]+=D[h-1][(s-j)%M]
def ram(d,s):
 if d==1:return 1
 if s%d==0:return d//2
 if s%(d//2)==0:return -d//2
 return 0
other=[]
for s in range(M):
 num=sum((-1)**(k+k//d)*math.comb(M//d-1,k//d)*ram(d,s) for d in [1,2,4,8,16,32])
 assert num%M==0
 other.append(num//M)
assert D[k]==other and sum(other)==math.comb(31,17)
r={'packet_order':8,'tag_order':M,'selected_packets':k,'product_class_counts':other,'maximum_complex_signature_fiber':max(other),'sum':sum(other),'independent_dp_ramanujan_pass':True,'benchmark_required':274980728111395088,'finite_field_average_guarantee':68579341025511059}
Path(__file__).with_suffix('.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
