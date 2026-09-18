import sympy as s,json,time
from pathlib import Path
start=time.monotonic();Pth=Path(__file__).with_suffix('.json');b,c,q,h,t,P,k=s.symbols('b c q h t P k');base={(0,1):s.Integer(1),(0,2):b,(0,3):c,(1,2):q/c,(1,3):q/b,(2,3):q};x=lambda i,j:base[tuple(sorted((i,j)))]+h;beta=[0,q-b*c,q-c,q-b];v=[0]+[s.factor(beta[i]*(sum(beta)-2*beta[i]))for i in range(1,4)];a=[1]+[1+t*v[i]for i in range(1,4)];out={}
def save():out['seconds']=time.monotonic()-start;Pth.write_text(json.dumps(out,indent=2))
def H(i,j):return (a[i]*s.prod(x(i,l)for l in range(4)if l not in(i,j))-a[j]*s.prod(x(j,l)for l in range(4)if l not in(i,j)))/(a[i]-a[j])
E=[s.factor(s.cancel((H(0,i)-H(*[j for j in range(1,4)if j!=i]))*t))for i in range(1,4)];out['H_times_t']=list(map(str,E));save();num=s.fraction(E[0])[0];tt=s.factor(-num.subs(t,0)/s.diff(num,t));out['t_solution']=str(tt);aa=[s.factor(z.subs(t,tt))if hasattr(z,'subs')else z for z in a];out['leading']=list(map(str,aa));out['H_consistent']=[s.cancel(e.subs(t,tt))==0 for e in E];save();assert all(out['H_consistent'])
G=[]
for i in range(1,4):
 j,l=[j for j in range(1,4)if j!=i];G.append(s.factor(aa[i]*(P+x(i,j)-h)*(P+x(i,l)-h)-(P+x(0,j)-h)*(P+x(0,l)-h)-k*(P-h)*beta[i]))
out['all_plus']=list(map(str,G));save();elim=[s.factor(s.cancel(G[i]*beta[1]-G[0]*beta[i+1]))for i in range(1,3)];out['eliminate_k']=list(map(str,elim));save();print(json.dumps(out,indent=2))
