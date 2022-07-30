"""The main CLI file"""
import os

from typer import Typer
from typer import Option
from typer import launch as launch_browser

from .commands import new
from .commands import generate
from .templates import base_structure
from piecutter import __version__ as _version


app = Typer()


# Adding subcommands
app.add_typer(new.app, name="new")
app.add_typer(generate.app, name="generate")


@app.command()
def docs() -> None:
    """
    Opens the official Piecutter CLI documentation on the browser.
    """
    launch_browser("https://github.com/g0nz4rth/piecutter-cli")


@app.command()
def version() -> str:
    """Returns the current version of the package."""
    print(_version)


if __name__ == "__main__":
    app()
