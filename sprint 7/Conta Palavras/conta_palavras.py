"""O primeiro teste foi feito com o conteúdo readme que foi disponibilizado
 na udemy, o segundo teste foi feito com um poema que continha 18 palavras.
 O terceiro teste foi feito com eu arquivo readme do github"""


from pyspark.sql import SparkSession
from pyspark.sql.functions import *


df = spark.read.text("README.md").selectExpr("explode(split(value, ' ')) as palavra").where("palavra != ''").groupBy("palavra").count()
conta_palavras_df = df.agg(sum("count")).head()[0]
df = df.withColumn("total_palavras", lit(conta_palavras_df))
df.show()
df.show(df.count(), truncate=False)
print("O total de palavras é: ", conta_palavras_df)
