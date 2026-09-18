import sympy as S,json,time
from pathlib import Path
st=time.time();u,w,z,K=S.symbols('u w z K');s=w+z-1;v=w*z*(1-u)/(w*z+u*(1-w-z));KG=(u-w)*(w-1)*(z-1)**2/(w*w*z*(z-u));data=json.loads(Path(__file__).with_name('orbit6_quotients.json').read_text());out={}
for kind,sub in [('generic',{K:KG}),('exceptional',{u:w/s})]:
 arr=[]
 for item in data['determinants']:
  f=S.factor(S.cancel(S.sympify(item).subs(sub)));arr.append(str(f));print(kind,f,flush=True)
 out[kind]=arr
out['seconds']=time.time()-st;Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
