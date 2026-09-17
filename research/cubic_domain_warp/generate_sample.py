"""Sample the code/domain/line directly, without enumerating a moment class.

Coverage has a generator-level probability guarantee. This program does
not claim to deterministically certify coverage of its individual output.
"""
from pathlib import Path
from secrets import SystemRandom
import argparse,json,time
BASE=Path(__file__).resolve().parent


def coefficients(roots,p):
 a=[1]
 for root in roots:
  b=[0]*(len(a)+1)
  for i,v in enumerate(a):b[i]=(b[i]-root*v)%p;b[i+1]=(b[i+1]+v)%p
  a=b
 return a


def evaluate(a,x,p):
 v=0
 for c in reversed(a):v=(v*x+c)%p
 return v


def generate():
 start=time.monotonic();rng=SystemRandom();b=521;p=(1<<b)-1
 n=990;K=495;m=900;t=497;s=1;q=n-m+1
 support=[0]+sorted(rng.sample(range(1,m),t-1))
 tries=0
 while True:
  a=rng.randrange(p);bcoef=rng.randrange(p);tries+=1
  images=[(x*x*x+bcoef*x*x+a*x)%p for x in range(m)]
  if len(set(images))==m:break
 core=images[1:];chosen=set(core);padding=[]
 while len(padding)<q:
  x=rng.randrange(p)
  if x not in chosen:chosen.add(x);padding.append(x)
 directions=[rng.randrange(1,p) for _ in padding]
 roots=[images[x] for x in support if x]
 w=coefficients(roots,p);domain=core+padding
 f=[evaluate(w,x,p) for x in domain];g=[0]*len(core)+directions
 assert len(set(domain))==n and len(f)==len(g)==n
 assert sum(v==0 for v in f)==t-1
 return dict(format='cubic-prime-field-line-v1',prime_exponent=521,p=str(p),n=n,K=K,m=m,
             threshold=t,seed_moments=3*s,transformed_moments=s,anchor=0,
             original_support=support,cubic_a=str(a),cubic_b=str(bcoef),
             domain=[str(x) for x in domain],f=[str(x) for x in f],g=[str(x) for x in g],
             injectivity_trials=tries,seconds=time.monotonic()-start,
             generator_failure_probability_bound='less than 2^-128',
             probability_scope='Over the uniform randomness of the generator; not a deterministic coverage certificate for this individual sample.',
             deterministic_properties=['distinct domain points','half rate','global starting polynomial degree496','exact zero-parameter maximum agreement496','no correlated agreement at threshold497'])

if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,default=BASE/'samples/m521_n990.json');args=parser.parse_args()
 if args.output.exists():raise SystemExit('Output already exists; choose a fresh --output path.')
 out=generate();args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(dict(output=str(args.output),n=out['n'],K=out['K'],seconds=out['seconds'],injectivity_trials=out['injectivity_trials'],probability_scope=out['probability_scope']),indent=2))
