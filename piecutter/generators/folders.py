import os


class CoreDirectories(object):

    """Implements the generator for the new project's
    folders.
    """

    @staticmethod
    def get_project_base_folders(project_name) -> list:
        """Generates a list of folders to be created in the new project.

        Returns:
            list: The base folders to be created.
        """
        return [
            os.path.join(project_name, "data"),
            os.path.join(project_name, "data", "raw"),
            os.path.join(project_name, "data", "processed"),
            os.path.join(project_name, "data", "finalized"),
            os.path.join(project_name, "models"),
            os.path.join(project_name, "notebooks"),
            os.path.join(project_name, "references"),
            os.path.join(project_name, "reports"),
            os.path.join(project_name, "reports", "figures"),
            os.path.join(project_name, "reports", "tables"),
            os.path.join(project_name, "scripts"),
        ]
