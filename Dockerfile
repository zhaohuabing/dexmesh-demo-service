FROM python:2.7-slim

ENV VERSION "1.0"

COPY demo.py /

RUN pip install --user flask flask-jsonpify  flask-restful 

ENTRYPOINT ["python", "/demo.py"]
