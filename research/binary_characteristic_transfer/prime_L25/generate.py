"""Deterministic L=25 prime-field certificate. Standard-library only."""
import hashlib
import json
import math
from pathlib import Path

HERE=Path(__file__).resolve().parent

def prime(n):
    return n>=2 and all(n%d for d in range(2,math.isqrt(n)+1))

L=25
p=2_000_001
while not prime(p):
    p+=1
small=[]
a=2
while len(small)<L:
    if prime(a): small.append(a)
    a+=1
bank=[[a*a%p,0,pow(a*a,-1,p)] for a in small]
core=[]
for i in range(L):
    for j in range(i+1,L):
        for sign in [1,-1]:
            x=sign*small[i]*small[j]%p
            w=(bank[i][0]+bank[i][2]*x*x)%p
            assert w==(bank[j][0]+bank[j][2]*x*x)%p
            core.append([x,w,i,j])
N0=L*(L-1)
t=N0+1
assert len(core)==N0 and len({r[0] for r in core})==N0
assert p>max(2*small[-1]**2,5*L**4)
used_x={r[0] for r in core}
seen={0,1}
fresh=[]
rows=[]
attempts=0
x=small[-1]**2
while len(fresh)<t:
    x+=1
    attempts+=1
    if x in used_x or x%p==0: continue
    x2=x*x%p
    x3=x2*x%p
    x4=x2*x2%p
    inv3=pow(x3,-1,p)
    values=[((c0+c2*x2-x4)*inv3)%p for c0,_,c2 in bank]
    if len(set(values))!=L or any(z in seen for z in values): continue
    j=len(fresh)
    fresh.append([x,x4,x3])
    used_x.add(x)
    for i,z in enumerate(values):
        seen.add(z)
        new=z*pow(1-z,-1,p)%p
        rows.append([z,new,i,j])
assert len(rows)==15025
nodes=[r[0] for r in core]+[r[0] for r in fresh]
f=[r[1] for r in core]+[r[1] for r in fresh]
g=[r[1] for r in core]+[(r[1]+r[2])%p for r in fresh]
data=dict(schema='prime_quadratic_line_v1',p=p,L=L,n=len(nodes),K=3,
          core_length=N0,fresh_length=t,source_agreement=48,threshold=49,
          bad_count=15026,small_primes=small,bank_coefficients=bank,
          coefficient_order='constant, linear, quadratic',
          nodes=nodes,source_f=f,source_g=g,
          core_pair_indices=[[r[2],r[3]] for r in core],
          finite_label_columns=['canonical_label','final_label','bank_index','fresh_index'],
          finite_labels=rows,
          witness_encoding='For each finite row (old,z,i,j), coefficient vector is (1+z)*bank_coefficients[i] modulo p.',
          infinity=dict(label=p-1,witness_coefficients=[0,0,0],agreement=N0),
          greedy=dict(first_tested=small[-1]**2+1,attempts=attempts,last_tested=x,
                      forbidden_canonical_labels=[0,1]),
          proof_contract=dict(nonbank_core_bound=L,nonbank_fresh_bound=4,
                              nonzero_infinity_bound=5,core_bank_agreement=48,
                              common_agreement=48),
          finite_support=dict(m=4,derivative_cap=2,total_jet_cap=98,
                              challenge_cap=4704,coefficient_count=28812,local_rank=23),
          generator_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
out=HERE/'certificate.json'
out.write_text(json.dumps(data,separators=(',',':'))+'\n')
print(json.dumps(dict(status='GENERATED',p=p,n=len(nodes),finite_labels=len(rows),
                      total_bad=15026,greedy_attempts=attempts,
                      certificate_bytes=out.stat().st_size,
                      sha256=hashlib.sha256(out.read_bytes()).hexdigest()),indent=2))
