# Use the official Jupyter PySpark Notebook image as the base image
FROM jupyter/pyspark-notebook:python-3.10.4

COPY jupyter_notebook_config.py /home/jovyan/.jupyter/

COPY requirements.txt /home/jovyan/work/

WORKDIR /home/jovyan/work
# Install boto3 and json packages
RUN pip install numpy pandas matplotlib seaborn scipy scikit-learn nbformat lightgbm h2o statsmodels xgboost statsforecast dash dash_bootstrap_components tbats