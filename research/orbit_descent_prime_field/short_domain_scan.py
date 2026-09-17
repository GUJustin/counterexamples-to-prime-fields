"""Complete small cyclic-word nearest-list scans across characteristics.

Fixed finite parameter range only; no asymptotic inference. Checkpoint after
 each complete field so a bounded run can resume without repeating work.
"""
from pathlib import Path
import subprocess,json,math
root=Path(__file__).resolve().parents[2]
out=Path(__file__).with_name('short_domain_scan.json')
rows=json.loads(out.read_text())['rows'] if out.exists() else []
done={(a['r'],a['p']) for a in rows}
fixtures=[(r,p) for r in range(2,9) for p in range(8*r+1,2001 if r<=6 else 501,4*r) if all(p%d for d in range(2,math.isqrt(p)+1))]
for r,p in fixtures:
 if (r,p) in done:continue
 row=json.loads(subprocess.run([str(root/'tmp/dickson-quotient-scan'),str(r),str(p)],capture_output=True,text=True,check=True).stdout)
 row['reaches_three_eighths_agreement']=2*row['maximum_agreement']>=3*r
 rows.append(row)
 out.write_text(json.dumps(dict(scope='Complete determining-support censuses for r=2,...,8 and primes 8r<p<=2000 (p<=500 for r>=7) with 4r dividing p-1. Only finite cyclic-word examples; does not certify a growing family or full-domain nearest descent.',planned_cases=len(fixtures),completed_cases=len(rows),rows=rows),indent=2)+'\n')
 if row['reaches_three_eighths_agreement']:print(json.dumps(row),flush=True)
print(json.dumps(dict(completed=len(rows),planned=len(fixtures),hits=sum(a['reaches_three_eighths_agreement'] for a in rows))),flush=True)
