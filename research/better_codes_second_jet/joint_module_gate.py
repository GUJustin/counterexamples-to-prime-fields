from pathlib import Path
import json
scope={}
exec(Path(__file__).with_name('curvature_upper_gate.py').read_text().split('checks=0')[0],scope)
m=128;s=40;J=177;L=5515
C,M=scope['counts'](m,s,1,J)
C0,M0=scope['counts'](m,s,0,J)
fixed_V=(L+1)*(C-C0)-(M-M0)
certified=53746080
out={'shape':{'m':m,'S':s,'J':J,'L':L,'Vcap':1},'fixed_factor_V_ambient_multiple_dimension':fixed_V,'certified_source_kernel_lower':certified,'integer_ratio_floor':fixed_V//certified,'scope':'Ambient common-factor dimension bound is far too large to force two rationally independent V-linear equations. This is not an example showing the actual kernel has a common factor.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
