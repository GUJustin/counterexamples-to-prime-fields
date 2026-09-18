import json
from pathlib import Path
n=262144;w=131071;y=55;s=12;L=3261;V=55*w
C=sum((V-w*i-(w-1)*j+1)*(L-i-j+1) for j in range(s+1) for i in range(y-j+1) if V-w*i-(w-1)*j>=0)
def rect(a,b,h):return a*b*(L+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
def R(m):
 return sum(rect(t+1,s+1,0)-rect(max(0,t+1-h),max(0,s+1-h),h) for t in range(m) for h in [m-t])
lo=0;hi=56
while hi-lo>1:
 mid=(lo+hi)//2
 if C-n*R(mid)>1:lo=mid
 else:hi=mid
rows=[{'uniform_contact':a,'local_rank_bound':R(a),'own_kernel_dimension_lower':C-n*R(a)} for a in sorted(set([10,lo,hi,43]))]
out={'n':n,'w':w,'y':y,'r':s,'t':L,'weight':V,'source_dimension':C,'largest_uniform_contact_excluded':lo,'first_uniform_contact_not_excluded':hi,'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
