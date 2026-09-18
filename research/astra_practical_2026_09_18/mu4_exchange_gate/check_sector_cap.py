from math import comb
from pathlib import Path
import json
n=64;k=34
dp=[[0]*n for _ in range(k+1)];dp[0][0]=1
for a in range(1,n):
 for j in range(min(a,k),0,-1):
  for b in range(n):dp[j][(b+a)%n]+=dp[j-1][b]
def ramanujan(d,e):
 if d==1:return 1
 return d//2 if e%d==0 else -d//2 if e%(d//2)==0 else 0
fourier=[]
for e in range(n):
 numerator=sum(ramanujan(d,e)*sum((-1)**(k+a)*comb(n//d,a) for a in range(k//d+1)) for d in [1,2,4,8,16,32,64])
 assert numerator%n==0
 fourier.append(numerator//n)
assert fourier==dp[k]
assert sum(dp[k])==comb(63,34)
r={'tags':63,'chosen':34,'product_class_counts':dp[k],'maximum':max(dp[k]),'required':274980728111395088,'shortfall_factor':274980728111395088/max(dp[k]),'independent_ramanujan_replay':True}
Path(__file__).with_name('sector_product_cap.json').write_text(json.dumps(r,indent=2)+'\n');print({'maximum':r['maximum'],'independent_ramanujan_replay':True})
