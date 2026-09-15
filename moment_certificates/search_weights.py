"""Numerical discovery, followed by exact integer certificate evaluation."""
from pathlib import Path
from math import gcd
from functools import reduce
import json
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csr_matrix, eye, hstack

root=Path(__file__).parent
record=json.loads((root/'exact_moments.json').read_text())
prior=json.loads((root.parent/'checks/conditional_moment_results.json').read_text())
row=next(r for r in prior['certificate']['first_moment_classes'] if r['first_moment']==record['q'])
center=record['center']
low,high=row['second_min'],row['second_max']
integers=list(range(low-center,high-center+1))
scale=1000
C=record['raw_moments'][0]
out=[]
for degree in range(2,record['degree']+1,2):
    powers=np.array([[float(x/scale)**j for j in range(degree+1)] for x in integers])
    expected=np.array([record['centered_moments'][j]/C/scale**j for j in range(degree+1)])
    A=hstack([csr_matrix(powers),-eye(len(integers),format='csr')],format='csr')
    result=linprog(np.r_[np.zeros(degree+1),np.ones(len(integers))],
        A_ub=A,b_ub=np.zeros(len(integers)),
        A_eq=csr_matrix(np.r_[expected,np.zeros(len(integers))].reshape(1,-1)),
        b_eq=[1.0],bounds=[(None,None)]*(degree+1)+[(0,None)]*len(integers),
        method='highs')
    if not result.success:
        print(degree,result.message,flush=True)
        continue
    # Any integer polynomial works in the certificate inequality. Rounding
    # can weaken its score, but cannot compromise exact validity.
    coeff=[int(round(v*10**10))*scale**(degree-j) for j,v in enumerate(result.x[:degree+1])]
    common=reduce(gcd,coeff)
    coeff=[x//common for x in coeff]
    def evaluate(x):
        value=0
        for a in reversed(coeff):
            value=value*x+a
        return value
    numerator=sum(c*m for c,m in zip(coeff,record['centered_moments']))
    denominator=sum(max(0,evaluate(x)) for x in integers)
    assert numerator>0 and denominator>0
    bound=(numerator+denominator-1)//denominator
    item=dict(degree=degree,center=center,low=low,high=high,coefficients_ascending=coeff,
              numerator=numerator,denominator=denominator,list_lower_bound=bound,
              numerical_search_bound=C/result.fun)
    roots=np.polynomial.polynomial.polyroots(result.x[:degree+1])
    if all(abs(z.imag)<1e-5 for z in roots):
        integer_roots=sorted(int(round(z.real*scale)) for z in roots)
        factored=[1 if coeff[-1]>0 else -1]
        for zero in integer_roots:
            new=[0]*(len(factored)+1)
            for j,a in enumerate(factored):
                new[j]-=zero*a
                new[j+1]+=a
            factored=new
        n2=sum(a*m for a,m in zip(factored,record['centered_moments']))
        d2=sum(max(0,(1 if coeff[-1]>0 else -1)*__import__('math').prod(x-z for z in integer_roots)) for x in integers)
        if n2>0 and d2>0:
            item['factored']=dict(roots=integer_roots,leading_coefficient=factored[-1],
                coefficients_ascending=factored,numerator=n2,denominator=d2,
                list_lower_bound=(n2+d2-1)//d2)
    out.append(item)
    print(json.dumps(item),flush=True)
(root/'weight_certificates.json').write_text(json.dumps(out,indent=2)+'\n')
