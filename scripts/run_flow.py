#!/usr/bin/env python3
"""Flow orchestrator for the example EDA flow.
Reads a YAML config and runs each step sequentially, capturing logs.
"""
import argparse, subprocess, yaml, os, sys, shlex, time
from pathlib import Path

def run_step(step, log_dir):
    script = step.get('script')
    args = step.get('args', [])
    cmd = [sys.executable, script] + args
    log_path = Path(log_dir) / f"{step.get('name')}.log"
    print(f"Running step: {step.get('name')} -> {' '.join(cmd)}")
    with open(log_path, 'w') as f:
        proc = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT)
        ret = proc.wait()
    return ret, log_path

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--config', required=True, help='Path to flow yaml')
    args = p.parse_args()
    cfg = yaml.safe_load(open(args.config))
    log_dir = cfg.get('log_dir','logs')
    os.makedirs(log_dir, exist_ok=True)
    results = []
    for step in cfg.get('steps', []):
        start = time.time()
        ret, log_path = run_step(step, log_dir)
        duration = time.time()-start
        results.append({'step': step.get('name'), 'returncode': ret, 'log': str(log_path), 'duration_s': duration})
    print('\nFlow finished. Summary:')
    for r in results:
        print(f" - {r['step']}: rc={r['returncode']}, log={r['log']}, time={r['duration_s']:.2f}s")

if __name__ == '__main__':
    main()
