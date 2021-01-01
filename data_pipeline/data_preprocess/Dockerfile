FROM python:3.8.4
WORKDIR /data_preprocess
RUN pip install -U scikit-learn numpy pandas
COPY preprocess.py /data_preprocess
ENTRYPOINT [ "python", "preprocess.py" ]
