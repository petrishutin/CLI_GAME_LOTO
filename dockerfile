FROM python:3.7.7-slim

WORKDIR ./

COPY /* ./

RUN pip install -r requirements.txt

CMD python3 main.py