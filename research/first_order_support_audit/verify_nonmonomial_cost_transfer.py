"""Check the degree-preserving degeneration used in the cost converse.

These finite matrix checks corroborate, but do not replace, the flat-limit
argument for all translation-stable spaces.
"""
from itertools import product
from math import comb
from pathlib import Path
import json

P=1009

def echelon(rows,key):
    basis={}
    for original in rows:
        row={x:c%P for x,c in original.items() if c%P}
        while row:
            pivot=max(row,key=key)
            if pivot not in basis:
                inv=pow(row[pivot],-1,P)
                basis[pivot]={x:c*inv%P for x,c in row.items()}
                break
            scale=row[pivot]
            for x,c in basis[pivot].items():
                value=(row.get(x,0)-scale*c)%P
                if value:row[x]=value
                else:row.pop(x,None)
    return basis

def rank(polys,m):
    cols=[]
    for poly in polys:
        for x in range(m):
            col={}
            for (u,b),c in poly.items():
                for j in range(u+1):
                    i=x+u-j
                    if i+2*j>=m:continue
                    row=(i,j,b+u-j)
                    col[row]=(col.get(row,0)+c*comb(u,j))%P
            cols.append(col)
    return len(echelon(cols,lambda x:x))

def main():
    checks=0; strict=0; nonlinear=0
    # Images under Y0 -> Y0+cY1^d and Y1 -> Y1+z are still
    # Y0-translation-stable, but need not be homogeneous or monomial.
    for H in product(range(1,4),repeat=2):
        for c,d,z in product((1,2),(1,2),(0,1)):
            polys=[]
            for b,h in enumerate(H):
                for u in range(h):
                    poly={}
                    for j in range(u+1):
                        power=d*(u-j)+b
                        for t in range(power+1):
                            coeff=comb(u,j)*c**(u-j)*comb(power,t)*z**(power-t)
                            poly[(j,t)]=(poly.get((j,t),0)+coeff)%P
                    polys.append({x:v for x,v in poly.items() if v})
            pivots=echelon(polys,lambda ub:(sum(ub),-ub[1]))
            S=set(pivots)
            assert len(S)==len(polys)
            assert all(u==0 or (u-1,b) in S for u,b in S)
            umax=max(u for f in polys for u,b in f)
            bmax=max(b for f in polys for u,b in f)
            assert max(u for u,b in S)<=umax
            assert max(b for u,b in S)<=bmax
            # Filtration degrees are those of the adapted echelon basis.
            assert sorted(map(sum,S))==sorted(max(map(sum,f)) for f in pivots.values())
            for m in range(1,8):
                r=rank(polys,m);r0=rank([{ub:1} for ub in S],m)
                assert r0<=r
                strict+=r0<r
                checks+=1
            nonlinear+=d==2
    report=dict(status='passed',matrix_comparisons=checks,strict_rank_drops=strict,nonlinear_shear_spaces=nonlinear,characteristic=P,scope='Degree bounds and saturated-rank domination under filtered monomial degeneration; finite corroboration, not an intrinsic list lower bound.')
    Path(__file__).with_name('nonmonomial_cost_transfer_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
