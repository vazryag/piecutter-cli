"""Helper functions used across piecutter"""
import os


def get_available_frameworks():
    """Returns the current machine learning frameworks for validating
    user's input.

    Returns:
        tuple: Tuple with the current available base frameworks.
    """
    return (
        "catboost",
        "fastai",
        "keras",
        "onnx",
        "pytorch",
        "pytorch_lightning",
        "sklearn",
        "tensorflow",
        "transformers",
        "xgboost",
        "custom",
    )
