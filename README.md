## Introduction

### Prepare

1. It needs to setup environment to integrate dagshub and mlflow.
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

### Folder structure

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

### Reference
