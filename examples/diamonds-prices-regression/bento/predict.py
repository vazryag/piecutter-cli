# import libs you need for sample processing and prediction
import pandas as pd
from pycaret.regression import predict_model

 
def __sample_preprocessing(input_data: dict) -> pd.DataFrame:
    """Pre-process the data sent by the client for machine learning."""
    return pd.DataFrame(input_data, index=[0])
 
def model_predict(model, input_data: dict) -> list:
    """Uses the trained model to generate predictions on processed sample."""
    sample = __sample_preprocessing(input_data=input_data)
    prediction = model.predict(sample)
    
    return [round(item, 3) for item in prediction]