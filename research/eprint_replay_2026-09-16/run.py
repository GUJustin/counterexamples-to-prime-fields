"""Sequential, resource-bounded replay of the manuscript's mathematical checks."""
from datetime import datetime,timezone
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
import time

BASE=Path(__file__).resolve().parent
ROOT=BASE.parent.parent
GUARD=ROOT/'research/overnight_2026-09-16/certificates/run_bounded.py'

def main():
    commands=re.findall(r'^\t\$\(PYTHON\) (.+)$',(ROOT/'Makefile').read_text(),re.M)
    env=os.environ.copy()
    env['PATH']=str(ROOT/'tmp/eprint-replay-bin')+os.pathsep+env['PATH']
    started=time.monotonic()
    report={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'running','checks':[],
            'scope':'Default mathematical Makefile verify commands, sequentially under a 384 MiB process-group watchdog. No protocol execution and no --full cubic rerun.'}
    for i,command in enumerate(commands):
        print(f'[{i+1}/{len(commands)}] {command}',flush=True)
        limit=10800 if command=='research/overnight_2026-09-16/verify.py' else 900
        log=BASE/f'{i:02d}.log';resources=BASE/f'{i:02d}_resources.json'
        with log.open('w') as out:
            result=subprocess.run([sys.executable,str(GUARD),'--rss-mib','384','--seconds',str(limit),
                                   '--report',str(resources),'--',sys.executable,*shlex.split(command)],
                                  cwd=ROOT,env=env,stdout=out,stderr=subprocess.STDOUT)
        row={'command':command,'returncode':result.returncode,'log':log.name}
        if resources.exists():row['resources']=json.loads(resources.read_text())
        report['checks'].append(row)
        report['elapsed_seconds']=time.monotonic()-started
        (BASE/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
        print('PASS' if result.returncode==0 else f'FAILED ({result.returncode}), see {log.name}',flush=True)
    report['status']='PASS' if all(r['returncode']==0 for r in report['checks']) else 'INCOMPLETE'
    (BASE/'verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(report['status'],flush=True)

if __name__=='__main__':main()
