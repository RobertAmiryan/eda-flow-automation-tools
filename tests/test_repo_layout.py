from pathlib import Path


def test_repo_layout_files_and_dirs():
    """Ensure the repository contains the expected top-level files and directories."""
    root = Path(__file__).resolve().parents[1]

    expected_files = [
        'README.md',
        'LICENSE',
        'requirements.txt',
    ]
    expected_dirs = [
        'configs',
        'scripts',
        'logs',
        'tests',
    ]

    for fn in expected_files:
        p = root / fn
        assert p.is_file(), f"Missing file at repo root: {fn}"

    for dn in expected_dirs:
        p = root / dn
        assert p.is_dir(), f"Missing directory at repo root: {dn}"

    # Quick sanity checks for important scripts
    assert (root / 'scripts' / 'run_flow.py').is_file(), 'Missing scripts/run_flow.py'
    assert (root / 'scripts' / 'log_parser.py').is_file(), 'Missing scripts/log_parser.py'
