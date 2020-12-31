FROM python:3.8.4

WORKDIR /data_pipeline

RUN pip install -U scikit-learn numpy pandas

COPY model_training.py ./model_training.py

ENTRYPOINT [ "python", "model_training.py" ]