"""Boundary-characteristic checks for the multiplicity proof of Riccati lists."""
import importlib.util,itertools,json,random
from pathlib import Path
BASE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('riccati',BASE/'verify.py');h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)

def order(poly,x,p):
    m=0
    while h.evaluate(poly,x,p)==0:
        poly,rem=h.divide(poly,[-x%p,1],p)
        assert rem==[0]
        m+=1
    return m

def main():
    rng=random.Random(202609162237)
    cases=[]
    for coeff in itertools.product(range(5),repeat=4):
        v=h.trim(coeff)
        if len(v)!=4:continue
        u=h.add(v,[1],5)
        cases.append((5,3,u,v))
    for p,D,number in [(7,4,12),(7,5,4),(11,6,0)]:
        for _ in range(number):
            v=[rng.randrange(p) for _ in range(D)]+[rng.randrange(1,p)]
            u=h.add(v,[1],p)
            cases.append((p,D,u,v))
    # Boundary cases p=D+1, including four solutions in characteristic two.
    cases += [(3,2,[1,1,1],[0,1,1])]
    for _ in range(32):
        p,D=5,4
        v=[rng.randrange(p) for _ in range(D)]+[rng.randrange(1,p)]
        cases.append((p,D,h.add(v,[1],p),v))
    enumerated=coordinates=mixed=nonconstant=0
    exceptional=[];mixed_example=None
    for p,D,u,v in cases:
        eq=h.equation_from_pencil(u,v,[1],[0],p)
        candidates=[]
        for coeff in itertools.product(range(p),repeat=D+1):
            enumerated+=1
            P=h.trim(coeff)
            if h.residual(P,eq,p)==[0]:candidates.append(P)
        assert len(candidates)>=3
        assert len(candidates)<= (D+2 if p>D+1 else 2*D+2)
        if len(candidates)>D+2:
            exceptional.append(dict(p=p,D=D,solutions=len(candidates),u=u,v=v))
        for quadruple in itertools.combinations(candidates,4):
            constant,_,_,_=h.cross_ratio(quadruple,p)
            nonconstant+=not constant
        subsets=[candidates]
        if len(candidates)>=5:
            subsets += [list(s) for s in itertools.combinations(candidates,4)]
        for family in subsets:
            M=len(family)
            for x in range(p):
                values=[h.evaluate(P,x,p) for P in family]
                frequencies=[values.count(y) for y in set(values)]
                orders={(i,j):order(h.subtract(family[i],family[j],p),x,p)
                        for i,j in itertools.combinations(range(M),2)}
                C=sum(orders.values())
                if max(frequencies)>1 and max(frequencies)<M-1:
                    mixed+=1
                    assert len(frequencies)==2 and min(frequencies)>=2
                    assert all(q>=p-D for q in orders.values() if q)
                    if mixed_example is None:
                        mixed_example=dict(p=p,D=D,polynomials=family,x=x,values=values,
                                           pair_orders={f'{i},{j}':q for (i,j),q in orders.items()})
                for matches in [0]+frequencies:
                    assert (matches-1)*(M-1)<=2*C
                coordinates+=1
    # A sharp 2D+2 boundary count: (X^2+X) P' = P^2+P over F_2.
    p,D=2,1
    equation=([0,1,1],[0],[1],[1])
    sharp_boundary=[h.trim(c) for c in itertools.product(range(p),repeat=D+1)
                    if h.residual(h.trim(c),equation,p)==[0]]
    assert len(sharp_boundary)==2*D+2==4
    result=dict(status='PASS',sharp_boundary_solutions=sharp_boundary,equations=len(cases),polynomials_enumerated=enumerated,
                coordinate_family_checks=coordinates,mixed_two_cluster_coordinates=mixed,
                nonconstant_cross_ratios=nonconstant,solution_count_exceptions=exceptional,
                mixed_example=mixed_example,
                scope='Characteristics p>D, including p=D+1. Local multiplicity inequality holds for every received value; nonlinear solution counts obey D+2 above the boundary and 2D+2 at the boundary.')
    (BASE/'multiplicity_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
