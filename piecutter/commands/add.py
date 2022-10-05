"""Source code behind the 'add' command"""
import os

from typer import Typer
from typer import Option
from ..generators.code import CoreCodes
from ..utils import get_available_frameworks


app = Typer()


@app.command()
def api_endpoint(
    name: str,
    input: str = Option("JSON"),
    output: str = Option("JSON"),
) -> None:
    """Add a new route to the BentoML's API server."""
    if not os.path.exists("service.py"):
        raise Exception("You have no service file in this project!")

    # Reading the service file
    with open("service.py", "a") as f:
        new_route_code = CoreCodes.generate_new_route_code(
            route_name=name, input_type=input, output_type=output
        )
        f.write(new_route_code)
        f.close()

    print(f"A new API endpoint named '{name}' was added to your service!")


@app.command()
def bento_build(base_framework: str = Option("custom")) -> None:
    """Add all BentoML files in a project with no Bento build."""
    if base_framework.lower() not in get_available_frameworks():
        raise Exception(
            "The selected base framework doesn't exist or isn't supported yet!"
        )

    if os.path.exists("service.py"):
        raise Exception("You already have a buildable BentoML in this project.")

    if not os.path.exists(os.path.join("scripts")):
        raise Exception("You need a subdirectory called 'scripts' in this project!")

    FILES_TO_ADD = [
        "service.py",
        "bentofile.yaml",
        "api_config.yaml",
        os.path.join("scripts", "load_model.py"),
    ]

    for file in FILES_TO_ADD:
        with open(file, "w") as f:
            bento_file_content = CoreCodes(base_framework)
            bento_file_content = bento_file_content.get_writable_content(
                current_file=os.path.split(file)[-1]
            )
            f.write(bento_file_content)
            f.close()

    print("The buildable BentoML code was added to your project!")


if __name__ == "__main__":
    app()
