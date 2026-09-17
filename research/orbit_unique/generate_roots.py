"""Find and save certified prime-order roots; every accepted output is valid."""
from pathlib import Path
import hashlib,json,secrets,time
BASE=Path(__file__).resolve().parent

def modmul(x,y,p,b):
 v=x*y;r=(v&p)+(v>>b)
 return r-p if r>=p else r

def modpow(x,e,p,b):
 y=1
 for bit in bin(e)[2:]:
  y=modmul(y,y,p,b)
  if bit=='1':y=modmul(y,x,p,b)
 return y

if __name__=='__main__':
 start=time.monotonic();rows=[]
 for row in json.loads((BASE/'parameters.json').read_text())['rows']:
  b=row['b'];d=row['d'];p=(1<<b)-1;t0=time.monotonic();trials=0
  while True:
   h=secrets.randbelow(p-1)+1;trials+=1;omega=modpow(h,(p-1)//d,p,b)
   if omega!=1:break
  # The independent native modular power has only log2(d) multiplications.
  assert pow(omega,d,p)==1 and 1<omega<p
  out=dict(b=b,d=d,omega_hex=hex(omega),trials=trials,seconds=time.monotonic()-t0,
   sha256=hashlib.sha256(omega.to_bytes((b+7)//8,'big')).hexdigest())
  rows.append(out);print(json.dumps({k:v for k,v in out.items() if k!='omega_hex'}),flush=True)
 (BASE/'roots.json').write_text(json.dumps(dict(rows=rows,seconds=time.monotonic()-start),indent=2)+'\n')
