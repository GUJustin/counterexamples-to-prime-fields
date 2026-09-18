"""Bounded degree62 Nullstellensatz search; exact Hasse jets through order14."""
import argparse,hashlib,json,math
from pathlib import Path
from flint import nmod_mat,nmod_poly
ap=argparse.ArgumentParser();ap.add_argument('--input',type=Path,default=Path(__file__).with_name('gauss_image_interpolation.json'))
ap.add_argument('--output',type=Path,default=Path(__file__).with_name('hasse_multiplicity_gate.json'));args=ap.parse_args()
raw=args.input.read_bytes();data=json.loads(raw);terms=[(tuple(e),c) for e,c in data['image_terms']]
p=29;assert all(sum(e)==62 and (2*e[1]+4*e[2])%7==5 for e,c in terms)
cols=[(i,j) for i in range(63) for j in range(63-i) if (2*i+4*j)%7==0]
colindex={e:i for i,e in enumerate(cols)};rows=[];metadata=[]
for t in range(15):
    for db in range(t+1):
        dc=t-db
        deriv={(b-db,c-dc):v*math.comb(b,db)*math.comb(c,dc)%p
               for (a,b,c),v in terms if b>=db and c>=dc}
        deriv={e:v for e,v in deriv.items() if v}
        for mb in range(t+1):
            for mc in range(t+1-mb):
                if (5-2*db-4*dc+2*mb+4*mc)%7:continue
                row=[0]*len(cols)
                for (b,c),v in deriv.items():row[colindex[b+mb,c+mc]]=v
                if any(row):rows.append(row);metadata.append([db,dc,mb,mc])
M=nmod_mat(rows,p);rt,rank=M.transpose().rref()
selected=[]
for i in range(rank):selected.append(next(j for j in range(len(rows)) if rt[i,j]))
basis=[rows[i] for i in selected];rr,_=nmod_mat(basis,p).rref()
piv=[next(j for j in range(len(cols)) if rr[i,j]) for i in range(rank)]
target=[int(e==(0,0)) for e in cols]
square=nmod_mat([[row[j] for j in piv] for row in basis],p)
solution=nmod_mat([[target[j] for j in piv]],p)*square.inv()
weights=[int(solution[0,i]) for i in range(rank)]
combined=[sum(w*row[j] for w,row in zip(weights,basis))%p for j in range(len(cols))]
success=combined==target
out={'input_sha256':hashlib.sha256(raw).hexdigest(),'p':p,'Hasse_orders':[0,14],
     'affine_chart':'a=1','degree_bound':62,'character':0,
     'matrix_rows':len(rows),'matrix_columns':len(cols),'rank':rank,
     'constant_in_span':success,'selected_row_indices':selected,'pivot_columns':piv}
if success:
    out['affine_certificate']=[{'coefficient':w,'derivative_b':metadata[i][0],
         'derivative_c':metadata[i][1],'multiplier_b':metadata[i][2],
         'multiplier_c':metadata[i][3]} for i,w in zip(selected,weights) if w]
else:
    out['scope']='Bounded span inconclusive; no affine-locus exclusion.'
args.output.write_text(json.dumps(out,indent=2))
print('Affine degree62 span',len(rows),len(cols),'rank',rank,'contains1',success,flush=True)

# Boundary a=0, c=1: evaluate ALL a,b Hasse jets of total order<=14.
jets=[];jetmeta=[]
for t in range(15):
    for da in range(t+1):
        db=t-da;coeff=[0]*63
        for (a,b,c),v in terms:
            if a==da and b>=db:coeff[b-db]=(coeff[b-db]+v*math.comb(b,db))%p
        f=nmod_poly(coeff,p)
        if f:jets.append(f);jetmeta.append([da,db])
g=nmod_poly([],p);representation={}
for index,f in enumerate(jets):
    gg,s,t=g.xgcd(f)
    representation={j:s*v for j,v in representation.items() if s*v}
    representation[index]=representation.get(index,nmod_poly([],p))+t
    g=gg
    if g.degree()==0:break
boundary_success=g.degree()==0
out['boundary_gcd_coefficients']=[int(g[i]) for i in range(g.degree()+1)]
out['boundary_empty']=boundary_success
out['boundary_certificate']=[{'derivative_a':jetmeta[j][0],'derivative_b':jetmeta[j][1],
    'multiplier_coefficients':[int(f[i]) for i in range(f.degree()+1)]}
    for j,f in representation.items() if f]
replay=sum((f*jets[j] for j,f in representation.items()),nmod_poly([],p));assert replay==g
endpoint=min(a+c for (a,b,c),v in terms)
out['endpoint_010_multiplicity']=endpoint
out['global_exclusion']=success and boundary_success and endpoint<15
args.output.write_text(json.dumps(out,indent=2))
print('Boundary gcd',g,'endpoint multiplicity',endpoint,'global exclusion',out['global_exclusion'],flush=True)
