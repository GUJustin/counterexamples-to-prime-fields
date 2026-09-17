"""Build and check exhaustive small rational-fiber pencil enumerations."""
from pathlib import Path
from math import comb
import json,subprocess

ROOT=Path(__file__).resolve().parent


def main():
    binary=ROOT/'check_balanced_rational_pencils'
    subprocess.run(['clang++','-O2','-UNDEBUG','-std=c++17',str(ROOT/'check_balanced_rational_pencils.cpp'),
                    '-o',str(binary)],check=True)
    output=subprocess.check_output([str(binary)],text=True)
    rows=[json.loads(line) for line in output.splitlines()]
    assert len(rows)==5
    for row in rows:
        p,n,B=row['p'],row['n'],row['B']
        assert row['subsets']==comb(n,B)
        assert row['disjoint_pairs_checked']==comb(n,B)*comb(n-B,B)//2
        hypothesis=(p-1)%n==0 and (p-1)//n>=6 and n>6*(B-1)
        assert hypothesis==row['satisfies_candidate_hypotheses']
        assert row['balanced_pairs']==sum(row[key] for key in ('cyclic_pairs','dihedral_pairs','other_pairs'))
        if hypothesis:assert row['other_pairs']==0
        else:assert row['other_pairs']>0
    assert rows[0]['balanced_pairs']==10 and rows[0]['other_pairs']==9
    assert rows[1]['balanced_pairs']==35 and rows[1]['other_pairs']==32
    result=dict(status='passed',rows=rows,total_disjoint_pairs_checked=sum(r['disjoint_pairs_checked'] for r in rows),
                scope='All rational-map pencils induced by two complete fibers on the selected small domains; supplementary finite checks, not a replacement for the proof.')
    (ROOT/'balanced_rational_pencils_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)


if __name__=='__main__':main()
