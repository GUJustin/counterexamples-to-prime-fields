"""Generate a specialized complete large-coset pencil scanner.

Applicable when every >=A match candidate has a coset containing m>=ceil(A/4)
with ceil((A-m)/2)>=k-1-m. Otherwise use the separate W12 balanced branch.
The template is the audited W12 implementation, with that branch removed.
"""
from pathlib import Path
import argparse, re
ap=argparse.ArgumentParser();ap.add_argument('k',type=int);ap.add_argument('agreement',type=int);ap.add_argument('prime',type=int);args=ap.parse_args()
k,A,p=args.k,args.agreement,args.prime;n=4*k;m0=(A+3)//4
assert A>k and all((A-m+1)//2>=k-1-m for m in range(m0,k))
assert (p-1)%n==0
s=(Path(__file__).parent/'r12_unrestricted/search.cpp').read_text()
s=s[:s.index('void balanced()')]+s[s.index('int main('):]
s=s.replace('if(!stop())balanced();','')
s=s.replace('const int p=1009','const int p=FIELDPRIME')
s=re.sub(r'\b48\b',str(n),s);s=re.sub(r'\b12\b',str(k),s)
s=s.replace('m=5;m<=11',f'm={m0};m<={k-1}').replace('int d=11-m',f'int d={k-1}-m')
s=s.replace('hits<16',f'hits<{A}').replace('bucket[t]>=5',f'bucket[t]>={A-k+1}')
a=(3*k+1)//2
s=s.replace('vector<int>v(outside.begin()+18*half,outside.begin()+18*(half+1));',f'vector<int>v(outside.begin()+(half?{a}:0),outside.begin()+(half?{3*k}:{a}));')
factors=[q for q in range(2,n+1) if n%q==0 and all(q%d for d in range(2,int(q**.5)+1))]
check='&&'.join([f'pw(a,{n})==1']+[f'pw(a,{n//q})!=1' for q in factors])
s=s.replace(f'pw(a,{n})==1&&pw(a,24)!=1&&pw(a,16)!=1',check)
s=s.replace('FIELDPRIME',str(p))
d=Path(__file__).parent/f'r{k}_unrestricted';d.mkdir(exist_ok=True);(d/'search.cpp').write_text(s)
print(d/'search.cpp')
