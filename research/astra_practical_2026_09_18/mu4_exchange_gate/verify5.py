import json,math
from pathlib import Path
D=Path(__file__).parent
r=json.loads((D/'result5.json').read_text());p=r['p'];omega=pow(3,(p-1)//256,p)
assert pow(omega,256,p)==1 and pow(omega,128,p)!=1
canon=set();verified=[]
for aa,bb in r['genuine_disjoint_examples']:
 A=[a+64*k for a in aa for k in range(4)];B=[b+64*k for b in bb for k in range(4)]
 assert len(set(A+B))==40 and 0 not in A+B
 va=[pow(omega,a,p) for a in A];vb=[pow(omega,b,p) for b in B]
 assert all(sum(pow(a,j,p) for a in va)%p==sum(pow(b,j,p) for b in vb)%p for j in range(1,7))
 assert math.prod(va)%p==math.prod(vb)%p
 coeff=[0]*32
 for sign,seq in [(1,aa),(-1,bb)]:
  for a in seq:coeff[a%32]+=sign*(1 if a<32 else -1)
 assert any(coeff)
 orbit=[]
 for t in range(64):
  a=tuple(sorted((x+t)%64 for x in aa));b=tuple(sorted((x+t)%64 for x in bb));orbit.append(tuple(sorted((a,b))))
 canon.add(min(orbit));verified.append([A,B])
assert len(verified)==r['genuine_disjoint_pairs']==54
N=math.comb(255,136);req=274980728111395088;w=math.comb(215,116)
out={'independent_direct_256_root_verifications':54,'rotation_orbits':len(canon),'canonical_orbit_representatives':list(canon),'E20_genuine_certified':108,'weighted_contribution':str(108*w),'fraction_target_log2':math.log2(108*w)-math.log2(N*(req-1)+1),'second_moment_bound_increment':108*w/N,'underlying_root_exponent_examples':verified}
(D/'verified5.json').write_text(json.dumps(out,indent=2)+'\n')
print({k:v for k,v in out.items() if k!='underlying_root_exponent_examples'})
