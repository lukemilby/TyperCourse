import typer
from typer.testing import CliRunner

import main

runner = CliRunner()


def test_app():
    result = runner.invoke(main.app, ["pew", "Luke"])
    print(result)
    assert result.exit_code == 0
    assert "You pew Luke" in result.stdout