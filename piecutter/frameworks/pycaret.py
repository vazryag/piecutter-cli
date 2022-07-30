"""Writes PyCaret-wide files"""


def write_pycaret_service() -> None:
    """Writes a custom BentoML runnable for PyCaret."""
    return "\n".join(
        (
            "from typing import Dict, Any",
            " ",
            "import bentoml",
            "from bentoml.io import JSON",
            " ",
            "# Uncomment the one you need",
            "# from pycaret.[classification/regression] import load_model",
            "from starlette_authlib.middleware import AuthlibMiddleware as SessionMiddleware",
            " ",
            "from predict import predict_model",
            " ",
            " ",
            "class PyCaretRunnable(bentoml.Runnable):",
            " ",
            '    SUPPORTED_RESOURCES = ("cpu",)',
            "    SUPPORTS_CPU_MULTI_THREADING = True",
            " ",
            "    def __init__(self):",
            '        """Constructor method for loading the model"""',
            '        self.model = load_model("PATH_TO_YOUR_MODEL", verbose=False)',
            " ",
            "    @bentoml.Runnable.method(batchable=False)",
            "    def make_prediction(self, input_data: dict) -> list:",
            '        """This method uses the trained model to generate predictions.',
            " ",
            "        Args:",
            "            input_data (dict): The JSON data sent by the client.",
            " ",
            "        Returns:",
            "            list: A list with the predicted values.",
            '        """',
            "        return predict_model(input_data)",
            " ",
            " ",
            "# Service build",
            "model_runner = bentoml.Runner(PyCaretRunnable)",
            'svc = bentoml.Service("NAME_OF_YOUR_SERVICE", runners=[model_runner])',
        )
    )
