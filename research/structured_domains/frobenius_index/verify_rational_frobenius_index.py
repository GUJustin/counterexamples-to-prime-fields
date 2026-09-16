"""Finite checks for the Frobenius-index rational-map argument.

These checks support, rather than replace, the function-field proof.
All arithmetic is exact. No native proving system is exercised.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def determinant(matrix,p):
    rows=[list(row) for row in matrix];answer=1
    for column in range(len(rows)):
        pivot=next((i for i in range(column,len(rows)) if rows[i][column]%p),None)
        if pivot is None:return 0
        if pivot!=column:rows[pivot],rows[column]=rows[column],rows[pivot];answer=-answer
        value=rows[column][column]%p;answer=answer*value%p;inverse=pow(value,-1,p)
        for i in range(column+1,len(rows)):
            multiplier=rows[i][column]*inverse%p
            for j in range(column,len(rows)):rows[i][j]=(rows[i][j]-multiplier*rows[column][j])%p
    return answer%p


class Series:
    def __init__(self,p,length=9):self.p=p;self.length=length
    def constant(self,value):return [value%self.p]+[0]*(self.length-1)
    def add(self,a,b):return [(x+y)%self.p for x,y in zip(a,b)]
    def neg(self,a):return [-x%self.p for x in a]
    def scale(self,a,c):return [x*c%self.p for x in a]
    def mul(self,a,b):
        return [sum(a[j]*b[i-j] for j in range(i+1))%self.p for i in range(self.length)]
    def inverse(self,a):
        p=self.p;out=[pow(a[0],-1,p)]
        for i in range(1,self.length):out.append(-out[0]*sum(a[j]*out[i-j] for j in range(1,i+1))%p)
        assert self.mul(a,out)==self.constant(1)
        return out
    def power(self,a,e):
        out=self.constant(1)
        while e:
            if e&1:out=self.mul(out,a)
            a=self.mul(a,a);e//=2
        return out


def wronskian_fixture(p,n,ell,epsilon):
    assert p==ell*n+epsilon and ell>=6 and 2*ell*3<p
    # R(X)=X^3+X has non-diagonal collision component
    # x^2+x*y+y^2+1=0, a nonsingular rational conic when p>3.
    x0,y0=next((x,y) for x in range(p) for y in range(p)
               if (x*x+x*y+y*y+1)%p==0)
    ring=Series(p);one=ring.constant(1);certificates=[]
    for center in range(p):
        parameter=ring.constant(center);parameter[1]=1
        denominator=ring.add(ring.add(one,parameter),ring.mul(parameter,parameter))
        if not denominator[0]:continue
        numerator=ring.add(ring.constant(2*x0+y0),ring.scale(parameter,x0+2*y0))
        offset=ring.neg(ring.mul(numerator,ring.inverse(denominator)))
        x=ring.add(ring.constant(x0),offset)
        y=ring.add(ring.constant(y0),ring.mul(parameter,offset))
        if not x[0] or not y[0]:continue
        assert ring.add(ring.add(ring.mul(x,x),ring.mul(x,y)),ring.add(ring.mul(y,y),one))==ring.constant(0)
        assert ring.add(ring.power(x,3),x)==ring.add(ring.power(y,3),y)
        u=ring.power(x,n);v=ring.power(y,n)
        # Frobenius is constant through jet order8<p.
        assert ring.power(x,p)==ring.constant(x[0]) and ring.power(y,p)==ring.constant(y[0])
        xepsilon=ring.mul(ring.constant(x[0]),ring.inverse(ring.power(u,ell)))
        yepsilon=ring.mul(ring.constant(y[0]),ring.inverse(ring.power(v,ell)))
        assert xepsilon==(x if epsilon==1 else ring.inverse(x))
        assert yepsilon==(y if epsilon==1 else ring.inverse(y))
        vminus=ring.add(v,ring.constant(-1))
        if not vminus[0]:continue
        functions=[ring.mul(ring.add(u,ring.constant(-1)),ring.inverse(vminus))]
        functions += [ring.mul(ring.power(u,r),ring.power(v,s)) for r in range(2) for s in range(4)]
        value=determinant([[function[j] for function in functions] for j in range(9)],p)
        three=determinant([[function[j] for function in (functions[0],one,u)] for j in range(3)],p)
        if value and three:
            certificates.append(dict(parameter=center,three_function_jet_determinant=three,
                                     additional_nine_function_jet_determinant=value))
            if len(certificates)==3:break
    assert len(certificates)==3
    # The torus exception u=v makes the first function the constant1,
    # which duplicates the r=s=0 column.
    torus=[one]+[ring.power(u,r+s) for r in range(2) for s in range(4)]
    assert determinant([[function[j] for function in torus] for j in range(9)],p)==0
    return dict(p=p,n=n,index=ell,epsilon=epsilon,conic_point=[x0,y0],
                nonzero_wronskians=certificates,
                torus_exception_has_zero_wronskian=True)


def poly_value(coefficients,x,p):
    result=0
    for c in reversed(coefficients):result=(result*x+c)%p
    return result


def deck_fixture(p,ell,A,V):
    assert (p-1)%ell==0 and ell>=6
    B=max(len(A),len(V))-1;degree=ell*B
    assert 2*degree<p
    # Evaluate F=R(X^ell) on P1(Fp), using p as the infinity symbol.
    def rational(z):
        if z==p:
            if len(A)>len(V):return p
            if len(A)<len(V):return 0
            return A[-1]*pow(V[-1],-1,p)%p
        a,b=poly_value(A,z,p),poly_value(V,z,p)
        assert a or b
        return a*pow(b,-1,p)%p if b else p
    values=[rational(pow(x,ell,p)) for x in range(p)]+[rational(p)]
    inverses=[0]+[pow(x,-1,p) for x in range(1,p)]
    checked=0;decks=[]
    def consider(a,b,c,d):
        nonlocal checked
        checked+=1
        # A nonzero cross-multiplied identity has degree at most2*degree.
        # Testing all p+1 projective points therefore certifies identity.
        for x in [p,0,1]+list(range(2,p)):
            numerator,denominator=(a,c) if x==p else ((a*x+b)%p,(c*x+d)%p)
            image=numerator*inverses[denominator]%p if denominator else p
            if values[image]!=values[x]:return
        assert (b==c==0) or (a==d==0)
        decks.append([a,b,c,d])
    # Unique projective representatives: c=1, or c=0,d=1.
    for a in range(p):
        for d in range(p):
            for b in range(p):
                if (a*d-b)%p:consider(a,b,1,d)
    for a in range(1,p):
        for b in range(p):consider(a,b,0,1)
    assert checked==p*(p*p-1)
    scalings=[a for a in range(1,p) if pow(a,ell,p)==1]
    assert len(scalings)==ell
    assert all([a,0,0,1] in decks for a in scalings)
    # Replacing X^ell by X^-ell conjugates every deck map by inversion;
    # the tested normalizer is closed under this conjugation.
    return dict(p=p,index=ell,rational_numerator=A,rational_denominator=V,
                composed_degree=degree,projective_maps_checked=checked,
                deck_maps=decks,all_decks_preserve_zero_infinity=True,
                reciprocal_composition_follows_by_inversion_conjugacy=True)


def main():
    p,n=2130706433,262144;ell=(p-1)//n
    assert p==ell*n+1 and ell==8128
    maximum=(n-1)//6+1
    assert maximum==43691 and n>6*(32768-1) and not n>6*(65536-1)
    arithmetic=0
    for B in range(2,maximum+1):
        assert n>6*(B-1) and 2*ell*B<p and ell*B<p
        for a in {1,B-1}:
            assert 6*a*a<n*a
            arithmetic+=1
    wronskians=[wronskian_fixture(*row) for row in
                ((127,21,6,1),(131,22,6,-1),(193,32,6,1),(191,32,6,-1))]
    decks=[deck_fixture(*row) for row in
           ((31,6,[0,0,1],[1]),(31,6,[1,0,1],[0,1]),
            (43,7,[1,1,0,1],[2,1]),(61,6,[1,1,0,0,1],[2,1]))]
    result=dict(status='passed',pinned_p=p,pinned_n=n,pinned_index=ell,
                sufficient_maximum_integer_degree=maximum,largest_covered_dyadic_degree=32768,
                degree65536_not_covered=True,unclassified_dyadic_maximum_fiber_unions=16,
                exact_inequality_checks=arithmetic,
                wronskian_fixtures=wronskians,deck_group_fixtures=decks,
                scope='Finite algebraic checks supporting the Frobenius-index proof; no score improvement.')
    Path(__file__).with_name('rational_frobenius_index_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
