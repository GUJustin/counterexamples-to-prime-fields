"""Three norm selectors already force colliding old edge squares."""
import sympy as s,json,itertools
from pathlib import Path
base=Path(__file__).parent
m=s.symbols('m0:4');h=s.symbols('h0:4');H,K=s.symbols('H K');loc={str(x):x for x in m}
d=json.loads((base/'paired_root_gate.json').read_text());rows=[0,1,3]
M=s.Matrix([[s.sympify(v,locals=loc) for v in d['matrix'][i]] for i in rows])
v=s.Matrix([m[0],-m[1],-m[2],m[3]])
assert M*s.ones(4,1)==s.zeros(3,1)
assert s.simplify(M*v)==s.zeros(3,1)
assert all(s.expand(M[:,cc].det())==0 for cc in itertools.combinations(range(4),3))
minor=[]
for rr in itertools.combinations(range(3),2):
 for cc in itertools.combinations(range(4),2):
  minor.append({'rows':rr,'columns':cc,'determinant':str(s.factor(M[list(rr),list(cc)].det()))})
sgn=d['selector_group_signs'][:3]
edge=[]
for i,j in itertools.combinations(range(3),2):
 E=[g for g in range(4) if sgn[i][g]==sgn[j][g]]
 a,b=E
 e1=2*(sgn[i][a]*m[a]+sgn[i][b]*m[b])
 e3=2*(sgn[i][a]*m[a]*(H+K*v[b])+sgn[i][b]*m[b]*(H+K*v[a]))
 assert s.expand(e3-H*e1)==0
 edge.append({'pair':[i,j],'E1':str(e1),'E3_after_kernel_substitution':str(s.factor(e3)),'edge_square':'-H'})
(base/'three_selector_gate.json').write_text(json.dumps({'matrix':[[str(x) for x in row] for row in M.tolist()],'kernel':['(1,1,1,1)','(m0,-m1,-m2,m3)'],'maximal_minors_zero':True,'two_by_two_minors':minor,'edge_identities':edge},indent=2))
print('All kernel, rank-upper-bound, 18 minor, and three edge identities verified.')
