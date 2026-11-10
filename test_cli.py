import subprocess
import sys

def test_cli_runs():
    result = subprocess.run(
        [sys.executable, "main.py", "--kind", "sine", "--n", "10", "--window", "3"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert "тип ряда: sine" in result.stdout