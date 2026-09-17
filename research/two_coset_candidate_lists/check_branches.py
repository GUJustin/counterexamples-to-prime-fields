"""Exact checks of constant-branch masks and residual fibers of binomial sections."""
from pathlib import Path
from math import comb,isqrt
import json,time
import numpy as np
BASE=Path(__file__).resolve().parent


def prime(p):return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def generator(p):
    m=p-1;fac=[];d=2
    while d*d<=m:
        if m%d==0:
            fac.append(d)
            while m%d==0:m//=d
        d+=1
    if m>1:fac.append(m)
    return next(g for g in range(2,p) if all(pow(g,(p-1)//d,p)!=1 for d in fac))


def modular_coeffs(p,r,k,j):
    e=r*k+j;selected=[];current=1
    for i in range(e+1):
        if i%r==j:selected.append(current)
        if i<e:current=current*(e-i)*pow(i+1,-1,p)%p
    assert len(selected)==k+1
    for i in sorted({0,1,k//2,k-1,k}):
        assert selected[i]==comb(e,r*i+j)%p
    return selected


def fixture(p,r,j):
    started=time.monotonic();assert prime(p) and (p-1)%(2*r)==0
    k=(p-1)//(2*r);g=generator(p);omega=pow(g,(p-1)//r,p)
    points=np.arange(p,dtype=np.int64)
    G=np.zeros(p,dtype=np.int64)
    coeff=modular_coeffs(p,r,k,j)
    for a in reversed(coeff):G=(G*points+a)%p
    chi=np.full(p,-1,dtype=np.int64);chi[points[1:]**2%p]=1;chi[0]=0
    t=points[1:];tr=np.ones(p-1,dtype=np.int64)
    for _ in range(r):tr=tr*t%p
    powers=[pow(omega,a,p) for a in range(r)]
    signs=np.array([chi[(1+w*t)%p] for w in powers])
    eligible=np.all(signs!=0,axis=0)
    for ell in range(j):
        weighted=np.zeros(p-1,dtype=np.int64)
        for a in range(r):weighted+=signs[a]*pow(omega,a*(ell-j),p)
        eligible&=(weighted%p==0)
    val=signs.sum(axis=0)*pow(r,-1,p)%p
    tags=np.full(p,-1,dtype=np.int64)
    assert np.all(G[tr[eligible]]==val[eligible])
    multiplicities=np.bincount(tr[eligible],minlength=p)
    assert set(multiplicities[multiplicities!=0])<={r}
    tags[tr[eligible]]=val[eligible]
    cube_count=int(np.count_nonzero(tags>=0))
    order_two_count=0
    if r%2==0 and j==1:
        d=next(x for x in range(2,p) if chi[x]==-1)
        norms=np.array([chi[(1-pow(omega,2*a,p)*d%p*(t*t%p))%p] for a in range(r//2)])
        yes=np.all(norms==1,axis=0)
        x=pow(d,r//2,p)*tr%p
        assert np.all(G[x[yes]]==0)
        assert np.all(tags[x[yes]]==-1)
        multiplicities=np.bincount(x[yes],minlength=p)
        assert set(multiplicities[multiplicities!=0])<={r}
        tags[x[yes]]=0
        order_two_count=int(np.count_nonzero(multiplicities))
    step=pow(g,2*r,p);H=[];z=1
    for _ in range(k):H.append(z);z=z*step%p
    max_residual=0;modal=[];spectra=[]
    bound=r*2**r+1
    for b in range(2*r):
        xs=np.array([pow(g,b,p)*h%p for h in H],dtype=np.int64)
        _,counts=np.unique(G[xs],return_counts=True)
        modal.append(int(counts.max()))
        _,counts=np.unique(G[xs[tags[xs]<0]],return_counts=True)
        largest=int(counts.max()) if len(counts) else 0
        assert largest<=bound
        max_residual=max(max_residual,largest)
        for v in np.unique(tags[xs]):
            if v<0:continue
            mask=(tags[xs]==v).astype(float)
            transform=np.fft.fft(mask)
            observed=float(np.max(np.abs(transform[1:]))) if k>1 else 0.0
            # Diagnostic Fourier values only; theorem uses analytic character bounds.
            spectra.append(observed)
    # The root-filter identity itself is checked over every t in the prime field.
    for tt in range(1,p):
        rhs=sum(pow(omega,-a*j,p)*pow((1+pow(omega,a,p)*tt)%p,r*k+j,p) for a in range(r))
        rhs=rhs*pow(r*pow(tt,j,p)%p,-1,p)%p
        assert rhs==int(G[pow(tt,r,p)])
    return dict(p=p,r=r,j=j,k=k,constant_power_class_points=cube_count,
                constant_order_two_points=order_two_count,max_residual_fiber=max_residual,
                conservative_residual_bound=bound,full_orbit_four_coset_agreement=sum(sorted(modal,reverse=True)[:4]),
                largest_nontrivial_mask_fourier_diagnostic=max(spectra,default=0),
                seconds=time.monotonic()-started)


def main():
    cases=[(97,3,j) for j in range(3)]+[(257,4,j) for j in range(4)]+[(769,6,j) for j in range(6)]
    cases += [(12289,3,j) for j in range(3)]+[(12289,4,j) for j in range(4)]+[(12289,6,j) for j in range(6)]
    rows=[]
    for case in cases:
        row=fixture(*case);rows.append(row);print(json.dumps(row),flush=True)
        (BASE/'branch_verification.json').write_text(json.dumps(dict(status='running',rows=rows),indent=2)+'\n')
    (BASE/'branch_verification.json').write_text(json.dumps(dict(status='passed',cases=len(rows),rows=rows,scope='Exact coefficient, root-filter, constant-mask and residual-fiber tests. Fourier values are floating-point diagnostics only; universal bounds rely on the proof.'),indent=2)+'\n')

if __name__=='__main__':main()
