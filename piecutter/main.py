"""The main CLI file"""
import os
import subprocess

import typer
from typer import Typer
from typer import Option

from .commands import add
from .generators.code import CoreCodes
from .generators.files import CoreFiles
from .utils import get_available_frameworks
from piecutter import __version__ as _version
from .generators.folders import CoreDirectories


app = Typer()


# Subcommands
app.add_typer(add.app, name="add", help="Add a new resource to the project.")


# Commands
@app.command()
def new(
    project_name: str,
    include_bento: bool = Option(True),
    base_framework: str = Option("custom"),
) -> None:
    """Generates a new structured project folder with files."""

    if base_framework.lower() not in get_available_frameworks():
        raise Exception("This framework doesn't exist or isn't supported yet!")

    if os.path.exists(project_name):
        raise Exception("A project with the same name already exists!")

    # Creating project folder and subdirectories
    print(f"Creating project root directory: {project_name}")
    os.mkdir(project_name)

    for core_dir in CoreDirectories.get_project_base_folders(project_name):
        print(f"Creating subdirectory: {core_dir}")
        os.mkdir(core_dir)

    # Writing framework-specific code
    generatable_files = CoreFiles(project_name, include_bento)
    writable_framework_code = CoreCodes(base_framework)

    for file in generatable_files.get_generetable_files():
        print(f"Writing project file: {file}")
        with open(file, "w") as f:
            f.write(writable_framework_code.get_writable_content(file))
            f.close()


@app.command()
def docs() -> None:
    """Opens the official Piecutter CLI documentation on the browser."""
    typer.launch_browser("https://github.com/g0nz4rth/piecutter-cli")


@app.command()
def version() -> str:
    """Returns the current version of the package."""
    print(_version)


if __name__ == "__main__":
    app()
