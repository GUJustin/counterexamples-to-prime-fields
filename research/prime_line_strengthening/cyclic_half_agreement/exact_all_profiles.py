"""Complete exact cyclic two-coset test using all compatible support profiles."""
import argparse,json,time,gzip
from pathlib import Path
import sympy as s
from sympy.polys.densearith import dup_rem,dup_sub,dup_mul,dup_mul_ground,dup_add,dup_exquo
from sympy.polys.euclidtools import dup_gcd,dup_gcdex
ap=argparse.ArgumentParser();ap.add_argument('q',type=int);args=ap.parse_args();q=args.q;r=(q-1)//2;root=Path(__file__).parent;start=time.monotonic()
Z=s.Symbol('zeta');K=s.QQ.algebraic_field((s.Poly(s.cyclotomic_poly(q,Z),Z,domain=s.QQ),Z));z=K([1,0]);powers=[z**i for i in range(q)];one=K.one;zero=K.zero
assert z**q==one and all(z**i!=one for i in range(1,q))
def rootpoly(indices):
 a=[one]
 for j in indices:a=dup_mul(a,[one,-powers[j]],K)
 return a
def monomial(n):return [one]+[zero]*n
def enc(a):return [[str(x) for x in c.to_list()] for c in a]
def bits(mask):return [j for j in range(q) if mask>>j&1]
profile=json.loads((root/f'profiles_q{q}.json').read_text());profiles={a['key']:a for a in profile['profiles']};rows=[];certs=[]
for row in profile['profiles']:
 for Cmask in row['C_masks']:
  C=set(bits(Cmask));S=[i for i in range(q) if i not in C];modulus=rootpoly(S)
  for h in range(r+1,q):
   P=dup_rem(monomial(h),modulus,K);coeff=[P[-j-1] if j<len(P) else zero for j in range(r+1)]
   for Tmask in profiles[row['target_key']]['C_masks']:
    T=bits(Tmask);t0=T[0];inputs=[]
    for t in T[1:]:
     f=[coeff[j]*(powers[((j-h)*t)%q]-powers[((j-h)*t0)%q]) for j in reversed(range(r+1))]
     while f and f[0]==zero:f.pop(0)
     inputs.append(f)
    G=[];representation=[[] for _ in inputs]
    for i,f in enumerate(inputs):
     if not f:continue
     if not G:
      c=one/f[0];G=dup_mul_ground(f,c,K);representation[i]=[c]
     else:
      a,b,Gnew=dup_gcdex(G,f,K)
      representation=[dup_mul(a,c,K) for c in representation];representation[i]=dup_add(representation[i],b,K);G=Gnew
     if len(G)==1:break
    assert G
    check=[]
    for b,f in zip(representation,inputs):check=dup_add(check,dup_mul(b,f,K),K)
    assert check==G
    forbidden=dup_mul([one,zero],dup_sub(monomial(q),[one],K),K)
    valid=G
    while len(valid)>1:
     g=dup_gcd(valid,forbidden,K)
     if len(g)<=1:break
     valid=dup_exquo(valid,g,K)
    rec={'C_mask':Cmask,'T_mask':Tmask,'h':h,'P':enc(P),'raw_gcd':enc(G),'valid_gcd':enc(valid),'valid_degree':len(valid)-1}
    rows.append(rec)
    certificate={'C_mask':Cmask,'T_mask':Tmask,'h':h,'gcd':enc(G),'inputs':[enc(f) for f in inputs],'bezout':[enc(b) for b in representation]}
    if len(valid)==1:
     Bpow=[one]
     for _ in range(r):Bpow=dup_mul(Bpow,forbidden,K)
     quotient=dup_exquo(Bpow,G,K);assert dup_mul(G,quotient,K)==Bpow
     certificate['forbidden_power_quotient']=enc(quotient)
    certs.append(certificate)
 print('profile',row['key'],'tests',len(rows),'seconds',time.monotonic()-start,flush=True)
out={'q':q,'field_polynomial':str(s.cyclotomic_poly(q,Z)),'complete_for_cyclic_two_coset_ansatz':True,'tests':len(rows),'survivors':[a for a in rows if a['valid_degree']>0],'rows':rows,'seconds':time.monotonic()-start}
(root/f'exact_profiles_q{q}.json').write_text(json.dumps(out,indent=2)+'\n')
with gzip.open(root/f'exact_profiles_q{q}_bezout.json.gz','wt') as f:json.dump({'q':q,'rows':certs},f,separators=(',',':'))
print(json.dumps({'q':q,'tests':len(rows),'survivors':[(a['C_mask'],a['T_mask'],a['h'],a['valid_degree']) for a in out['survivors']],'seconds':out['seconds']}),flush=True)
