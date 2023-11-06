import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

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
df_temporario = df_filmes_fixo.join(df_analise_ids, df_filmes_fixo['id'] == df_analise_ids['id'], 'inner').dropDuplicates(['id'])

# Seleciona as colunas especificas de acordo com o join
df_dim_filme = df_temporario.select(df_filmes_fixo['id'], 'tituloPincipal', 'tituloOriginal', 'genero')

# Renomeia as colunas que serão visualizadas no ATHENA
df_dim_filme = df_dim_filme.withColumnRenamed('id', 'id_filme').withColumnRenamed('tituloPincipal', 'titulo_principal') .withColumnRenamed('tituloOriginal', 'titulo_original').withColumnRenamed('genero', 'genero_filme')

# Usa o banco de dados criado
spark.sql("use projetofinalmarina")

# particiona o df em 1, salva o arquivo parquet e cria a tabela no BD
df_dim_filme.coalesce(1).write.saveAsTable(name="dim_filmes",mode="overwrite",path='s3://data-lake-marina/Refined/DimFilmesAnalise/',format="parquet")

job.commit()
