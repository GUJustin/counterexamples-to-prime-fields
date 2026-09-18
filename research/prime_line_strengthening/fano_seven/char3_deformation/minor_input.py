from pathlib import Path
# Reuse independent polynomial-field reconstruction, not the solver's tower arithmetic.
P=Path(__file__).parent
exec((P/'verify.py').read_text().split('reports=[]')[0])
def code(v):return sum(c*3**i for i,c in enumerate(v))
f=(P/'rank_minors.in').open('w');f.write('5\n')
for case in d['cases']:
 mask=case['triple_mask']|128;rows=[]
 for j in range(44):
  x=nodes[j] if j<42 else zero
  ids=d['core_masks'][j] if j<42 else [i for i in range(8) if bool(mask>>i&1)==(j==42)]
  for i in ids:
   row=[zero]*176;v=one
   for k in range(11):row[11*i+k]=v;v=mul(v,x)
   row[88+j]=ev([tuple(k*c%3 for c in polys[i][k]) for k in range(1,11)],x)
   row[132+j]=neg(one);rows.append(row)
 rr=case['pivot_rows'];cc=case['pivot_columns'];assert len(rr)==len(cc)==156
 f.write(str(case['triple_mask'])+' 156\n')
 for r in rr:f.write(' '.join(str(code(rows[r][c])) for c in cc)+'\n')
f.close();print('Five156x156 minors independently reconstructed.')
