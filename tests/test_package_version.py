from typer.testing import CliRunner

from piecutter import __version__
from piecutter import main


runner = CliRunner()


def test_version():
    assert __version__ == "0.1.0"
