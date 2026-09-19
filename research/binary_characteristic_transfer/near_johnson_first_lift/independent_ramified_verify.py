import importlib.util,json,struct,time
from pathlib import Path
sp=importlib.util.spec_from_file_location('base','independent_verify.py');b=importlib.util.module_from_spec(sp);sp.loader.exec_module(b)
start=time.monotonic();F=37;C=len(b.coeff);raw=struct.unpack('<'+'I'*(F*C),Path('tangent_basis.bin').read_bytes());basis=[raw[i*C:(i+1)*C] for i in range(F)]
witnessed=set()
for col in range(3*b.N):
 nonzero=[i for i in range(F) if basis[i][col]]
 if len(nonzero)==1 and basis[nonzero[0]][col]==1:witnessed.add(nonzero[0])
assert len(witnessed)==F, 'No full identity minor in tangent basis'
quad=[[0]*F for _ in range(F)]
def qvalue(vec):
 out=0
 for bi,(_,_,z,h,support) in enumerate(b.banks):
  off=3*b.N+bi*(b.K+1)
  for ri,idx in enumerate(support):
   wt=b.weights[bi*b.T+ri]
   if not wt:continue
   x,_,_=b.nodes[idx];a=vec[idx];d=vec[2*b.N+idx];c=vec[off+b.K]
   linear=0;h2=0
   for j in range(1,b.K,2):linear^=b.mul(vec[off+j],b.power(x,j-1))
   for j in range(2,b.K):
    if (j*(j-1)//2)&1:h2^=b.mul(h[j],b.power(x,j-2))
   out^=b.mul(wt,b.mul(a,linear)^b.mul(h2,b.mul(a,a))^b.mul(c,d))
 return out
for bi,(_,_,z,h,support) in enumerate(b.banks):
 off=3*b.N+bi*(b.K+1)
 for ri,idx in enumerate(support):
  x,_,g=b.nodes[idx];xp=[b.power(x,j) for j in range(b.K)];der=0;h2=0
  for j in range(1,b.K,2):der^=b.mul(h[j],xp[j-1])
  for j in range(2,b.K):
   if (j*(j-1)//2)&1:h2^=b.mul(h[j],xp[j-2])
  linear=[]
  for v in basis:
   val=b.mul(v[idx],der)^v[b.N+idx]^b.mul(z,v[2*b.N+idx])^b.mul(g,v[off+b.K])
   for j in range(b.K):val^=b.mul(v[off+j],xp[j])
   assert val==0
   l=0
   for j in range(1,b.K,2):l^=b.mul(v[off+j],xp[j-1])
   linear.append(l)
  wt=b.weights[bi*b.T+ri]
  if not wt:continue
  for i,v in enumerate(basis):
   a=v[idx];c=v[off+b.K];d=v[2*b.N+idx]
   quad[i][i]^=b.mul(wt,b.mul(h2,b.mul(a,a))^b.mul(a,linear[i])^b.mul(c,d))
   for j in range(i+1,F):
    u=basis[j]
    quad[i][j]^=b.mul(wt,b.mul(a,linear[j])^b.mul(u[idx],linear[i])^b.mul(c,u[2*b.N+idx])^b.mul(u[off+b.K],d))
flat=[quad[i][j] for i in range(F) for j in range(i,F)]
assert tuple(flat)==struct.unpack('<703I',Path('restricted_quadratic.bin').read_bytes())
# Exact pure gauge tangent: translate every node and countertranslate witnesses.
v=[0]*C
for i in range(b.N):v[i]=1
for bi,(_,_,z,h,support) in enumerate(b.banks):
 off=3*b.N+bi*(b.K+1)
 for j in range(b.K-1):
  if (j+1)&1:v[off+j]=h[j+1]
assert qvalue(v)==0
# Label/direction reciprocal scaling is a genuine gauge, with a second-order correction.
v=[0]*C
for i,(_,_,g) in enumerate(b.nodes):v[2*b.N+i]=g
for bi,(_,_,z,_,_) in enumerate(b.banks):v[3*b.N+bi*(b.K+1)+b.K]=z
assert qvalue(v)==0
res={'PASS':True,'basis_vectors_checked_in_full_original_kernel':F,'basis_independence_identity_minor':len(witnessed),'quadratic_coefficients_recomputed':len(flat),'nonzero_diagonal':sum(quad[i][i]!=0 for i in range(F)),'nonzero_cross':sum(quad[i][j]!=0 for i in range(F) for j in range(i+1,F)),'gauge_checks':['node translation','reciprocal label/direction scaling'],'kernel_completeness':'requires independent rank receipt, not inferred from null vectors','seconds':time.monotonic()-start}
Path('independent_ramified_verified.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
