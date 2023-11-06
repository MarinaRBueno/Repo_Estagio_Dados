# Relatório do Desafio: Filmes/Animações Multiculturais

## Justificativa

O tema escolhido para este desafio foi "Filmes/Animações Multiculturais: Uma Janela para o Mundo - Explorando Diversidade e Sucesso Financeiro". A ideia por trás dessa escolha é destacar filmes que abordam a diversidade cultural e foram bem-sucedidos financeiramente. Considerando que a Compass é a favor da diversidade, essa temática se alinha aos valores da empresa.

## Passo a Passo do Projeto

1. Filtro dos filmes desejados: Utilizando o arquivo "movies.csv" armazenado no bucket, foram selecionados os filmes desejados. Para isso, foi aplicado um filtro na coluna "tituloPrincipal".
Sprint 6 desafio lambda, contribuiu para essa etapa.

![Config Bucket](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/b577cfda-8459-43fd-a0eb-fc5e3d67bc27)

2. Análise das colunas selecionadas: Com base nos filmes selecionados, algumas colunas do arquivo "movies.csv" foram consideradas relevantes para a análise. Um exemplo é a coluna "id", que foi utilizada para identificar de forma única cada filme. Além disso, foram removidos os duplicados de "id" e "tituloPrincipal" para evitar informações repetidas. Também foi aplicado o critério de que o gênero do filme contivesse a palavra "Animation".
Sprint 7 desafio do pandas contribuiu para essa etapa.

![Filtrando Movies](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/fcf0f335-139a-469d-bbb5-65bf0e2c2c59)

3. Utilização do endpoint do TMDB: Observou-se que os IDs(IMDB) dos filmes presentes no arquivo "movies.csv" correspondiam aos IDs utilizados no TMDB. Portanto, foi utilizado o endpoint do TMDB para obter informações adicionais sobre os filmes, como orçamento, receita e popularidade. Esses dados foram obtidos por meio de pesquisas utilizando os IDs dos filmes presentes no arquivo.
Sprint 8 exercicío TMDB contribuiu para essa etapa, o script fornecido serviu como base.

![Endpoint TMDB](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/fa780c33-9a4f-4f35-bc7d-4302d516882a)

![Filmes por id](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/706423f4-925e-4d9f-8cc6-66825bfb6a93)

![id imdb](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/79e49d7a-288c-404b-98f8-8be016e856df)

4. Filtragem dos dados obtidos: Utilizando um loop, os dados de cada filme foram analisados. Apenas os filmes com orçamento, receita e popularidade maiores do que zero foram selecionados. Os dados relevantes, como título, orçamento, receita e popularidade, foram salvos em um dicionário e depois adicionados em uma lista.
Sprint 3 introdução ao python e os exercicícios contribuiram para essa etapa.

![Filtrando Dados API (2)](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/1ec96876-1318-4d85-825e-0381a51fa3ad)

5. Salvando o resultado em memória: Devido ao uso do lambda, não era possível salvar os arquivos localmente. Portanto, o resultado foi armazenado em memória, em formato JSON, em uma variável.
Mentor Augusto nos deu a dica de usar variáveis e sprint 6 desafio lambda contribuiram para essa etapa. 

![Salvando Json](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/9bb3a09f-3fb3-42bb-9200-8eccf75804a7)

6. Envio do arquivo para o bucket: Utilizando a função `put_object`, o arquivo em formato JSON foi enviado para o bucket. Essa função permite enviar o conteúdo do objeto a partir de uma variável, sem a necessidade de um arquivo local.
Sprint 7 desafio ETL contribuiu para a conclusão dessa etapa.

![Envio ao bucket](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/66b37129-01aa-46fc-8275-6d54f8c244b7)

## Conclusão

O projeto teve como objetivo selecionar filmes/animações multiculturais bem-sucedidos financeiramente e destacar a importância da diversidade cultural. Utilizando o arquivo "movies.csv", foram aplicados filtros e consultas na API do TMDB para obter informações adicionais. O resultado final foi armazenado em memória e enviado para o bucket utilizando a função `put_object`. Essa etapa abrangeu a construção do tema a ser trabalhado, bem como a extração de dados da API do TMDB com base nesse tema.

OBS: Tive um problema na conversão do json para o parquet, então tive que fazer uma pequena alteração no código, coloquei uma lista vazia e depois fui adicionando as informações da API dentro da lista. O id do filme também entrou na lista, foram práticas necessárias para seguir na Trusted e Refined.