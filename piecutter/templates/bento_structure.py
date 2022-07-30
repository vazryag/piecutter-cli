import os


BENTO_DIR_NAME = "bento"


def define_bento_files() -> list:
    """
    This function returns a list of files to be written on
    the project's bento folder.
    """
    return [
        os.path.join(BENTO_DIR_NAME, "bentofile.yaml"),
        os.path.join(BENTO_DIR_NAME, "service.py"),
        os.path.join(BENTO_DIR_NAME, "train.py"),
        os.path.join(BENTO_DIR_NAME, "predict.py"),
    ]


def define_available_frameworks() -> list:
    """
    This function returns a list of frameworks available
    for backing up the Bento build.

    Returns:
        list: A list of available frameworks.
    """
    return ["pycaret"]
