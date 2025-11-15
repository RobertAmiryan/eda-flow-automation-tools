from pathlib import Path
import importlib


def test_ensure_dirs_creates_expected_dirs(tmp_path, monkeypatch):
    # Make a fake __file__ path inside tmp_path so ensure_dirs creates dirs under tmp_path/src
    fake_utils = importlib.import_module('scripts.utils')
    fake_file = tmp_path / 'src' / 'scripts' / 'utils.py'
    fake_file.parent.mkdir(parents=True)
    # monkeypatch the module __file__ so Path(__file__).resolve() uses our fake path
    monkeypatch.setattr(fake_utils, '__file__', str(fake_file))

    # call ensure_dirs and verify created directories
    fake_utils.ensure_dirs()
    root = Path(str(fake_file)).resolve().parents[1]
    expected = [
        root / 'logs',
        root / 'flow' / 'step_1_prep',
        root / 'flow' / 'step_2_synthesis',
        root / 'flow' / 'step_3_place',
        root / 'flow' / 'step_4_route',
        root / 'flow' / 'step_5_sta',
    ]
    for p in expected:
        assert p.exists()
