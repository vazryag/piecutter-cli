"""Core scripts generator dependencies"""
import os


class CoreCodes(object):

    """Genetares the core scripts for each project
    as strings to be written in the files.
    """

    def __init__(self, base_framework: str) -> None:
        """Constructor method.

        Args:
            base_framework (str): The base ML framework.
        """
        self.base_framework = base_framework

    def get_writable_content(self, current_file: str) -> str:
        """Get writable content for the current file.

        Args:
            file_name (str): File code content as string.
        """
        writable_file_key = os.path.split(current_file)[-1]

        WRITABLE_CONTENT = {
            "README.md": self.__generate_readme_file(),
            "requirements.txt": self.__generate_requirements_txt_file(),
            "train.py": self.__generate_train_file_content(),
            "service.py": self.__generate_service_file_content(),
            "custom_service.py": self.__generate_custom_service_file_content(),
            "bentofile.yaml": self.__generate_bento_config_file(),
            "api_config.yaml": self.__generate_api_config_file(),
            "load_model.py": self.__generate_load_model_file_content(),
        }

        # Condition for custom services
        if self.base_framework.lower() == "custom":
            writable_file_key = writable_file_key.replace(
                "service.py", "custom_service.py"
            )

        return WRITABLE_CONTENT[writable_file_key]

    def __generate_readme_file(self) -> str:
        """Generates the README.md file content.

        Returns:
            str: The Readme.md file content as string.
        """
        return "\n".join(
            (
                "# This Project is Based on Piecutter CLI",
                "",
                "    ------------",
                "       ├── README.md             -> The README.md file for describing your project.",
                "       ├── requirements.txt      -> List of requirements to run your code.",
                "       ├── data                  -> The dataset of your project at different stages.",
                "       │        ├── raw",
                "       │        ├── processed,",
                "       │        ├── finalized,",
                "       ├── notebooks             -> Your jupyter notebooks.,",
                "       ├── references            -> Any external reference used in your project.",
                "       ├── reports               -> Reports folder to store figures and tables.",
                "       │        ├── figures",
                "       │        ├── tables",
                "       ├── scripts               -> Python scripts for training/saving models.",
                "       │        ├── load_model.py",
                "       │        ├── train.py",
                "       ├── models                -> Serialized models will be stored here!",
                "       ├── service.py            -> Production service file to run BentoML models.",
                "       ├── bentofile.yaml        -> YAML file for BentoML build (Do not change this file name!).",
                "       ├── api_config.yaml       -> YAML file for BentoML's API configuration (Do not change this file name!).",
                "    ------------",
                "",
                "",
                'Visit the <a href="https://github.com/g0nz4rth/piecutter-cli">Piecutter CLI official documentation</a> page.',
            )
        )

    def __generate_requirements_txt_file(self) -> str:
        """Generates the requirements.txt file.

        Returns:
            str: The requirements.txt file content as string.
        """
        return "\n".join(("bentoml==1.0.0rc3", "pydantic"))

    def __generate_api_config_file(self) -> str:
        """Generates the BentoML package-wide configuration file.

        Returns:
            str: The BentoML config.yaml file content as string.
        """
        return "\n".join(
            (
                "api_server:",
                "  workers: 4",
                "  timeout: 60",
                "http:",
                "  host: 0.0.0.0",
                "  port: 6000",
                "runners:",
                "  batching:",
                "    enabled: true",
                "    max_batch_size: 100",
                "    max_latency_ms: 10000",
                "  metrics:",
                "    enabled: true",
                "    namespace: bentoml_runner",
                "  timeout: 300",
            )
        )

    def __generate_service_file_content(self) -> str:
        """Generates the BentoML service.py script content.

        Returns:
            str: The service.py code as string.
        """
        return "\n".join(
            (
                "# Tip 1: Try not to change the model_runner and svc variables names.",
                "# Tip 2: If you need to change the default names, make sure your code is working!",
                "",
                "import bentoml",
                "from bentoml.io import *",
                "from pydantic import BaseModel",
                "",
                "",
                "# Model & Service names",
                "MODEL_NAME = 'YOUR_MODEL_NAME:latest'",
                "SERVICE_NAME = 'YOUR_SERVICE_NAME'",
                "",
                "",
                "class InputSchema(BaseModel):",
                "   # Specify your input schema (e.g. how a JSON payload needs to be structured)",
                "   # E.g. Iris dataset expected input JSON structure", 
                "   # sepal_len: float",
                "   # sepal_width: float",
                "   # petal_len: float",
                "   # petal_width: float",
                "",
                "",
                "# Runner & Service load",
                f"model_runner = bentoml.{self.base_framework}.get(MODEL_NAME).to_runner()",
                "svc = bentoml.Service(SERVICE_NAME, runners=[model_runner])",
            )
        )

    def __generate_custom_service_file_content(self) -> str:
        """Generates a custom service runner script content.

        Returns:
            str: The custom service.py code as string.
        """
        return "\n".join(
            (
                "# Tip 1: Use CustomRunnable to apply a custom_logic() on input_data before prediction.",
                "# Tip 2: Try not to change the default variable names!",
                "",
                "from typing import Any",
                "",
                "import bentoml",
                "from bentoml.io import *",
                "from pydantic import BaseModel",
                "",
                "",
                'MODEL_NAME = "YOUR_MODEL_NAME:latest"',
                'SERVICE_NAME = "YOUR_SERVICE_NAME"',
                "",
                "",
                "class InputSchema(BaseModel):",
                "   # Specify your input schema (e.g. how a JSON payload needs to be structured)",
                "   # E.g. Iris dataset expected input JSON structure", 
                "   # sepal_len: float",
                "   # sepal_width: float",
                "   # petal_len: float",
                "   # petal_width: float",
                "",
                "",
                "class CustomRunnable(bentoml.Runnable):",
                '   SUPPORTED_RESOURCES = ("cpu",)  # Add "nvidia.com/gpu" support if needed!',
                "   SUPPORTS_CPU_MULTI_THREADING = True",
                "",
                "   def __init__(self):",
                f"       self.model = bentoml.{self.base_framework}.get(MODEL_NAME)",
                "",
                "   @bentoml.Runnable.method(batchable=False)",
                "   def custom_logic(self, input_data):",
                '       """Summary',
                "",
                "       Returns:",
                "           TYPE: Description",
                '       """',
                "       input_data = # Custom data processing...",
                "",
                "       return self.model.predict(input_data)",
                "",
                "",
                "custom_runner = bentoml.Runner(CustomRunnable)",
                "svc = bentoml.Service(SERVICE_NAME, runners=[custom_runner])",
            )
        )

    def __generate_bento_config_file(self) -> str:
        """Generates the bentofile.yaml script content.

        Returns:
            str: The bentofile.yaml code as string.
        """
        return "\n".join(
            (
                'service: "service:svc"  # The service file (do not change it!)',
                'description: "file: ./README.md"',
                "labels:",
                "  owner: your-name",
                "  stage: dev",
                "include:  # List of what will be in the prod build",
                '- "/scripts/*.py"',
                '- "requirements.txt"',
                "exclude:  # List of what to not include in the prod build.",
                '- "/scripts/load_model.py',
                '- "/venv"',
                '- "/references"',
                '- "/reports"',
                '- "/data"',
                '- "/notebooks"',
                "python:",
                '  requirements_txt: "./requirements.txt"  # List your pip packages',
                "  lock_packages: true",
                "  trusted_host:  # Add any trusted host you want",
                '  - "pypi.python.org"',
                '  pip_args: "--pre -U --force-reinstall"',
                "docker:",
                "  distro: debian",
                '  python_version: "3.8.12"',
                '  cuda_version: "11.6.2"  # Remove if you do not need CUDA',
                "  env:  # Put your environmental variables here",
                "  - FOO=value1",
            )
        )

    def __generate_load_model_file_content(self) -> str:
        """Generates the load model file content as string.

        Returns:
            str: The load_model.py file content as string.
        """
        return "\n".join(
            (
                "# Tip 1: Use this script to save a trained mode to Bento's local storage.",
                "# Tip 2: Use any officially supported ML/AI framework to load your trained model.",
                "# Tip 3: The metadata at model_metadata will be deployed with the model for performance tracking.",
                "",
                "import os",
                "import bentoml",
                "",
                "",
                'if __name__ == "__main__":',
                "",
                '   MODEL_PATH = os.path.join("your", "model", "path")',
                "",
                f"   # Load your {self.base_framework} model",
                "   # loaded_model = ...",
                "",
                "   # Your model's metadata (edit as you need)",
                "   model_metadata = {",
                '       "accuracy": None,',
                '       "auc_score": None,',
                '       "recall": None,',
                '       "precision": None,',
                '       "f1_score": None,',
                '       "kappa": None,',
                '       "mcc": None,',
                '       "mae": None,',
                '       "mse": None,',
                '       "rmse": None,',
                '       "r2_score": None,',
                '       "rmsle": None,',
                '       "mape": None,',
                '       "dataset_version": None',
                "   }",
                "",
                "   # Storing to BentoML's local storage",
                "   try:",
                f"       model = bentoml.{self.base_framework}.save_model(",
                "           name=MODEL_NAME,",
                "           model=loaded_model,",
                "           metadata=model_metadata,",
                "           labels={",
                '               "owner": "your-name",',
                '               "stage": "dev"',
                "           },",
                "           signatures={",
                "               __call__: {",
                '                   "batchable": False,',
                '                   "batch_size": 0,',
                "               }",
                "           }",
                "       )",
                "   except:",
                '       raise Exception("Error when saving model to BentoML!")',
            )
        )

    def __generate_train_file_content(self) -> str:
        """Generates the ML model/pipeline train script content.

        Returns:
            str: The train.py code as string.
        """
        return "\n".join(
            (
                "# Tip 1: Use this script to process the dataset and train a model.",
                "# Tip 2: Call __data_processing() within train_model() before the training starts.",
                "# Tip 3: Save the trained model with BentoML for local storaging (at the end of train_model()).",
                "",
                "",
                "def __data_processing():",
                "   pass",
                "",
                "",
                "def train_model():",
                "   pass",
            )
        )

    @staticmethod
    def generate_new_route_code(
        route_name: str, input_type: str, output_type: str
    ) -> str:
        """Generates a new route code as string.

        Returns:
            str: New route code as string.
        """
        INPUT_TYPES = {
            "ARRAY": "NumpyNdarray()",
            "DATAFRAME": "PandasDataFrame",
            "JSON": "JSON(pydantic_model=InputSchema)",
            "TEXT": "Text()",
            "IMAGE": "Image()",
            "FILE": "File()",
        }

        OUTPUT_TYPES = {
            "ARRAY": "NumpyNdarray()",
            "DATAFRAME": "PandasDataFrame",
            "JSON": "JSON()",
            "TEXT": "Text()",
            "IMAGE": "Image()",
            "FILE": "File()",
        }

        try:
            input_type = INPUT_TYPES[input_type.upper()]
            output_type = OUTPUT_TYPES[output_type.upper()]
        except:
            raise Exception(
                "Invalid route input/output type (try: ARRAY, DATAFRAME, JSON, TEXT, IMAGE or FILE)."
            )

        return "\n".join(
            (
                "",
                "",
                f"@svc.api(input={input_type}, output={output_type})",
                f"def {route_name}(posted_data):",
                '"""Describe here what this endpoint should do."""',
                "pass",
            )
        )
