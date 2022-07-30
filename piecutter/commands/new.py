from optparse import Option
import os

from typer import Typer
from typer import Option

from ..templates import base_structure


app = Typer()


@app.command()
def project(name: str = Option(...)) -> None:
    """Automatically generates a project directory with a structure.

    Args:
        name (str): The name of the project.
    """
    try:
        # initializing files and folders template
        project_directories = base_structure.define_initial_directories(name)
        project_files = base_structure.define_initial_files(name)

        # creating the project root dir, its files and folders
        os.makedirs(name)
        for folder in project_directories:
            os.makedirs(folder)

        for files in project_files:
            with open(files, "w") as f:
                f.close()

        print(f"The project '{name}' was successfully created!")

    except OSError as e:
        print(e)


if __name__ == "__main__":
    app()
