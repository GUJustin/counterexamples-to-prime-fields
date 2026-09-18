"""sage -python exact_kernel.sage.py --gate gate.json --fibers fiber_patterns.json

Three 31-by-32 systems over Q(eta); no cyclotomic degree-six extension and
no characteristic-zero discriminant reconstruction.
"""
import argparse, hashlib, json, math, time
from pathlib import Path
from sage.all import QQ, ZZ, GF, NumberField, PolynomialRing, matrix
ap=argparse.ArgumentParser()
ap.add_argument('--gate',type=Path,default=Path(__file__).with_name('gate.json'))
ap.add_argument('--fibers',type=Path,default=Path(__file__).resolve().parent.parent/'quadratic_one_pole_route'/'fiber_patterns.json')
ap.add_argument('--output',type=Path,default=Path(__file__).with_name('exact_kernel.json'))
args=ap.parse_args();started=time.monotonic()
raw=args.gate.read_bytes();bank=next(x for x in json.loads(raw) if x['bank']=='paley')
fraw=args.fibers.read_bytes();fib=json.loads(fraw)
assert bank['p']==fib['p']==29 and fib['eta']==7
assert bank['rank']==217 and len(bank['columns'])==220 and bank['leading_projection_rank']==3
assert sum(pow(fib['zeta'],j,29) for j in (1,2,4))%29==7
R=PolynomialRing(QQ,'v');v=R.gen();K=NumberField(v*v+v+2,'eta');eta=K.gen()
alpha=(eta-1)/2;cv=3*(eta+3)/4
assert alpha and alpha**7!=1 and cv
def pair(x):
 a=K(x).list();a += [QQ.zero()]*(2-len(a));return list(map(str,a))
def reduction(x):
 # Allows denominators divisible by29 when canceled at the chosen split
 # prime: Hensel-lift eta before dividing, rather than dividing by zero.
 aa=K(x).list();aa += [QQ.zero()]*(2-len(aa))
 den=ZZ(1)
 for z in aa:den=den.lcm(z.denominator())
 nums=[ZZ(z*den) for z in aa];val=den.valuation(29);mod=29**(val+1)
 root=ZZ(7);power=ZZ(29)
 for j in range(val):
  correction=(-((root*root+root+2)//power)*pow(int(2*root+1),-1,29))%29
  root+=power*correction;power*=29
 num=(nums[0]+nums[1]*root)%mod
 assert num%(29**val)==0, 'Coefficient is not integral at eta=7'
 return int((num//(29**val))*pow(int(den//(29**val)),-1,29)%29)
assert reduction(alpha)==fib['alpha'] and reduction(cv)==fib['c']
cols=[tuple(c) for c in bank['columns']]
conditions=[(x,y,dx,total-dx) for x,y,m in [(K(1),K(1),4),(alpha,cv,6)] for total in range(m) for dx in range(total+1)]
out={'schema_version':1,'field_polynomial':'eta^2+eta+2','prime':29,'eta_reduction':7,
     'gate_sha256':hashlib.sha256(raw).hexdigest(),'fibers_sha256':hashlib.sha256(fraw).hexdigest(),
     'alpha':pair(alpha),'c':pair(cv),'columns':bank['columns'],'components':[]}
def checkpoint():
 out['seconds']=time.monotonic()-started
 tmp=args.output.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2));tmp.replace(args.output)
for idx,char in enumerate((1,3,5)):
 positions=[h for h,(i,j) in enumerate(cols) if (i+5*j)%7==char]
 subcols=[cols[h] for h in positions];assert len(subcols)==32
 rows=[[K(math.comb(i,dx)*math.comb(j,dy))*x**(i-dx)*y**(j-dy) if i>=dx and j>=dy else K.zero()
        for i,j in subcols] for x,y,dx,dy in conditions]
 M=matrix(K,rows);assert M.nrows()==31
 ker=M.right_kernel();assert ker.dimension()==1
 vec=ker.basis()[0];lead=(2*idx,10);at=subcols.index(lead)
 target=bank['kernel'][idx][cols.index(lead)];assert target
 vec=vec*(K(target)/vec[at]);assert not any(M*vec)
 full=[K.zero()]*len(cols)
 for pos,coeff in zip(positions,vec):full[pos]=coeff
 reduced=list(map(reduction,full));assert reduced==bank['kernel'][idx]
 # Independently certify the exact rank by a nonzero square minor.
 piv=list(M.pivots());assert len(piv)==31
 determinant=M.matrix_from_columns(piv).determinant();assert determinant
 rec={'character':char,'shape':[31,32],'rank':31,'nullity':1,
      'leading_monomial':list(lead),'leading_coefficient':target,
      'terms':[[i,j,pair(coeff)] for (i,j),coeff in zip(cols,full) if coeff],
      'rank_minor_columns':piv,'rank_minor_determinant':pair(determinant),
      'mod29_matches_saved_basis':True,'representative_jets_zero':True}
 out['components'].append(rec);checkpoint()
 print('character',char,'rank31','terms',len(rec['terms']),'seconds',round(out['seconds'],3),flush=True)
# Eigenweights extend ideal-power vanishing from the representatives to
# every point in both mu7 orbits. Three independent forms + the existing
# rank217 good-prime minor prove the full characteristic-zero kernel is3D.
out['full_characteristic_zero_kernel_dimension']=3
out['mu7_extension']='F(zeta X,zeta^5 Y)=zeta^character F(X,Y)'
out['status']='PASS';checkpoint();print(json.dumps({'status':'PASS','seconds':out['seconds']}))
