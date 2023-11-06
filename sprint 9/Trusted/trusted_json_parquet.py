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

# Lê os arquivos json
df_movies_api = spark.read.json('s3://data-lake-marina/Raw/API/TMDB/JSON/Orcamento_Receita_Popularidade/2023/6/12/json_filmes_info_O_R_P.json')

# Escreve o arquivo parquet
df_movies_api.write.parquet('s3://data-lake-marina/Trusted/TMDB/2023/06/12')

job.commit()
