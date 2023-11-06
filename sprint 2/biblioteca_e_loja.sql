'Observei o DER, as tabelas criadas e os comandos para cria-las com o intuito de entender a relação entre chave primária e estrangeira, explorei o uso do Join,  do SGBD SQLite  (https://sqliteonline.com/) e sua sintaxe. O conteúdo do curso SQL contribui para fixar o conhecimento obtido na faculdade e mostrar possibilidades novas, a melhor parte do exercício foi a oportunidade de observar o DER e o banco de dados, extraindo deles as informações necessárias para realizar as consultas. 
O curso de lógica para programação que faço por fora, também contribuiu para entender a lógica que envolve as "queries".

Criação das tabelas do Schema Biblioteca:'

Tabela Autor:
CREATE TABLE autor (
  codautor int NOT NULL,
  nome varchar(90) NOT NULL,
  nascimento date NOT NULL,
  PRIMARY KEY (CodAutor)
)

Tabela Editora:
CREATE TABLE editora (
  codeditora int NOT NULL,
  nome varchar(90) DEFAULT NULL,
  endereco int DEFAULT NULL,
  PRIMARY KEY (codeditora),
  FOREIGN KEY (endereco) REFERENCES endereco (codendereco)
)

Tabela Endereco:
CREATE TABLE endereco (
  codendereco int NOT NULL,
  pais varchar(90) DEFAULT NULL,
  estado varchar(90) DEFAULT NULL,
  cidade varchar(90) DEFAULT NULL,
  PRIMARY KEY (codendereco)
)

Tabela Livro: 
CREATE TABLE livro (
  cod int NOT NULL,
  titulo varchar(90) NOT NULL,
  autor int NOT NULL,
  editora int NOT NULL,
  valor float DEFAULT NULL,
  publicacao date DEFAULT NULL,
  edicao varchar(20) DEFAULT NULL,
  idioma varchar(20) DEFAULT 'Português',
  primary KEY (cod),
  FOREIGN KEY (Autor) REFERENCES autor (codautor),
  FOREIGN KEY (Editora) REFERENCES editora (codeditora)
)

Exercícios e resoluções:


'1 )Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas. 
 Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma'

SELECT *
FROM livro
WHERE publicacao > '2014-31-12'
ORDER BY cod;


'2 )Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.
 Atenção às colunas esperadas no resultado final:  titulo, valor.'

SELECT titulo, valor
FROM livro
ORDER BY valor DESC
LIMIT (10);

'3) Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. 
Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.'

SELECT DISTINCT COUNT(p.editora) AS quantidade, 
r.nome, q.estado, q.cidade
FROM livro as p 
INNER JOIN editora AS r
ON r.codeditora = p.editora
INNER JOIN endereco AS q
ON r.endereco = q.codendereco
Group BY p.editora
ORDER BY quantidade desc 
LIMIT (5);

'4)Apresente a query para listar a quantidade de livros publicada por cada autor. 
Ordenar as linhas pela coluna nome (autor), em ordem crescente. 
Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).'

SELECT p.nome,p.codAutor, p.nascimento,
COUNT (q.autor) AS quantidade
FROM autor AS p 
LEFT JOIN livro AS q 
ON p.codAutor = q.autor 
Group BY p.nome 
Order BY p.nome;

'5)Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
 Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.'

SELECT DISTINCT p.nome 
FROM autor AS p
INNER join livro AS q 
ON p.codautor = q.autor
INNER JOIN editora AS s
ON s.codeditora = q.editora
INNER JOIN endereco AS t
ON t.codendereco = s.endereco
WHERE estado <> 'PARANÁ' OR 'RIO GRANDE DO SUL' 
ORDER BY p.nome;

'6)Apresente a query para listar o autor com maior número de livros publicados. 
O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.'

SELECT p.codAutor, p.nome,
COUNT(q.autor) as quantidade_publicacoes
FROM autor AS p 
LEFT JOIN livro AS q 
ON p.codAutor = q.autor 
GROUP BY p.nome 
ORDER By  quantidade_publicacoes DESC 
LIMIT (1);

'7)Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.'

SELECT p.nome
FROM autor AS p
LEFT JOIN livro as q
ON p.codautor = q.autor
WHERE q.autor ISNULL;

Criação do Schema Loja:

CREATE TABLE tbdependente (
  cddep int not null,
  nmdep varchar(20) default null,
  dtnasc datetime default null,
  sxdep varchar(10) default null,
  cdvdd int default null,
  inepescola varchar(10) default null,
  primary key (cddep), 
  foreign key (cdvdd) references tbvendedor (cdvdd)
)

CREATE TABLE tbestoqueproduto (
  cdpro int not null,
  qtdpro int default null,
  status varchar(15) default null,
  primary key (cdpro)
)

CREATE TABLE tbvendas (
  cdven int not null,
  dtven datetime default null,
  cdcli int default null,
  nmcli varchar(100) default null,
  cidade varchar(45) default null,
  estado varchar(45) default null,
  pais varchar(45) default null,
  cdpro int default null,
  nmpro varchar(45) default null,
  tppro varchar(5) default null,
  qtd int default null,
  und varchar(5) default null,
  vrunt decimal(19,2) default null,
  cdvdd int default null,
  cdcanalvendas int default null,
  nmcanalvendas varchar(20) default null,
  status varchar(15) default null,
  deletado char(1) default null,
  primary key (cdven),
  constraint fk_vendas_produto_estoque foreign key (cdpro) references tbestoqueproduto (cdpro),
  constraint fk_vendas_vendedor foreign key (cdvdd) references tbvendedor (cdvdd)
)

CREATE TABLE tbvendedor (
  cdvdd int not null,
  nmvdd varchar(20) default null,
  sxvdd int default null,
  perccomissao decimal(19,2) default null,
  primary key (cdvdd)
)

'8) Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.
 As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.'

SELECT p.cdvdd, p.nmvdd
FROM tbvendedor AS p
INNER JOIN tbvendas AS q
ON p.cdvdd = q.cdvdd
WHERE q.status = 'Concluído'
GROUP BY q.status
ORDER BY COUNT(q.status);

'9) Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, 
e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.'

SELECT p.cdpro, q.nmpro
FROM tbestoqueproduto AS p
INNER JOIN tbvendas AS q 
ON p.cdpro = q.cdpro
WHERE q.dtven BETWEEN '2014-02-03' AND '2018-02-02'
GROUP BY q.nmpro
ORDER BY COUNT(q.nmpro) DESC
LIMIT(1);

'10)A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. 
O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao.
O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.'

SELECT q.nmvdd AS vendedor, 
ROUND(SUM(p.qtd * p.vrunt) ,2) AS valor_total_vendas,
ROUND(SUM(p.qtd * p.vrunt)  * q.perccomissao / 100 ,2) AS comissao
FROM tbvendas AS p
LEFT JOIN tbvendedor AS q 
ON p.cdvdd = q.cdvdd
WHERE p.status = 'Concluído'
GROUP BY q.nmvdd
ORDER BY comissao DESC;

'11)Apresente a query para listar o código e nome cliente com maior gasto na loja.
As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.'

SELECT cdcli, nmcli, 
SUM(vrunt * qtd) AS gasto
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY cdcli
ORDER BY gasto DESC
LIMIT(1);

'12) Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
Observação: Apenas vendas com status concluído.'

SELECT p.cddep, p.nmdep, p.dtnasc,
ROUND(SUM(r.qtd * r.vrunt) ,2)  as valor_total_vendas
FROM tbdependente AS p
LEFT JOIN tbvendedor AS q
ON p.cdvdd = q.cdvdd
LEFT JOIN tbvendas as r
ON q.cdvdd = r.cdvdd
WHERE r.status = 'Concluído' 
GROUP BY p.nmdep
ORDER BY p.nmdep DESC
LIMIT (1);

'13)Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas). 
As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.'

SELECT cdpro, nmcanalvendas,nmpro,
SUM(qtd) AS quantidade_vendas
FROM tbvendas
WHERE status = 'Concluído'
GROUP BY cdpro, nmcanalvendas
ORDER BY quantidade_vendas;

'14)Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.
Observação: Apenas vendas com status concluído.'

SELECT estado, 
ROUND (AVG(qtd * vrunt) , 2) AS gastomedio
FROM tbvendas 
WHERE status = 'Concluído'
GROUP BY estado
ORDEr by gastomedio desc;

'15) Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.'
SELECT cdven
FROM tbvendas
WHERE deletado = 1;

'16)Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. 
As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).
Obs: Somente vendas concluídas.'

SELECT estado, nmpro,
ROUND(AVG(qtd) , 4) AS quantidade_media
FROM tbvendas 
WHERE status = 'Concluído'
GROUP BY nmpro, cidade
ORDEr BY estado;

'RESOLUÇÃO DO DO EXERCÍCIO DE EXPORTAÇÃO DE DADOS:

1)'

SELECT p.cod as CodLivro,
p.titulo as Título, 
q.codautor as CodAutor,
q.nome as NomeAutor,
p.valor as Valor,
r.codeditora as CodEditora, 
r.nome as NomeEditora
FROM livro as p
INNER Join autor as q 
On p.autor = q.codautor
Inner Join editora as r
ON p.editora = codeditora
ORDER BY valor DESC
LIMIT (10);

'2)'

SELECT DISTINCT  codeditora as CodEditora, COUNT(p.editora) AS QuantidadeLivros, 
r.nome as NomeEditora
FROM livro as p 
INNER JOIN editora AS r
ON r.codeditora = p.editora
INNER JOIN endereco AS q
ON r.endereco = q.codendereco
Group BY p.editora
ORDER BY QuantidadeLivros desc 
LIMIT (5);