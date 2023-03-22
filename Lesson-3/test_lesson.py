import typer
from typer.testing import CliRunner

import main

runner = CliRunner()


def test_app_single():
    result = runner.invoke(main.app, ["printer", "omg hi!"])
    assert result.exit_code == 0
    assert "OMG HI!" in result.stdout


def test_app_multi():
    result = runner.invoke(main.app, ["printer", "--multi", "Let's just break this"])
    assert result.exit_code == 0
    assert "LET'S\nJUST\nBREAK\nTHIS\n" in result.stdout


def test_app_quite():
    result = runner.invoke(main.app, ["printer", "--no-yell", "Can you hear that?"])
    assert result.exit_code == 0
    assert "Can you hear that?" in result.stdout


