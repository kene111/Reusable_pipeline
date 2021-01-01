FROM python:3.8.4
WORKDIR /model_testing
RUN pip install -U scikit-learn numpy 
COPY model_test.py /model_testing
ENTRYPOINT [ "python", "model_test.py" ]
 