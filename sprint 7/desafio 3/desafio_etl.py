import boto3

from datetime import datetime


s3 = boto3.client('s3',
                   aws_access_key_id='CHAVE DE ACESSO',
                   aws_secret_access_key='CHAVE SECRETA',
                   region_name='us-east-1')

data_atual = datetime.now()
datas = f'{data_atual.year}/{data_atual.month}/{data_atual.day}'

s3.upload_file('movies.csv', 'data-lake-marina', f'Raw/Local/CSV/Movies/{datas}/movies.csv')
s3.upload_file('series.csv', 'data-lake-marina', f'Raw/Local/CSV/Series/{datas}/series.csv')
