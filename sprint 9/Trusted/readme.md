## Transformação de Arquivos da Raw Zone para a Trusted Zone

Nesta etapa do processo, foi necessário transformar os arquivos da Raw Zone, que estavam no formato CSV, em arquivos no formato Parquet e armazená-los na Trusted Zone. Para isso, utilizei as instruções fornecidas no Glue Lab da sprint 7.

No job responsável pela transformação dos arquivos CSV em Parquet, mantive o script padrão do Spark que é fornecido ao criar o job. Realizei as alterações recomendadas de configuração de hardware para otimizar o desempenho do job.

![Script padrão glue](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/d9de0f45-afc1-48a5-be68-e0c514f0bff4)

O processo de transformação e armazenamento dos dados na Trusted Zone foi realizado a partir do ponto em que o job foi inicializado com a função `job.init(args['JOB_NAME'], args)`. Os passos executados foram os seguintes:

1. Criei dois DataFrames a partir dos arquivos CSV da Raw Zone.
2. Utilizei a função `repartition(1)` nos DataFrames para garantir que apenas um arquivo Parquet fosse gerado.
3. Em seguida, utilizei a função `write.parquet` para salvar os DataFrames no formato Parquet.
4. Os arquivos Parquet resultantes foram armazenados no bucket da AWS designado para a Trusted Zone.

![Spark job init](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/4194fe63-3551-43a7-9f09-a922b39bd9d7)

Obs: repeti o mesmo processo adaptando para o Json com os dados da TMDB;

## Conclusão
Essa transformação e armazenamento dos dados em um formato mais eficiente e seguro permite a utilização posterior dos dados na Trusted Zone, proporcionando melhor desempenho e facilitando a implementação de processos de análise e extração de informações.



