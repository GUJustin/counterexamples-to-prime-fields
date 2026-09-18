import hashlib,json,math,pathlib
base=pathlib.Path(__file__).resolve().parent
a=json.loads((base/'pilot_d3.json').read_text())
b=json.loads((base/'verify_d3.json').read_text())
checks={k:a[k]==b[k] for k in b if k!='seconds'}
p=a['p'];hits=a['bank_fresh_hit_histogram'];owners=a['owner_histogram']
checks.update({
    'prime':p>1 and all(p%j for j in range(2,math.isqrt(p)+1)),
    'hit_mass':sum(hits)==a['L']*p,
    'hit_incidence_mass':sum(j*v for j,v in enumerate(hits))==a['L']*a['t'],
    'owner_mass':sum(owners.values())==p,
    'qualifying_witness_mass':sum(int(j)*v for j,v in owners.items())==sum(hits[a['d']:]),
    'below_johnson':a['T']**2<2*a['n'],
    'nonbank_cap':a['L']+a['D']<=a['A'],
    'count_exceeds_domain_size':a['transformed_singleton_labels']>a['n'],
})
assert all(checks.values()),checks
out={'status':'PASS','method':'separately structured C++ replay; no generator import','checks':checks,
     'canonical_singleton_labels':b['canonical_singleton_labels'],
     'transformed_singleton_labels':b['canonical_singleton_labels']+1,
     'canonical_bad_labels':b['canonical_bad_labels'],
     'transformed_bad_labels':b['canonical_bad_labels']+1,'replay_seconds':b['seconds']}
for key,name in [('generator','pilot.cpp'),('verifier','verify.cpp'),('input','pilot_d3.json')]:
    out[key+'_sha256']=hashlib.sha256((base/name).read_bytes()).hexdigest()
(base/'pilot_d3.verified.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
