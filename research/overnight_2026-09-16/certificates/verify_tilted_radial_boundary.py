"""Raw-moment and Cartesian-integral audit of a displaced radial boundary."""
from fractions import Fraction as F
from math import comb,prod,isqrt
from pathlib import Path
import argparse,json,time,hashlib
from compute_radial_projection_moments10 import orbit
from verify_radial_projection_moments14 import noise_direct,multiply
from verify_radial_weight_certificates import pi_bounds
from rational_circle_bounds import ln,ln2,entropy,div,elias


def convolve(a,b):
    result=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b):result[i+j]+=u*v
    return result


def square_root_interval(x):
    scale=10**95;k=isqrt(x.numerator*scale**2//x.denominator)
    return F(k,scale),F(k+1,scale)


def exact_root(x):
    a,b=isqrt(x.numerator),isqrt(x.denominator)
    assert a*a==x.numerator and b*b==x.denominator
    return F(a,b)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--dimension',type=int,choices=(3,4),required=True);args=parser.parse_args()
    d=args.dimension;start=time.monotonic();certificate=Path(f'tilted_radial{d}d_boundary_verification.json');claim=json.loads(certificate.read_text())
    all_data=json.loads(Path('radial_projection_moments14.json').read_text());scales4=all_data['scales']
    if d==4:
        data=all_data;design=data;base=json.loads(Path('radial_moment_optimum7_verification.json').read_text())
        roots=list(map(F,base['refined_roots']));lookup={tuple(r['direction']):r['orbit'] for r in data['records']}
        prior='radial_projection_moments14_verification.json'
    else:
        data=json.loads(Path('radial3d_projection_moments14.json').read_text());design=json.loads(Path('radial3d_projection_design14.json').read_text())
        base=json.loads(Path('radial3d_moment_optimum7_verification.json').read_text());roots=list(map(F,base['candidates'][0]['roots']))
        lookup={v+(0,):i for i,b in enumerate(design['orbit_bases']) for v in orbit(tuple(b))}
        prior='radial3d_projection_moments14_verification.json'
    assert json.loads(Path(prior).read_text())['status']=='passed'
    i=claim['omitted_root_index'];r=roots[i];vector=list(map(F,claim['vector']));q=sum(v*v for v in vector);A=q/4;R=r+A
    assert q==F(claim['norm_squared'])
    if i:assert q*roots[i-1]<(r-roots[i-1])**2
    if i<6:assert q*roots[i+1]<(roots[i+1]-r)**2
    l=[F(1)]
    for j,root in enumerate(roots):
        if j!=i:l=convolve(l,[-root,F(1)])
    assert l==list(map(F,claim['common_polynomial']))
    w=convolve(l,[r,F(-1)]);E0=sum(c*F(m) for c,m in zip(w,data['radial_moments']))
    gradients=[F(0)]*7;cache={};C=data['count'];weights=[list(map(F,row)) for row in design['radial_identity_weights']]
    for record in data['records']:
        direction=record['direction'];dot=sum(v*c for v,c in zip(vector,direction));oid=lookup[tuple(direction)]
        if not dot:continue
        path=Path(record['down_file']) if d==3 else Path('radial_projections14')/f"down_{record['index']:03d}.json"
        raw=json.loads(path.read_text());assert raw['raw_moments'][0]==C;den=record['denominator'];mean=F(record['mean'])
        centered=[sum(comb(j,h)*(-mean)**(j-h)*F(raw['raw_moments'][h],C*den**h) for h in range(j+1)) for j in range(14)]
        key=tuple(abs(c) for c in direction)
        if key not in cache:cache[key]=noise_direct(key,scales4)
        noise=cache[key]
        for j in range(7):
            degree=2*j+1;smooth=sum(comb(degree,h)*centered[h]*noise[degree-h] for h in range(degree+1))
            gradients[j]+=weights[j][oid]/design['orbit_sizes'][oid]*dot*smooth
    expectation=E0+sum(c*v for c,v in zip(l,gradients));assert expectation==F(claim['expectation'])
    # Expand l(|y+v/2|^2) in Cartesian coordinates, independently of the
    # producer's angular averaging formula.
    zero=(0,)*d;shifted_norm={zero:A}
    for j,v in enumerate(vector):
        shifted_norm[tuple(2*int(k==j) for k in range(d))]=F(1)
        if v:shifted_norm[tuple(int(k==j) for k in range(d))]=v
    power={zero:F(1)};expanded={}
    for c in l:
        for alpha,v in power.items():expanded[alpha]=expanded.get(alpha,F(0))+c*v
        power=multiply(power,shifted_norm)
    integral_factor=F(0)
    for alpha,c in expanded.items():
        if any(v%2 for v in alpha):continue
        beta=[v//2 for v in alpha];b=sum(beta)
        angular=F(prod(prod(F(1,2)+j for j in range(v)) for v in beta))/F(prod(F(d,2)+j for j in range(b)))
        exponent=b+3 if d==4 else b+2
        integral_factor+=c*angular*R**exponent/((F(b)+F(d,2))*(F(b)+F(d,2)+1))
    def primitive(x):
        if d==4:return sum(c*x**(j+2)/F(j+2) for j,c in enumerate(w))
        return exact_root(x)*sum(c*x**(j+1)/F(2*j+3,2) for j,c in enumerate(w)) if x else F(0)
    endpoints=[F(0)]+roots
    baseline=sum(primitive(b)-primitive(a) for a,b in zip(endpoints[::2],endpoints[1::2]))
    old_ball=primitive(r);sign=(-1)**i
    if d==4:integral=baseline+sign*(integral_factor-old_ball)
    else:
        interval=square_root_interval(R)
        integral=baseline+max(sign*(bound*integral_factor-old_ball) for bound in interval)
    assert integral>0 and integral<=F(claim['integral_upper_without_sphere_factor'])
    pi=pi_bounds()[1];factor=pi*pi if d==4 else 2*pi
    ratio=F(C,prod(data['scales']))*expectation/(factor*integral);independent=-(-ratio.numerator//ratio.denominator)
    N=claim['source_class'];assert independent>=N
    assert elias(F(63,157),F(5,157))[0]>0
    checked_cases=[]
    for case in claim.get('cases',[]):
        quotient,remainder=divmod(N*68,157);shared=157*quotient*(quotient-1)//2+remainder*quotient
        cap=(63*N*(N-1)//2-shared)//((2**31-1)**case['extension_degree']-157);J=case['distinct_labels']
        def pairs(j):
            a,b=divmod(N,j);return j*a*(a-1)//2+b*a
        assert pairs(J)<=cap and (J==1 or pairs(J-1)>cap)
        a,b,h=ln(F(J)),ln(F(157)),entropy(F(63,157));eta=F(5,157)
        excess=div((a[0]-b[1]-h[1]/eta,a[1]-b[0]-h[0]/eta),ln2)
        assert list(map(str,excess))==case['exact_excess_bits'];checked_cases.append(dict(extension_degree=case['extension_degree'],distinct_labels=J,excess_bits_lower=float(excess[0])))
    if d==4:
        a,h=ln(F(N)),entropy(F(63,157));eta=F(5,157);excess=div((a[0]-h[1]/eta,a[1]-h[0]/eta),ln2)
        assert list(map(str,excess))==claim['exact_excess_bits']
    result=dict(status='passed',dimension=d,source_class=N,independently_guaranteed=independent,
        raw_moment_and_separate_cube_noise_expectation_match=True,independent_Cartesian_ball_integral=True,
        exact_nested_sphere_checks=True,independent_Machin_pi=True,cases=checked_cases,seconds=time.monotonic()-start,
        scope='Selected tilted radial boundary; no global nonradial optimum claim.')
    Path(f'tilted_radial{d}d_boundary_independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    claim['status']='passed';certificate.write_text(json.dumps(claim,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
