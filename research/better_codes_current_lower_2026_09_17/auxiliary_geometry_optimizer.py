"""Bounded, actual-context optimizer for one auxiliary source in one group.
CLI: group source r v z. Outputs dedicated candidate JSON; no manifest mutation.
"""
import ast,json,sys,math
from pathlib import Path
import repaired_auxiliary_roots as roots
ROOT=Path(__file__).resolve().parent
ns={'n':262144,'w':131071};tree=ast.parse((ROOT/'replay_sources.py').read_text());exec(compile(ast.Module(body=[x for x in tree.body if isinstance(x,ast.FunctionDef)],type_ignores=[]),'counts','exec'),ns)
rank,coeff=ns['rank'],ns['coefficients'];A=181275;n=262144

def optimize(group,idx,r,v,z):
 assert idx in roots.GROUPS[group]
 original=roots.SOURCES[idx];m0,B0,s0,U0,L0,k,n0=original
 baseline=roots.root_upper(group,r,v,z) if roots.root_domain(group,r,v) and roots.root_domain(group,r,v)[0]<=z<=roots.root_domain(group,r,v)[1] else None
 best=[];tested=0
 for dm in range(-2,3):
  for dB in range(-2,3):
   for ds in range(-1,2):
    for dU in range(-2,3):
     m=m0+dm;B=B0+dB;s=s0+ds;U=U0+dU;lower=max(U,m+B+s)
     if not(2*s<=B<=m and m+s<=U and k<=s<m and k+1<=n0 and 2*(n0-k-1)<=B):continue
     p=[m,B,s,U,max(L0,lower),k,n0];L=p[4]
     try:
      R=rank(*p);C=coeff(A,*p);p[4]+=1;slope=coeff(A,*p)-n*rank(*p)-(C-n*R)
     except AssertionError:continue
     tested+=1;gap=C-n*R
     if slope<=0:continue
     req=max(lower,L+(-gap)//slope+1);p[4]=req
     if req>=r+v+z:continue
     assert coeff(A,*p)>n*rank(*p)
     params=[p if i==idx else roots.SOURCES[i] for i in roots.GROUPS[group]]
     if max(P[4] for P in params)>=r+v+z:continue
     def numerator_at(zz):
      y=r+v;t=y+zz;helpers=[];cc=0
      for Q in params:
       _,BB,ss,UU,LL,_,_=Q
       helpers.append((roots.pair_numerator(r,y,t,BB+ss*(r-1),UU+ss*(y-1),LL+ss*(t-1)),roots.GAP))
       cc+=roots.pair_numerator(r,y,t,BB,UU,LL)
      g,scale=roots.graph_value(params,r,v,zz)
      return helpers+[(roots.GAP*g+scale*cc,roots.GAP*scale)]
     n0s=numerator_at(0);n1s=numerator_at(1)
     lines=[(roots.ceildiv(q1-q0,d),roots.ceildiv(q0,d)) for(q0,d),(q1,_) in zip(n0s,n1s)]
     bound=max(aa*z+bb for aa,bb in lines)
     best.append(dict(parameters=p.copy(),bound=bound,delta=bound-baseline if baseline is not None else None,source_L=req,group_source_limit=max(P[4] for P in params),flag=roots.flag(p),nullity=coeff(A,*p)-n*rank(*p)))
 best.sort(key=lambda x:(x['bound'],x['source_L']))
 return dict(group=group,source=idx,context=[r,v,z],original=original,baseline_bound=baseline,tested=tested,valid_at_context=len(best),best=best[:20],scope='Bounded dm,dB,dU in[-2,2],ds in[-1,1], analytically minimumL; ranked by actual roundedroot max4 atcontext. Identity/characteristic/topcandidate global group effects must be audited before use.')
if __name__=='__main__':
 g,i,r,v,z=map(int,sys.argv[1:]);out=optimize(g,i,r,v,z);(ROOT/f'aux_geometry_opt_g{g}_s{i}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='best'},indent=2));print('best',out['best'][:3])
