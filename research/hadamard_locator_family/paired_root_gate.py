"""Six exact linear equations for the dependent Hadamard selector type."""
import itertools,json
from pathlib import Path
import sympy as s
m=s.symbols('m0:4');h=s.symbols('h0:4')
signs=[(1,1,1,1),(1,1,-1,-1),(1,-1,1,-1),(1,-1,-1,1)]
eq=[];pairs=[]
for i,j in itertools.combinations(range(4),2):
    E=[g for g in range(4) if signs[i][g]==signs[j][g]]
    D=[g for g in range(4) if signs[i][g]!=signs[j][g]]
    def odd_parts(groups):
        a,b=groups
        return (signs[i][a]*m[a]+signs[i][b]*m[b],
                signs[i][a]*m[a]*h[b]+signs[i][b]*m[b]*h[a])
    E1,E3=odd_parts(E);D1,D3=odd_parts(D)
    f=s.expand(E1*D3-E3*D1);assert f.subs(dict.fromkeys(h,1))==0
    eq.append(f);pairs.append([i,j])
M=s.Matrix([[f.coeff(v) for v in h] for f in eq])
# Remove the universal kernel (1,1,1,1) by h3=0.
A=M[:,:3];minors=[]
for rows in itertools.combinations(range(6),3):
    f=s.factor(A[list(rows),:].det())
    if f:minors.append({'rows':rows,'determinant':str(f)})
out={'selector_group_signs':signs,'pair_order':pairs,
     'equations':[str(f) for f in eq],'matrix':[[str(z) for z in row] for row in M.tolist()],
     'three_by_three_minors':minors,
     'universal_solution':'h0=h1=h2=h3; all six edge squares then equal -h0',
     'scope':'Dependent selector type; no field scan.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
