# Tip 1: Use CustomRunnable to apply a custom_logic() on input_data before prediction.
# Tip 2: Try not to change the default variable names!

import os
from typing import Any

import bentoml
import numpy as np
import pandas as pd
from bentoml.io import *
from pydantic import BaseModel
from pycaret.regression import load_model, predict_model


MODEL_NAME = "lightgbm_price_regressor"
SERVICE_NAME = "DIAMOND_PRICE_PREDICTION"


class InputSchema(BaseModel):
    carat: float = 0.23
    cut: str = "Ideal"
    color: str = "E"
    clarity: str = "SI2"
    depth: float = 61.5
    table: float = 55.0
    x: float = 3.95
    y: float = 3.98
    z: float = 2.43


class CustomRunnable(bentoml.Runnable):
    SUPPORTED_RESOURCES = ("cpu",)  # Add "nvidia.com/gpu" support if needed!
    SUPPORTS_CPU_MULTI_THREADING = True

    def __init__(self):
        self.model = load_model(os.path.join("models", MODEL_NAME), verbose=False)

    @bentoml.Runnable.method(batchable=False)
    def custom_logic(self, input_data):
        """Run the request data processing and ML pipeline.

        Returns:
            float: The predicted price.
        """
        sample_df = pd.DataFrame(
            {
                "carat": input_data.carat,
                "cut": input_data.cut,
                "color": input_data.color,
                "clarity": input_data.clarity,
                "depth": input_data.depth,
                "table": input_data.table,
                "x": input_data.x,
                "y": input_data.y,
                "z": input_data.z
            },
            index=[0]
        )

        return self.model.predict(sample_df)[0]


custom_runner = bentoml.Runner(CustomRunnable)
svc = bentoml.Service(SERVICE_NAME, runners=[custom_runner])

@svc.api(input=JSON(pydantic_model=InputSchema), output=JSON())
def predict(posted_data):
    """Describe here what this endpoint should do."""
    return {"predicted_price": custom_runner.custom_logic.run(posted_data)}

@svc.api(input=NumpyNdarray(), output=JSON())
def estimate(posted_data):
"""Describe here what this endpoint should do."""
pass