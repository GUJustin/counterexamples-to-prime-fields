import itertools,json,time,collections
from pathlib import Path
start=time.time(); mod=0x11b

def mul(a,b):
 c=0
 while b:
  if b&1:c^=a
  b>>=1;a<<=1
  if a&256:a^=mod
 return c
M=[[mul(a,b) for b in range(256)] for a in range(256)]
def pw(a,n):
 r=1
 while n:
  if n&1:r=M[r][a]
  a=M[a][a];n>>=1
 return r
inv=[0]+[pw(a,254) for a in range(1,256)]
assert all(M[a][inv[a]]==1 for a in range(1,256))
def loc(rows):
 c=[1]
 for x in rows:
  z=0;y=x
  for a in c:z^=M[a][y];y=M[y][y]
  assert z
  c=[M[z][c[0]]]+[M[c[j-1]][c[j-1]]^M[z][c[j]] for j in range(1,len(c))]+[M[c[-1]][c[-1]]]
 return c
G=collections.defaultdict(list);universal=[];impossible=0;count=0
for piv in itertools.combinations(range(7),4):
 free=[(i,j) for i in range(4) for j in range(piv[i]+1,7) if j not in piv]
 for bits in range(1<<len(free)):
  rows=[1<<j for j in piv]
  for n,(i,j) in enumerate(free):
   if bits>>n&1:rows[i]|=1<<j
  E,C,B,A,one=loc(rows);assert one==1;count+=1
  u=pw(C,2)^M[B][pw(A,2)];v=B
  k=pw(E,4)^M[pw(A,4)][pw(C,2)]^pw(B,5)^M[B][pw(A,6)]
  rec={'rows':rows,'locator':[E,C,B,A,1]}
  if not(u or v):
   if k:impossible+=1
   else:universal.append(rec)
   continue
  scale=inv[u or v]; key=(M[scale][u],M[scale][v],M[scale][k]);G[key].append(rec)
# Parameterize each line by theta in quadratic extension; retain z as affine pair.
out=[]
for (u,v,k),rr in G.items():
 labels={}
 for rec in rr+universal:
  E,C,B,A,_=rec['locator']
  zs=pw(B,2)^pw(A,3)
  zc=pw(C,4)^M[pw(A,4)][pw(B,2)]^M[A][pw(B,4)]^pw(A,7)
  if v: # theta1=theta,theta2=(u/v)theta+k/v
   slope=zs^M[A][M[u][inv[v]]];const=zc^M[A][M[k][inv[v]]]
  else: # theta1=k/u,theta2=theta
   slope=A;const=zc^M[zs][M[k][inv[u]]]
  labels.setdefault((slope,const),[]).append(rec)
 out.append({'head_line':[u,v,k],'subspaces':len(rr),'labels':len(labels),'max_label_multiplicity':max(map(len,labels.values())),'label_pairs':[list(z) for z in labels]})
out.sort(key=lambda r:(r['labels'],r['subspaces']),reverse=True)
result={'p':2,'field_modulus':mod,'coefficient_field_dimension':8,'dimension':7,'subspace_dimension':4,'subspaces':count,'head_lines':len(G),'universal_subspaces':len(universal),'impossible_subspaces':impossible,'group_size_histogram':dict(collections.Counter(map(len,G.values()))),'label_histogram':dict(collections.Counter(r['labels'] for r in out)),'best':out[:12],'elapsed_seconds':time.time()-start}
assert count==11811
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k!='best'},indent=2)); print('best',[(r['head_line'],r['subspaces'],r['labels']) for r in out[:12]])
