#!/usr/bin/env python3
"""Parse logs in logs/ and produce a simple summary report (errors, warnings, timing)."""
import argparse, re, os
from pathlib import Path

def parse_log(path):
    errors = 0
    warnings = 0
    wslack = None
    err_lines = []
    with open(path) as f:
        for line in f:
            if 'ERROR' in line:
                errors += 1
                err_lines.append(line.strip())
            if 'WARNING' in line:
                warnings += 1
            m = re.search(r'Worst negative slack:\s*([\-\d\.]+)\s*ns', line)
            if m:
                try:
                    wslack = float(m.group(1))
                except:
                    pass
    return {'errors': errors, 'warnings': warnings, 'worst_negative_slack_ns': wslack, 'errors_sample': err_lines[:5]}

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--logdir', default='logs')
    args = p.parse_args()
    logdir = Path(args.logdir)
    summary = {}
    for fp in sorted(logdir.glob('*.log')):
        summary[fp.name] = parse_log(fp)
    # Print a human-readable report
    print('Log summary:')
    for name, s in summary.items():
        print(f" - {name}: errors={s['errors']}, warnings={s['warnings']}, wns={s['worst_negative_slack_ns']}")
        if s['errors_sample']:
            print('   sample error lines:')
            for el in s['errors_sample']:
                print('    ', el)

if __name__ == '__main__':
    main()
