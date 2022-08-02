import os

from typer.testing import CliRunner

from piecutter import __version__
from piecutter import main


runner = CliRunner()


def test_command_new():
    result = runner.invoke(main.app, ["new", "project", "--name", "test_files/example-project"])
    assert result.exit_code == 0
    assert "The project 'test_files/example-project' was successfully created!" in result.stdout
