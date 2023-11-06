# 1) Imprima o schema do dataframe gerado no passo anterior.

data_frame = df.toDF()
data_frame.printSchema()

"""root
 |-- nome: string (nullable = true)
 |-- sexo: string (nullable = true)
 |-- total: string (nullable = true)
 |-- ano: string (nullable = true)"""

# 2) Escrever o código necessário para alterar a caixa dos valores da coluna nome para MAIÚSCULO.

data_frame = df.toDF()
data_frame = data_frame.withColumn("nome_upper", upper(data_frame["nome"]))
data_frame.show()

"""
+---------+----+-----+----+----------+
|     nome|sexo|total| ano|nome_upper|
+---------+----+-----+----+----------+
| Jennifer|   F|54336|1983|  JENNIFER|
|  Jessica|   F|45278|1983|   JESSICA|
|   Amanda|   F|33752|1983|    AMANDA|
|   Ashley|   F|33292|1983|    ASHLEY|
|    Sarah|   F|27228|1983|     SARAH|
|  Melissa|   F|23472|1983|   MELISSA|
|   Nicole|   F|22392|1983|    NICOLE|
|Stephanie|   F|22323|1983| STEPHANIE|
|  Heather|   F|20749|1983|   HEATHER|
|Elizabeth|   F|19838|1983| ELIZABETH|
|  Crystal|   F|17904|1983|   CRYSTAL|
|      Amy|   F|17095|1983|       AMY|
| Michelle|   F|16828|1983|  MICHELLE|
|  Tiffany|   F|15960|1983|   TIFFANY|
| Kimberly|   F|15374|1983|  KIMBERLY|
|Christina|   F|15359|1983| CHRISTINA|
|    Amber|   F|14886|1983|     AMBER|
|     Erin|   F|14835|1983|      ERIN|
|  Rebecca|   F|14711|1983|   REBECCA|
|   Rachel|   F|14588|1983|    RACHEL|
+---------+----+-----+----+----------+
only showing top 20 rows"""

# 3) Imprimir a contagem de linhas presentes no dataframe.

countagem_de_linhas = df.count()
print("Contagem de linhas:", countagem_de_linhas)

"Contagem de linhas: 1825433"

# 4) Imprimir a contagem de nomes, agrupando os dados do dataframe pelas colunas ano e sexo.Ordene os dados de modo que o ano mais recente apareça como primeiro registro do dataframe.

data_frame = df.toDF()
contagem_nome_sexo_ano = data_frame.groupBy(["ano", "sexo"]).count()
contagem_nome_sexo_ano.orderBy("ano", ascending=False).show()

"""
+----+----+-----+
| ano|sexo|count|
+----+----+-----+
|2014|   M|13977|
|2014|   F|19067|
|2013|   F|19191|
|2013|   M|14012|
|2012|   M|14216|
|2012|   F|19468|
|2011|   F|19540|
|2011|   M|14329|
|2010|   F|19800|
|2010|   M|14241|
|2009|   F|20165|
|2009|   M|14519|
|2008|   F|20439|
|2008|   M|14606|
|2007|   M|14383|
|2007|   F|20548|
|2006|   F|20043|
|2006|   M|14026|
|2005|   M|13358|
|2005|   F|19175|
+----+----+-----+
only showing top 20 rows"""

# 5) Apresentar qual foi o nome feminino com mais registros e em que ano ocorreu.

"Nome feminino com mais registros: Nicole em 1983"

nome_fem_com_mais_registros = data_frame.filter(data_frame["sexo"] == "F").groupBy("nome", "ano").count().orderBy("count", ascending=False).first()
print("Nome feminino com mais registros:", nome_fem_com_mais_registros.nome, "em", nome_fem_com_mais_registros.ano)

# 6)  qual foi o nome masculino com mais registros e em que ano ocorreu.

"Nome masculino com mais registros: Joshua em 1983"

nome_masc_com_mais_registro = data_frame.filter(data_frame["sexo"] == "M").groupBy("nome", "ano").count().orderBy("count", ascending=False).first()
print("Nome feminino com mais registros:", nome_masc_com_mais_registro.nome, "em", nome_masc_com_mais_registro.ano)

# 7) Apresentar o total de registros (masculinos e femininos) para cada ano presente no dataframe.Considere apenas as primeiras 10 linhas, ordenadas pelo ano, de forma crescente.
data_frame = df.toDF()
resultado = data_frame.groupBy("ano", "sexo").agg(count("*").alias("total_registros")).orderBy("ano")
resultado.show()
"""
+----+----+---------------+
| ano|sexo|total_registros|
+----+----+---------------+
|1880|   M|           1058|
|1880|   F|            942|
|1881|   M|            997|
|1881|   F|            938|
|1882|   F|           1028|
|1882|   M|           1099|
|1883|   F|           1054|
|1883|   M|           1030|
|1884|   M|           1125|
|1884|   F|           1172|
|1885|   F|           1197|
|1885|   M|           1097|
|1886|   M|           1110|
|1886|   F|           1282|
|1887|   M|           1067|
|1887|   F|           1306|
|1888|   F|           1474|
|1888|   M|           1177|
|1889|   M|           1111|
|1889|   F|           1479|
+----+----+---------------+
only showing top 20 rows"""

# 8) Escrever o conteúdo do dataframe com os valores de nome em maiúsculo no S3.
"""Atenção aos requisitos:
A gravação deve ocorrer no subdiretório frequencia_registro_nomes_eua do paths3://<BUCKET>/lab-glue/O formato deve ser JSONO particionamento deverá ser realizado pelas colunas sexo e ano (nesta ordem)"""

data_frame = df.toDF()
data_frame = data_frame.withColumn("nome_upper", upper(data_frame["nome"]))
conversao = DynamicFrame.fromDF(data_frame, glueContext, "conversao" )

"""
{"nome":"Mary","total":"7065","nome_upper":"MARY"}
{"nome":"Anna","total":"2604","nome_upper":"ANNA"}
{"nome":"Emma","total":"2003","nome_upper":"EMMA"}
{"nome":"Elizabeth","total":"1939","nome_upper":"ELIZABETH"}
{"nome":"Minnie","total":"1746","nome_upper":"MINNIE"}
{"nome":"Margaret","total":"1578","nome_upper":"MARGARET"}
{"nome":"Ida","total":"1472","nome_upper":"IDA"}
"""
