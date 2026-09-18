"""Run with sage -python; exact reconstruction, checkpointed after every point."""
import argparse, hashlib, json, math, time
from pathlib import Path
from sage.all import GF, PolynomialRing, prod, save

ap=argparse.ArgumentParser()
ap.add_argument('--max-evaluations',type=int,default=190)
ap.add_argument('--input',type=Path,default=Path(__file__).resolve().parents[1]/'gate.json')
ap.add_argument('--output',type=Path,default=Path(__file__).resolve().parent/'reconstruction.json')
args=ap.parse_args()
input_bytes=args.input.read_bytes()
bank=next(b for b in json.loads(input_bytes) if b['bank']=='paley')
assert bank['p']==29 and len(bank['kernel'])==3
assert args.max_evaluations>=0
assert len(bank['base'])==14 and len(set(bank['base']))==14
assert all(len(v)==len(bank['columns']) for v in bank['kernel'])
assert all((i-2*j)%7==r for r,v in zip((1,3,5),bank['kernel'])
           for (i,j),a in zip(bank['columns'],v) if a)
k=GF(29); RX=PolynomialRing(k,'X'); X=RX.gen()
RY=PolynomialRing(RX,'Y'); Y=RY.gen()
forms=[sum((RX(a)*X**i)*Y**j for (i,j),a in zip(bank['columns'],v))
       for v in bank['kernel']]
T=prod((X-k(x))**(12 if i<7 else 30) for i,x in enumerate(bank['base']))
assert T.degree()==294
metadata={'schema_version':1,'input_sha256':hashlib.sha256(input_bytes).hexdigest(),
          'p':29,'chart':'F0+s F1+t F2','parameter_degree_bound':18,
          'residual_X_degree_bound':48}
out=dict(metadata,evaluations=[])
if args.output.exists():
    out=json.loads(args.output.read_text())
    if not isinstance(out,dict) or any(out.get(key)!=value for key,value in metadata.items()):
        raise ValueError('Checkpoint metadata/input hash mismatch; refusing resume')
points=[(a,d-a) for d in range(19) for a in range(d+1)]
seen={}
if not isinstance(out.get('evaluations'),list):
    raise ValueError('Checkpoint evaluations must be a list')
for rec in out['evaluations']:
    if not isinstance(rec,dict) or any(type(rec.get(key)) is not int for key in ('s','t')):
        raise ValueError('Malformed evaluation point')
    pt=(rec['s'],rec['t'])
    if pt not in points or pt in seen:
        raise ValueError('Unexpected or duplicate checkpoint point: '+str(pt))
    cc=rec.get('coefficients')
    if (not isinstance(cc,list) or len(cc)>49 or
        any(type(z) is not int or not 0<=z<29 for z in cc) or
        (cc and cc[-1]==0)):
        raise ValueError('Invalid/noncanonical residual coefficient list at '+str(pt))
    seen[pt]=rec
def checkpoint():
    temporary=args.output.with_suffix(args.output.suffix+'.tmp')
    temporary.write_text(json.dumps(out,indent=2))
    temporary.replace(args.output)
start=time.monotonic(); added=0
for a,b in points:
    if (a,b) in seen: continue
    if added>=args.max_evaluations: break
    tick=time.monotonic()
    f=forms[0]+k(a)*forms[1]+k(b)*forms[2]
    assert f.degree()==10
    delta=RX(f.discriminant())
    q,r=delta.quo_rem(T)
    assert not r and q.degree()<=48
    rec={'s':a,'t':b,'coefficients':list(map(int,q.list())),
         'seconds':time.monotonic()-tick}
    seen[a,b]=rec;out['evaluations'].append(rec);added+=1
    checkpoint()
    print('evaluation',len(seen),'of190',a,b,'degree',q.degree(),
          'seconds',round(rec['seconds'],3),flush=True)
if len(seen)<190:
    print('Checkpoint only; coefficient reconstruction not complete.',flush=True)
    raise SystemExit(0)
assert len(out['evaluations'])==190 and set(seen)==set(points)

# Exact triangular Newton interpolation. Every factorial through18 is a unit.
newton={}
def ff(a,i):
    return k(prod(a-j for j in range(i)))
for a,b in points:
    v=RX(seen[a,b]['coefficients'])
    for (i,j),c in newton.items():
        if i<=a and j<=b: v-=c*ff(a,i)*ff(b,j)
    newton[a,b]=v/k(math.factorial(a)*math.factorial(b))
R=PolynomialRing(k,('s','t'));s,t=R.gens()
coeff=[R.zero() for _ in range(49)]
for (a,b),v in newton.items():
    mon=prod(s-i for i in range(a))*prod(t-j for j in range(b))
    for d,z in enumerate(v.list()): coeff[d]+=z*mon
for a,b in points:
    assert RX([c(k(a),k(b)) for c in coeff])==RX(seen[a,b]['coefficients'])
assert all(c.total_degree()<=18 for c in coeff if c)
# F(zet*X,zet^-2*Y;s,t)=zet*F(X,Y;zet^2*s,zet^4*t).
# The discriminant scales by zet^(180+18)=zet^2; T is invariant.
assert all((d-2-2*int(a)-4*int(b))%7==0
           for d,c in enumerate(coeff) for (a,b) in c.dict())
out['residual_coefficient_terms']=[
    [[list(map(int,e)),int(z)] for e,z in c.dict().items()] for c in coeff]
out['interpolation_verified_at_all_190_nodes']=True
out['mu7_sparsity_verified']=True
out['seconds_this_invocation']=time.monotonic()-start
checkpoint()
SX=PolynomialRing(R,'X');D=SX(coeff)
save(D,str(args.output.with_suffix('.sobj')))
print('COMPLETE: residual discriminant degree',D.degree(),
      'parameter terms',sum(len(c.dict()) for c in coeff),flush=True)
