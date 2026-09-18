import json, pathlib, sys, hashlib
base=pathlib.Path(__file__).resolve().parent
source=base/(sys.argv[1] if len(sys.argv)>1 else 'pilot_d3.json')
a=json.loads(source.read_text())
assert a['schema']==1 and a['D']==13 and a['h_coefficients_ascending'][-1]==1
mapping={'L':'L','P':'p','Q':'q','G':'primitive_root','LAST':'last_fresh_node','TCOUNT':'t','GAP':'d'}
s='\n'.join(f'constexpr int {k}={int(a[v])};' for k,v in mapping.items())
s+='\nconstexpr int HC[14]={'+','.join(map(str,a['h_coefficients_ascending']))+'};\n'
(base/'verify_input.h').write_text(s)
print('input sha256',hashlib.sha256(source.read_bytes()).hexdigest())
