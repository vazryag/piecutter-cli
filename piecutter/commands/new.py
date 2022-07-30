import os

from typer import Typer
from typer import Option

from ..templates import base_structure
from ..utils import write_piecutter_project_files


app = Typer()


@app.command()
def project(name: str = Option(...)) -> None:
    """
    Generates a new project folder with a pre-built structure for research.
    """
    try:
        # initializing files and folders template
        project_directories = base_structure.define_initial_directories(name)
        project_files = base_structure.define_initial_files(name)

        # creating the project root dir, its files and folders
        os.makedirs(name)
        for folder in project_directories:
            os.makedirs(folder)

        for file in project_files:
            with open(file, "w") as f:
                f.write(write_piecutter_project_files(os.path.join(name, file)))
                f.close()

        print(f"The project '{name}' was successfully created!")

    except OSError as e:
        print(e)


if __name__ == "__main__":
    app()
