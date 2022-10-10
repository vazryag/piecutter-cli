# This Project is Based on Piecutter CLI

    ------------
       ├── README.md             -> The README.md file for describing your project.
       ├── requirements.txt      -> List of requirements to run your code.
       ├── data                  -> The dataset of your project at different stages.
       │        ├── raw
       │        ├── processed,
       │        ├── finalized,
       ├── notebooks             -> Your jupyter notebooks.,
       ├── references            -> Any external reference used in your project.
       ├── reports               -> Reports folder to store figures and tables.
       │        ├── figures
       │        ├── tables
       ├── scripts               -> Python scripts for training/saving models.
       │        ├── load_model.py
       │        ├── train.py
       ├── models                -> Serialized models will be stored here!
       ├── service.py            -> Production service file to run BentoML models.
       ├── bentofile.yaml        -> YAML file for BentoML build (Do not change this file name!).
       ├── api_config.yaml       -> YAML file for BentoML's API configuration (Do not change this file name!).
    ------------


Visit the <a href="https://github.com/g0nz4rth/piecutter-cli">Piecutter CLI official documentation</a> page.