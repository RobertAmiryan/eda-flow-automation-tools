#!/usr/bin/env python3
"""A dummy EDA step runner. Simulates logs with warnings/errors and timing info."""
import argparse, time, random, sys
def main():
    p = argparse.ArgumentParser()
    p.add_argument('--name', required=True)
    p.add_argument('--duration', type=float, default=0.2)
    p.add_argument('--errors', type=int, default=0)
    p.add_argument('--warnings', type=int, default=0)
    args = p.parse_args()
    print(f"[INFO] Starting step {args.name}")
    time.sleep(args.duration)
    for i in range(args.warnings):
        print(f"[WARNING] Sample warning {i+1} in {args.name}")
    for i in range(args.errors):
        print(f"[ERROR] Sample error {i+1} in {args.name}")
    # Simulate timing slack lines for sta
    if args.name == 'sta':
        slack = round(random.uniform(-0.05, 0.5), 3)
        print(f"[INFO] Worst negative slack: {slack} ns")
    print(f"[INFO] Finished step {args.name}")
if __name__ == '__main__':
    main()
