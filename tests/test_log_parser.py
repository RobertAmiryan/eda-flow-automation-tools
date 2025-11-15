import textwrap
from pathlib import Path
from scripts import log_parser


def test_parse_log_counts_and_slack(tmp_path):
    content = textwrap.dedent("""
        [INFO] Starting
        [WARNING] Something odd
        [ERROR] Failure happened
        [INFO] Worst negative slack: -0.123 ns
    """)
    p = tmp_path / "sample.log"
    p.write_text(content)

    res = log_parser.parse_log(p)
    assert res["errors"] == 1
    assert res["warnings"] == 1
    assert abs(res["worst_negative_slack_ns"] + 0.123) < 1e-6
    assert "Failure happened" in res["errors_sample"][0]
