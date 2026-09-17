"""Independent integer-binomial replay of subgroup-orbit scans."""
from math import comb,isqrt
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent

def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def fixture(row,c):
 r,j,k,L,p,g=(row[x] for x in ('r','section','k','L','p','generator'))
 e=r*k+j;coeff=[comb(e,r*i+j)%p for i in range(k+1)]
 assert coeff[-1]==1 and coeff[1]!=0
 assert len({pow(g,i,p) for i in range(p-1)})==p-1
 H=[pow(g,(p-1)//L*i,p) for i in range(L)]
 assert len(set(H))==L and all(pow(h,k,p)==1 for h in H)
 def value(x):return sum(a*pow(x,i,p) for i,a in enumerate(coeff))%p
 cosets=[]
 for t in range((p-1)//L):
  xs=[pow(g,t,p)*h%p for h in H];counts={}
  for x in xs:counts[value(x)]=counts.get(value(x),0)+1
  best=max(counts.values());symbol=min(v for v,m in counts.items() if m==best)
  cosets.append((best,t,symbol,xs))
 cosets.sort(key=lambda x:(-x[0],x[1]));chosen=cosets[:c*k//L]
 A=sum(x[0] for x in chosen);assert [c,A] in row['agreements']
 domain=[x for _,_,_,xs in chosen for x in xs]
 word={x:(v-pow(x,k,p))%p for _,_,v,xs in chosen for x in xs}
 assert len(domain)==len(set(domain))==c*k
 profiles=[sum((value(h*x%p)-pow(x,k,p))%p==word[x] for x in domain) for h in H]
 assert profiles==[A]*L
 return dict(r=r,section=j,k=k,L=L,p=p,n=c*k,A=A,all_candidates_replayed=L)

def main():
 start=time.monotonic();rows=json.loads((BASE/'subgroup_sections_scan.json').read_text())
 expected={(r,j,k,L) for k in (16,32,64,128) for r in range(2,49) if prime(2*r*k+1)
           for j in range(r) for L in (4,8,16,32,64,128) if L<=k}
 assert {(x['r'],x['section'],x['k'],x['L']) for x in rows}==expected
 assert len(rows)==len(expected)
 old={(x['r'],x['section'],x['k']):x for x in json.loads((BASE/'all_sections_scan.json').read_text())}
 hits={c:[] for c in (4,8,16,32)}
 for row in rows:
  k,L,p=row['k'],row['L'],row['p'];assert p==2*row['r']*k+1
  assert [v[0] for v in row['agreements']]==[c for c in hits if c*k<=p-1]
  for c,A in row['agreements']:
   n=c*k
   if L==k:assert A==sum(x[1] for x in old[row['r'],row['section'],k]['cosets'][:c])
   if A>k and n**n*(p-1)**(n-A)<(n-A)**(n-A)*A**A*p**(n-k):
    hits[c].append(dict(r=row['r'],section=row['section'],k=k,L=L,p=p,n=n,A=A))
 selected=[]
 for c,entries in hits.items():
  if entries:
   entry=max(entries,key=lambda x:(x['L'],x['k'],-x['r']))
   row=next(x for x in rows if all(x[t]==entry[t] for t in ('r','section','k','L')))
   selected.append(fixture(row,c))
 # Additional genuinely restricted orbits at larger dimensions.
 for r,j,k,L,c in ((2,1,64,32,4),(3,1,16,8,4),(3,1,128,32,4),(33,0,32,8,4)):
  candidate=next((x for x in rows if (x['r'],x['section'],x['k'],x['L'])==(r,j,k,L)),None)
  if candidate:selected.append(fixture(candidate,c))
 summary={str(c):dict(below_elias_cases=len(v),largest_L=max((x['L'] for x in v),default=0),
             largest_k=max((x['k'] for x in v),default=0),hits=v) for c,v in hits.items()}
 out=dict(status='passed',cases=len(rows),independent_fixtures=selected,summary=summary,
          seconds=time.monotonic()-start,scope='Finite subgroup orbit search; no unbounded family claim.')
 (BASE/'subgroup_sections_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({**out,'summary':{c:{k:v for k,v in x.items() if k!='hits'} for c,x in summary.items()}},indent=2))
if __name__=='__main__':main()
