FROM python:3.9-slim

WORKDIR /app

COPY desafio_etl.py /app/
COPY "movies.csv" /app/
COPY "series.csv" /app/

RUN pip install boto3

CMD ["python", "desafio_etl.py"]

