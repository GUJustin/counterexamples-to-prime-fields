"""Exact witness audit in Q[q]/(q^4-q^2+1), using only Fraction."""
from fractions import Fraction as F
from pathlib import Path
import itertools,json

def elt(*xs): return tuple(F(x) for x in xs)+(F(0),)*(4-len(xs))
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    v=[F(0)]*7
    for i in range(4):
        for j in range(4): v[i+j]+=a[i]*b[j]
    for i in range(6,3,-1):
        v[i-2]+=v[i];v[i-4]-=v[i]
    return tuple(v[:4])
def power(a,k):
    out=elt(1)
    for _ in range(k):out=mul(out,a)
    return out
q=elt(0,1);one=elt(1);zero=elt()
assert power(q,12)==one and all(power(q,d)!=one for d in (1,2,3,4,6))
xs=[power(q,j) for j in range(12)]
u_exp=[0,2,4,8]
H=[[add(mul(power(q,e),mul(x,x)),power(q,(-e)%12)) for x in xs] for e in u_exp]
word=[];pair_profile=[]
for j in range(12):
    pairs=[(i,k) for i,k in itertools.combinations(range(4),2) if H[i][j]==H[k][j]]
    assert len(pairs)==1
    word.append(H[pairs[0][0]][j]);pair_profile.append(pairs[0])
old_matches=[[j for j in range(12) if H[i][j]==word[j]] for i in range(4)]
assert all(len(v)==6 for v in old_matches)
w0=[sub(word[j],H[3][j]) for j in range(12)]
assert [j for j,v in enumerate(w0) if v==zero]==[0,1,2,6,7,8]
# Direct conversion of the displayed sqrt(3),i formulas, using sqrt(3)=2q-q^3.
a=elt(F(3,13),F(-6,13),F(9,13),F(8,13))
c=elt(F(8,13),F(-3,13),F(11,13),F(-9,13))
def V(x):
    out=one
    for j in (0,1,2):out=mul(out,sub(x,xs[j]))
    return out
matches=[j for j,x in enumerate(xs) if mul(c,V(x))==mul(sub(x,a),w0[j])]
assert matches==[0,1,2,3,4,5]
assert a not in xs and V(a)!=zero and c!=zero
assert a!=zero and a!=elt(4) and power(a,12)!=one
result={'arithmetic':'Fraction basis 1,q,q^2,q^3; q^4=q^2-1',
        'old_matches':old_matches,'pair_profile':pair_profile,
        'a_basis':[str(v) for v in a],'c_basis':[str(v) for v in c],
        'witness_matches':matches,'pole_off_domain':True,'proper':True,
        'lift_distinctness_guards':['a != 0','a != 4','a^12 != 1'],
        'lift_domain_size':28,'lift_degree_cap':6,'lift_agreements_at_least':14,
        'scope':'Exact first-witness verification; completeness independently proved in audit, not a second 300-case census.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
