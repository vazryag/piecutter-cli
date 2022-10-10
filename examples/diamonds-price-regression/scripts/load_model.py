# Tip 1: Use this script to save a trained mode to Bento's local storage.
# Tip 2: Use any officially supported ML/AI framework to load your trained model.
# Tip 3: The metadata at model_metadata will be deployed with the model for performance tracking.

import os
import bentoml


if __name__ == "__main__":

   MODEL_PATH = os.path.join("your", "model", "path")

   # Load your custom model
   # loaded_model = ...

   # Your model's metadata (edit as you need)
   model_metadata = {
       "accuracy": None,
       "auc_score": None,
       "recall": None,
       "precision": None,
       "f1_score": None,
       "kappa": None,
       "mcc": None,
       "mae": None,
       "mse": None,
       "rmse": None,
       "r2_score": None,
       "rmsle": None,
       "mape": None,
       "dataset_version": None
   }

   # Storing to BentoML's local storage
   try:
       model = bentoml.tensorflow.save_model(
           name=MODEL_NAME,
           model=loaded_model,
           metadata=model_metadata,
           labels={
               "owner": "your-name",
               "stage": "dev"
           },
           signatures={
               __call__: {
                   "batchable": False,
                   "batch_size": 0,
               }
           }
       )
   except:
       raise Exception("Error when saving model to BentoML!")