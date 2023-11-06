# Modelagem Relacional

## Tabela TbCliente:

### Está na 1FN, 2FN e 3FN.
Possui chave primária única (IdCliente) e campos atômicos (NomeCliente, CidadeCliente, EstadoCliente, PaisCliente).

## Tabela TbCarro:

Está na 1FN, 2FN e 3FN.
Possui chave primária única (IdCarro), campos atômicos (ModeloCarro, AnoCarro, MarcaCarro, ClassiCarro) e uma chave estrangeira (IdCombustivel) referenciando a tabela TbCombustivel.

## Tabela TbCombustivel:

### Está na 1FN, 2FN e 3FN.
Possui chave primária única (IdCombustivel) e campo atômico (TipoCombustivel).

## Tabela TbVendedor:

### Está na 1FN, 2FN e 3FN.
Possui chave primária única (IdVendedor) e campos atômicos (NomeVendedor, SexoVendedor, EstadoVendedor).

## Tabela TbLocacao:

### Está na 1FN, 2FN e 3FN.
Possui chave primária única (IdLocacao), campos atômicos (DataLocacao, HoraLocacao, QtdDiaria, VlrDiaria, DataEntrega, HoraEntrega, KmCarro) e chaves estrangeiras (IdCliente, IdCarro, IdVendedor) referenciando as tabelas TbCliente, TbCarro e TbVendedor, respectivamente.

Em resumo, todas as tabelas estão normalizadas até a Terceira Forma Normal (3FN). Elas possuem chaves primárias únicas, não apresentam dependências parciais ou transitivas, e os campos estão atomicamente armazenados em locais específicos. Isso garante a integridade dos dados e facilita consultas e manipulações eficientes no banco de dados.
Segue abaixo um exemplo de Modelo Lógico Relacional:

![Modelo Lógico Relacional](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/fcaaaf44-6c05-41d3-9d79-432a343f3ab1)

# Modelagem Dimensional

Tabelas Dimensões e Fatos criadas a partir do modelo relacional. No video explicativo da atividade, foi deixado claro que no dia-a-dia não usaremos as Views, teriamos que ter as tabelas Dimensões e Fato armazenadas fisicamente, mas que para fins educativos seria permitido fazer a modelagem dimensional criando as views.
No entanto eu quis criar as tabelas sem as Views (para ver como funciona), e depois criei as views a partir das Dim's e Fato já criadas. 

As tabelas DimCliente, DimCarro, DimCombustivel e DimVendedor são as tabelas de dimensão, e a tabela FatoLocacao é a tabela de fato.

Nas tabelas de dimensão, é armazenado as informações descritivas e os atributos relevantes sobre cada dimensão. Cada tabela de dimensão tem uma chave primária (por exemplo, IdCliente, IdCarro, IdCombustivel, IdVendedor) e outras colunas que fornecem detalhes sobre os membros da dimensão.

A tabela de fato (FatoLocacao) contém as métricas e medidas relacionadas às transações ou eventos do negócio. Ela faz referência às tabelas de dimensão por meio de chaves estrangeiras (por exemplo, IdCliente, IdCarro, IdVendedor), permitindo a análise multidimensional e a combinação de dados de diferentes dimensões.

Segue abaixo a representação do Modelo Lógico Dimensional:

![Modelo Lógico Dimensional](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/d6c4894d-78b0-4935-b9c7-344f335859e9)

Também fiz um modelo lógico paras as views criadas a partir da Modelagem Dimensional:

![Modelo Lógico View](https://github.com/MarinaRBueno/Repo_Compass_uol_MarinaRBueno/assets/125372666/ec78b95b-6b2a-40ce-944d-2039306029f8)

