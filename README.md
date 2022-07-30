<div align="center">
    <img src="statics/logo.png" width="250" />
    <h4>
        An open-source CLI app to build your entire ML project, from research to production. <br />
        Piecutter-CLI 0.1.0 is released! :rocket:
    </h4> 
</div>

## Base Piecutter Project Structure
    ------------
        ├── Makefile              -> The Makefile of your project.
        ├── README.md             -> The README.md file for describing your project.
        ├── requirements.txt      -> List of requirements to run your code.
        ├── data                  -> The dataset of your project at different stages.
        │   ├── raw
        │   ├── processed
        │   ├── finalized
        ├── notebooks             -> Your jupyter notebooks.
        ├── references            -> Any external reference used in your project.
        ├── results               -> Results folder to store figures, tables and trained models.
        │   ├── figures
        │   ├── models
        │   ├── tables
        ├── tests                 -> Write tests to your scripts here!
        |    ├── test_predict.py
        |    ├── test_train.py
    ------------

## Why Piecutter?
Piecutter CLI is a project highly inspired by the well-known <a href="https://github.com/cookiecutter/cookiecutter" target="_blank">Cookiecutter</a> project. 

*But why another CLI app inspired in a well established one?*

A lot of data scientists need to put models into production right after the modeling phase, and Cookiecutter doesn't help with this important step of the machine learning lifecycle. Moreover, the project template generated by Cookiecutter has some files and folders that we, as data scientists, don't use very often in a research-to-production environment. Piecutter generates a much more cleaner structure of folders and files for the research phase of a ML project.

*And about the production phase?*

Piecutter implements a standardized way to put trained models and ML pipelines into production by using BentoML. BentoML is a tool to standardize the process of ML model deployment by building an inference API around your trained pipeline as well as containerizing this application with docker, making it available for deployment right off the bat.

*But why should I use Piecutter CLI if BentoML exists?*

Well, BentoML's development is in full swing, and this is good and bad at the same time. Although very standardized, the BentoML team constantly make significant changes on the package design, which affects not only the user experience, but also makes the official documentation outdated very fast. Piecutter puts all this mess out of your sight and gives you few commands for you to generate your entire research environment structure as well as to generate your production-ready inference API code in a matter of seconds.

Moreover, BentoML isn't capable of generating the research and the production structure in the same codebase, it isn't meant for that actually. Piecutter takes care of this integration and on top of that implements *Custom Runnables* for any unsupported framework as well as for more complex AI pipelines just by running one or two commands.

## Supported Frameworks
The first version of Piecutter has just been released and for now the package only has support for **PyCaret** deployment. *You can expect support for all major frameworks in the coming days (I'm developing this package in my spare time, as fast as I can)*.

## Installation
To install `piecutter-cli` it's really simple.

    $ pip install piecutter-cli

## Usage
### Package Version
With `piecutter-cli` installed, you're ready to use it! Run the command down below to check if it's working properly.

    $ piecutter version

### Package Documentation
It should returns the current version of the package. You can also run the command down below to open the official documentation on the browser.

    $ piecutter docs

And then this GitHub page should appear in your browser.

### Generate a New Project
To generate a new project structure you need to run:

    $ piecutter new project --name diamonds-prices-regression

In the example above we've created a new project called `diamonds-prices-regression` with the following structure:

    ------------
        ├── Makefile              -> The Makefile of your project.
        ├── README.md             -> The README.md file for describing your project.
        ├── requirements.txt      -> List of requirements to run your code.
        ├── data                  -> The dataset of your project at different stages.
        │   ├── raw
        │   ├── processed
        │   ├── finalized
        ├── notebooks             -> Your jupyter notebooks.
        ├── references            -> Any external reference used in your project.
        ├── results               -> Results folder to store figures, tables and trained models.
        │   ├── figures
        │   ├── models
        │   ├── tables
        ├── tests                 -> Write tests to your scripts here!
        |    ├── test_predict.py
        |    ├── test_train.py
    ------------

You can check out this real world project implemented in our <a href="https://github.com/g0nz4rth/piecutter-cli/tree/main/examples/diamonds-prices-regression" target="_blank">example/diamonds-prices-regression</a> folder.

When you have your final model trained and ready for production, you need to generate a bento.

### Generate a New Bento
With the command shown below Piecutter will generate a `/bento` folder inside your project directory with all the necessary files to put your model into production as a docker image.

    $ piecutter generate bento --base-framework pycaret

And a folder with the following structure will be added to your project directory:

    ------------
        ├── bentofile.yaml          -> File used by bento to build the BentoML image.
        ├── predict.py              -> Script to generate predictions with your trained model.
        ├── service.py              -> The BentoML service file, which starts the Bento server.
        ├── train.py                -> Script to retrain your model (and serialize it in the current dir)
    ------------

You can see the real world version of this file in the <a href="https://github.com/g0nz4rth/piecutter-cli/tree/main/examples/diamonds-prices-regression/bento" target="_blank">examples/diamonds-prices-regression/bento</a>.

*OBS.: Please, execute this command form the outside of your project root dir. This bug will be fixed in the next release.*

### Generate a New API Route
The `piecutter generate bento` command generates the file responsible to start the BentoML server, but without any API endpoint. You can use the command below to generate a new secured/unsecured API endpoint.

    $ piecutter generate api-route predict [--secured / --no-secured]

Use `--secured` for generating a JWT secured API and `--no-secured` for an endpoint without any authentication strategy.

In the <a href="https://github.com/g0nz4rth/piecutter-cli/tree/main/examples/diamonds-prices-regression" target="_blank">example/diamonds-prices-regression</a> project I've generated an unsecure API endpoint for inference.