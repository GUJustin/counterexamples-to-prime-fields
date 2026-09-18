import json, math
from fractions import Fraction
from pathlib import Path
N,d,T,C=262144,131071,139782,139781
required=274980728111395088
fall=lambda n,k: math.prod(range(n-k+1,n+1))
rows=[]
for r in range(1,10):
    line=Fraction(fall(N,r+1),T*(T-d)**(r-1)*(T-C))
    word=Fraction(fall(N,r),T*(T-d)**(r-1))
    rows.append(dict(r=r,line_numerator=line.numerator,line_denominator=line.denominator,line_floor=line.numerator//line.denominator,fixed_word_floor=word.numerator//word.denominator))
assert rows[7]['line_floor']<required<=rows[8]['line_floor']
assert rows[1]['fixed_word_floor']==56
out=dict(N=N,d=d,T=T,C=C,required=required,rows=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
