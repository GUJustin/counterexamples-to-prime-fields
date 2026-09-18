import json
from pathlib import Path
n=262144;w=131071;m=118;s=36;L0=176421;D=m*181275
def C(cut,L):
 return sum((cut-w*i-(w-1)*j)*(L-i-j+1) for j in range(s+1) for i in range((cut-1-(w-1)*j)//w+1))
def rect(a,b,h,L):return a*b*(L+1-h)-b*a*(a-1)//2-a*b*(b-1)//2
def R(L):
 return sum(rect(r+1,s+1,0,L)-rect(max(0,r+1-h),max(0,s+1-h),h,L) for r in range(m) for h in [min(r+1,m-r)])
rows=[]
for reserve in [0,1,2,2*(n-1-w)]:
 cut=D-reserve;a=C(cut,L0)-n*R(L0);slope=C(cut,L0+1)-n*R(L0+1)-a
 Lmin=L0+((-a)//slope+1) if slope>0 else None
 if Lmin is not None:assert C(cut,Lmin)-n*R(Lmin)>0>=C(cut,Lmin-1)-n*R(Lmin-1)
 rows.append({'reserve':reserve,'cutoff':cut,'slope_in_L':slope,'gap_at_old_L':a,'minimum_L_in_affine_regime':Lmin,'L_increase':None if Lmin is None else Lmin-L0,'gap_at_minimum_L':None if Lmin is None else C(cut,Lmin)-n*R(Lmin)})
out={'n':n,'w':w,'m':m,'s':s,'old_L':L0,'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
