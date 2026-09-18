"""Exact classification of QR+{0} / QR-or-NQR cyclic two-orbit ansatz.
Uses cyclotomic integer multiplication to recover period polynomials, then
univariate gcds over the quadratic period field. No parameter sampling.
"""
import argparse,json,time
import sympy as s

def period(q):
    qr={i*i%q for i in range(1,q)}
    # coefficient vectors in Z[Z]/(1+Z+...+Z^(q-1))
    def mulroot(v,j):
        a=[0]*q
        for i,c in enumerate(v): a[(i+j)%q]+=c
        return [a[i]-a[q-1] for i in range(q-1)]
    coeff=[[1]+[0]*(q-2)]
    for j in sorted(qr):
        out=[[0]*(q-1) for _ in range(len(coeff)+1)]
        for k,v in enumerate(coeff):
            vj=mulroot(v,j)
            for i in range(q-1):
                out[k][i]-=vj[i];out[k+1][i]+=v[i]
        coeff=out
    pairs=[]
    for v in coeff:
        a=v[0];b=v[1]
        assert all(v[i]==(b if i in qr else 0) for i in range(1,q-1))
        pairs.append((a,b))
    return pairs

def run(q):
    X,T=s.symbols('X T'); eta=(-1+s.sqrt(-q))/2
    K=s.QQ.algebraic_field(s.sqrt(-q))
    pairs=period(q)
    A=s.Poly(sum((a+b*eta)*X**i for i,(a,b) in enumerate(pairs)),X,domain=K)
    An=s.Poly(sum((a+b*(-1-eta))*X**i for i,(a,b) in enumerate(pairs)),X,domain=K)
    assert A*An==s.Poly(sum(X**i for i in range(q)),X,domain=K)
    r=(q-1)//2; modulus=A*s.Poly(X-1,X,domain=K)
    rows=[]
    for h in range(r+1,q):
        P=s.rem(s.Poly(X**h,X,domain=K),modulus)
        for name,B in [('QR',A),('NQR',An)]:
            powers=[s.rem(s.Poly(X**j,X,domain=K),B) for j in range(q)]
            v=[powers[h].nth(i) for i in range(r)]
            R=[s.Poly(sum(P.nth(j)*powers[j].nth(i)*T**j for j in range(r+1)),T,domain=K) for i in range(r)]
            pivot=next(i for i,x in enumerate(v) if x!=0)
            polys=[R[i].mul_ground(v[pivot])-R[pivot].mul_ground(v[i]) for i in range(r) if i!=pivot]
            G=s.Poly(0,T,domain=K)
            for f in polys: G=s.gcd(G,f)
            # Remove precisely alpha=0 and equal-orbit roots alpha^q=1.
            raw=G.monic();valid=raw
            forbidden=s.Poly(T*(T**q-1),T,domain=K)
            while valid.degree()>0:
                d=s.gcd(valid,forbidden)
                if d.degree()==0:break
                valid=s.exquo(valid,d)
            rows.append({'h':h,'target':name,'P':str(P.as_expr()),'raw_gcd':str(raw.as_expr()),'valid_gcd':str(valid.monic().as_expr()),'valid_degree':int(valid.degree())})
    return {'q':q,'period_pairs':pairs,'rows':rows}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('q',type=int);ap.add_argument('--output',required=True);a=ap.parse_args()
    t=time.time();out=run(a.q);out['elapsed']=time.time()-t
    with open(a.output,'w') as f:json.dump(out,f,indent=2)
    print(json.dumps({'q':a.q,'elapsed':out['elapsed'],'survivors':[(x['h'],x['target'],x['valid_gcd']) for x in out['rows'] if x['valid_degree']>0]}))
