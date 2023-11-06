# Processo Refined:

Na tarefa da modelagem relacional, pude entender tabelas Dimensão e Fato. Relembrei sobre o modelo lógico que aprendi nas aulas de Banco de Dados na faculdade, com esses conceitos em mente o primeiro passo foi criar um Modelo Lógico Dimensional das minhas tabelas de acordo com a Análise do meu projeto final. (A explicação da análise que farei no projeto e todo o estudo de caso, encontra-se na sprint 8 em um arquivo Análise.txt.)

![Modelo Lógico Análise](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/c4b49a66-72b2-4c13-959b-bb6a44ae5fdc)

Usarei a tabela ` dim_personagem ` contendo a maior explicação e a partir dela explicarei somente o que for necessário, para não repetir palavras. 

### Tabela dim_personagem:

O Script base usado foi o padrão disponibilizado na construção do Job no Glue/AWS. Importei algumas bibliotecas e funções que utilizei na tabela.

![Importação bibliotecas](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/4e1c1f11-0302-43f6-8d2f-7cbf07d22086)

Na etapa seguinte, utilizei o `spark.read.option` para abrir os arquivos Parquet, "movies.parquet" (originado do antigo "movies.csv") e "tmdb.json". Durante a sprint anterior, filtrei o arquivo JSON ("tmdb.json") da melhor maneira possível e organizei os dados para usá-lo como ponto de partida.

Em seguida, realizei um join entre os dataframes usando a coluna "ID", presente tanto no "tmdb.parquet" quanto no "movies.parquet". Essa conexão entre os dataframes foi fundamental para filtrar o "movies.parquet" apenas com os dados relevantes para minha consulta.

A partir do identificador ("ID") presente no dataframe "tmdb.parquet", selecionei as colunas desejadas no dataframe "movies.parquet", mantendo a correspondência com o ID.

Dessa forma, pude obter no dataframe "movies.parquet" somente os dados que eram relevantes para a minha análise, garantindo um conjunto de dados mais adequado e reduzindo o volume de informações desnecessárias.

![Filtrando os DataFrames](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/9e7b9ed6-f218-4deb-89dd-97053b9e1d7c)


O próximo passo foi criar uma nova coluna de "ID" para a tabela resultante, usando como base o ID do filme do arquivo "tmdb.parquet". Segue abaixo o passo a passo:

1. `window = Window.orderBy("id")`: É criada uma janela de ordenação chamada "window" com base na coluna "id" do DataFrame.
2. `df_analise_final = df_analise_final.withColumn("row_number", row_number().over(window))`: Uma nova coluna chamada "row_number" é adicionada ao DataFrame `df_analise_final`, atribuindo um número de linha sequencial único para cada registro, levando em consideração a ordenação definida na janela "window". Na sprint 8 teve um exercício com spark onde distribuíamos valores as tabelas de maneira proporcional, então apliquei a lógica nesse caso, adaptando para situação.
3. `df_analise_final = df_analise_final.withColumn("id_personagem", concat(lit("P0"), col("row_number"))).drop("row_number")`: É criada uma nova coluna chamada "id_personagem" no DataFrame `df_analise_final`, que concatena a string "P0" com o valor da coluna "row_number". Em seguida, a coluna "row_number" é removida do DataFrame.

Em resumo, esses códigos adicionam uma nova coluna chamada "id_personagem" ao DataFrame `df_analise_final`, que contém um identificador único para cada registro. Esse identificador é obtido a partir de uma numeração sequencial baseada na coluna "id", adicionando a string "P0" antes do número de linha.

![Criiando ID](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/55a9c6b3-9025-4fc0-9724-36a6abbac492)

Em seguida renomeio as colunas presentes no “dataframe” e com o “select” posso organizar as colunas em um novo “dataframe”. Posteriormente o comando `spark.sql("use projetofinalmarina")` é usado para definir o banco de dados padrão a ser utilizado nas consultas SQL executadas no Spark, `df_dim_personagem.coalesce(1).write.saveAsTable(name="dim_personagem",mode="overwrite",path='s3://data-lake-marina/Refined/DimpersonagemAnalise/',format="parquet")` fica responsável por criar a tabela (contida no DF) no BD e mandar o arquivo para o bucket s3 em formato parquet.

![Finalizando script](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/47cb0906-f3d5-4457-8cd6-fd28d16e19d7)

### Tabela fato_info_filme

Basicamente utilizei o mesmo script adaptando somente o necessário. Vale a pena ressaltar que criei a coluna lucro_filme já com a operação realizada (receita_filme - orcamento_filme). 

![lucro filme](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/129b0ba1-b52e-442f-9d36-34f79e3c38e1)

### Tabela dim_filmes

O script foi o mesmo, adpatado para o que foi necessário. A coluna `id_filme` permaneceu a mesma do movies.parquet e tmdb.parquet, ela esta presente nas três tabelas permitindo assim o `join` entre as mesmas no Athena. 


### Tabelas Views

Na próxima sprint irei criar Views com as operações necessarias para mostrar no Amazon Quick Sight. 

![Views](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/7fd4c370-4b8a-4d64-8efd-08c676b90812)


### Modelo utilizado Snow Flake

Acho interessante a ideia de trazer o personagem e o nome do artista sobre determinado filme para comprovar alguma análise, por exemplo "Os artistas principais de Raya e o ultimo dragão são: ....", mas não achei válido trazer esse dado para a tabela fato. Partindo desse princípio eu utilizei o snow flake pois permite que dimensões conectem-se e depois seja ligado a tabela fato. 
Posso trazer por exemplo "os personagem do filme que obteve mais lucro", fiz uma querie para poder comprovar minha tese e realmente retornou o que era desejado:

`SELECT d.id_filme, d.titulo_principal, p.id_personagem, p.personagem_filme, p.nome_artista, f.lucro_filme
FROM dim_filmes d
JOIN dim_personagem p ON d.id_filme = p.id_filme
JOIN (
    SELECT id_filme, MAX(lucro_filme) AS max_lucro
    FROM fato_info_filme
    GROUP BY id_filme
) max_f ON d.id_filme = max_f.id_filme
JOIN fato_info_filme f ON d.id_filme = f.id_filme AND f.lucro_filme = max_f.max_lucro
ORDER BY f.lucro_filme DESC;
`
![Comprovando querie](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/fc928a5b-0e48-406c-8994-02bb354666b8)

A ideia da dim_personagem é interessante pois posso criar análises entre as dimensões como por exemplo: "Quero saber os personagens do filme homem aranha no aranhaverso, porque o cliente deseja saber os atores principais do filme." Outro fato é que como comprovado acima posso trazer outras analises com as três tabelas se relacionando pelo id_filme.

Eu só utilizei esse modelo ("snow flake") porque são poucos dados, entendi que as queries serão mais trabalhosas e talvez os resultados demorem um pouco a mais, entretanto como são 03 tabelas, duas com 20 linhas e uma com 80 linhas pude continuar com esse modelo. Em uma análise com mais tabelas e maior quantidade de dados não é recomendado esse tipo de modelo.

## Conclusão

O script teve um modelo padrão e foi adaptado de acordo com a necessidade de criação das tabelas. Esse processo foi muito enriquecedor, como havia desenvolvido  a lógica e o código feito na sprint 8 para extração de dados, e também sabia exatamente como meu projeto funcionaria, ficou mais fácil adaptar o script spark. 

OBS: O grande desafio da sprint foi descobrir o comando que salvaria as tabelas no glue catalog, mas a mentora Dilmara descobriu uma maneira de ajudar e com isso toda squad pode seguir, deixo registrado minha gratidão!