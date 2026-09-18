"""Exact symmetry interpolation over F29 from certified Gauss-image points.

Input schema: field_modulus (ascending), image_points (triples of three
coefficient lists). The point set must contain complete Frobenius/mu7 orbits.
"""
import argparse,hashlib,json
from pathlib import Path
from flint import nmod_poly,nmod_mat,nmod_mpoly_ctx
ap=argparse.ArgumentParser();ap.add_argument('input',type=Path)
ap.add_argument('--output',type=Path);args=ap.parse_args()
if args.output is None:args.output=args.input.with_name('gauss_image_interpolation.json')
raw=args.input.read_bytes();data=json.loads(raw);p=29;degree=62
mod=list(data['field_modulus']);assert len(mod)==4 and mod[-1]==1
assert all(sum(c*pow(a,i,p) for i,c in enumerate(mod))%p for a in range(p)), 'Cubic modulus has a base-field root'
zero=(0,0,0);one=(1,0,0)
def add(a,b):return tuple((a[i]+b[i])%p for i in range(3))
def mul(a,b):
    c=[0]*5
    for i in range(3):
        for j in range(3):c[i+j]+=a[i]*b[j]
    for i in (4,3):
        t=c[i]%p
        for j in range(3):c[i-3+j]-=t*mod[j]
    return tuple(c[i]%p for i in range(3))
def power(a,n):
    r=one
    while n:
        if n&1:r=mul(r,a)
        a=mul(a,a);n//=2
    return r
def scale(a,c):return tuple(z*c%p for z in a)
def normalize(q):
    q=tuple(tuple(int(z) for z in c) for c in q)
    assert len(q)==3 and all(len(c)==3 and all(0<=z<p for z in c) for c in q)
    first=next(c for c in q if c!=zero)
    inv=power(first,p**3-2)
    return tuple(mul(c,inv) for c in q)
points={normalize(q) for q in data['image_points']}
assert len(points)>degree**2
zeta=16;assert pow(zeta,7,p)==1 and zeta!=1
remaining=set(points);representatives=[];orbit_sizes=[]
while remaining:
    q=min(remaining);orb=set();frob=q
    for j in range(3):
        for i in range(7):
            orb.add(normalize((frob[0],scale(frob[1],pow(zeta,(-2*i)%7,p)),
                               scale(frob[2],pow(zeta,(-4*i)%7,p)))))
        frob=tuple(power(c,p) for c in frob)
    assert orb<=points,'Sampler point set is not closed under required symmetries'
    assert orb<=remaining,'Symmetry orbits unexpectedly overlap'
    representatives.append(q);orbit_sizes.append(len(orb));remaining-=orb
assert sum(orbit_sizes)==len(points)
columns=[[(degree-i-j,i,j) for i in range(degree+1) for j in range(degree+1-i)
          if (2*i+4*j)%7==r] for r in range(7)]
matrices=[[] for _ in range(7)]
for q in representatives:
    powers=[]
    for coord in q:
        row=[one]
        for i in range(degree):row.append(mul(row[-1],coord))
        powers.append(row)
    for r,cols in enumerate(columns):
        vals=[mul(mul(powers[0][a],powers[1][b]),powers[2][c]) for a,b,c in cols]
        matrices[r].extend([[v[k] for v in vals] for k in range(3)])
ctx=nmod_mpoly_ctx.get(['a','b','c'],p);common=None;records=[];basis_terms=[]
for r,(M,cols) in enumerate(zip(matrices,columns)):
    R,rank=nmod_mat(M,p).rref()
    reduced=[[int(R[i,j]) for j in range(len(cols))] for i in range(rank)]
    piv=[next(j for j,x in enumerate(row) if x) for row in reduced]
    free=[j for j in range(len(cols)) if j not in piv]
    for f in free:
        v=[0]*len(cols);v[f]=1
        for row,j in zip(reduced,piv):v[j]=-row[f]%p
        assert all(sum(a*b for a,b in zip(row,v))%p==0 for row in M)
        poly=ctx.from_dict({e:c for e,c in zip(cols,v) if c})
        common=poly if common is None else common.gcd(poly)
        basis_terms.append([[list(e),c] for e,c in zip(cols,v) if c])
    records.append({'character':r,'columns':len(cols),'rows':len(M),'rank':rank,'nullity':len(free)})
    print(records[-1],flush=True)
assert common is not None,'No degree<=62 image equation found: check geometric assumptions/data'
terms=[(tuple(map(int,e)),int(c)) for e,c in common.to_dict().items()]
degrees={sum(e) for e,c in terms};assert len(degrees)==1
image_degree=degrees.pop();assert 1<=image_degree<=degree
assert len(basis_terms)==(degree-image_degree+1)*(degree-image_degree+2)//2
# Independent direct evaluation on EVERY point, not only orbit representatives.
for q in points:
    powers=[]
    for coord in q:
        row=[one]
        for i in range(image_degree):row.append(mul(row[-1],coord))
        powers.append(row)
    value=zero
    for (a,b,c),coef in terms:
        term=mul(mul(powers[0][a],powers[1][b]),powers[2][c])
        value=add(value,scale(term,coef))
    assert value==zero
out={'input_sha256':hashlib.sha256(raw).hexdigest(),'field_modulus':mod,
     'distinct_points':len(points),'orbit_count':len(representatives),
     'orbit_sizes':orbit_sizes,'blocks':records,'degree62_kernel_dimension':len(basis_terms),
     'image_degree':image_degree,'image_terms':[[list(e),c] for e,c in terms],
     'kernel_basis_terms':basis_terms,'all_points_directly_verified':True,
     'bezout_threshold':degree**2,
     'conditional_scope':'Exact image equation provided sampled points belong to the audited absolutely irreducible Gauss image of degree<=62.'}
args.output.write_text(json.dumps(out,indent=2));print('Image degree',image_degree,'terms',len(terms),flush=True)
