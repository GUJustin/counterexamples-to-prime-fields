#!/usr/bin/env python3
import sympy as s,pathlib,json,itertools,time
start=time.monotonic();base=pathlib.Path(__file__).resolve().parent
u,v,z,d=s.symbols('u v z d');env={str(x):x for x in [u,v,z,d]}
j=json.loads((base/'nonfano2_projective.json').read_text());rows=[[s.sympify(q,locals=env) for q in r['primitive_row']] for r in j['rows']]
assert rows[2][0]==-1
r2=[];labels=[]
for i,r in enumerate(rows):
 if i==2:continue
 labels.append(i);r2.append([s.factor(r[k]+r[0]*rows[2][k]) for k in [1,2]])
mins=[]
for i,k in itertools.combinations(range(6),2):
 det=s.factor(r2[i][0]*r2[k][1]-r2[i][1]*r2[k][0]);mins.append({'rows':[labels[i],labels[k]],'determinant':str(det)})
out={'elimination':'a = row2_b*b + row2_c*c; exact since row2_a=-1','rows':[{'old_row':i,'T':j['rows'][i]['T'],'coefficients':[str(q) for q in r]} for i,r in zip(labels,r2)],'minors':mins,'seconds':time.monotonic()-start}
(base/'nonfano2_minors.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
