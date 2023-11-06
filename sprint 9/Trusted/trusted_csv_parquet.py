import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Lê os arquivos
df_movies_csv = spark.read.csv('s3://data-lake-marina/Raw/Local/CSV/Movies/2023/5/15/movies.csv', header=True, inferSchema=True, sep='|')
# Somente 1 arquivo parquet
df_movies_csv = df_movies_csv.repartition(1)
# Salva em parquet
df_movies_csv.write.parquet('s3://data-lake-marina/Trusted/Movies')

# Lê os arquivos
df_series_csv = spark.read.csv('s3://data-lake-marina/Raw/Local/CSV/Series/2023/5/15/series.csv', header=True, inferSchema=True, sep='|')
# Somente 1 arquivo parquet
df_series_csv = df_series_csv.repartition(1)
# Escreve o arquivo parquet
df_series_csv.write.parquet('s3://data-lake-marina/Trusted/Series')


job.commit()
