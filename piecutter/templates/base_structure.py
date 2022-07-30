import os


def define_initial_directories(project_root_name: str) -> list:
    """
    This function returns a list of directories to be created.
    To make piecutter-cli to create a new default directory it's
    just add a new one on the list returned by this function.

    Args:
        project_root_name (str): The new project root dir name.

    Returns:
        list: List of folders to be created in the root dir.
    """
    return [
        os.path.join(project_root_name, "data", "raw"),
        os.path.join(project_root_name, "data", "processed"),
        os.path.join(project_root_name, "data", "finalized"),
        os.path.join(project_root_name, "notebooks"),
        os.path.join(project_root_name, "results", "figures"),
        os.path.join(project_root_name, "results", "tables"),
        os.path.join(project_root_name, "results", "models"),
        os.path.join(project_root_name, "tests"),
        os.path.join(project_root_name, "references"),
    ]


def define_initial_files(project_root_name: str) -> list:
    """
    This function returns a list of files to be created
    in the new project's directory. To make piecutter-cli to
    create a new default file it's just add a new one on
    the list returned by this function.

    Args:
        project_root_name (str): The new project root dir name.

    Returns:
        list: list of files to be created in the root dir.
    """
    return [
        os.path.join(project_root_name, "Makefile"),
        os.path.join(project_root_name, "README.md"),
        os.path.join(project_root_name, "requirements.txt"),
        os.path.join(project_root_name, "tests", "test_train.py"),
        os.path.join(project_root_name, "tests", "test_predict.py"),
    ]
