"""Check every numeric hypothesis in the primary phase-source adapter."""
import ast,json
from pathlib import Path
ROOT=Path(__file__).parent
source=ast.parse((ROOT/'replay_phase_kernels.py').read_text());exec(compile(ast.Module(body=[x for x in source.body if isinstance(x,(ast.Import,ast.ImportFrom,ast.FunctionDef))],type_ignores=[]),'replay_phase_kernels.py','exec'))
A=181275;n=262144;w=131071;p=2130706433
out=[]
for file in sorted(ROOT.glob('new_phase*finalist_*.json')):
    if file.stem.endswith(('resources','all_rows')):continue
    data=json.loads(file.read_text());candidate=data['candidate'];m,L,s,Y=[candidate[k] for k in ['m','L','s','Y']];D=A*m
    C=count(D,L,s);R=rank(m,L,s);gap=C-n*R
    assert gap==candidate['gap']>0
    assert D+s<=w*(Y+1) and s<=m<p
    q,r=divmod(D,w)
    assert s<=q<=L and r+s<=w and 2*s<=m and m+s<=L+1
    mixed=[35*L+9275*s,159*L+9275*Y,159*s+35*Y]
    assert max(mixed+[159,35,9275])<p
    cy,cr,cz=1+2*w*159,w*69,1+2*w*9275
    numerators=[(n-w)*(cy*s+cr*Y),(n-w)*(cr*L+cz*s)+(n-A+1)*(A-w)*s,(n-w)*(cy*L+cz*Y)+(n-A+1)*(A-w)*Y]
    assert all(x<=(A-w)*y for x,y in zip(numerators,candidate['potential']))
    out.append(dict(file=file.name,source=candidate,coefficient_count=C,local_rank=R,shape_slack=w*(Y+1)-D-s,max_mixed_costs=mixed,char_gate_slack=p-max(mixed),potential_inequality_slacks=[(A-w)*y-x for x,y in zip(numerators,candidate['potential'])]))
(ROOT/'new_phase_parameter_audit.json').write_text(json.dumps(dict(A=A,scope='Numeric hypotheses for the existing algebraic source adapter after explicit target-A substitution. No Lean rebuild or complete target certificate.',sources=out),indent=2)+'\n')
print('All source dimension, shape, characteristic, and potential hypotheses pass for',len(out),'finalists.')
