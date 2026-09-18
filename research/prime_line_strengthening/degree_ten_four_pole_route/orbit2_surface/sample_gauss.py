"""Exact Gauss-image point certificates over F83^3; bounded deterministic sampling.

This samples source-curve points for interpolation, not candidate members.
Every saved distinct image is independently checked against all three jet
kernel equations. A later polynomial identity needs a separate certificate.
"""
import argparse,json,hashlib,math,time
from pathlib import Path
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx
ap=argparse.ArgumentParser();ap.add_argument('--target',type=int,default=500);ap.add_argument('--seconds',type=float,default=50);ap.add_argument('--max-x',type=int,default=3000);ap.add_argument('--output',type=Path,default=Path(__file__).with_name('gauss_samples.json'));args=ap.parse_args()
P=Path(__file__).parent;raw=(P/'profile.json').read_bytes();gdata=json.loads(raw)['quotient'];assert len(gdata['factors'])==1 and gdata['factors'][0]['exponent']==1
G=[tuple(map(int,t)) for t in gdata['factors'][0]['terms']]
rawb=(P.parent/'gate.json').read_bytes();B=next(v for v in json.loads(rawb) if v['bank']=='orbit2');forms=[[(int(i),int(j),int(c)) for (i,j),c in zip(B['columns'],row) if c] for row in B['kernel']]
modulus=[80,82,0,1];F=fq_default_ctx(modulus=fmpz_mod_poly_ctx(83)(modulus),var='r');PX=fq_default_poly_ctx(F);zero=F(0);one=F(1)
def enc(a):return list(map(int,a.to_list()))
def code(a):return sum(v*(83**i) for i,v in enumerate(enc(a)))
def element(k):return F([k%83,(k//83)%83,k//6889])
def powers(a,n):
 out=[one]
 for i in range(n):out.append(out[-1]*a)
 return out
def evaluate(terms,xp,yp,dx=0,dy=0):
 return sum((c*(i if dx else 1)*(j if dy else 1)*xp[i-dx]*yp[j-dy] for i,j,c in terms if i>=dx and j>=dy),zero)
def cross(a,b):return[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
# Smooth rational point proves geometric irreducibility of the recorded
# F83-irreducible residual factor.
xp,yp=powers(F(1),76),powers(F(75),21)
assert evaluate(G,xp,yp)==zero and evaluate(G,xp,yp,1,0)==F(64) and evaluate(G,xp,yp,0,1)==F(11)
out={'schema_version':1,'p':83,'field_modulus':modulus,'coordinate_encoding':'[c0,c1,c2] in basis1,r,r^2',
 'normalization':'first nonzero projective coordinate is1','gauss_input_sha256':hashlib.sha256(raw).hexdigest(),'gate_input_sha256':hashlib.sha256(rawb).hexdigest(),
 'source_points':[],'image_points':[],'smooth_rational_point':[1,75],'smooth_gradient':[64,11],
 'status':'running','target':args.target,'checked_kernel_equations_per_point':3}
start=time.monotonic();images=set();seen_x=set();calls=0;last_saved=0

def checkpoint():
 out.update(seconds=time.monotonic()-start,root_calls=calls,distinct_image_count=len(images))
 tmp=args.output.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,separators=(',',':')));tmp.replace(args.output)

def accept(x,y):
 xp,yp=powers(x,76),powers(y,21)
 assert evaluate(G,xp,yp)==zero
 f=[evaluate(T,xp,yp) for T in forms];fx=[evaluate(T,xp,yp,1,0) for T in forms];fy=[evaluate(T,xp,yp,0,1) for T in forms]
 a=cross(f,fx)
 if all(u==zero for u in a):a=cross(f,fy)
 if all(u==zero for u in a):return
 for row in(f,fx,fy):assert sum((u*v for u,v in zip(a,row)),zero)==zero
 pivot=next(u for u in a if u!=zero);a=[u/pivot for u in a]
 key=tuple(code(u) for u in a)
 if key in images:return
 images.add(key);out['source_points'].append([enc(x),enc(y)]);out['image_points'].append([enc(u) for u in a])
checkpoint()
for trial in range(83**3):
 if calls>=args.max_x or len(images)>=args.target or time.monotonic()-start>args.seconds:break
 x=element((997*trial+17)%(83**3))
 if code(x) in seen_x:continue
 # Mark the Frobenius X orbit.
 for q in range(3):seen_x.add(code(x**(83**q)))
 xp=powers(x,76);coeff=[sum((c*xp[i] for i,j,c in G if j==d),zero) for d in range(22)];poly=PX(coeff)
 if not poly:continue
 calls+=1
 for y,mult in poly.roots():
  for q in range(3):
   xx,yy=x**(83**q),y**(83**q)
   accept(xx,yy)
  if len(images)>=args.target:break
 if len(images)-last_saved>=100:
  checkpoint();last_saved=len(images);print('points',len(images),'rootcalls',calls,'seconds',round(out['seconds'],3),flush=True)
out['status']='target_reached' if len(images)>=args.target else 'bounded_stop';checkpoint()
print(json.dumps({'status':out['status'],'points':len(images),'root_calls':calls,'seconds':out['seconds']}),flush=True)
