"""Sample the paired n2518, rate1/2, four-fifths-gap construction."""
from pathlib import Path
from random import SystemRandom
import argparse,json,time
BASE=Path(__file__).resolve().parent

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=BASE/'samples/m521_r2_n2518.json');args=parser.parse_args()
 if args.output.exists():raise SystemExit('Refusing to replace an existing sample')
 start=time.monotonic();rng=SystemRandom();p=2**521-1;n=2518;K=1259;m=1211;D=630;r=2;q=24
 reps=[];seen=set()
 while len(reps)<n//2:
  a=rng.randrange(1,(p+1)//2)
  if a not in seen:seen.add(a);reps.append(a)
 # Polynomial in Y=X²; independent verifier uses direct root products.
 coeff=[1]
 for a in reps[:D]:
  root=a*a%p;new=[0]*(len(coeff)+1)
  for j,c in enumerate(coeff):new[j]=(new[j]-root*c)%p;new[j+1]=(new[j+1]+c)%p
  coeff=new
 domain=[];f=[];g=[]
 for i,a in enumerate(reps):
  y=a*a%p;v=0
  for c in reversed(coeff):v=(v*y+c)%p
  h=0 if i<m else rng.randrange(1,p)
  domain.extend([str(a),str(p-a)]);f.extend([str(v),str(v)]);g.extend([str(h),str(h)])
 out=dict(format='paired-domain-line-v1',p=str(p),mersenne_exponent=521,n=n,K=K,m=m,D=D,r=r,blocks=q,reference_support='first D core orbits',domain=domain,f=f,g=g,generator='SystemRandom uniform distinct nonzero sign-orbits, independent uniform nonzero pair directions',guarantee='Generator failure probability <2^-128 by the paired-block theorem; individual all-parameter coverage is not deterministically certified.',seconds=time.monotonic()-start)
 args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(dict(output=str(args.output),bytes=args.output.stat().st_size,seconds=out['seconds'])))
if __name__=='__main__':main()
