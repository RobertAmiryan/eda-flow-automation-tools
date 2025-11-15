import os
from pathlib import Path
from scripts import run_flow


def test_run_step_with_dummy(tmp_path):
    # use the provided dummy runner script to avoid heavy work
    repo_root = Path(__file__).resolve().parents[1]
    dummy_script = repo_root / 'scripts' / 'run_step_dummy.py'
    assert dummy_script.exists()

    logdir = tmp_path / 'logs'
    logdir.mkdir()

    step = {'name': 'teststep', 'script': str(dummy_script), 'args': ['--name', 'teststep', '--duration', '0', '--warnings', '1', '--errors', '1']}
    ret, log_path = run_flow.run_step(step, str(logdir))

    assert ret == 0
    assert Path(log_path).exists()
    text = Path(log_path).read_text()
    assert 'Sample warning' in text
    assert 'Sample error' in text
