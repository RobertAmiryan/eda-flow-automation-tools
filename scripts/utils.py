# Small helper utilities used by scripts
import os
from pathlib import Path

def ensure_dirs():
    root = Path(__file__).resolve().parents[1]
    for d in ['logs','flow/step_1_prep','flow/step_2_synthesis','flow/step_3_place','flow/step_4_route','flow/step_5_sta']:
        Path(root / d).mkdir(parents=True, exist_ok=True)
