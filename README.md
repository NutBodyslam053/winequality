# MLOps Project: Wine Quality

## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

# How to run?
### STEP 00: Clone the repository
```bash
https://github.com/NutBodyslam053/winequality
```
### STEP 01: Create a conda environment after opening the repository
```bash
conda create -n mlproj python=3.9 -y
```
```bash
conda activate mlproj
```

### STEP 02: Install the requirements
```bash
pip install -r requirements.txt
```
```bash
# Finally run the following command
python app.py
```
Now, open up you local host and port

## MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/NutBodyslam053/winequality.mlflow \
MLFLOW_TRACKING_USERNAME=NutBodyslam053 \
MLFLOW_TRACKING_PASSWORD=b85bafd69d98861fee89f5bf70dc5f62cf41c2e5 \
python script.py

#### Run this to export as env variables:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/NutBodyslam053/winequality.mlflow
export MLFLOW_TRACKING_USERNAME=NutBodyslam053
export MLFLOW_TRACKING_PASSWORD=b85bafd69d98861fee89f5bf70dc5f62cf41c2e5
```