"""Independent all-subset modular rank audit and exact sqrt(d)-basis replay."""
import json,itertools,time
from pathlib import Path
from flint import fmpq as Q,fmpq_mat,nmod_mat,nmod_poly
D=Path(__file__).parent;source=json.loads((D/'rational_seed.json').read_text());fresh=json.loads((D/'pair_padding_gate.json').read_text())['candidates']
for label,disc in [('ten',17),('eleven',39)]:
 start=time.monotonic();screen=json.loads((D/f'{label}_quadratic_norm_screen.json').read_text());prime=screen['prime'];xm=screen['nodes'];wm=screen['word'];n=len(xm)
 z=(Q(0),Q(0));one=(Q(1),Q(0))
 def add(a,b):return a[0]+b[0],a[1]+b[1]
 def neg(a):return -a[0],-a[1]
 def sub(a,b):return add(a,neg(b))
 def mul(a,b):return a[0]*b[0]+disc*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
 def inv(a):
  norm=a[0]*a[0]-disc*a[1]*a[1];assert norm!=0
  return a[0]/norm,-a[1]/norm
 def div(a,b):return mul(a,inv(b))
 def scale(a,k):return a[0]*k,a[1]*k
 def power(a,k):
  b=one
  for _ in range(k):b=mul(b,a)
  return b
 def ev(c,x):
  v=z
  for a in reversed(c):v=add(mul(v,x),a)
  return v
 X=[(Q(x),Q(0)) for x in source['affine_nodes']];W=[(Q(x),Q(0)) for x in source['affine_word']]
 F0=[(Q(x),Q(0)) for x in fresh[0]['coefficients']]
 if label=='ten':
  a=(Q(-125,716),Q(55,716));b=(a[0],-a[1]);X +=[a,b];W +=[ev(F0,a),ev(F0,b)]
 else:
  a=(Q(-80,163),Q(0));b=(Q(-135,262),Q(0));c=(Q(-4175,7652),Q(55,7652));X +=[a,b,c]
  F2=[(Q(x),Q(0)) for x in fresh[2]['coefficients']];W +=[ev(F0,a),ev(F0,b),ev(F2,c)]
 # Identify the embedding sqrt(d) -> residue field from the actual new node.
 idx=16 if label=='ten' else 18
 def redq(a):return int(a.numerator)%prime*pow(int(a.denominator)%prime,-1,prime)%prime
 root=(xm[idx]-redq(X[idx][0]))*pow(redq(X[idx][1]),-1,prime)%prime
 assert root*root%prime==disc%prime
 red=lambda a:(redq(a[0])+root*redq(a[1]))%prime
 assert list(map(red,X))==xm and list(map(red,W))==wm
 # Reverse variable ordering: C6..C0,B3..B0.
 R=[[power(x,i) for i in range(6,-1,-1)]+[mul(w,power(x,i)) for i in range(3,-1,-1)]+[neg(mul(w,w))] for x,w in zip(X,W)]
 H=[]
 for x,w in zip(X,W):
  hy=[z]*7+[power(x,i) for i in range(3,-1,-1)]+[scale(w,-2)]
  hx=[scale(power(x,i-1),i) if i else z for i in range(6,-1,-1)]+[scale(mul(w,power(x,i-1)),i) if i else z for i in range(3,-1,-1)]+[z]
  H.append([hy,hx])
 RM=[[red(a) for a in row] for row in R];HM=[[[red(a) for a in row] for row in pair] for pair in H]
 def canon(v):return list(reversed(v[7:]))+list(reversed(v[:7]))
 # Retain every coefficient-rank exception, regardless of augmented consistency.
 needed=[];exceptions=[];mod_counts={'inconsistent_full_rank':0,'unique_rejected':0,'unique_retained':0}
 for size in [11,12]:
  for I in itertools.combinations(range(n),size):
   a,rank=nmod_mat([RM[j] for j in I],prime).rref();piv=[];inconsistent=False;vv=[0]*11
   for i in range(rank):
    c=next(j for j in range(12) if a[i,j]!=0)
    if c==11:inconsistent=True
    else:piv.append(c);vv[c]=int(a[i,11])
   if len(piv)<11:exceptions.append(I);needed.append(I);continue
   if inconsistent:mod_counts['inconsistent_full_rank']+=1;continue
   if size==11:
    good=[j for j in I if all(sum(a*b for a,b in zip(row[:11],vv))%prime==row[11] for row in HM[j])]
    if len(good)<2:mod_counts['unique_rejected']+=1;continue
   v=canon(vv);E=nmod_poly([-a*pow(2,-1,prime)%prime for a in v[:4]],prime);J=E*E-nmod_poly(v[4:],prime)
   odd=0 if J.is_zero() else sum(f.degree() for f,e in J.factor()[1] if e%2)+(6-J.degree())%2
   if odd<=2:needed.append(I);mod_counts['unique_retained']+=1
   else:mod_counts['unique_rejected']+=1
 assert set(exceptions)=={tuple(r['subset']) for r in screen['rank_exceptional_systems']}
 retained={tuple(r['subset']) for r in screen['accepted_systems']}|set(exceptions)
 assert set(needed)<=retained
 def solve(rows):
  rr=[]
  for row in rows:
   aa=[];bb=[]
   for a,b in row[:11]:aa +=[a,disc*b];bb +=[b,a]
   rr +=[aa+[row[11][0]],bb+[row[11][1]]]
  a,rank=fmpq_mat(rr).rref();vv=[Q(0)]*22;cnt=0
  for i in range(rank):
   c=next(j for j in range(23) if a[i,j]!=0)
   if c==22:return None,0
   vv[c]=a[i,22];cnt+=1
  return [(vv[2*j],vv[2*j+1]) for j in range(11)],22-cnt
 def sat(row,v):
  a=z
  for x,y in zip(row[:11],v):a=add(a,mul(x,y))
  return a==row[11]
 unique=set();unresolved=[];exact_pairs=0
 for I in needed:
  rows=[R[j] for j in I];v,dim=solve(rows)
  if v is None:continue
  if dim:
   if len(I)==12:unresolved.append(I);continue
   for pair in itertools.combinations(I,2):
    exact_pairs+=1;vv,dd=solve(rows+[r for j in pair for r in H[j]])
    if vv is None:continue
    if dd:unresolved.append((I,pair));continue
    unique.add(tuple(canon(vv)))
  else:
   if len(I)==11 and sum(all(sat(row,v) for row in H[j]) for j in I)<2:continue
   unique.add(tuple(canon(v)))
 assert not unresolved
 def trim(a):
  while a and a[-1]==z:a.pop()
  return a
 def pdiv(a,b):
  a=trim(list(a));b=trim(list(b));assert b
  q=[z]*max(0,len(a)-len(b)+1)
  while len(a)>=len(b):
   i=len(a)-len(b);c=div(a[-1],b[-1]);q[i]=c
   for j,t in enumerate(b):a[i+j]=sub(a[i+j],mul(c,t))
   trim(a)
  return trim(q),a
 def gcd(a,b):
  while b:a,b=b,pdiv(a,b)[1]
  return [div(x,a[-1]) for x in a] if a else []
 oddhist={};norms=[]
 for v in unique:
  E=[scale(a,Q(-1,2)) for a in v[:4]];J=[neg(a) for a in v[4:]]
  for i,a in enumerate(E):
   for j,b in enumerate(E):J[i+j]=add(J[i+j],mul(a,b))
  J=trim(J);odd=0
  if J:
   odd=(7-len(J))%2
   deriv=[scale(J[i],i) for i in range(1,len(J))];c=gcd(J,deriv);w,rr=pdiv(J,c);assert not rr;i=1
   while len(w)>1:
    y=gcd(w,c);zz,rr=pdiv(w,y);assert not rr
    if i%2:odd+=len(zz)-1
    w=y;c,rr=pdiv(c,y);assert not rr;i+=1
  oddhist[odd]=oddhist.get(odd,0)+1
  norms.append({'B':[[str(a),str(b)] for a,b in v[:4]],'C':[[str(a),str(b)] for a,b in v[4:]],'odd_degree':odd})
 assert set(oddhist)=={0}
 expected=json.loads((D/f'{label}_quadratic_norm_exact.json').read_text());assert len(unique)==expected['exact_norms']
 out=dict(pass_all=True,prime=prime,embedding_sqrt=root,total_subsets=sum(1 for size in [11,12] for I in itertools.combinations(range(n),size)),rank_exceptions=len(exceptions),retained_base_systems=len(needed),mod_counts=mod_counts,exact_pair_refinements=exact_pairs,exact_norms=len(unique),unresolved=unresolved,odd_degree_counts=oddhist,records=norms,seconds=time.monotonic()-start)
 (D/f'{label}_quadratic_norm_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(label,{k:v for k,v in out.items() if k!='records'})
