import typer
from typer.testing import CliRunner

import main

runner = CliRunner()


def test_app_default():
    result = runner.invoke(main.app, ["pew", "Luke"])
    assert result.exit_code == 0
    assert "You pew Luke" in result.stdout


def test_app_count():
    result = runner.invoke(main.app, ["pew", "Luke", "3"])
    assert result.exit_code == 0
    assert "You pew pew pew Luke" in result.stdout
