"""Destroy only this task's recorded rental at its local hard deadline."""
import json
from pathlib import Path
import subprocess
import sys
import time

state_path = Path(sys.argv[1])
cli = sys.argv[2]
while True:
    state = json.loads(state_path.read_text())
    assert state['label'].startswith('proximity-cyclic-')
    if state.get('destroyed'):
        break
    if time.time() < state['destroy_by_unix']:
        time.sleep(min(30, state['destroy_by_unix'] - time.time()))
        continue
    result = subprocess.run(
        [cli, 'destroy', 'instance', str(state['instance_id']), '-y', '--raw'],
        capture_output=True, text=True, timeout=60,
    )
    print(json.dumps({'time': time.time(), 'instance_id': state['instance_id'],
                      'returncode': result.returncode}), flush=True)
    if result.returncode == 0:
        state['destroyed'] = True
        state['destroyed_unix'] = time.time()
        state_path.write_text(json.dumps(state, indent=2) + '\n')
        break
    time.sleep(30)
