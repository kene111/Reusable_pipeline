FROM python:3.8.4

WORKDIR /data_pipeline

RUN pip install -U scikit-learn numpy 

COPY model_test.py ./model_test.py

ENTRYPOINT [ "python", "model_test.py" ]