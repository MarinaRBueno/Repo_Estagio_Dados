CREATE TABLE TbCliente (
    IdCliente INTEGER PRIMARY KEY,
    NomeCliente VARCHAR(100) NOT NULL,
    CidadeCliente VARCHAR(40) NOT NULL,
    EstadoCliente VARCHAR(40) NOT NULL,
    PaisCliente VARCHAR(40) NOT NULL
);

INSERT INTO TbCliente (IdCliente, NomeCliente, CidadeCliente, EstadoCliente, PaisCliente)
SELECT DISTINCT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM tb_locacao;

SELECT * FROM TbCliente;


CREATE TABLE TbCarro (
    IdCarro INTEGER PRIMARY KEY,
    ModeloCarro VARCHAR(80) NOT NULL,
    AnoCarro INTEGER NOT NULL,
    MarcaCarro VARCHAR(80) NOT NULL,
    ClassiCarro VARCHAR(50) NOT NULL,
    IdCombustivel INTEGER NOT NULL,
    FOREIGN KEY (IdCombustivel) REFERENCES TbCombustivel (IdCombustivel)
);


INSERT INTO TbCarro (IdCarro, ModeloCarro, AnoCarro, MarcaCarro, ClassiCarro, IdCombustivel)
SELECT idCarro, modeloCarro, anoCarro, marcaCarro, classiCarro, idCombustivel
FROM tb_locacao
WHERE (idCarro, datalocacao) IN (
  SELECT idCarro, MIN(datalocacao)
  FROM tb_locacao
  GROUP BY idCarro
);

SELECT * FROM TbCarro;

CREATE TABLE TbCombustivel (
    IdCombustivel INTEGER PRIMARY KEY,
    TipoCombustivel VARCHAR(20) NOT NULL
);

INSERT INTO TbCombustivel (IdCombustivel, TipoCombustivel)
SELECT DISTINCT idCombustivel, tipoCombustivel
FROM tb_locacao;

SELECT * FROM TbCombustivel;

CREATE TABLE TbVendedor (
    IdVendedor INTEGER PRIMARY KEY,
    NomeVendedor VARCHAR(15) NOT NULL,
    SexoVendedor INTEGER NOT NULL,
    EstadoVendedor VARCHAR(40) NOT NULL
);

INSERT INTO TbVendedor (IdVendedor, NomeVendedor, SexoVendedor, EstadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM tb_locacao;

SELECT * FROM TbVendedor;

CREATE TABLE TbLocacao (
    IdLocacao INTEGER PRIMARY KEY,
    IdCliente INTEGER NOT NULL,
    IdCarro INTEGER NOT NULL,
    IdVendedor INTEGER NOT NULL,
    DataLocacao DATE NOT NULL,
    HoraLocacao TIME NOT NULL,
    QtdDiaria INTEGER NOT NULL,
    VlrDiaria DECIMAL(18,2) NOT NULL,
    DataEntrega DATE NOT NULL,
    HoraEntrega TIME NOT NULL,
    KmCarro INTEGER NOT NULL,
    FOREIGN KEY (IdCliente) REFERENCES TbCliente (IdCliente),
    FOREIGN KEY (IdCarro) REFERENCES TbCarro (IdCarro),
    FOREIGN KEY (IdVendedor) REFERENCES TbVendedor (IdVendedor)
);


INSERT INTO TbLocacao (IdLocacao, IdCliente, IdCarro, IdVendedor, DataLocacao, HoraLocacao, QtdDiaria, VlrDiaria, DataEntrega, HoraEntrega, KmCarro)
SELECT DISTINCT idlocacao, idcliente, idcarro, idvendedor, datalocacao, horalocacao, qtddiaria, vlrdiaria, dataentrega, horaentrega, kmcarro
FROM tb_locacao;

DROP TABLE tb_locacao;


