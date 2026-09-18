#!/usr/bin/env python3
import sympy as s, json, pathlib, time, itertools, sys
base=pathlib.Path(__file__).resolve().parent; start=time.monotonic()
orb=int(sys.argv[1]) if len(sys.argv)>1 else 0
entry=[json.loads(l) for l in (base/'design_orbits.jsonl').read_text().splitlines()][orb]
x=s.Symbol('X'); amps=s.symbols('a b c'); u,v,z,d=s.symbols('u v z d'); nodes=[u,v,z,-u,-v,-z,d]
if orb==3:nodes=[u,-u,d,v,z,-v,-z]
if orb==2:nodes=[s.Integer(0),s.Integer(1),s.Integer(-1),u,v,z,d]
P={}
for i in range(1,8):
    roots=[nodes[j] for j,C in enumerate(entry['C']) if i not in C]
    e=[s.Integer(1)]+[s.expand(sum(s.prod(c) for c in itertools.combinations(roots,h))) for h in range(1,5)]
    e1,e2,e3,e4=e[1:]; a,b,c=amps
    co=[-e4*(a+b*e1+c*(e1**2-e2)),a*e3+b*(e1*e3-e4)+c*((e1**2-e2)*e3-e1*e4),-a*e2+b*(-e1*e2+e3)+c*(-e1**2*e2+e2**2+e1*e3-e4),a*e1+b*(e1**2-e2)+c*(e1**3-2*e1*e2+e3)]
    P[i]=s.Poly(sum(co[h]*x**h for h in range(4)),x).as_expr().expand()
def qr(i,j):return set(h for h,C in enumerate(entry['C']) if i not in C and j not in C)
rows=[]; meta=[]
for T in entry['T']:
    if orb!=2 and T==([1,5,6] if orb==3 else [3,4,5]):continue
    common=set.intersection(*(qr(i,j) for i,j in itertools.combinations(T,2)))
    if common:
        assert len(common)==1
        i,j,k=T; h=next(iter(common))
        aa=nodes[next(iter(qr(i,j)-common))];bb=nodes[next(iter(qr(i,k)-common))];cc=nodes[next(iter(qr(j,k)-common))]
        U=(cc-bb)*(x-aa);V=(cc-aa)*(x-bb)
        A=s.div(P[i]-P[j],x-nodes[h],x)[0];B=s.div(P[i]-P[k],x-nodes[h],x)[0]
    else:
        i,j=next((i,j) for i,j in itertools.combinations(T,2) if len(qr(i,j))==1)
        k=next(k for k in T if k not in [i,j]); aa=nodes[next(iter(qr(i,j)))]
        VV=s.prod(x-nodes[h] for h in qr(i,k));WW=s.prod(x-nodes[h] for h in qr(j,k))
        U=s.expand(WW.subs(x,aa)*VV-VV.subs(x,aa)*WW);V=s.expand(WW.subs(x,aa)*VV)
        A=P[i]-P[j]; B=P[i]-P[k]
    cross=s.Poly(s.expand(A*V-B*U),x)
    coeff=next(cc for cc in cross.all_coeffs() if cc!=0)
    row=[s.expand(coeff).coeff(a) for a in amps]
    gcd=s.factor(s.gcd_list(row)); pr=[s.factor(rr/gcd) for rr in row]
    rows.append(pr)
    meta.append({'T':T,'chosen_x_degree':int(cross.degree()),'row_content':str(gcd),'primitive_row':[str(rr) for rr in pr]})
minors=[]
for inds in ([] if '--rows-only' in sys.argv else itertools.combinations(range(len(rows)),3)):
    det=s.factor(s.det(s.Matrix([rows[i] for i in inds])))
    minors.append({'rows':inds,'determinant':str(det)})
out={'orbit':orb,'nodes':[str(n) for n in nodes],'row_content_requires_nonzero_guard':True,'rows':meta,'minors':minors,'seconds':time.monotonic()-start}
(base/f'nonfano_involution_{orb}.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
