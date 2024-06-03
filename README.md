## Introduction

It is a tutorial of setting up a template project for training a model with python. It uses Mlflow, dagshub and DVC to track and version model and data.

### Components

Training model contains 4 components.

1. Prepare training data. Load data from storage to local storage
2. Load basic model. Load model to local storage
3. Train model.
4. Evaluate model

### Workflow to update a component

1. Update config.yaml
2. Update secretes.yaml(Optional)
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

### Prepare

1. It needs to create an account in dagshub.

2. It needs to setup environment to integrate dagshub and mlflow.

```shell
export MLFLOW_TRACKING_URI=https://dagshub.com/liang3030/dl-tutorial.mlflow

export MLFLOW_TRACKING_USERNAME=liang3030

export MLFLOW_TRACKING_PASSWORD=XXXX...XXXX

```

### Setup Project

1. Create `template.py` with project folder structure. Then run `python template.py`

2. Create `setup.py` to set up project basic information and introduction

3. Use conda to setup dependency managing environment `conda create -n dl python=3.8 -y` then activate with `conda activate dl`

4. Install depenedency with `pip install -r requirements.txt`

### Data version control

DVC is used for data version control. The dependency is set in `requirements.txt`. The core concept is similar as git. The core concept that given all related file or parameter in dvc.yaml a hash value. Then if the hash value is not change, the step will be skip.

1. Initialize DVC with `dvc init`. It will generate a file called `.dvcignore` and a folder called `.dvc`.

2. run `dvc repro`. It will scan `dvc.yaml` file, and execute file command that defined by `cmd`.

3. run `dvc dag`. It will show pipeline.

### Folder structure

Main folder structure of project

```
├── src
│   ├── template_dl_tutorial
│   │   ├── components										Core functionality of each step
│   │ 	├── config												Load or prepare entity for each steps
│   │ 	├── constants											Constants across steps
│   │ 	├── entity												Entity property of each step
│   │ 	├── pipeline
│   │ 	├── utils
├── model																	Store final trained model
│   ├── model.h5
├── config
│   ├── config.yaml												Config read and write directory across training steps
├── research 															Try out code about correspond steps
│   ├── 01_data_ingestion.ipynb
│   ├── 02_prepare_base_model.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_model_evaluation.ipynb
├── template															HTML template for UI of predict result by upload an image.
│   ├── index.html
├── requirements.txt  										Dependency management file
├── main.py																Main steps of training model
├── app.py																Flask route to render html file in template
├── template.py														Setup project folder structure by it
├── setup.py															Setup project metadata
└── .gitignore

```

### Workflow to create a new component/step

1. Update config.yaml
2. Update secretes.yaml(Optional)
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

### Issues

1. It could not register model in mlflow

### Reference

[Complete End to End Deep Learning Project With MLFLOW,DVC And Deployment](https://www.youtube.com/watch?v=86BKEv0X2xU)
