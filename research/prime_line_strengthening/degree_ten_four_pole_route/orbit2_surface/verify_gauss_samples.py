"""Independent stdlib F83^3 replay of EVERY source/Gauss-image witness."""
import json,hashlib,time
from pathlib import Path
P=Path(__file__).parent;raw=(P/'gauss_samples.json').read_bytes();d=json.loads(raw);gr=(P/'profile.json').read_bytes();br=(P.parent/'gate.json').read_bytes()
assert d['gauss_input_sha256']==hashlib.sha256(gr).hexdigest() and d['gate_input_sha256']==hashlib.sha256(br).hexdigest()
assert d['field_modulus']==[80,82,0,1]
zero=(0,0,0);one=(1,0,0)
def add(a,b):return tuple((x+y)%83 for x,y in zip(a,b))
def sub(a,b):return tuple((x-y)%83 for x,y in zip(a,b))
def mul(a,b):
 a0,a1,a2=a;b0,b1,b2=b
 d3=a1*b2+a2*b1;d4=a2*b2
 return((a0*b0+3*d3)%83,(a0*b1+a1*b0+d3+3*d4)%83,(a0*b2+a1*b1+a2*b0+d4)%83)
def powers(a,n):
 r=[one]
 for _ in range(n):r.append(mul(r[-1],a))
 return r
def evaluate(terms,xp,yp):
 a=b=c=0
 for i,j,v in terms:
  x,y,z=mul(xp[i],yp[j]);a+=v*x;b+=v*y;c+=v*z
 return(a%83,b%83,c%83)
def cross(a,b):return(sub(mul(a[1],b[2]),mul(a[2],b[1])),sub(mul(a[2],b[0]),mul(a[0],b[2])),sub(mul(a[0],b[1]),mul(a[1],b[0])))
def parse(v):
 assert len(v)==3 and all(type(x)==int and 0<=x<83 for x in v)
 return tuple(v)
G=json.loads(gr)['quotient']['factors'][0]['terms'];B=next(x for x in json.loads(br) if x['bank']=='orbit2')
F=[[(i,j,c) for (i,j),c in zip(B['columns'],r) if c] for r in B['kernel']]
FX=[[(i-1,j,c*i%83) for i,j,c in T if i] for T in F];FY=[[(i,j-1,c*j%83) for i,j,c in T if j] for T in F]
assert len(d['source_points'])==len(d['image_points'])==d['distinct_image_count']
images=set();start=time.monotonic()
for point,image in zip(d['source_points'],d['image_points']):
 x,y=map(parse,point);a=tuple(map(parse,image));assert next(z for z in a if z!=zero)==one
 assert a not in images;images.add(a)
 xp,yp=powers(x,76),powers(y,21);assert evaluate(G,xp,yp)==zero
 rows=[[evaluate(T,xp,yp) for T in forms] for forms in (F,FX,FY)]
 assert any(z!=zero for z in cross(rows[0],rows[1])) or any(z!=zero for z in cross(rows[0],rows[2]))
 for row in rows:
  value=zero
  for aa,bb in zip(a,row):value=add(value,mul(aa,bb))
  assert value==zero
assert len(images)>62*62
out={'status':'PASS','sample_sha256':hashlib.sha256(raw).hexdigest(),'field_arithmetic':'independent tuple arithmetic, r^3=r+3',
 'distinct_projective_images':len(images),'source_curve_checks':len(images),'jet_kernel_equations_checked':3*len(images),'rank_two_checks':len(images),
 'Bezout_threshold':62*62,'seconds':time.monotonic()-start}
(P/'gauss_samples.verified.json').write_text(json.dumps(out,indent=2));print(out)
