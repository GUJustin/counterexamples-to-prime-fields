from pathlib import Path
P=Path(__file__).parent
exec((P/'verify.py').read_text().split('left=list(map(decode')[0])
def code(v):return sum(c*3**i for i,c in enumerate(v))
rr=d['pivot_rows'];cc=d['pivot_columns'];assert len(rr)==len(cc)==164
with (P/'rank_minor.in').open('w') as f:
 f.write('1\n0 164\n')
 for r in rr:f.write(' '.join(str(code(rows[r].get(c,zero))) for c in cc)+'\n')
print('Independent 164x164 matrix reconstructed')
