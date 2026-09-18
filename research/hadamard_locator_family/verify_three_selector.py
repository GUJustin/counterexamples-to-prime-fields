import sympy as s,json,itertools,time
from pathlib import Path
P=Path(__file__).parent;start=time.monotonic();m=s.symbols('m0:4');h=s.symbols('h0:4');rows=[(1,1,1,1),(1,1,-1,-1),(1,-1,1,-1)];eq=[]
for i,j in [(0,1),(0,2),(1,2)]:
 agree=[k for k in range(4)if rows[i][k]==rows[j][k]];diff=[k for k in range(4)if rows[i][k]!=rows[j][k]]
 def es(cells):
  a,b=cells;return rows[i][a]*m[a]+rows[i][b]*m[b],rows[i][a]*m[a]*h[b]+rows[i][b]*m[b]*h[a]
 e1,e3=es(agree);d1,d3=es(diff);eq.append(s.expand(e1*d3-e3*d1))
M=s.Matrix([[s.diff(v,x)for x in h]for v in eq]);assert M*s.ones(4,1)==s.zeros(3,1);assert M*s.Matrix([m[0],-m[1],-m[2],m[3]])==s.zeros(3,1) or all(s.expand(v)==0 for v in M*s.Matrix([m[0],-m[1],-m[2],m[3]]))
A=m[0]*m[1]*m[2];B=m[0]*m[1]*m[3];C=m[0]*m[2]*m[3];D=m[1]*m[2]*m[3];Ss=[A+B+C+D,A+B-C-D,A-B+C-D];linear=[m[2]+m[3],m[1]+m[3],m[1]-m[2],m[0]-m[3],m[0]+m[2],m[0]+m[1]];mins=[]
for n,pair in enumerate([(0,1),(0,2),(1,2)]):
 vals=[]
 for cc in itertools.combinations(range(4),2):
  v=s.factor(M.extract(pair,cc).det());quot=s.cancel(v/Ss[n]);assert any(s.expand(quot-sg*l)==0 for l in linear for sg in[-1,1]);vals.append(str(quot))
 mins.append(vals)
assert all(s.expand(M.extract(range(3),cc).det())==0 for cc in itertools.combinations(range(4),3))
out={'status':'PASS','matrix':list(map(str,list(M))),'minor_quotients':mins,'seconds':time.monotonic()-start};(P/'verify_three_selector.json').write_text(json.dumps(out,indent=2));print(out)
