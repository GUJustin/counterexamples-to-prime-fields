import sympy as S,json,time
from pathlib import Path
st=time.time();u,w,z=S.symbols('u w z');v=w*z*(1-u)/(w*z+u*(1-w-z));r=(1-w)*(1-z)/(w*z)
K=S.factor((1/(u*z)-1/(v*w))/(1/((1-v)*(1-z))-1/((1-u)*(1-w))))
L=S.factor(K/((1-v)*(1-z))-1/(u*z))
print('k/j',K,'l/j',L,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'v':str(v),'k_over_j':str(K),'l_over_j':str(L),'seconds':time.time()-st},indent=2))
