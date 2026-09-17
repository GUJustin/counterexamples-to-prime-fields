import ast,json
from pathlib import Path
p=Path(__file__).with_name('continuum.py'); tree=ast.parse(p.read_text());keep=[]
for x in tree.body:
 if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef)):keep.append(x)
 elif isinstance(x,ast.Assign) and all(isinstance(t,ast.Name) and t.id!='rows' for t in x.targets):keep.append(x)
exec(compile(ast.Module(body=keep,type_ignores=[]),str(p),'exec'))
def f(l,s,t=3261):
 l=F(str(round(l,8)));s=F(str(round(s,12)));return float(gap(l,s)-thin(l,s,t=t))
def opt(t):
 l=70.;s=.3098
 for it in range(6):
  a=.05;b=.00005;f0=f(l,s,t);fp=f(l+a,s,t);fm=f(l-a,s,t);sp=f(l,s+b,t);sm=f(l,s-b,t)
  gl=(fp-fm)/(2*a);gs=(sp-sm)/(2*b);hl=(fp-2*f0+fm)/(a*a);hs=(sp-2*f0+sm)/(b*b);hx=(f(l+a,s+b,t)-fp-sp+f0)/(a*b);det=hl*hs-hx*hx
  dl=(-hs*gl+hx*gs)/det;ds=(hx*gl-hl*gs)/det;l+=dl;s+=ds
  if abs(dl)<1e-5 and abs(ds)<1e-7:break
 return dict(t=t,lambda_ratio=l,sigma=s,margin=f(l,s,t))
local=[opt(t) for t in [3261,3250,3240,3230,3220,3005]]
def slope(s):return f(201,s)-f(200,s)
s=.305
for i in range(5):
 e=.00001;c=slope(s);l=slope(s-e);r=slope(s+e);s-=((r-l)/(2*e))/((r-2*c+l)/(e*e))
large=[]
for sig in [.304,.304785714,.305,.306,s]:
 aa=slope(sig);bb=f(200,sig)-200*aa;bt=f(200,sig,3262)-f(200,sig,3261)
 large.append(dict(sigma=sig,lambda_coefficient=aa,constant_at_t3261=bb,total_degree_coefficient=bt,continuum_total_threshold_lambda260=3261-f(260,sig)/bt,lambda_needed_t3005=(256*bt-bb)/aa if aa>0 else None))
for name,rows in [('stationary_diagnostic',local),('high_lambda_diagnostic',large)]:
 out=dict(scope='Correct w versus w−1 weights; continuum diagnostics, not finite certificates or global bounds',rows=rows)
 p.with_name(name+'.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(local=local,large=large),indent=2))
