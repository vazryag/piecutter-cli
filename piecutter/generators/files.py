import os


class CoreFiles(object):

    """Implements the code used to generate
    the project files.
    """

    def __init__(self, project_name: str, include_bento: bool = True) -> None:
        """Constructor method

        Args:
            project_name (str): The new project name.
        """
        self.project_name = project_name
        self.include_bento = include_bento

    def get_generetable_files(self) -> list:
        """Returns the list of files to generate based on
        user's input conditions.

        Returns:
            list: The list of files to be generated.
        """
        if self.include_bento == False:
            return self.__base_files_to_generate()

        return self.__base_files_to_generate() + self.__bento_files_to_generate()

    def __base_files_to_generate(self) -> list:
        """Returns the default base files common to any data
        science project, whether it have BentoML or not.

        Returns:
            list: List of base common files.
        """
        return [
            os.path.join(self.project_name, "README.md"),
            os.path.join(self.project_name, "requirements.txt"),
            os.path.join(self.project_name, "scripts", "train.py"),
        ]

    def __bento_files_to_generate(self) -> list:
        """BentoML-specific files to be generated.

        Returns:
            list: The list of BentoML files to create.
        """
        return [
            os.path.join(self.project_name, "service.py"),
            os.path.join(self.project_name, "bentofile.yaml"),
            os.path.join(self.project_name, "api_config.yaml"),
            os.path.join(self.project_name, "scripts", "load_model.py"),
        ]
