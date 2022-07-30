import os

from typer import Typer
from typer import Option

from ..utils import read_script_files
from ..utils import write_bento_deployable_files
from ..utils import checks_for_session_middleware
from ..frameworks.bento import write_api_endpoint
from ..templates.bento_structure import BENTO_DIR_NAME
from ..templates.bento_structure import define_bento_files
from ..templates.bento_structure import define_available_frameworks


app = Typer()


@app.command()
def bento(
    base_framework: str = Option(
        ..., help=f"Available: {', '.join(define_available_frameworks())}"
    )
) -> None:
    """
    Generates a BentoML deployable folder on the project's root directory.
    """
    # checking for existing projects, bentos and frameworks
    check_for_requirements = not os.path.isfile("requirements.txt")
    check_for_bento = os.path.isdir("bento")
    check_for_framework = base_framework.lower() not in define_available_frameworks()
    if check_for_requirements or check_for_bento or check_for_framework:
        raise Exception(
            "You may not have either started a project, selected "
            "a valid framework or already has an existing bento!"
        )

    try:
        # initializing bento files template
        bento_files = define_bento_files()

        # creating bento files
        os.makedirs(BENTO_DIR_NAME)
        for file in bento_files:
            with open(file, "w") as f:
                f.write(write_bento_deployable_files(file, base_framework))
                f.close()

        print(f"Your deployable BentoML folder was created!")

    except OSError as e:
        print(e)


@app.command()
def api_route(endpoint_name: str, secured: bool = Option(...)) -> None:
    """
    Creates a brand new BentoML API endpoint on an existing Bento.
    """
    # checking if a service.py file does exist
    service_file_path = os.path.join(BENTO_DIR_NAME, "service.py")
    if not os.path.isfile(service_file_path):
        raise Exception("You need to generate a bento before an API endpoint!")

    # reading the service.py file to look for middlewares and then
    # writing the endpoint
    service_file_content = read_script_files(service_file_path)
    with open(service_file_path, "a") as csf:
        csf.write(
            write_api_endpoint(
                name=endpoint_name,
                secured=secured,
                has_session_middleware=checks_for_session_middleware(
                    service_file_content
                ),
            )
        )
        csf.close()

    if secured:
        print(f"The secured '{endpoint_name}' endpoint was successfully created!")
        return None

    print(f"The unsecured '{endpoint_name}' endpoint was successfully created!")


if __name__ == "__main__":
    app()
