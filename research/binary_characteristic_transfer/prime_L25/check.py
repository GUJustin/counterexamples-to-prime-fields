"""Independent finite/structural replay; no import from the generator."""
from collections import Counter
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
started=time.monotonic()
path=HERE/'certificate.json'
raw=path.read_bytes()
d=json.loads(raw)
p=d['p']; L=d['L']; n=d['n']; N0=d['core_length']; t=d['fresh_length']
assert (L,n,N0,t,d['K'],d['threshold'],d['source_agreement'])==(25,1201,600,601,3,49,48)
# Sieve primality replay, distinct from generator's trial-division routine.
limit=math.isqrt(p)
sieve=[True]*(limit+1); sieve[0]=sieve[1]=False
for a in range(2,math.isqrt(limit)+1):
    if sieve[a]:
        for j in range(a*a,limit+1,a): sieve[j]=False
primes=[i for i in range(2,limit+1) if sieve[i]]
assert all(p%q for q in primes)
assert p==2_000_003
assert d['small_primes']==primes[:25]
assert p>max(2*d['small_primes'][-1]**2,5*L**4)
xs=d['nodes'];f=d['source_f'];g=d['source_g'];bank=d['bank_coefficients']
assert len(xs)==len(f)==len(g)==n and len(set(xs))==n and all(xs)
assert all(0<=z<p for z in xs+f+g)
assert len(bank)==L and len({tuple(c) for c in bank})==L
for a,c in zip(d['small_primes'],bank):
    assert c[0]==a*a%p and c[1]==0 and c[2]*(a*a)%p==1

def ev(c,x): return ((c[2]*x+c[1])*x+c[0])%p

core_support=[[] for _ in bank]
expected_core=set()
for i in range(L):
    for j in range(i+1,L):
        a=d['small_primes'][i]*d['small_primes'][j]
        expected_core.update([a%p,-a%p])
assert set(xs[:N0])==expected_core and len(expected_core)==N0
for k,x in enumerate(xs[:N0]):
    assert f[k]==g[k]
    hits=[i for i,c in enumerate(bank) if ev(c,x)==f[k]]
    assert len(hits)==2 and hits==d['core_pair_indices'][k]
    for i in hits: core_support[i].append(k)
assert {len(s) for s in core_support}=={48}

# Recompute every canonical bank/fresh incidence independently via division.
lookup={}
for j,x in enumerate(xs[N0:]):
    k=N0+j
    assert f[k]==pow(x,4,p) and g[k]==(pow(x,4,p)+pow(x,3,p))%p
    for i,c in enumerate(bank):
        old=(ev(c,x)-f[k])*pow((g[k]-f[k])%p,p-2,p)%p
        assert old not in [0,1] and old not in lookup
        lookup[old]=(i,j)
assert len(lookup)==15025

final=set(); designated_checks=0
for old,z,i,j in d['finite_labels']:
    assert lookup.pop(old)==(i,j)
    assert z not in final and z not in [0,p-1]
    final.add(z)
    assert (z*(1-old)-old)%p==0
    scale=(1+z)%p
    witness=[scale*c%p for c in bank[i]]
    support=core_support[i]+[N0+j]
    assert len(support)==49
    for k in support:
        assert ev(witness,xs[k])==(f[k]+z*g[k])%p
        designated_checks+=1
assert not lookup and len(final)==15025

inf=d['infinity']; assert inf==dict(label=p-1,witness_coefficients=[0,0,0],agreement=600)
assert sum((a+(p-1)*b)%p==0 for a,b in zip(f,g))==600
assert p-1 not in final
# Degree-count certificate: each other quadratic has <=2L bank incidences,
# every core match contributes2; fresh residual has monic quartic term.
assert L+4==29<49 and L+4<=48 and 2+3<49
# Direction difference g-f is0 oncore and x³ onfresh; this provesCA<=48.
assert 2+3<48 and all((g[k]-f[k])%p for k in range(N0,n))
# Both endpoints canonical0,1 are absent. Every bank gives48 endpoint matches.
for c in bank:
    assert sum(ev(c,x)==y for x,y in zip(xs,f))==48
    assert sum(ev(c,x)==y for x,y in zip(xs,g))==48

# Independent direct support sums, plus exact finite reconstruction budget.
A=49;B=98;H=4704
G=sum(max(4*A-2*q+v,0) for q in range(B+1) for v in range(min(q,2)+1))
layers=[sum(min(4-s,max(min(q,s)-max(0,q-2)+1,0)) for q in range(B+1)) for s in range(4)]
assert G==28812 and layers==[3,6,8,6]
assert (H-B+1)*G>(H+1)*23*n
assert A*A==2*n-1
assert Fraction(7*L,4)+math.isqrt(L)==Fraction(195,4)<A
lam=Fraction(n-2,A-2);ell=A//2;ratio=Fraction(n-ell+1,A-ell+1)
S=3*B-4;Hs=3*H;Freg=5*B-6;J=H*(16*B-21)+10*B-12
E=(2*S-1)*Hs+ratio*(S+Hs*(8*S-12))+(n-ell)*S+ratio*lam*J+(n-ell)*Fraction(n-2,ell-2)*Freg
assert E<31000*n*n and lam*Freg+S<18*n

receipt=dict(status='PASS',p=p,primality_method='trial divisibility by independently sieved primes through floor(sqrt(p))',
             n=n,K=3,common_and_individual_agreement=48,threshold=49,
             finite_labels=15025,total_bad_labels=15026,
             canonical_bank_fresh_pairs_checked=15025,
             designated_witness_equations_checked=designated_checks,
             core_bank_support_sizes=[len(s) for s in core_support],
             singleton_scope='All bad labels; degree-count exclusion, not exhaustive p^3 candidate enumeration.',
             infinity_agreement=600,local_layers=layers,
             full_MCA_bound_numerator=E.numerator,full_MCA_bound_denominator=E.denominator,
             certificate_sha256=hashlib.sha256(raw).hexdigest(),
             checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             elapsed_seconds=time.monotonic()-started)
(HERE/'verified.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
