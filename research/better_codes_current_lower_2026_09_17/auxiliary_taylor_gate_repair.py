"""Bounded k/n0 structural trade; all other source coordinates frozen."""
import json,itertools
import auxiliary_geometry_optimizer as O
R=O.roots;ROOT=O.ROOT
out=[]
for idx in (21,5,22):
 old=R.SOURCES[idx];records=[]
 for dk,dn,dm,du in itertools.product((1,2),range(0,3),(0,1,2),(-2,-1,0)):
  p=old.copy();p[5]+=dk;p[6]+=dn;p[0]+=dm;p[3]+=du;m,B,s,U,L,k,n0=p
  if not(m+s<=U and 0<=k<=s<m and k+1<=n0 and 2*(n0-k-1)<=B):continue
  caps=[(m*O.A-(h if h<n0 else k)*(O.A-131069)+B-1)//131071 for h in range(s+1)]
  if min(caps)<U:
   records.append(dict(dm=dm,du=du,dk=dk,dn0=dn,parameters=p.copy(),feasible_L=None,reason='closed rank cutoff cap fails',minimum_cutoff_cap=min(caps)));continue
  gap=O.coeff(O.A,*p)-O.n*O.rank(*p);p[4]+=1;slope=O.coeff(O.A,*p)-O.n*O.rank(*p)-gap;p[4]=L
  rec=dict(dm=dm,du=du,dk=dk,dn0=dn,parameters=p.copy(),surplus_at_old_L=gap,surplus_slope=slope)
  if slope<=0:
   rec['feasible_L']=None;records.append(rec);continue
  req=max(U,m+B+s,L+(-gap)//slope+1);p[4]=req;rec['parameters']=p.copy();rec['feasible_L']=req;rec['nullity']=O.coeff(O.A,*p)-O.n*O.rank(*p);assert rec['nullity']>0
  R.SOURCES[idx]=p;R.root_lines.cache_clear();lines=R.root_lines(11,12,43);domain=R.root_domain(11,12,43);rec['activation_z']=domain[0] if domain else None;rec['active_at_contact']=bool(domain and domain[0]<=3206<=domain[1]);rec['contact_bound']=max(a*3206+b for a,b in lines);rec['lines']=lines;rec['flag']=R.flag(p)
  R.SOURCES[idx]=old;R.root_lines.cache_clear();records.append(rec)
 out.append(dict(source=idx,original=old,records=records))
(ROOT/'auxiliary_taylor_gate_repair.json').write_text(json.dumps(out,indent=2)+'\n')
for row in out:
 feasible=[r for r in row['records'] if r.get('active_at_contact')];feasible.sort(key=lambda r:r['contact_bound']);print('source',row['source'],'best',feasible[:2])
