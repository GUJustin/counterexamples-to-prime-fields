"""Independent exact cyclic triple-convolution engine; does not import producer code."""
MOD=998244353
ROOT=3

def transform(a,inverse=False):
    n=len(a)
    j=0
    for i in range(1,n):
        bit=n>>1
        while j&bit:
            j^=bit; bit>>=1
        j^=bit
        if i<j: a[i],a[j]=a[j],a[i]
    length=2
    while length<=n:
        step=pow(ROOT,(MOD-1)//length,MOD)
        if inverse: step=pow(step,MOD-2,MOD)
        half=length//2
        for start in range(0,n,length):
            twiddle=1
            for j in range(start,start+half):
                u=a[j]; v=a[j+half]*twiddle%MOD
                a[j]=(u+v)%MOD; a[j+half]=(u-v)%MOD
                twiddle=twiddle*step%MOD
        length*=2
    if inverse:
        scale=pow(n,MOD-2,MOD)
        for i in range(n): a[i]=a[i]*scale%MOD
    return a

def triple_counts(exponents,order):
    assert order&(order-1)==0 and (MOD-1)%order==0
    assert len(set(exponents))==len(exponents)
    s=len(exponents)
    assert s*s<MOD # Every coefficient counts at most s^2 ordered pairs.
    a=[0]*order
    for e in exponents: a[e]=1
    transform(a)
    a=[pow(x,3,MOD) for x in a]
    transform(a,True)
    assert max(a)<=s*s and sum(a)==s**3
    return a

if __name__=='__main__':
    import json,struct,hashlib,time,math
    from pathlib import Path
    from fractions import Fraction
    start=time.monotonic(); folder=Path(__file__).resolve().parent
    data=json.loads((folder/'tags_and_domain.json').read_text())
    tags=data['sampled_tags']; exps=data['factor_logs_base_3']
    p=65537;s=len(tags);order=p-1
    assert all(p%d for d in range(2,math.isqrt(p)+1))
    assert pow(3,32768,p)==p-1
    assert len(set(tags))==s==1420 and 1 not in tags
    assert all(0<a<p and pow(a,32768,p)==1 for a in tags)
    assert sorted(pow(3,e,p) for e in exps)==sorted((3-a)%p for a in tags)
    domain=[x for x in range(p) if x*x%p in set(tags+[1])]
    assert len(domain)==2842 and all((x*x-3)%p for x in domain)
    counts=triple_counts(exps,order)
    producer=list(struct.unpack('<65536I',(folder/'cyclic_triple_convolution_u32le.bin').read_bytes()))
    assert counts==producer
    energy=sum(x*x for x in counts)
    moment=order*energy-s**6
    assert 0<=moment<(s//2)**6
    r=712;theta=Fraction(r,s);u=theta*(1-theta)*Fraction(s,2)
    pref=(p-2)*(s+1)
    assert u**5>120*pref
    J=1421;A=1422;T=1424
    assert J-1==(r-2)*2 and A==(r-1)*2 and T==r*2
    result={'status':'PASS','method':'independent radix-two cyclic NTT; all coefficients agree with FLINT','energy':energy,'sixth_moment':moment,'maximum_c3':max(counts),'cauchy_exponent':str(u),'cauchy_prefactor':pref,'domain_size':len(domain),'J':J,'A':A,'T':T,'elapsed_seconds':time.monotonic()-start,'producer_binary_sha256':hashlib.sha256((folder/'cyclic_triple_convolution_u32le.bin').read_bytes()).hexdigest()}
    (folder/'independent_ntt.verified.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
