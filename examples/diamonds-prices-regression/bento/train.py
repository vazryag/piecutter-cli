# import your training libs
import os
import numpy as np
import pandas as pd
from pycaret.regression import *


# loading the data
train_data = pd.read_csv("train.csv")

 
def train_model(data: pd.DataFrame = train_data):
    """Trains and serialize your model/pipeline in the bento folder."""
    # setting up the experiment
    reg_exp = setup(
        data=data,
        target="price",
        train_size=0.8,
        ordinal_features={"cut" : ["Fair", "Good", "Very Good", "Ideal", "Premium"]},
        numeric_features=["carat", "depth", "table", "x", "y", "z"],
        categorical_features=["color", "clarity"],
        polynomial_features=True,
        normalize=True,
        remove_multicollinearity=True,
        transform_target=True,
        transform_target_method="box-cox",
        silent=True,
        html=False,
        use_gpu=False
    )
    
    # creating the model
    model = create_model(
        estimator="lightgbm",
        boosting_type="gbdt",
        colsample_bytree=1.0,
        importance_type="split",
        learning_rate=0.1,
        max_depth=-1,
        min_child_samples=20,
        min_child_weight=0.001,
        min_split_gain=0.0,
        n_estimators=100,
        num_leaves=31,
        random_state=4235,
        silent="warn",
        subsample=1.0,
        subsample_for_bin=200000,
        subsample_freq=0,
        power_transformer_method="box-cox",
        power_transformer_standardize=True
    )
    
    # finalizing the model
    final_model = finalize_model(model)
    
    # serializing the model
    save_model(final_model, "lightgbm_price_regressor", verbose=False)


train_model()