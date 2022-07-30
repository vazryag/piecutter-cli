"""Helper functions used through piecutter"""
import os
import secrets

from .frameworks.bento import write_train_file
from .frameworks.bento import write_predict_file
from .frameworks.bento import write_bentofile_file
from .frameworks.pycaret import write_pycaret_service
from .templates.bento_structure import BENTO_DIR_NAME


def read_script_files(script_path: str) -> str:
    """Reads script files and extracts their codes as strings.

    Args:
        script_path (str): The path of the script file.

    Returns:
        str: Script's code as string.
    """
    with open(script_path) as f:
        script_content = f.readlines()
        f.close()

    return script_content


def checks_for_session_middleware(
    file_lines: list, pattern: str = "add_asgi_middleware"
) -> bool:
    """Reads a script's lines and checks for an existing asgi middleware.

    Args:
        file_lines (list): A file read.
        pattern (str): The pattern to look for.

    Returns:
        bool: A boolean indication the existence or not o a asgi middleware.
    """
    script_lines = [line.replace("\n", "") for line in file_lines]

    for line in script_lines:
        if pattern in line:
            return True

    return False


def write_bento_deployable_files(file: str, base_framework: str) -> str:
    """Writes the right code on the write bento build file.

    Args:
        file (str): The file name to get code written in.
        base_framework (str): The base framework the service will run.

    Returns:
        str: The file code.
    """
    if file == os.path.join(BENTO_DIR_NAME, "service.py"):
        if base_framework == "pycaret":
            return write_pycaret_service()

    if file == os.path.join(BENTO_DIR_NAME, "bentofile.yaml"):
        return write_bentofile_file()

    if file == os.path.join(BENTO_DIR_NAME, "train.py"):
        return write_train_file()

    if file == os.path.join(BENTO_DIR_NAME, "predict.py"):
        return write_predict_file()
