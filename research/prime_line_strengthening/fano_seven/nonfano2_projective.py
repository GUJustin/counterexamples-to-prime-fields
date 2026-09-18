#!/usr/bin/env python3
import sympy as s,json,pathlib,itertools,time,sys
start=time.monotonic();base=pathlib.Path(__file__).resolve().parent
entry=[json.loads(l) for l in (base/'design_orbits.jsonl').read_text().splitlines()][2]
x=s.Symbol('X');amps=s.symbols('a b c');a,b,c=amps;u,v,z,d=s.symbols('u v z d'); nodes=[None,s.Integer(0),s.Integer(1),u,v,z,d]
W=a*x**3+b*x**4+c*x**5;P={}
for i in range(1,8):
    roots=[nodes[j] for j,C in enumerate(entry['C']) if i not in C and j!=0]
    L=s.expand(s.prod(x-t for t in roots));P[i]=s.rem(W,L,x).expand()
    assert s.degree(P[i],x)<= (3 if i in entry['C'][0] else 2)
def qr(i,j):return set(h for h,C in enumerate(entry['C']) if i not in C and j not in C)
def loc(indices):return s.prod(x-nodes[h] for h in indices if h!=0)
def ev2(f,h):return s.Poly(f,x).coeff_monomial(x**2) if h==0 else f.subs(x,nodes[h])
rows=[];meta=[]
for T in entry['T']:
    common=set.intersection(*(qr(i,j) for i,j in itertools.combinations(T,2)))
    if common:
        assert len(common)==1 and 0 not in common
        i,j,k=T;h=next(iter(common))
        ai=next(iter(qr(i,j)-common));bi=next(iter(qr(i,k)-common));ci=next(iter(qr(j,k)-common))
        LA=loc({ai});LB=loc({bi})
        eva=lambda f: s.Poly(f,x).coeff_monomial(x) if ci==0 else f.subs(x,nodes[ci])
        U=eva(LB)*LA;V=eva(LA)*LB
        A=s.div(P[i]-P[j],x-nodes[h],x)[0];B=s.div(P[i]-P[k],x-nodes[h],x)[0]
    else:
        i,j=next((i,j) for i,j in itertools.combinations(T,2) if len(qr(i,j))==1)
        k=next(k for k in T if k not in [i,j]);ai=next(iter(qr(i,j)))
        V0=loc(qr(i,k));W0=loc(qr(j,k));U=s.expand(ev2(W0,ai)*V0-ev2(V0,ai)*W0);V=s.expand(ev2(W0,ai)*V0)
        A=P[i]-P[j];B=P[i]-P[k]
    cross=s.Poly(s.expand(A*V-B*U),x);coeff=next(cc for cc in cross.all_coeffs() if cc!=0)
    row=[s.expand(coeff).coeff(amp) for amp in amps]; gcd=s.factor(s.gcd_list(row));pr=[s.factor(rr/gcd) for rr in row]
    rows.append(pr);meta.append({'T':T,'x_degree':int(cross.degree()),'row_content':str(gcd),'primitive_row':[str(rr) for rr in pr]})
minors=[]
if '--minors' in sys.argv:
 for inds in itertools.combinations(range(7),3):
    det=s.factor(s.det(s.Matrix([rows[i] for i in inds])));minors.append({'rows':inds,'determinant':str(det)})
out={'nodes':['infinity']+[str(t) for t in nodes[1:]],'row_division_requires_content_guards':True,'rows':meta,'minors':minors,'seconds':time.monotonic()-start}
(base/'nonfano2_projective.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
