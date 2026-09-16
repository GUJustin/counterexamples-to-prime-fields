"""Independent 3D identities, Gram weights, cube noise and reflection checks."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import hashlib,json
from compute_radial_projection_moments10 import orbit
from verify_radial_projection_moments14 import multiply,noise_direct

ROOT=Path(__file__).resolve().parent


def main():
    data=json.loads((ROOT/'radial3d_projection_moments14.json').read_text())
    design=json.loads((ROOT/'radial3d_projection_design14.json').read_text())
    base=json.loads((ROOT/'radial_projection_moments14.json').read_text())
    meta=json.loads((ROOT/'radial_projections/metadata.json').read_text())
    assert data['status']=='computed_and_complement_checked'
    assert json.loads((ROOT/'radial_projection_moments14_verification.json').read_text())['status']=='passed'
    n,t,q,C=(data[k] for k in ('n','t','q','count'))
    assert all(data[k]==base[k]==meta[k] for k in ('n','t','q','count'))
    assert data['scales']==base['scales'][:3]==meta['scales'][:3]
    groups=[orbit(tuple(v)) for v in design['orbit_bases']]
    group_of={v+(0,):i for i,group in enumerate(groups) for v in group}
    assert set(group_of)==set(tuple(r['direction']) for r in data['records'])
    assert len(data['records'])==design['total_directions']==73
    identities=[list(map(F,row)) for row in design['radial_identity_weights']]
    zero=(0,0,0);norm={(2,0,0):1,(0,2,0):1,(0,0,2):1}
    target={zero:1};targets=[];actual=[{} for _ in range(7)]
    for _ in range(7):target=multiply(target,norm);targets.append(target)
    coefficients=[list(map(F,row)) for row in meta['gram_coefficients']]
    normalized=[[sum(c*comb(a,j) for j,c in enumerate(row))/meta['scales'][i]
                 for a in range(n)] for i,row in enumerate(coefficients)]
    all_records={}
    for record in base['records']:
        for mode in ('down','up'):
            all_records[str(ROOT/'radial_projections14'/f"{mode}_{record['index']:03d}.json")]=record
    for record in data['records']:
        for mode in ('down','up'):all_records[record[mode+'_file']]=record
    radial=[F(1)]+[F(0)]*7;reflections=0;noises={}
    for record in data['records']:
        direction=tuple(record['direction']);oid=group_of[direction];den=record['denominator']
        linear={tuple(int(i==j) for i in range(3)):c for j,c in enumerate(direction[:3]) if c}
        power={zero:1}
        for j in range(1,15):
            power=multiply(power,linear)
            if j%2:continue
            r=j//2;factor=identities[r-1][oid]/len(groups[oid])
            for exponent,c in power.items():actual[r-1][exponent]=actual[r-1].get(exponent,F(0))+factor*c
        weight_text=Path(record['weights_file']).read_text()
        assert hashlib.sha256(weight_text.encode()).hexdigest()==record['weights_sha256']
        weights=list(map(int,weight_text.split()))
        assert all(F(value,den)==sum(direction[j]*normalized[j][a] for j in range(4))
                   for a,value in enumerate(weights))
        outputs=[]
        for count,total,mode in ((t,q,'down'),(n-t,comb(n,2)-q,'up')):
            raw=json.loads(Path(record[mode+'_file']).read_text())
            assert (raw['n'],raw['t'],raw['q'],raw['degree'],raw['direction'])==(n,count,total,14,mode)
            assert len(raw['raw_moments'])==15 and raw['raw_moments'][0]==C
            source_file=raw.get('reflection_source_file')
            if source_file is None and 'reflection_source_index' in raw:
                source_file=str(ROOT/'radial_projections14'/f"{mode}_{raw['reflection_source_index']:03d}.json")
            if source_file is not None:
                source=json.loads(Path(source_file).read_text());source_record=all_records[source_file]
                assert 'reflection_source_file' not in source and 'reflection_source_index' not in source
                sign=raw['reflection_sign'];assert sign in (-1,1)
                assert source_record['denominator']==den and 2*total==count*(n-1)
                source_text=Path(source_record['weights_file']).read_text()
                source_hash=hashlib.sha256(source_text.encode()).hexdigest()
                assert source_hash==raw['reflection_source_weights_sha256']==source_record['weights_sha256']
                assert weights==[sign*v for v in reversed(list(map(int,source_text.split())))]
                assert raw['raw_moments']==[sign**j*v for j,v in enumerate(source['raw_moments'])]
                reflections+=1
            outputs.append(raw['raw_moments'])
        down,up=outputs;assert up==[(-1)**j*v for j,v in enumerate(down)]
        mean=F(down[1],C*den);assert mean==F(record['mean'])
        assert F(down[2],C*den**2)-mean**2==F(record['variance'])
        centered=[sum(comb(j,i)*(-mean)**(j-i)*F(down[i],C*den**i) for i in range(j+1)) for j in range(15)]
        key=tuple(abs(v) for v in direction)
        if key not in noises:noises[key]=noise_direct(key,meta['scales'])
        smooth=[sum(comb(j,i)*centered[i]*noises[key][j-i] for i in range(j+1)) for j in range(15)]
        assert smooth==list(map(F,record['smoothed_centered_moments']))
        for r in range(1,8):radial[r]+=identities[r-1][oid]*smooth[2*r]/len(groups[oid])
    assert all({e:c for e,c in row.items() if c}==target for row,target in zip(actual,targets))
    assert radial==list(map(F,data['radial_moments']))
    prior=json.loads((ROOT/'interval_extension_line_verification.json').read_text())
    assert radial[:6]==list(map(F,prior['radial_moments']))
    result=dict(status='passed',dimension=3,degree=14,directions=73,extra_directions=12,
                radial_moments=list(map(str,radial)),all_polynomial_coefficients_checked=True,
                independently_reconstructed_Gram_weights=True,independent_multinomial_noise=True,
                complementary_subset_checks=True,reflection_mode_outputs_checked=reflections,
                prior_first_five_radial_moments_match=True)
    (ROOT/'radial3d_projection_moments14_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='radial_moments'},indent=2),flush=True)


if __name__=='__main__':main()
