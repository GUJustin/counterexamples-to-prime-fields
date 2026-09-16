"""Separate exact audit of selected radial weights and line conversion.

Uses different integration and pi routines from the certificate producers.
Does not certify optimality of the truncated moment problem.
"""
from fractions import Fraction as F
from math import isqrt,prod
from pathlib import Path
import argparse,hashlib,json
from rational_circle_bounds import entropy,ln,ln2,div,elias


def multiply(a,b):
    return [sum(a[i]*b[j] for i in range(len(a)) for j in range(len(b)) if i+j==d)
            for d in range(len(a)+len(b)-1)]


def pi_bounds():
    def atan(q):
        value=sum(F((-1)**j,(2*j+1)*q**(2*j+1)) for j in range(100))
        return value,value+F(1,201*q**201)
    a,b=atan(5),atan(239)
    return 16*a[0]-4*b[1],16*a[1]-4*b[0]


def interval_multiply(a,b):
    values=[x*y for x in a for y in b];return min(values),max(values)


def antiderivative3(coefficients,x):
    if not x:return F(0),F(0)
    scale=10**90;r=isqrt(x.numerator*scale*scale//x.denominator)
    root=F(r,scale),F(r+1,scale)
    assert root[0]**2<=x<root[1]**2
    # Substitute s=z^2 and integrate 2*z^2*w(z^2) in z.
    expanded=[F(0)]*(2*len(coefficients)+2)
    for j,c in enumerate(coefficients):expanded[2*j+3]=2*c/F(2*j+3)
    answer=F(0),F(0)
    for c in reversed(expanded):
        answer=interval_multiply(answer,root)
        answer=answer[0]+c,answer[1]+c
    return answer


def weight_check(row,moments,population,scales,dimension):
    coefficients=list(map(F,row['coefficients']))
    if 'polynomial' in row:
        P=list(map(F,row['polynomial']));R=F(row['radius'])
        assert R>0 and coefficients==multiply(multiply(P,P),[R,F(-1)])
        bands=[(F(0),R)]
    else:
        roots=list(map(F,row['roots']))
        assert roots[0]>0 and all(a<b for a,b in zip(roots,roots[1:]))
        rebuilt=[F(-1)]
        for r in roots:rebuilt=multiply(rebuilt,[-r,F(1)])
        assert rebuilt==coefficients and len(roots)%2==1
        endpoints=[F(0)]+roots;bands=list(zip(endpoints[::2],endpoints[1::2]))
    if 'positive_bands' in row:assert bands==[tuple(map(F,b)) for b in row['positive_bands']]
    expectation=sum(c*m for c,m in zip(coefficients,moments))
    assert expectation==F(row['expectation'])>0
    lower=upper=F(0)
    for a,b in bands:
        if dimension==4:
            value=sum(c*F(b**(j+2)-a**(j+2),j+2) for j,c in enumerate(coefficients))
            lower+=value;upper+=value
        else:
            left,right=antiderivative3(coefficients,a),antiderivative3(coefficients,b)
            lower+=right[0]-left[1];upper+=right[1]-left[0]
    assert 0<lower<=upper
    pi=pi_bounds()
    denominator=prod(scales)*upper*(pi[1]**2 if dimension==4 else 2*pi[1])
    ratio=population*expectation/denominator
    independently_guaranteed=-(-ratio.numerator//ratio.denominator)
    claimed=int(row['count']);assert independently_guaranteed>=claimed
    return dict(claimed_count=claimed,independently_guaranteed=independently_guaranteed,
                positive_bands=len(bands),expectation=str(expectation),
                independently_integrated_radial_interval=[str(lower),str(upper)])


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--dimension',type=int,choices=(3,4),required=True)
    parser.add_argument('--prior',action='store_true');parser.add_argument('--optimum',action='store_true');args=parser.parse_args()
    assert not args.optimum or (args.dimension==3 and not args.prior)
    sources={}
    def read(name):
        raw=Path(name).read_bytes();sources[name]=hashlib.sha256(raw).hexdigest();return json.loads(raw)
    dim=args.dimension;rows=[];line=None
    if dim==3 and args.prior:
        data=read('interval_extension_line_verification.json');line=data
        moments=list(map(F,data['radial_moments']));population=data['conditional_population'];scales=data['scales']
        R=F(data['radius_parameter']);q=list(map(F,data['polynomial_in_s_over_R']))
        rows=[dict(coefficients=data['weight_coefficients'],expectation=data['expectation'],
                   radius=str(R),polynomial=[str(c/R**i) for i,c in enumerate(q)],
                   count=data['source_class_lower_bound'])]
    elif dim==3:
        checked=read('radial3d_projection_moments14_verification.json');assert checked['status']=='passed'
        data=read('radial3d_moment_optimum7_verification.json' if args.optimum else 'radial3d_weight14_verification.json');line=data
        moments=list(map(F,checked['radial_moments']));population=data['conditional_population'];scales=data['scales']
        rows=[dict(row,count=row['source_class']) for row in data['candidates']]
    else:
        if args.prior:
            base=read('radial_projection_moments10.json');one=read('radial_weight10_verification.json')
            multi=read('radial_multiband_verification.json');opt=read('radial_moment_optimum_verification.json')
        else:
            base=read('radial_projection_moments14_verification.json');assert base['status']=='passed'
            one=read('radial_weight14_verification.json');multi=read('radial_multiband7_verification.json')
            opt=read('radial_moment_optimum7_verification.json')
        data=one;moments=list(map(F,base['radial_moments']));population=base['count'];scales=base['scales']
        R=F(one['radius_parameter']);q=list(map(F,one['polynomial_in_s_over_R']))
        rows=[dict(coefficients=one['signed_weight_coefficients'],
                   expectation=one.get('expectation',one.get('weight_expectation')),
                   radius=str(R),polynomial=[str(c/R**i) for i,c in enumerate(q)],count=one['list_lower_bound'])]
        rows.extend(dict(row,count=row['list_lower_bound']) for row in multi['results'])
        rows.append(dict(coefficients=opt['refined_weight_coefficients'],roots=opt['refined_roots'],
                         expectation=opt['refined_expectation'],count=opt['list_lower_bound']))
    checks=[weight_check(row,moments,population,scales,dim) for row in rows]
    n,k,t,p=(data[key] for key in ('n','k','t','p'))
    assert p==2**31-1 and t-k==5 and elias(F(k,n),F(t-k,n))[0]>0
    cases=[]
    if line:
        N=int(line.get('source_class',line.get('source_class_lower_bound')))
        assert N==max(r['count'] for r in rows)
        q,r=divmod(N*t,n)
        shared=n*q*(q-1)//2+r*q
        budget=k*N*(N-1)//2-shared;assert budget>=0
        for case in line['cases']:
            ext=case['extension_degree'];J=int(case['distinct_labels']);poles=p**ext-n
            def pairs(bins):
                q,r=divmod(N,bins)
                return bins*q*(q-1)//2+r*q
            assert 1<=J<=N and pairs(J)<=budget//poles
            assert J==1 or pairs(J-1)>budget//poles
            a,b,h=ln(F(J)),ln(F(n)),entropy(F(k,n));eta=F(t-k,n)
            excess=div((a[0]-b[1]-h[1]/eta,a[1]-b[0]-h[0]/eta),ln2)
            cases.append(dict(extension_degree=ext,distinct_labels=J,
                              independent_excess_bits_lower=float(excess[0]),concurrency=(n-k)//(t-k)))
    else:
        L=max(r['count'] for r in rows);a,h=ln(F(L)),entropy(F(k,n));eta=F(t-k,n)
        excess=div((a[0]-h[1]/eta,a[1]-h[0]/eta),ln2)
        cases=[dict(list_lower_bound=L,independent_excess_bits_lower=float(excess[0]))]
    result=dict(status='passed',dimension=dim,prior_fixture=args.prior,input_hashes=sources,
                weight_checks=checks,cases=cases,
                independent_Machin_pi_bounds=True,independent_integrals_and_weight_factorization=True,
                scope='Selected rational weights and pole conversion only; does not independently certify truncated-moment optimality.')
    suffix='prior' if args.prior else ('14opt' if args.optimum else '14')
    Path(f'radial{dim}d_weight{suffix}_independent_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('weight_checks','input_hashes')},indent=2))


if __name__=='__main__':main()
