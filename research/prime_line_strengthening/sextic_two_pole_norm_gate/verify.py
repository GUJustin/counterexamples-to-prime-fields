"""Independent exact integer determinant replay of the two sextic gates."""
import json
from pathlib import Path
P=Path(__file__).parent

def powers_shift(x,n,p):
    # Coefficients of (x+T)^n, by repeated multiplication.
    a=[1]
    for _ in range(n):
        b=[0]*(len(a)+1)
        for i,v in enumerate(a): b[i]=(b[i]+x*v)%p; b[i+1]=(b[i+1]+v)%p
        a=b
    return a

def bareiss(a):
    a=[r[:] for r in a]; n=len(a); prev=1; sign=1
    for k in range(n-1):
        z=next((i for i in range(k,n) if a[i][k]),None)
        if z is None:return 0
        if z!=k:a[k],a[z]=a[z],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=a[i][j]*pivot-a[i][k]*a[k][j]
                assert value%prev==0
                a[i][j]=value//prev
            a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

out=[]
for rec in json.loads((P/'gate.json').read_text()):
    p=rec['p']; filename='fiber_patterns.json' if rec['bank']=='paley' else 'orbit2_bank83.json'
    bank=json.loads((P.parent/'quadratic_one_pole_route'/filename).read_text())
    cols=[(i,j) for j in range(6,-1,-1) for i in range(3*(6-j)+3)]
    assert cols==list(map(tuple,rec['columns'])) and len(cols)==84
    rows=[]; conditions=[]
    for index,(x,y) in enumerate(zip(bank['base'],bank['word'])):
        multiplicity=2 if index<7 else 4
        px=[powers_shift(x,i,p) for i in range(21)]
        py=[powers_shift(y,j,p) for j in range(7)]
        for total in range(multiplicity):
            for dx in range(total+1):
                dy=total-dx
                rows.append([(px[i][dx]*py[j][dy])%p if dx<=i and dy<=j else 0 for i,j in cols])
                conditions.append([index,dx,dy])
    assert len(rows)==91 and rows==rec['matrix'] and conditions==rec['conditions']
    selected=rec['pivot_rows'];assert len(set(selected))==84
    determinant=bareiss([rows[i] for i in selected]); residue=determinant%p
    assert residue
    out.append({'bank':rec['bank'],'prime':p,'rows':91,'columns':84,'minor_mod_p':residue,'exact_integer_determinant':str(determinant),'pass':True})
(P/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:v for k,v in r.items() if k!='exact_integer_determinant'} for r in out]))
