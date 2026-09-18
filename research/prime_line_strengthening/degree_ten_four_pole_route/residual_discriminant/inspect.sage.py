"""Staged exact inspection. Each invocation performs ONE named bounded phase."""
import argparse, hashlib, json, time
from pathlib import Path
from sage.all import GF, PolynomialRing, prod

ap=argparse.ArgumentParser()
ap.add_argument('--phase',choices=['inspect','generic-gcd','factor','line-subresultants'],required=True)
ap.add_argument('--input',type=Path,default=Path(__file__).with_name('reconstruction.json'))
ap.add_argument('--gate',type=Path,default=Path(__file__).resolve().parents[1]/'gate.json')
ap.add_argument('--line-t',type=int,default=1)
ap.add_argument('--parameter-chart',choices=['a1','a0'],default='a1',
                help='a1: [1:u:line-t]; a0: entire boundary line [0:1:u]')
ap.add_argument('--output',type=Path)
args=ap.parse_args()
if args.output is None: args.output=Path(__file__).with_name(args.phase+'.json')
raw=args.input.read_bytes();data=json.loads(raw)
assert data['schema_version']==1 and data['p']==29
assert data['input_sha256']==hashlib.sha256(args.gate.read_bytes()).hexdigest()
assert data['interpolation_verified_at_all_190_nodes'] and data['mu7_sparsity_verified']
k=GF(29);R=PolynomialRing(k,('s','t'));s,t=R.gens()
cc=[R({tuple(e):k(c) for e,c in terms}) for terms in data['residual_coefficient_terms']]
SX=PolynomialRing(R,'X');X=SX.gen();D=SX(cc)
assert D.degree()==48
out={'phase':args.phase,'input_sha256':hashlib.sha256(raw).hexdigest(),'status':'started'}
start=time.monotonic()
def checkpoint():
    out['seconds']=time.monotonic()-start
    tmp=args.output.with_suffix(args.output.suffix+'.tmp')
    tmp.write_text(json.dumps(out,indent=2));tmp.replace(args.output)
def factrec(f):
    f=R(f)
    if not f: return {'zero':True}
    fs=f.factor()
    return {'degree':int(f.total_degree()),'terms':len(f.dict()),'unit':str(fs.unit()),
            'factors':[{'polynomial':str(g),'exponent':int(e),'degree':int(g.total_degree())}
                       for g,e in fs]}
checkpoint()

if args.phase=='inspect':
    out['specialized_gcds']=[]
    for a,b in [(0,0),(0,1),(1,0),(1,1),(1,2),(2,1),(2,3),(3,2),(4,7),(7,4),(11,13),(13,11)]:
        RX=PolynomialRing(k,'x');f=RX([c(k(a),k(b)) for c in cc])
        g=f.gcd(f.derivative()) if f else RX.zero()
        out['specialized_gcds'].append({'s':a,'t':b,'degree':int(f.degree()),
                                       'gcd_degree':int(g.degree())})
        checkpoint()
    full=[v['gcd_degree'] for v in out['specialized_gcds'] if v['degree']==48]
    out['generic_gcd_degree_upper_bound']=min(full) if full else None
    bank=next(v for v in json.loads(args.gate.read_bytes()) if v['bank']=='paley')
    terms={}
    for weight,vec in zip((R.one(),s,t),bank['kernel']):
        for ij,a in zip(bank['columns'],vec):
            ij=tuple(ij);terms[ij]=terms.get(ij,R.zero())+weight*k(a)
    B=SX([terms.get((i,10),R.zero()) for i in range(5)])
    C=SX([terms.get((i,9),R.zero()) for i in range(8)])
    guards=[('residual_degree48',cc[48]),('B_degree4',B[4]),
            ('B_squarefree',B.discriminant()),('B_C_resultant',B.resultant(C))]
    for idx,(x,y) in enumerate(zip(bank['base'],bank['word'])):
        m=4 if idx<7 else 6
        import math
        ym=sum(c*k(math.comb(j,m))*k(x)**i*k(y)**(j-m)
               for (i,j),c in terms.items() if j>=m)
        guards.extend([('B_node_'+str(idx),B(k(x))),('Y_multiplicity_'+str(idx),ym)])
    infinity=SX([terms.get((34-3*j,j),R.zero()) for j in range(11)])
    guards.extend([('infinity_degree10',infinity[10]),
                   ('infinity_squarefree',infinity.discriminant())])
    out['guards']=[]
    for name,f in guards:
        out['guards'].append({'name':name,**factrec(f)});checkpoint()
elif args.phase=='generic-gcd':
    K=R.fraction_field();PX=PolynomialRing(K,'x');f=PX([K(c) for c in cc])
    g=f.gcd(f.derivative())
    out['gcd_degree']=int(g.degree());out['gcd_coefficients']=list(map(str,g.list()))
elif args.phase=='factor':
    M=PolynomialRing(k,('s','t','x'));ms,mt,mx=M.gens()
    f=sum(k(c)*ms**int(a)*mt**int(b)*mx**d
          for d,v in enumerate(cc) for (a,b),c in v.dict().items())
    fac=f.factor()
    out['unit']=str(fac.unit())
    out['factors']=[{'polynomial':str(g),'exponent':int(e),
                     'degrees':list(map(int,g.degrees())),'terms':len(g.dict())} for g,e in fac]
elif args.phase=='line-subresultants':
    # A projective algebraic line test; leading-degree drops are retained separately.
    A=PolynomialRing(k,'u');u=A.gen();PX=PolynomialRing(A,'x')
    line=k(args.line_t)
    if args.parameter_chart=='a1':
        fc=[sum(k(z)*u**int(a)*line**int(b) for (a,b),z in c.dict().items()) for c in cc]
        endpoint=[sum(z for e,z in c.dict().items() if tuple(e)==(18,0)) for c in cc]
        out['projective_line']='[1:u:'+str(int(line))+']; endpoint [0:1:0]'
    else:
        fc=[sum(k(z)*u**int(b) for (a,b),z in c.dict().items() if a+b==18) for c in cc]
        endpoint=[sum(z for e,z in c.dict().items() if tuple(e)==(0,18)) for c in cc]
        out['projective_line']='[0:1:u]; endpoint [0:0:1]'
    fc=[A(v) for v in fc]
    f=PX(fc)
    assert f
    generic_degree=int(f.degree())
    infinity_generic=max(47-generic_degree,0)
    finite_required=max(15-infinity_generic,0)
    out['generic_X_degree']=generic_degree
    out['generic_infinity_gcd_contribution']=infinity_generic
    out['required_finite_gcd_degree']=finite_required
    out['leading_coefficient']=str(f.leading_coefficient());checkpoint()
    seq=f.subresultants(f.derivative())
    out['subresultant_profile']=[{'X_degree':int(v.degree()),
         'coefficient_degree':max(int(c.degree()) for c in v.list() if c),
         'coefficient_terms':sum(len(c.list()) for c in v.list())} for v in seq]
    low=[A(v.leading_coefficient()) for v in seq if 0<=v.degree()<finite_required]
    h=A.zero()
    for v in low:h=h.gcd(v)
    out['low_principal_subresultant_gcd']=str(h)
    out['line_candidate_factorization']=str(h.factor()) if h else 'identically zero'
    def binary_check(values,field):
        Q=PolynomialRing(field,'z');g=Q(values)
        if not g:return {'zero_discriminant':True,'eligible':True,
                         'curve_candidate_requires_separate_analysis':True,
                         'separate_degenerate_case':True}
        dg=int(g.degree());gg=int(g.gcd(g.derivative()).degree())
        inf=max(47-dg,0)
        return {'X_degree':dg,'finite_gcd_degree':gg,'infinity_gcd_contribution':inf,
                'binary_partial_gcd_degree':gg+inf,'eligible':gg+inf>=15}
    out['projective_endpoint']=binary_check(endpoint,k)
    out['exact_algebraic_parameter_checks']=[]
    if h:
        # Outside leading-degree drops, the subresultant criterion gives every
        # possible solution. Include ALL leading drops before exact fiber checks.
        candidates=h*f.leading_coefficient()
        for factor,exponent in candidates.factor():
            deg=int(factor.degree())
            if deg==1:
                field=k;alpha=-factor[0]/factor[1]
            else:
                field=GF(29**deg,name='alpha',modulus=factor.monic());alpha=field.gen()
            values=[sum(field(z)*alpha**i for i,z in enumerate(c.list())) for c in fc]
            out['exact_algebraic_parameter_checks'].append(
                {'parameter_polynomial':str(factor),'residue_degree':deg,
                 **binary_check(values,field)})
            checkpoint()
    else:
        out['positive_dimensional_line_locus_possible']=True
    out['scope']='Global binary gcd>=15 test on this projective parameter line; zero discriminants require separate treatment; no plane exclusion.'
out['status']='complete';checkpoint()
print(json.dumps(out,indent=2),flush=True)
