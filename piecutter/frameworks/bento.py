"""Writes BentoML-wide files"""
import secrets


def __generate_bento_auth_token() -> str:
    """Generates an authentication token for secured endpoints.

    Returns:
        str: An auth token as string.
    """
    return secrets.token_urlsafe(32)


def write_train_file() -> str:
    """Writes the python train file inside bento's dir.

    Returns:
        str: The python train file
    """
    return "\n".join(
        (
            "# import your training libs",
            "# ...",
            " ",
            " ",
            "def train_model():",
            '    """Trains and serialize your model/pipeline in the bento folder."""',
            "    pass",
        )
    )


def write_predict_file() -> str:
    """Writes the python predict file.

    Returns:
        str: The python predict content.
    """
    return "\n".join(
        (
            "# import libs you need for sample processing and prediction",
            "# ...",
            " ",
            "def __sample_preprocessing(input_data):",
            '    """Pre-process the data sent by the client for machine learning."""',
            "    pass",
            " ",
            "def predict_model(model, input_data):",
            '    """Uses the trained model to generate predictions on processed sample."""',
            "    pass",
        )
    )


def write_bentofile_file() -> str:
    """Writes the bentofile.yaml inside bento's dir.

    Returns:
        str: The bentofile.yaml content
    """
    return "\n".join(
        (
            "service: 'service:svc'",
            "labels:",
            "    owner: your-name",
            "    stage: dev",
            "include:",
            "    - '*.py'",
            "    - '*.pkl'",
            "python:",
            "    packages: # Pip packages required by your service",
            "        - pandas # It's just and example, remove if you don't need it",
        )
    )


def write_api_endpoint(name: str, secured: bool, has_session_middleware: bool) -> str:
    """Writes a snippet of code defining a new api endpoint.

    Args:
        secured (bool): Defines if the endpoint is JWT secured or not.
        has_session_middleware (bool): Checks if service.py has SessionMiddleware already.

    Returns:
        str: New API endpoint as string.
    """
    if secured:
        if has_session_middleware:
            return "\n".join(
                (
                    "\n",
                    "@svc.api(input=JSON(), output=JSON())",
                    f"def {name}(input_data: dict) -> Dict[str, Any]:",
                    '    """Response back the prediction made by the model."""',
                    '    return {"prediction": model_runner.make_prediction.run(input_data)}',
                )
            )

        security_token = __generate_bento_auth_token()
        return "\n".join(
            (
                " ",
                f"svc.add_asgi_middleware(SessionMiddleware, secret_key='{security_token}')",
                " ",
                "@svc.api(input=JSON(), output=JSON())",
                f"def {name}(input_data: dict) -> Dict[str, Any]:",
                '    """Response back the prediction made by the model."""',
                '    return {"prediction": MODEL_RUNNER.make_prediction.run(input_data)}',
            )
        )

    return "\n".join(
        (
            "\n",
            "@svc.api(input=JSON(), output=JSON())",
            f"def {name}(input_data: dict) -> Dict[str, Any]:",
            '    """Response back the prediction made by the model."""',
            '    return {"prediction": model_runner.make_prediction.run(input_data)}',
        )
    )
