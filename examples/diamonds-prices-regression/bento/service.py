from typing import Dict, Any
 
import bentoml
from bentoml.io import JSON
 
# Uncomment the one you need
from pycaret.regression import load_model
from starlette_authlib.middleware import AuthlibMiddleware as SessionMiddleware
 
from predict import model_predict


class PyCaretRunnable(bentoml.Runnable):
 
    SUPPORTED_RESOURCES = ("cpu",)
    SUPPORTS_CPU_MULTI_THREADING = True
 
    def __init__(self):
        """Constructor method for loading the model"""
        self.model = load_model("lightgbm_price_regressor", verbose=False)
 
    @bentoml.Runnable.method(batchable=False)
    def make_prediction(self, input_data: dict) -> list:
        """This method uses the trained model to generate predictions.
 
        Args:
            input_data (dict): The JSON data sent by the client.
 
        Returns:
            list: A list with the predicted values.
        """       
        return model_predict(self.model, input_data)
 
 
# Service build
model_runner = bentoml.Runner(PyCaretRunnable)
svc = bentoml.Service("australian_diamonds_price_regression_api", runners=[model_runner])

@svc.api(input=JSON(), output=JSON())
def predict(input_data: dict) -> Dict[str, Any]:
    """Response back the prediction made by the model."""
    return {"prediction": model_runner.make_prediction.run(input_data)}