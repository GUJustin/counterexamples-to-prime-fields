#!/usr/bin/env python3
"""Independent NumPy polynomial arithmetic; no FLINT finite-field operations."""
from pathlib import Path
from hashlib import sha256
import json,time,signal
import numpy as np
start=time.monotonic()
signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(TimeoutError('60-second cap')))
signal.alarm(60)
root=Path(__file__).resolve().parent
receipt=json.loads((root/'receipt.json').read_text())
rows=np.load(root/'domain_and_sources.npz')['rows']
assert rows.shape==(70560,5) and rows.dtype==np.dtype('<u4')
assert sha256(rows.tobytes()).hexdigest()==receipt['rows_sha256']
p=97;order=p**4-1;modulus=[5,80,6,0]
def decode(x):
    x=np.asarray(x,dtype=np.int64)
    assert np.all((0<=x)&(x<p**4))
    return np.stack([(x//p**i)%p for i in range(4)],axis=-1)
def mul(a,b):
    a,b=np.broadcast_arrays(a,b)
    out=np.zeros(a.shape[:-1]+(7,),dtype=np.int64)
    for i in range(4):
        for j in range(4):out[...,i+j]+=a[...,i]*b[...,j]
    out%=p
    for k in range(6,3,-1):
        top=out[...,k].copy()
        for j in range(4):out[...,k-4+j]=(out[...,k-4+j]-top*modulus[j])%p
        out[...,k]=0
    return out[...,:4]
def power(a,e):
    result=np.zeros_like(a);result[...,0]=1
    while e:
        if e&1:result=mul(result,a)
        a=mul(a,a);e//=2
    return result
one=np.array([1,0,0,0],dtype=np.int64)
s=np.array([0,1,0,0],dtype=np.int64)
assert np.array_equal(power(s,order),one)
assert all(not np.array_equal(power(s,order//q),one) for q in [2,3,5,7,941])
z=power(s,9410);eta=power(s,5)
assert not np.array_equal(power(z,97),z)
X,F,G,W0,W1=[decode(rows[:,i]) for i in range(5)]
assert len(np.unique(rows[:,0]))==70560
assert np.all(rows[:47040,2]==0) and np.all(rows[47040:,2]==1)
raw=power(X,485)
raw[47040:]=mul(raw[47040:],power(eta,order-96))
assert np.array_equal(F,raw)
lam0=(one+mul(eta,z))%p
lam1=(one+mul(eta,(z+one)%p))%p
assert np.array_equal(lam0,receipt['endpoint0'])
assert np.array_equal(lam1,receipt['endpoint1'])
assert np.array_equal(W0,(F+mul(G,lam0))%p)
assert np.array_equal(W1,(F+mul(G,lam1))%p)
y=power(X,5)
assert np.array_equal(power(y[:47040],p*p),y[:47040])
fresh_y=mul(y[47040:],power(eta,order-1))
assert np.array_equal(power(fresh_y,p*p),fresh_y)
# Independent common-agreement witness: q=X^5+(z^p-z), explanation of g=0.
b=(power(z,p)-z)%p
q=(y+b)%p
joint=np.all(F==q,axis=1)&np.all(G==0,axis=1)
assert int(joint.sum())==485
result={'PASS':True,'scope':'All saved coordinate/source values checked with independent polynomial arithmetic; one common-agreement witness explicitly counted; universal upper bounds remain proof-based',
 'coordinates_checked':70560,'source_word_values_checked':141120,
 'raw_source_values_checked':70560,'domain_coordinates_distinct':True,
 'primitive_order_checked':order,'common_witness_matches':485,
 'rows_sha256':sha256(rows.tobytes()).hexdigest(),
 'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
 'elapsed_seconds':time.monotonic()-start}
(root/'independent_archive_check.json').write_text(json.dumps(result,indent=2)+'\n')
signal.alarm(0)
print(json.dumps(result,indent=2))
