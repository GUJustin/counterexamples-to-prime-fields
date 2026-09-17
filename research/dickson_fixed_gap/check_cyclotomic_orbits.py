"""Check whether either multiplicative orbit of seed supports lifts."""
from pathlib import Path
import json,time
from check_cyclotomic_lift import supports,rank,prime,generator

start=time.monotonic();rows=[]
for p in [17,41,97,193,257,337]:
 n=p-1;k=n//4;sets=supports(p);g=generator(p)
 q=((65536+n-1)//n)*n+1
 while not prime(q):q+=n
 z=pow(generator(q),(q-1)//n,q)
 nodes={pow(g,j,p):pow(z,j,q) for j in range(n)}
 for chi in [1,p-1]:
  selected=[S for a,S in enumerate(sets,1) if pow(a,(p-1)//2,p)==chi]
  used=set().union(*map(set,selected))
  # Eliminate unused columns so the kernel cannot hide in untouched positions.
  order=sorted(used);index={x:i+1 for i,x in enumerate(order)}
  relabeled=[[index[x] for x in S] for S in selected]
  mapped={index[x]:nodes[x] for x in order}
  r,count,prefix=rank(relabeled,len(order),k,q,mapped)
  rows.append(dict(p=p,n=n,K=k,chi=1 if chi==1 else -1,supports=len(selected),
                   used_coordinates=len(used),auxiliary_prime=q,rank=r,
                   kernel_dimension=len(used)-r,only_global_codewords=(r==len(used)-k),
                   rows_used=count,prefix_sufficing=prefix))
out=dict(status='passed',results=rows,seconds=time.monotonic()-start,
         scope='Exact modular ranks on each full seed orbit, excluding unused coordinates. Full rank certifies no characteristic-zero lift of that orbit on natural cyclotomic nodes; deficient rank would require further analysis.')
Path(__file__).with_name('cyclotomic_orbits_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
