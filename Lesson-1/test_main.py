from typer.testing import CliRunner
import typer

import main

runner = CliRunner()


def test_app():
    result = runner.invoke(main.app, ["Tim"])
    assert result.exit_code == 0
    assert "Hello Tim!" in result.stdout