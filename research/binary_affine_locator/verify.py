"""Exact checks of the odd-characteristic binary-affine locator bound."""
from pathlib import Path
from itertools import combinations,product
from collections import defaultdict
import json,time


class Prime:
    def __init__(self,p):self.p=p;self.q=p
    def add(self,a,b):return (a+b)%self.p
    def neg(self,a):return -a%self.p
    def mul(self,a,b):return a*b%self.p


class F9:
    q=9;p=3
    def add(self,a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
    def neg(self,a):return (-a%3)+3*(-(a//3)%3)
    def mul(self,a,b):return ((a%3*(b%3)-a//3*(b//3))%3)+3*((a%3*(b//3)+a//3*(b%3))%3)


class F16:
    q=16;p=2
    def add(self,a,b):return a^b
    def neg(self,a):return a
    def mul(self,a,b):
        out=0
        while b:
            if b&1:out^=a
            b>>=1;a<<=1
            if a&16:a^=19
        return out


def power(F,a,e):
    out=1
    while e:
        if e&1:out=F.mul(out,a)
        a=F.mul(a,a);e>>=1
    return out


def locator(F,roots):
    out=[1]
    for a in roots:
        nxt=[0]*(len(out)+1)
        for i,c in enumerate(out):
            nxt[i]=F.add(nxt[i],F.mul(F.neg(a),c));nxt[i+1]=F.add(nxt[i+1],c)
        out=nxt
    return out


def affine_spaces(n,r):
    for pivots in combinations(range(n),r):
        nonpivots=[j for j in range(n) if j not in pivots]
        cells=[(i,j) for i,p in enumerate(pivots) for j in nonpivots if j>p]
        for bits in range(1<<len(cells)):
            basis=[1<<p for p in pivots]
            for h,(i,j) in enumerate(cells):
                if bits>>h&1:basis[i]|=1<<j
            V=[0]
            for v in basis:V+=[u^v for u in V]
            for bs in range(1<<len(nonpivots)):
                b=sum(((bs>>i)&1)<<j for i,j in enumerate(nonpivots))
                yield basis,b,[u^b for u in V]


def verify_family(F,domain,basis,b,words,locators=None):
    n=len(domain);r=len(basis);t=words[0].bit_count()
    assert all(w.bit_count()==t for w in words)
    polys=locators or {w:locator(F,[domain[j] for j in range(n) if w>>j&1]) for w in words}
    prefix=0
    for j in range(1,t+1):
        if len({tuple(polys[w][t-j:t]) for w in words})!=1:break
        prefix=j
    assert prefix<t and r<=min(t,n-t)//(prefix+1)
    classes=defaultdict(lambda:[[],[]])
    for j,a in enumerate(domain):
        label=sum(((v>>j)&1)<<i for i,v in enumerate(basis))
        if label:classes[label][(b>>j)&1].append(a)
    assert r<=len(classes)
    for plus,minus in classes.values():
        assert len(plus)==len(minus)>=prefix+1
        L1=locator(F,plus);L2=locator(F,minus)
        assert L1[-prefix-1:]==L2[-prefix-1:]
    return prefix,len(classes)


def exhaustive():
    rows=[]
    for F,n,dimensions in [(Prime(7),6,(1,2,3)),(Prime(101),6,(1,2,3)),(F9(),6,(1,2,3)),(F9(),8,(1,))]:
        domain=list(range(n));polys={w:locator(F,[domain[j] for j in range(n) if w>>j&1]) for w in range(1<<n)}
        checked=0;constant=0;prefix_hist=defaultdict(int)
        for r in dimensions:
            for basis,b,words in affine_spaces(n,r):
                checked+=1;t=words[0].bit_count()
                if not all(w.bit_count()==t for w in words):continue
                constant+=1
                prefix,_=verify_family(F,domain,basis,b,words,polys)
                prefix_hist[prefix]+=1
        rows.append(dict(q=F.q,characteristic=F.p,n=n,affine_spaces=checked,
                         constant_weight_families=constant,prefix_histogram=dict(prefix_hist)))
    assert rows[-1]['prefix_histogram'].get(3,0)>0 # char3 <= prefix3
    return rows


def sharpness():
    F=Prime(1009);rows=[]
    for B in (1,2,3,4,6):
        fibers=defaultdict(list)
        for x in range(1,F.p):fibers[power(F,x,B)].append(x)
        assert all(len(v)==B for v in fibers.values())
        groups=list(fibers.values())
        for r in (1,2,3,4):
            domain=[x for group in groups[:2*r] for x in group]
            # Unequal selected/unselected fixed populations check min(t,n-t).
            unused=[x for x in range(F.p) if x not in domain]
            core=3;extra=5;domain+=unused[:core+extra]
            basis=[];b=0
            for i in range(r):
                start=2*B*i
                basis.append(((1<<(2*B))-1)<<start)
                b|=((1<<B)-1)<<start
            b|=((1<<core)-1)<<(2*r*B)
            words=[b]
            for v in basis:words+=[u^v for u in words]
            prefix,_=verify_family(F,domain,basis,b,words)
            assert prefix>=B-1
            # Ignore fixed coordinates to get exact equality in (1).
            n0=2*r*B;domain0=domain[:n0];b0=b&((1<<n0)-1)
            words0=[w&((1<<n0)-1) for w in words]
            prefix0,_=verify_family(F,domain0,basis,b0,words0)
            assert prefix0==B-1 and r==(r*B)//(prefix0+1)
            rows.append(dict(B=B,s=B-1,r=r,n=n0,t=r*B,list_size=1<<r))
    return rows


def binary_negative():
    F=F16();domain=list(range(16))
    def trace(a):
        out=0
        for _ in range(4):out^=a;a=F.mul(a,a)
        assert out in (0,1)
        return out
    words=[sum(trace(F.mul(a,x))<<x for x in domain) for a in range(8,16)]
    assert len(set(words))==8 and all(w.bit_count()==8 for w in words)
    b=words[0];basis=[words[1]^b,words[2]^b,words[4]^b]
    V=[b]
    for v in basis:V+=[w^v for w in V]
    assert set(V)==set(words)
    polys=[locator(F,[x for x in domain if w>>x&1]) for w in words]
    assert all(P[5:8]==[0,0,0] for P in polys)
    assert 3>min(8,16-8)//4
    return dict(q=16,n=16,t=8,s=3,r=3,odd_characteristic_bound=2,
                supports=words,locator_coefficients=polys)


def main():
    start=time.monotonic()
    result=dict(status='passed',exhaustive=exhaustive(),sharpness=sharpness(),
                characteristic_two_negative_control=binary_negative(),
                seconds=time.monotonic()-start,
                scope='Exhaustive small binary-affine support spaces, exact odd-characteristic locator prefixes including characteristic below prefix length, sharp full-fiber examples, and a characteristic-two counterexample. Finite checks supplement the proof.')
    Path(__file__).with_name('binary_affine_locator_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status='passed',exhaustive=result['exhaustive'],
                         sharpness_fixtures=len(result['sharpness']),characteristic_two_negative_control=True,
                         seconds=result['seconds']),indent=2))


if __name__=='__main__':main()
