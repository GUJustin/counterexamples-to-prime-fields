from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
import sympy as s
xs=s.symbols('a b c d');X=s.symbols('X')
def elementary(j):
    return sum(s.prod(t) for t in combinations(xs,j))
e1,e2,e3,e4=[elementary(j) for j in range(1,5)]
D=e1*e4-e3*X
N=e1*X**3+(e3-e1*e2)*X**2+(e2*e3-e1*e4)*X-e3*e4
for i,a in enumerate(xs):
    others=[v for j,v in enumerate(xs) if j!=i]
    assert s.expand(a*a*N-D*(X*X+a**4)-s.prod(a+v for v in others)*s.prod(X-a*v for v in others))==0
vals=[Q(1),Q(2),Q(5),Q(13)]
es=[sum((__import__('functools').reduce(lambda a,b:a*b,t,Q(1)) for t in combinations(vals,j)),Q(0)) for j in range(1,5)]
E1,E2,E3,E4=es
pole=E1*E4/E3
num=lambda x:E1*x**3+(E3-E1*E2)*x**2+(E2*E3-E1*E4)*x-E3*E4
den=lambda x:E1*E4-E3*x
nodes=[sgn*vals[i]*vals[j] for i,j in combinations(range(4),2) for sgn in (1,-1)]
assert len(set(nodes))==12 and pole not in nodes and num(pole)!=0
matches=[]
for i,j in combinations(range(4),2):
    for sgn in (1,-1):
        x=sgn*vals[i]*vals[j]
        if num(x)==den(x)*(vals[i]**2+vals[j]**2):matches.append(str(x))
assert len(matches)==6 and set(matches)=={str(vals[i]*vals[j]) for i,j in combinations(range(4),2)}
out={'symbolic_identities_passed':4,'parameters':[str(v) for v in vals],'elementary':[str(v) for v in es],'pole':str(pole),'numerator_at_pole':str(num(pole)),'matches':matches,'proper':True,'distinct_domain':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
