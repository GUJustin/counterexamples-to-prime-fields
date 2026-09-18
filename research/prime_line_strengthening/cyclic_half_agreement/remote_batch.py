"""Run a fixed manifest of public finite-field experiments with per-job limits."""
import concurrent.futures
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import threading
import time

manifest = json.loads(Path(sys.argv[1]).read_text())
out = Path('results')
out.mkdir(exist_ok=True)
source_hash = hashlib.sha256(Path('search.cpp').read_bytes()).hexdigest()
threading.stack_size(256 * 1024)

def run(job):
    saved = out / (job['id'] + '.json')
    if saved.exists():
        old = json.loads(saved.read_text())
        if old.get('job') == job and old.get('source_sha256') == source_hash and old.get('returncode') == 0:
            return {'id': job['id'], 'seconds': old['seconds'], 'returncode': 0,
                    'timed_out': False, 'reused': True}
    argv = ['./search', str(job['q']), str(job['p']), '20']
    if 'support' in job:
        argv.append(','.join(map(str, job['support'])))
    elif 'filter' in job:
        assert hashlib.sha256(Path(job['filter']).read_bytes()).hexdigest() == job['filter_sha256']
        argv.extend(['-', job['filter']])
    started = time.monotonic()
    receipt = {'job': job, 'source_sha256': source_hash}
    try:
        result = subprocess.run(argv, capture_output=True, text=True, timeout=90)
        receipt.update(returncode=result.returncode, stdout=result.stdout,
                       stderr=result.stderr, timed_out=False)
    except subprocess.TimeoutExpired as error:
        receipt.update(returncode=None, timed_out=True)
    receipt['seconds'] = time.monotonic() - started
    (out / (job['id'] + '.json')).write_text(json.dumps(receipt, indent=2)+'\n')
    return {'id': job['id'], 'seconds': receipt['seconds'],
            'returncode': receipt['returncode'], 'timed_out': receipt['timed_out']}

completed = []
with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
    for row in pool.map(run, manifest):
        completed.append(row)
        Path('batch_progress.json').write_text(json.dumps(completed, indent=2)+'\n')
Path('DONE.json').write_text(json.dumps({'completed': len(completed),
                                       'time': time.time()}, indent=2)+'\n')
