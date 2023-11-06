import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, row_number, concat, lit
from pyspark.sql.window import Window

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Abre o parquet do movies da pasta Trusted
df_filmes_fixo = spark.read.option("header", "true").option("inferSchema", "true").parquet('s3://data-lake-marina/Trusted/Movies/part-00000-f58a830c-2e58-4f2f-84d1-4cba1d4643bc-c000.snappy.parquet')

# Abre o parquet dos dados da TMDB
df_analise = spark.read.option("header", "true").option("inferSchema", "true").parquet('s3://data-lake-marina/Trusted/TMDB/2023/06/12/part-00000-7c6d7e64-1782-413d-880b-92c22317f52a-c000.snappy.parquet')

# Filtra a coluna ID dos dados TMDB
df_analise_ids = df_analise.select('id')

# Faz o Join com o movies procurando os filmes pelo ID
df = df_filmes_fixo.join(df_analise_ids, df_filmes_fixo['id'] == df_analise_ids['id'], 'inner').dropDuplicates(['id'])

# Seleciona as colunas especificas de acordo com o join
df_fato_analise_final = df.select(df_filmes_fixo['id'], 'notaMedia', 'numeroVotos')

# Junta o DF novo com algumas colunas do DF que contém dados da API
df_fato_analise_final = df_fato_analise_final.join(df_analise.select('id', 'orcamento', 'receita', 'popularidade'), 'id', 'inner')

# Renomeia as colunas que serão visualizadas no ATHENA
df_fato_analise_final = df_fato_analise_final.withColumnRenamed('id', 'id_filme').withColumnRenamed('notaMedia', 'nota_media').withColumnRenamed('numeroVotos', 'numero_votos').withColumnRenamed('orcamento', 'orcamento_filme').withColumnRenamed('receita', 'receita_filme').withColumnRenamed('popularidade', 'popularidade_filme')

# Adiciona uma coluna com o lucro dos filmes
df_fato_analise_final = df_fato_analise_final.withColumn('lucro_filme', col('receita_filme') - col('orcamento_filme'))


window = Window.orderBy("id_filme")
df_fato_analise_final = df_fato_analise_final.withColumn("row_number", row_number().over(window))

# Cria uma nova coluna de "id_info_filme" concatenando a string "IF0" com o/
# valor da coluna "row_number" e exclui a mesma.
df_fato_analise_final = df_fato_analise_final.withColumn("id_info_filme", concat(lit("IF0"), col("row_number"))).drop("row_number")

# Seleciona as colunas na ordem necessária
df_fato_fixa = df_fato_analise_final.select("id_info_filme", "id_filme", "nota_media", "numero_votos", "orcamento_filme", "receita_filme", "popularidade_filme", "lucro_filme")

# Usa o banco de dados criado
spark.sql("use projetofinalmarina")

# particiona o df em 1, salva o arquivo parquet e cria a tabela no BD
df_fato_fixa.coalesce(1).write.saveAsTable(name="fato_info_filme",mode="overwrite",path='s3://data-lake-marina/Refined/FatoFilmesAnalise/',format="parquet")

job.commit()
