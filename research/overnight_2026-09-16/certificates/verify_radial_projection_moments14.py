"""Independent streamed identity, weight, and noise checks for degree14 data."""
from fractions import Fraction as F
from itertools import combinations
from math import comb,factorial,prod
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parent
ZERO=(0,0,0,0)


def multiply(a,b):
    out={}
    for alpha,u in a.items():
        for beta,v in b.items():
            gamma=tuple(x+y for x,y in zip(alpha,beta))
            out[gamma]=out.get(gamma,0)+u*v
    return {a:v for a,v in out.items() if v}


def compositions(total,dimension=4):
    if dimension==1:
        yield (total,)
    else:
        for a in range(total+1):
            for b in compositions(total-a,dimension-1):yield (a,)+b


def check_identities(data):
    weights=[list(map(F,row)) for row in data['radial_identity_weights']]
    norm={tuple(2*int(i==j) for i in range(4)):1 for j in range(4)}
    target=[];power={ZERO:1}
    for _ in range(7):power=multiply(power,norm);target.append(power)
    actual=[{} for _ in range(7)]
    # Stream directions rather than retaining all280 degree14 expansions.
    for rec in data['records']:
        linear={tuple(int(i==j) for i in range(4)):c for j,c in enumerate(rec['direction']) if c}
        power={ZERO:1};oid=rec['orbit']
        for degree in range(1,15):
            power=multiply(power,linear)
            if degree%2:continue
            r=degree//2;w=weights[r-1][oid]/data['orbit_sizes'][oid]
            if not w:continue
            for a,v in power.items():actual[r-1][a]=actual[r-1].get(a,F(0))+w*v
    for r in range(7):assert {a:v for a,v in actual[r].items() if v}==target[r]


def noise_direct(direction,scales):
    result=[F(1)]+[F(0)]*14
    for r in range(1,8):
        total=F(0)
        for beta in compositions(r):
            term=F(factorial(2*r),prod(factorial(2*b) for b in beta))
            for d,s,b in zip(direction,scales,beta):term*=F(d,s)**(2*b)/F((2*b+1)*2**(2*b))
            total+=term
        result[2*r]=total
    return result


def main():
    data=json.loads((ROOT/'radial_projection_moments14.json').read_text())
    assert data['status']=='computed_and_complement_checked'
    assert data['degree']==14 and data['completed_directions']==data['total_directions']==280
    check_identities(data)
    print('all seven radial polynomial identities independently verified',flush=True)
    meta=json.loads((ROOT/'radial_projections/metadata.json').read_text())
    coeffs=[list(map(F,row)) for row in meta['gram_coefficients']]
    n,t,q,C=data['n'],data['t'],data['q'],data['count'];scales=data['scales']
    assert (n,t,q,C,scales)==(meta['n'],meta['t'],meta['q'],meta['count'],meta['scales'])
    # Evaluate the rational polynomials directly, independently of the
    # producer's cleared-denominator axis-vector arithmetic.
    normalized=[[sum(c*comb(a,j) for j,c in enumerate(row))/scales[i] for a in range(n)]
                for i,row in enumerate(coeffs)]
    conditional=json.loads((ROOT/'conditional_gram_covariance.json').read_text())
    means=[F(v,C) for v in conditional['first']]
    covariance=[[F(0)]*4 for _ in range(4)];at=0
    for i in range(4):
        for j in range(i,4):
            covariance[i][j]=covariance[j][i]=F(conditional['second_upper_triangle'][at],C)-means[i]*means[j]
            at+=1
    gram_means=[(row[0]*t+row[1]*q+sum(row[j+2]*means[j] for j in range(4)))/scales[i]
                for i,row in enumerate(coeffs)]
    gram_cov=[[sum(coeffs[i][a+2]*coeffs[j][b+2]*covariance[a][b]
                   for a in range(4) for b in range(4))/scales[i]/scales[j]
               for j in range(4)] for i in range(4)]
    previous=json.loads((ROOT/'radial_projection_moments10.json').read_text())
    old={tuple(rec['direction']):list(map(F,rec['smoothed_centered_moments'])) for rec in previous['records']}
    noise_cache={};radial=[F(1)]+[F(0)]*7;overlap=0;reflected_outputs=0
    identity=[list(map(F,row)) for row in data['radial_identity_weights']]
    for rec in data['records']:
        idx=rec['index'];direction=rec['direction'];den=rec['denominator']
        raw_text=Path(rec['weights_file']).read_text()
        assert hashlib.sha256(raw_text.encode()).hexdigest()==rec['weights_sha256']
        integers=list(map(int,raw_text.split()))
        assert len(integers)==n
        assert all(F(v,den)==sum(direction[j]*normalized[j][a] for j in range(4))
                   for a,v in enumerate(integers))
        mean=sum(direction[j]*gram_means[j] for j in range(4))
        variance=sum(direction[i]*direction[j]*gram_cov[i][j] for i in range(4) for j in range(4))
        assert mean==F(rec['mean']) and variance==F(rec['variance'])
        down=json.loads((ROOT/'radial_projections14'/f'down_{idx:03d}.json').read_text())
        up=json.loads((ROOT/'radial_projections14'/f'up_{idx:03d}.json').read_text())
        for raw,count,total,mode in ((down,t,q,'down'),(up,n-t,comb(n,2)-q,'up')):
            assert (raw['n'],raw['t'],raw['q'],raw['degree'],raw['direction'])==(n,count,total,14,mode)
            assert len(raw['raw_moments'])==15 and raw['raw_moments'][0]==C
            if 'reflection_source_index' in raw:
                source_index=raw['reflection_source_index'];sign=raw['reflection_sign']
                assert 0<=source_index<idx and sign in (-1,1)
                source_rec=data['records'][source_index]
                source=json.loads((ROOT/'radial_projections14'/f'{mode}_{source_index:03d}.json').read_text())
                assert 'reflection_source_index' not in source
                assert (source['n'],source['t'],source['q'],source['degree'],source['direction'])==(n,count,total,14,mode)
                assert raw['reflection_source_weights_sha256']==source_rec['weights_sha256']
                source_weights=list(map(int,Path(source_rec['weights_file']).read_text().split()))
                assert source_rec['denominator']==den and 2*total==count*(n-1)
                assert integers==[sign*v for v in reversed(source_weights)]
                assert raw['raw_moments']==[sign**j*v for j,v in enumerate(source['raw_moments'])]
                reflected_outputs+=1
        moments=down['raw_moments']
        assert up['raw_moments']==[(-1)**j*v for j,v in enumerate(moments)]
        assert F(moments[1],C*den)==mean and F(moments[2],C*den**2)==variance+mean**2
        centered=[sum(comb(j,i)*(-mean)**(j-i)*F(moments[i],C*den**i) for i in range(j+1))
                  for j in range(15)]
        key=tuple(abs(v) for v in direction)
        if key not in noise_cache:noise_cache[key]=noise_direct(key,scales)
        noises=noise_cache[key]
        smooth=[sum(comb(j,i)*centered[i]*noises[j-i] for i in range(j+1)) for j in range(15)]
        assert smooth==list(map(F,rec['smoothed_centered_moments']))
        if tuple(direction) in old:
            assert smooth[:11]==old[tuple(direction)];overlap+=1
        oid=rec['orbit']
        for r in range(1,8):radial[r]+=identity[r-1][oid]/data['orbit_sizes'][oid]*smooth[2*r]
    assert overlap==112
    assert radial==list(map(F,data['radial_moments']))
    assert radial[:6]==list(map(F,previous['radial_moments']))
    result=dict(status='passed',n=n,t=t,q=q,count=C,scales=scales,degree=14,
                radial_moments=[str(v) for v in radial],directions=280,
                independent_polynomial_multiplication_checks=True,
                independently_reconstructed_direction_weights=True,
                independent_multinomial_cube_noise_checks=True,
                all_complement_checks=True,independent_covariance_checks=True,
                direct_mode_outputs=560-reflected_outputs,
                reflected_mode_outputs=reflected_outputs,
                all_reflection_bijections_independently_checked=True,
                overlapping_degree10_directions_checked=overlap,
                lower_radial_moments_match_prior=True)
    (ROOT/'radial_projection_moments14_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='radial_moments'},indent=2),flush=True)
    print('radial moments',[float(v) for v in radial],flush=True)


if __name__=='__main__':main()
