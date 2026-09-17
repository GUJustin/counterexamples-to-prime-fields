"""Check smaller certificates by independent diagonal rank sums."""
from fractions import Fraction as F
from pathlib import Path
import json
from verify import cert


def sum_linear(lo,hi,slope,intercept):
    if hi<lo:return 0
    return slope*(lo+hi)*(hi-lo+1)//2+intercept*(hi-lo+1)


def diagonal_rank(q,k,m):
    # Before ell=q, active columns rise as ell-q+k; afterward they equal k.
    lo=max(0,q-k+1); hi=min(q-1,m-1)
    split=(m+q-k)//2
    first=sum_linear(lo,min(hi,split),1,k-q)
    first+=sum_linear(max(lo,split+1),hi,-1,m)
    lo=max(q,0);hi=m-1;split=m-k
    return first+sum_linear(lo,min(hi,split),0,k)+sum_linear(max(lo,split+1),hi,-1,m)


def main():
    checks=0
    for m in range(1,31):
        for q in range(2*m+1):
            for k in range(q+2):
                direct=sum(min(max(0,min(k,ell-q+k)),m-ell) for ell in range(m))
                assert diagonal_rank(q,k,m)==direct
                checks+=1
    out=[]
    for rho,a,m,B in [(F(9,10),F(47389,50000),4096,F(49,500)),(F(3,4),F(43049,50000),65536,F(173,1000))]:
        result=cert(rho,a,m,B)
        cap=(m*B).__floor__()+1
        qmax=(m*a/rho).__ceil__()-1
        rank=0;count=0;benefit=F(0)
        for q in range(qmax+1):
            length=max(0,min(q+1,cap,(2*m*a-m-(2*rho-1)*q).__floor__()+1))
            rank+=diagonal_rank(q,length,m)
            count+=length;benefit+=length*(m*a-rho*q)
        assert rank==result['rank'] and count==result['monomials'] and str(benefit)==result['benefit']
        out.append(result)
    report=dict(status='passed',direct_diagonal_formula_checks=checks,certificates=out,scope='Column certificates independently recounted by homogeneous diagonal ranks. No finite-support global optimality or practical parameter improvement is claimed.')
    Path(__file__).with_name('smaller_certificates_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
