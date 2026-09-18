import sys,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root/'better_codes_current_lower_2026_09_17'))
from fast_firstjet_count import coefficient_count
n=262144;w=131071;m=118;s=36;L=176421;D=m*181275

def rect(a,b,h):
 assert h+a+b-2<=L
 return a*b*(L+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
R=0
for r in range(m):
 h=min(r+1,m-r)
 R+=rect(r+1,s+1,0)-rect(max(0,r+1-h),max(0,s+1-h),h)
rows=[]
for reserve in [0,1,2]:
 cut=D-reserve;C=coefficient_count(cut,L,s)
 # Independent direct sum over the bounded Y/R rectangle, with X/Z counts closed.
 ref=0
 for j in range(s+1):
  for i in range((cut-1-(w-1)*j)//w+1):
   ref+=(cut-w*i-(w-1)*j)*(L-i-j+1)
 assert C==ref
 rows.append({'reserve':reserve,'strict_weight_cutoff':cut,'coefficient_count':C,'local_rank_bound':R,'kernel_dimension_lower_bound':C-n*R,'positive':C>n*R})
out={'m':m,'s':s,'L':L,'n':n,'w':w,'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
