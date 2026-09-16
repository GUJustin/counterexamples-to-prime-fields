"""Check incidences by formal division of the unconditioned subset product."""
from pathlib import Path
from math import comb
from fractions import Fraction as F
import argparse,csv,json,subprocess,time
from rational_circle_bounds import ln,ln2,entropy,div


def coefficient(n,k,q,Y):
    if k==0:return int(q==0 and Y==0)
    if q<k*(k-1)//2 or q>k*(2*n-k-1)//2 or Y<0:return 0
    path=Path('exact_support_incidence_deconvolution.csv')
    run=subprocess.run([str(Path('central_quadratic_histogram').resolve()),str(n),str(k),'linear',str(path),str(q)],check=True,text=True,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
    info=json.loads(run.stdout);index=Y-info['Y_offset']
    if index<0 or index>info['vmax']:return 0
    for row in csv.DictReader(path.open()):
        if int(row['v'])==index:return int(row['count'])
    raise AssertionError('missing coefficient')


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--n',type=int,default=82)
    parser.add_argument('--t',type=int,default=12);parser.add_argument('--q',type=int)
    args=parser.parse_args();n,t=args.n,args.t;q=t*(n-1)//2 if args.q is None else args.q
    start=time.monotonic();path=Path(f'exact_support_incidences_n{n}_t{t}_q{q}.json')
    data=json.loads(path.read_text());Y=data['Y'];counts=[]
    for x in range(n):
        count=sum((-1)**(j-1)*coefficient(n,t-j,q-j*x,Y-j*comb(x,2)) for j in range(1,t+1))
        assert count==data['incidences'][x];counts.append(count)
        if (x+1)%10==0:print('deconvolution checked',n,t,q,x+1,flush=True)
    N=data['source_words'];assert sum(counts)==t*N
    shared=sum(c*(c-1)//2 for c in counts)
    budget=data['k']*N*(N-1)//2-shared
    assert shared==data['shared_root_pair_total'] and budget==data['outside_pair_collision_budget']
    cap=budget//(data['p']-n);J=data['distinct_labels']
    def collisions(j):
        a,b=divmod(N,j);return b*(a+1)*a//2+(j-b)*a*(a-1)//2
    assert collisions(J)<=cap and (J==1 or collisions(J-1)>cap)
    rho=F(data['k'],n);eta=F(t-data['k'],n);a,b,h=ln(F(J)),ln(F(n)),entropy(rho)
    excess=div((a[0]-b[1]-h[1]/eta,a[1]-b[0]-h[0]/eta),ln2)
    assert list(map(str,excess))==data['exact_excess_bits']
    result=dict(status='passed',n=n,t=t,q=q,Y=Y,distinct_labels=J,source_words=N,
        exact_coordinate_incidences_match_unconditioned_formal_division=True,
        exact_collision_partition_check=True,exact_excess_bits_match=True,
        excess_bits_lower=float(excess[0]),seconds=time.monotonic()-start,
        scope='Different unconditioned recurrence identity and item order; same underlying centered histogram engine.')
    Path(f'exact_support_incidences_n{n}_t{t}_q{q}_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    data['status']='passed';data['separate_verification_file']=f'exact_support_incidences_n{n}_t{t}_q{q}_verification.json'
    path.write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
