"""Complete small proper-quotient censuses using the previously checked scanner."""
from pathlib import Path
import subprocess,json
root=Path(__file__).resolve().parents[2]
fixtures=[(5,41),(3,73),(6,73),(3,97),(4,97),(6,97),(8,97),(3,193),(4,193),(6,193),(8,193),(4,257),(8,257)]
rows=[]
for r,p in fixtures:
 assert (p-1)%(4*r)==0 and 4*r<p-1
 row=json.loads(subprocess.run([str(root/'tmp/dickson-quotient-scan'),str(r),str(p)],capture_output=True,text=True,check=True).stdout)
 row['reaches_full_dickson_agreement_fraction']=2*row['maximum_agreement']>=3*r
 rows.append(row)
 print(json.dumps(row),flush=True)
 Path(__file__).with_name('scan.json').write_text(json.dumps(dict(scope='Complete maximum-agreement census for the listed proper quotients only. Does not compute orbit sizes, full-domain nearestness, or prove a growing family.',rows=rows),indent=2)+'\n')
