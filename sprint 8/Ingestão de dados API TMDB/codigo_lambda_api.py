import pandas as pd
import requests
import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    s3_client = boto3.client('s3',
                   aws_access_key_id='CHAVE DE ACESSO',
                   aws_secret_access_key='CHAVE SECRETA',
                   region_name='us-east-1')

    # Informações das credenciais AWS e onde buscar o arquivo csv para
    # extrair os ids dos filmes para buscar na API

    bucket_name = 'data-lake-marina'
    s3_file_name = 'Raw/Local/CSV/Movies/2023/5/15/movies.csv'
    objeto = s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    filmes = pd.read_csv(objeto['Body'], sep='|')
    # Lê o arquivo movies.csv colocando como separador o |

    filmes_selecionados = ['Moana', 'Pocahontas', 'Spider-Man: Into the Spider-Verse', 'The Princess and the Frog', 'Mulan', 'Raya and the Last Dragon', 'Frozen', 'Aladdin', 'Spirited Away', 'Encanto', 'Turning Red', 'Coco', 'Anastasia', 'The Jungle Book', 'Lilo & Stitch', 'Atlantis: The Lost Empire', 'Brave', "The Emperor's New Groove", 'The Road to El Dorado', 'The Hunchback of Notre Dame']
    # Titulos de filmes ecolhidos do movies.csv p/ pesquisa

    filtrando_filmes = filmes[filmes['tituloPincipal'].isin(filmes_selecionados)]
    # Usando como base filmes_selecionados p/ buscar os titulos no movies.cvs

    df = filtrando_filmes[['id', 'genero', 'tituloPincipal', 'tituloOriginal', 'anoLancamento', 'notaMedia', 'personagem', 'nomeArtista', 'titulosMaisConhecidos']]
    # Um novo df com base nos titulos selecionados e com as colunas que
    # serão abordados mais a frente, para já ter uma noção na sprint 9

    id_unicos = df.drop_duplicates(subset=['id'])
    # Retirar duplicados com base no id e titulo principal

    df_animacao = id_unicos[df['genero'].str.contains('Animation')]
    # Somente filmes com Animation na coluna genero

    filmes_info_O_R_P = []
    # Lista vazia para armazenar valores que virão da API

    API_KEY = 'CHAVE SECRETA API'
    # Chave API

    for id_film in df_animacao['id']:
        # Fazer a requisição para obter as informações do filme com base no ID
        url = f"https://api.themoviedb.org/3/movie/{id_film}?api_key={API_KEY}"
        resposta = requests.get(url)

        # Verificar se a resposta foi bem-sucedida (código 200)
        if resposta.status_code == 200:
            # Acesso às informações do filme no formato JSON
            filme_informacoes = resposta.json()

            # Acesso às informações específicas do filme
            titulo = filme_informacoes['title']
            orcamento = filme_informacoes['budget']
            receita = filme_informacoes['revenue']
            popularidade = filme_informacoes['popularity']

            if orcamento > 0 and receita > 0 and popularidade > 0:
                # informações com valores acima de 0
                filme_info = {
                    'id': id_film,
                    'tituloPrincipal': titulo,
                    'orcamento': orcamento,
                    'receita': receita,
                    'popularidade': popularidade,
                }
                filmes_info_O_R_P.append(filme_info)
                # Adiciona o dicionário a lista
            else:
                print(f"O filme com o ID {id_film} e {titulo} possui valores indesejados (orcamento={orcamento}, receita={receita}, popularidade={popularidade})")
        else:
            print(f"Não foi possível obter as informações do filme com o ID {id_film}")

        json_filmes_info_O_R_P = json.dumps(filmes_info_O_R_P)
        # Salvando a lista no formato Json em memória

        data_atual = datetime.now()
        datas = f'{data_atual.year}/{data_atual.month}/{data_atual.day}'
        # Datas para organizar as pastas no Bucket

        caminho_filmes_s3 = f"Raw/API/TMDB/JSON/Orcamento_Receita_Popularidade/{datas}/json_filmes_info_O_R_P.json"
        # Caminho das pastas que armazenaram o arquivo

        s3_client.put_object(Body=json_filmes_info_O_R_P, Bucket=bucket_name, Key=caminho_filmes_s3)
        # Enviando Json ao Bucket

    return {
            'statusCode': 200,
            'body': "Operação feita com sucesso."
        }
