"""Run one owned computation with an RSS limit and a wall-clock deadline.

Only the subprocess group created here is terminated. Standard-library only.
The report survives failure; the child should write its own checkpoints.
"""
import argparse
import json
import os
from pathlib import Path
import signal
import subprocess
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--rss-mib', type=int, default=384)
    parser.add_argument('--seconds', type=int, default=900)
    parser.add_argument('--report', type=Path, required=True)
    parser.add_argument('command', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ['--'] else args.command
    if not command:
        parser.error('a command is required')
    env = os.environ.copy()
    for key in ['OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
                'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS']:
        env[key] = '1'
    started = time.monotonic()
    child = subprocess.Popen(command, env=env, start_new_session=True)
    peak = 0
    reason = 'completed'
    try:
        while child.poll() is None:
            rows = subprocess.check_output(['ps', '-axo', 'pgid=,rss='], text=True)
            rss = sum(int(parts[1]) for line in rows.splitlines()
                      if len(parts := line.split()) == 2 and int(parts[0]) == child.pid)
            peak = max(peak, rss)
            if rss > args.rss_mib * 1024:
                reason = 'rss_limit'
                break
            if time.monotonic() - started > args.seconds:
                reason = 'time_limit'
                break
            time.sleep(0.5)
    finally:
        if child.poll() is None:
            os.killpg(child.pid, signal.SIGTERM)
            try:
                child.wait(timeout=3)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid, signal.SIGKILL)
                child.wait()
        report = dict(command=command, reason=reason, returncode=child.returncode,
                      seconds=time.monotonic()-started, peak_rss_kib=peak,
                      rss_limit_mib=args.rss_mib, time_limit_seconds=args.seconds)
        args.report.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(report), flush=True)
    raise SystemExit(child.returncode if reason == 'completed' else 124)


if __name__ == '__main__':
    main()
