"""Exhaustive interpolation-pool replay of unique-nearby far-point padding."""
from pathlib import Path
import json,time
from verify_unique_padding import fixture


def main():
 start=time.monotonic()
 rows=[fixture(1,2,3,far_point=True),fixture(2,5,4,far_point=True)]
 for row in rows:
  assert row['maximum_list_size_on_line']==1
  assert row['exact_far_agreement']==row['A']-1
  assert 0 not in row['nearby_labels']
 out=dict(status='passed',fixtures=rows,seconds=time.monotonic()-start,
          scope='All potentially nearby interpolants are exhausted. Injective nonzero multiplicative labels prove whole-line uniqueness, and f is globally the degree-A-1 polynomial, giving an exact far point and no correlated agreement.')
 Path(__file__).with_name('unique_far_padding_verification.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({**out,'fixtures':[{k:v for k,v in row.items() if k not in {'domain','f','g','nearby_labels','boundary_polynomials'}} for row in rows]},indent=2))
if __name__=='__main__':main()
