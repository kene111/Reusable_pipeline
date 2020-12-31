FROM python:3.8.4

WORKDIR /data_pipeline

RUN pip install -U scikit-learn numpy pandas

COPY preprocess.py ./preprocess.py

ENTRYPOINT [ "python", "preprocess.py" ]