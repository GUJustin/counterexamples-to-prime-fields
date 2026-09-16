"""Degree-ten scalar moments on 112 rational directions, sequentially.

Six permutation/sign orbits span the even radial powers through degree ten.
All polynomial coefficients of each identity are verified exactly before
starting the compiled jobs. Every moment is checked by complementation.
"""
from fractions import Fraction as F
from itertools import combinations,permutations,product
from math import comb,factorial,gcd,lcm
from functools import reduce
from pathlib import Path
import json,subprocess,tempfile
import sympy as sp

ROOT=Path(__file__).resolve().parent
DEG=10

def compositions(total,d=4):
    if d==1:yield (total,);return
    for v in range(total+1):
        for rest in compositions(total-v,d-1):yield (v,)+rest

def orbit(base):
    out=set()
    for perm in set(permutations(base)):
        inds=[i for i,v in enumerate(perm) if v]
        for signs in product((-1,1),repeat=len(inds)-1):
            d=list(perm)
            for i,s in zip(inds[1:],signs):d[i]*=s
            out.add(tuple(d))
    return sorted(out)

def identity_weights(orbits,r):
    partitions=sorted({tuple(sorted(a,reverse=True)) for a in compositions(r)},reverse=True)
    def coefficient(group,beta):
        multinomial=factorial(sum(beta))
        for b in beta:multinomial//=factorial(b)
        # Sequential factorial division is not generally integral; use Fraction.
        multinomial=F(factorial(sum(beta)),reduce(lambda x,y:x*factorial(y),beta,1))
        return multinomial*sum(reduce(lambda x,iv:x*iv[0]**iv[1],zip(d,beta),1) for d in group)/len(group)
    matrix=sp.Matrix([[sp.Rational(coefficient(group,tuple(2*a for a in alpha))) for group in orbits] for alpha in partitions])
    target=sp.Matrix([sp.Rational(factorial(r),reduce(lambda x,y:x*factorial(y),alpha,1)) for alpha in partitions])
    solution,parameters=matrix.gauss_jordan_solve(target)
    solution=solution.subs({v:0 for v in parameters})
    weights=[F(int(v.p),int(v.q)) for v in solution]
    for beta in compositions(2*r):
        actual=sum(w*coefficient(group,beta) for w,group in zip(weights,orbits))
        wanted=F(0) if any(b%2 for b in beta) else F(factorial(r),reduce(lambda x,y:x*factorial(y//2),beta,1))
        assert actual==wanted,(r,beta,actual,wanted)
    return weights

def noise(direction,scales):
    out=[F(1)]+[F(0)]*DEG
    for c,s in zip(direction,scales):
        u=[F(c,s)**j/F((j+1)*2**j) if j%2==0 else F(0) for j in range(DEG+1)]
        out=[sum(comb(j,i)*out[i]*u[j-i] for i in range(j+1)) for j in range(DEG+1)]
    return out

def fixture(binary):
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp);n,t,Q=9,4,16
        weights=[(a-4)**5*2**97+3*(a-4) for a in range(n)]
        path=root/'weights.txt';path.write_text('\n'.join(map(str,weights))+'\n')
        vals=[sum(weights[a] for a in A) for A in combinations(range(n),t) if sum(A)==Q]
        expected=[sum(v**j for v in vals) for j in range(DEG+1)]
        for t0,q0,mode in [(t,Q,'down'),(n-t,comb(n,2)-Q,'up')]:
            output=root/'out.json'
            subprocess.run([str(binary),str(n),str(t0),str(q0),str(path),str(output),mode],check=True,stderr=subprocess.DEVNULL)
            actual=json.loads(output.read_text())['raw_moments']
            assert actual==[(-1)**j*v if mode=='up' else v for j,v in enumerate(expected)]

def main():
    binary=ROOT/'scalar_conditional_moments10';fixture(binary)
    old=json.loads((ROOT/'radial_projection_moments.json').read_text());n,t,Q,C=old['n'],old['t'],old['q'],old['count']
    axis={tuple(v['direction']).index(1):v for v in old['records'] if sum(x!=0 for x in v['direction'])==1}
    axis_values=[[int(s) for s in Path(axis[j]['weights_file']).read_text().split()] for j in range(4)]
    cov=[[F(0)]*4 for _ in range(4)]
    for j in range(4):cov[j][j]=F(axis[j]['variance'])
    for j,k in combinations(range(4),2):
        direction=[0]*4;direction[j]=direction[k]=1
        pair=next(v for v in old['records'] if v['direction']==direction)
        cov[j][k]=cov[k][j]=(F(pair['variance'])-cov[j][j]-cov[k][k])/2
    bases=[(1,0,0,0),(1,1,0,0),(2,1,0,0),(1,1,1,0),(2,1,1,0),(1,1,1,1)]
    orbits=[orbit(base) for base in bases]
    assert list(map(len,orbits))==[4,12,24,16,48,8]
    identities=[identity_weights(orbits,r) for r in range(1,6)]
    folder=ROOT/'radial_projections10';folder.mkdir(exist_ok=True)
    metadata=dict(n=n,t=t,q=Q,count=C,degree=DEG,scales=old['scales'],
                  orbit_bases=bases,orbit_sizes=list(map(len,orbits)),
                  radial_identity_weights=[[str(w) for w in row] for row in identities])
    (folder/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
    records=[];radial=[F(1)]+[F(0)]*5
    for oid,group in enumerate(orbits):
        for direction in group:
            idx=len(records);den=lcm(*(axis[j]['denominator'] for j in range(4) if direction[j]))
            integers=[sum(direction[j]*(den//axis[j]['denominator'])*axis_values[j][a] for j in range(4) if direction[j]) for a in range(n)]
            common=reduce(gcd,integers,den);den//=common;integers=[v//common for v in integers]
            assert sum(integers)==0
            wf=folder/f'weights_{idx:03d}.txt';wf.write_text('\n'.join(map(str,integers))+'\n')
            down=folder/f'down_{idx:03d}.json';up=folder/f'up_{idx:03d}.json'
            for t0,q0,path,mode in [(t,Q,down,'down'),(n-t,comb(n,2)-Q,up,'up')]:
                subprocess.run([str(binary),str(n),str(t0),str(q0),str(wf),str(path),mode],check=True,timeout=180)
            M=json.loads(down.read_text())['raw_moments'];Mup=json.loads(up.read_text())['raw_moments']
            assert M[0]==C and Mup==[(-1)**j*v for j,v in enumerate(M)]
            mean=sum(direction[j]*F(axis[j]['mean']) for j in range(4))
            variance=sum(direction[j]*direction[k]*cov[j][k] for j in range(4) for k in range(4))
            assert F(M[1],C*den)==mean and F(M[2],C*den*den)==variance+mean*mean
            raw=[F(v,C*den**j) for j,v in enumerate(M)]
            centered=[sum(comb(j,i)*(-mean)**(j-i)*raw[i] for i in range(j+1)) for j in range(DEG+1)]
            noises=noise(direction,old['scales'])
            smooth=[sum(comb(j,i)*centered[i]*noises[j-i] for i in range(j+1)) for j in range(DEG+1)]
            for r in range(1,6):radial[r]+=identities[r-1][oid]/len(group)*smooth[2*r]
            records.append(dict(index=idx,orbit=oid,direction=direction,denominator=den,
                                weights_file=str(wf),mean=str(mean),variance=str(variance),
                                smoothed_centered_moments=[str(v) for v in smooth],
                                complement_check=True,independent_covariance_check=True))
            result=dict(**metadata,status='in_progress' if len(records)<112 else 'computed_and_complement_checked',
                        completed_directions=len(records),radial_moments=[str(v) for v in radial],records=records)
            (ROOT/'radial_projection_moments10.json').write_text(json.dumps(result,indent=2)+'\n')
            print('verified projection',idx,'orbit',oid,'direction',direction,flush=True)
    assert radial[:4]==list(map(F,old['radial_moments']))
    print('radial moments',[float(v) for v in radial],flush=True)

if __name__=='__main__':main()
