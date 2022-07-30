import os

from typer.testing import CliRunner

from piecutter import __version__
from piecutter import main


runner = CliRunner()


def test_version():
    assert __version__ == "0.1.0"


def test_command_new():
    result = runner.invoke(main.app, ["new", "project", "--name", "example-project"])
    assert result.exit_code == 0
    assert "The project 'example-project' was successfully created!" in result.stdout
