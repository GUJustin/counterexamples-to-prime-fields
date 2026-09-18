import itertools,json,time,math
from pathlib import Path
start=time.time();results=[]
for p in (3,5):
 q=p**3
 c0,c1=next((c0,c1) for c0 in range(1,p) for c1 in range(p) if all((x**3+c1*x+c0)%p for x in range(p)))
 el=list(itertools.product(range(p),repeat=3));idx={t:i for i,t in enumerate(el)};zero=idx[(0,0,0)];one=idx[(1,0,0)]
 def add(x,y):return idx[tuple((a+b)%p for a,b in zip(el[x],el[y]))]
 def multiply(x,y):
  h=[0]*5
  for i in range(3):
   for j in range(3):h[i+j]+=el[x][i]*el[y][j]
  for k in (4,3):h[k-3]-=c0*h[k];h[k-2]-=c1*h[k]
  return idx[tuple(v%p for v in h[:3])]
 A=[[add(x,y) for y in range(q)] for x in range(q)];M=[[multiply(x,y) for y in range(q)] for x in range(q)]
 neg=[idx[tuple(-v%p for v in t)] for t in el]
 def power(x,k):
  z=one
  while k:
   if k&1:z=M[z][x]
   x=M[x][x];k//=2
  return z
 xs=[x for x in range(q) if x!=zero];w=[power(x,2*p) for x in xs];squares={M[x][x] for x in range(q)}
 maxima={};examples={};checked=0
 for a,c in itertools.product(range(q),repeat=2):
  b=A[one][neg[A[a][c]]]
  disc=A[M[c][c]][neg[M[idx[(4%p,0,0)]][M[a][b]]]]
  issquare=(a!=zero and disc==zero and a in squares) or (a==zero and c==zero and b in squares)
  typ='square' if issquare else ('non_even_nonsquare' if c!=zero else 'even_nonsquare')
  count=(b==zero)+sum(A[A[M[a][M[x][x]]][M[c][x]]][b]==v for x,v in zip(xs,w))
  bound=p+1 if issquare else (8 if c!=zero else p+math.isqrt(4*p))
  assert count<=bound,(p,a,c,b,count,typ)
  if count>maxima.get(typ,-1):maxima[typ]=count;examples[typ]=[el[a],el[c],el[b]]
  checked+=1
 results.append(dict(p=p,modulus=[c0,c1,0,1],normalized_polynomials=checked,maxima=maxima,examples=examples))
out=dict(method='all Q(1)=1, multiplicative scaling covers every nonzero matching coordinate; zero included iff b=0',results=results,seconds=time.time()-start)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
