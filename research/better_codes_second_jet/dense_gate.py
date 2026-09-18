"""Exact sufficient dimension gate for dense total-jet-degree second jets."""
import json
from fractions import Fraction
from pathlib import Path
N=262144; W=131071; A=181275

def layers(m):
    D=m*A
    for ell in range((D-1)//(W-2)+1):
        c=sum(max(D-W*ell+j+2*k,0)
              for k in range(ell+1) for j in range(ell-k+1))
        r=sum((m-3*b)*(ell-b+1)
              for b in range(min(ell,(m-1)//3)+1))
        yield c,r

def main():
    rows=[]
    for m in (4,8,16,32,64,128):
        slope=offset=0; best=None; positive=[]
        for J,(c,r) in enumerate(layers(m)):
            v=c-N*r; slope+=v; offset+=J*v
            at_min=(J+1)*slope-offset
            feasible=at_min>0 or slope>0
            g=dict(m=m,J=J,slope=slope,margin_L_equals_J=at_min,
                   feasible_affine_L=feasible)
            # Normalize by number of coefficient directions for fair diagnostic.
            score=Fraction(slope,(J+1)*(J+2)*(J+3))
            if best is None or score>best[0]:best=(score,g)
            if feasible:positive.append(g)
        rows.append(dict(m=m,tested_J=J+1,positive_count=len(positive),
                         best_normalized_slope=best[1]))
    # Continuum exact rational grid is a diagnostic, not global optimization.
    alpha=Fraction(A,W); q=Fraction(N,W)
    continuum=[]
    for c in (Fraction(1,3),Fraction(1,2),Fraction(3,4),Fraction(9,10),Fraction(1),Fraction(6,5),alpha):
        source=alpha*c**3/6-c**4/8
        rank=c*c/12-c/54+Fraction(1,648)
        continuum.append(dict(c=str(c),normalized_margin=str(source-q*rank)))
    out=dict(n=N,w=W,A=A,finite=rows,continuum=continuum,
       scope='Sufficient rank-bound gate for dense jet degree<=J and total jet+challenge degree<=L, all L>=J. Failure does not prove actual global kernel is zero.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
