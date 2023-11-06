from pyspark.sql import SparkSession
from pyspark.sql.functions import when, rand, lit


spark = SparkSession \
                .builder \
                .master("local[*]")\
                .appName("Exercicio Intro") \
                .getOrCreate()
# iniciando a sessão spark

df_nomes = spark.read.csv("C:/Caminho/do/arquivo/nomes_aleatorios.txt", header=False)
# importando arquivo txt de 10.000.000 de nomes

df_nomes.show(10)
# Mostrando os 10 primeiros nomes da coluna _c0

df_nomes.printSchema()
#  imprimindo o Schema

df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
# renomeando a coluna

df_nomes.show(10)
# apresenta o DF com 10 linhas

df_nomes.select("Nomes").show(10)
# seleciono somente a coluna que quero ver no DF

df_nomes.printSchema()
# imprimindo schema

df_nomes = df_nomes.withColumn("Escolaridade",
                               when(rand() < 1/3, lit("Fundamental"))
                               .when(rand() < 2/3, lit("Medio"))
                               .otherwise(lit("Superior")))

# when(condição, valor).otherwise(valor_padrao), funciona como um If no Python
# rand() < 1/3 é a condição gerada e se ela for verdadeira
# lit retorna o valor "fundamental" para a coluna
# otherwise age como um Else ou seja, se nenhuma condição when for verdadeira
# o valor padrão lit("Superior") é retornado

df_nomes.select("Escolaridade").show(10)
# estou usando o select somente para garantir que foi gerado o que pedi

paises = ["Brasil", "Argentina", "Colômbia", "Peru", "Venezuela", "Chile", "Equador",
          "Bolívia", "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]
# paises organizados em listas para dividi-los aleatóriamente a seguir

df_nomes = df_nomes.withColumn("Pais", when(rand() < 1/len(paises), lit(paises[0]))
                                      .when(rand() < 2/len(paises), lit(paises[1]))
                                      .when(rand() < 3/len(paises), lit(paises[2]))
                                      .when(rand() < 4/len(paises), lit(paises[3]))
                                      .when(rand() < 5/len(paises), lit(paises[4]))
                                      .when(rand() < 6/len(paises), lit(paises[5]))
                                      .when(rand() < 7/len(paises), lit(paises[6]))
                                      .when(rand() < 8/len(paises), lit(paises[7]))
                                      .when(rand() < 9/len(paises), lit(paises[8]))
                                      .when(rand() < 10/len(paises), lit(paises[9]))
                                      .when(rand() < 11/len(paises), lit(paises[10]))
                                      .when(rand() < 12/len(paises), lit(paises[11]))
                                      .otherwise(lit(paises[12])))


df_nomes.select("Pais").show(10)

df_nomes = df_nomes.withColumn("AnoNascimento", (rand() * (2010 - 1945 + 1) + 1945).cast("int"))
# adicionar coluna AnoNascimento com datas aleatórias

df_nomes.select("AnoNascimento").show(10)
df_nomes.show(30)

df_select = df_nomes.select("Nomes", "AnoNascimento").filter(df_nomes.AnoNascimento >= 2000).limit(10)
# selecionar colunas Nomes e AnoNascimento para conferir se veio acima de 2000

df_select.show()

df_select.show(100)
# somente se o .limit(10) não estiver no select

df_nomes.createOrReplaceTempView("pessoas")
# criando tabela temporária pessoas

spark.sql("SELECT Nomes, AnoNascimento FROM pessoas WHERE AnoNascimento >= 2000 LIMIT 10").show()
# utilizando sql para selecionar o que foi pedido da tabela temporária pessoas


df_millennials = df_nomes.select("AnoNascimento").filter(df_nomes.AnoNascimento.between(1980, 1994))
count_millennials = df_millennials.count()
# Pessoas de 1980 e 1994

print("Número de pessoas da geração Millennials:", count_millennials)

spark.sql("SELECT COUNT(*) FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").show()
# Pessoas entre 1980 e 1994

spark.sql('''
    SELECT Pais,
        CASE WHEN AnoNascimento BETWEEN 1944 AND 1964 THEN 'Baby Boomers'
             WHEN AnoNascimento BETWEEN 1965 AND 1979 THEN 'Geração X'
             WHEN AnoNascimento BETWEEN 1980 AND 1994 THEN 'Millennials'
             ELSE 'Geração Z'
        END AS Geracao,
        COUNT(*) AS Quantidade
    FROM pessoas
    GROUP BY Pais, Geracao
    ORDER BY Quantidade ASC
''').show(52)

# Quantidade de pessoas de cada país para uma das gerações
