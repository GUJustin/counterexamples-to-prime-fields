exec(open(__file__.replace('orbit7_factor_audit.py','orbit7_fixed.py')).read().split('quad=[]')[0])
def key(f):
 pp=S.Poly(f,a,b,c);v=[pp.coeff_monomial(t) for t in amp];i=next((z for z in v if z),None)
 return tuple(S.cancel(z/i) for z in v) if i else None
bad={}
for i,j in itertools.combinations(range(1,8),2):
 d=Ps[i-1]-Ps[j-1]
 bad.setdefault(key(S.Poly(d,X).coeff_monomial(X**3)),[]).append(('degree_drop',i,j))
 for k,bn in enumerate(bs):
  # Every pair not both selected at this b is forbidden to agree here.
  if i in C[k] or j in C[k]:
   val=S.expand(d.subs(X,bn))
   if val:bad.setdefault(key(val),[]).append(('extra_at_b',i,j,k))
records=[]
for i,j,k in T:
 f=lin[min(i,j),max(i,j)];g=lin[min(i,k),max(i,k)]
 det=S.factor(f.coeff_monomial(X)*g.coeff_monomial(1)-g.coeff_monomial(X)*f.coeff_monomial(1))
 rec={'triple':[i,j,k],'factors':[]}
 for fac,e in S.factor_list(det)[1]:rec['factors'].append({'factor':str(fac),'forbidden':bad.get(key(fac),[])})
 records.append(rec)
print(json.dumps(records,indent=2))
(root/'orbit7_factor_audit.json').write_text(json.dumps(records,indent=2)+'\n')
