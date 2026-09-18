from pathlib import Path
import json
scope={}
exec(Path(__file__).with_name('restored_flag_gate.py').read_text().split('# Reproduce')[0],scope)
N=scope['N'];w=scope['w'];A=scope['A']
rows=[]
for m,B,s,U,k,n0,oldL in ((114,47,21,155,5,7,2255),(116,47,21,157,5,7,2233),(96,38,17,130,4,5,2141),(108,41,19,146,4,7,2111)):
 R,T=scope['rankprofile'](m,B,s,U)
 C,M=scope['coefficients'](m,B,s,U,k,n0,A)
 gap=C-N*R
 L=max(U,m+B+s,(M-N*T)//gap) if gap>0 else None
 caps=[(m*A-(h if h<n0 else k)*(A-(w-2))+B-1)//w for h in range(s+1)]
 rows.append(dict(m=m,B=B,s=s,U=U,k=k,n0=n0,oldL=oldL,C=C,M=M,R=R,T=T,gap=gap,targetL=L,target_nullity=(L+1)*gap-M+N*T if L else None,minimum_cutoff_cap=min(caps),closed_rank_hypotheses=(B<=m and m+s<=U and min(caps)>=U),active_at_3261=L is not None and L<3261))
out={'agreement':A,'profiles':rows,'scope':'Exact restored-source arithmetic; no target geometry/cost/fullreceipt claim.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
