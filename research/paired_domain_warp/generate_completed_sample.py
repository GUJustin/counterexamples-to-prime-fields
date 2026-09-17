"""Sample a completed product image with a four-coordinate line direction."""
from pathlib import Path
from random import SystemRandom
import argparse,json,time
BASE=Path(__file__).resolve().parent
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=BASE/'completed_samples/m521_r2_n2518.json');args=parser.parse_args()
 if args.output.exists():raise SystemExit('Refusing to replace an existing sample')
 start=time.monotonic();rng=SystemRandom();p=2**521-1;n=2518;K=1259;r=2;t=8;m0=1241;D0=622;D=D0+t
 padding=[1,2];used=set(padding);core=[]
 while len(core)<m0+2*t:
  a=rng.randrange(1,(p+1)//2)
  if a not in used:used.add(a);core.append(a)
 reference=core[:D0]+[core[m0+2*j] for j in range(t)]
 coeff=[1]
 for a in reference:
  y=a*a%p;new=[0]*(len(coeff)+1)
  for j,c in enumerate(coeff):new[j]=(new[j]-y*c)%p;new[j+1]=(new[j+1]+c)%p
  coeff=new
 domain=[];f=[];g=[]
 for i,a in enumerate(core+padding):
  y=a*a%p;v=0
  for c in reversed(coeff):v=(v*y+c)%p
  direction=0 if i<len(core) else -v%p
  domain.extend([str(a),str(p-a)]);f.extend([str(v)]*2);g.extend([str(direction)]*2)
 out=dict(format='completed-paired-domain-v1',p=str(p),mersenne_exponent=521,n=n,K=K,r=r,base_orbits=m0,base_support=D0,sprinkling_pairs=t,D=D,padding=padding,reference_support='first base_support base orbits, then first orbit in each sprinkling pair',domain=domain,f=f,g=g,known_nearby_codeword_at_parameter_one='zero polynomial',generator='SystemRandom uniform distinct sign-orbits excluding fixed padding; deterministic direction -f on padding',guarantee='Generator fails to cover the entire two-dimensional product image with probability <2^-88. Individual complete coverage is not deterministically certified.',seconds=time.monotonic()-start)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(output=str(args.output),bytes=args.output.stat().st_size,seconds=out['seconds'])))
