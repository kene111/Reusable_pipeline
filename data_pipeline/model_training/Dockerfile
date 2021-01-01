FROM python:3.8.4
WORKDIR /model_training
RUN pip install -U scikit-learn numpy pandas
COPY model_training.py /model_training
ENTRYPOINT [ "python", "model_training.py" ]