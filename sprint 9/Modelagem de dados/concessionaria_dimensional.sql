CREATE TABLE DimCliente (
    IdCliente INTEGER PRIMARY KEY,
    NomeCliente VARCHAR(100) NOT NULL,
    CidadeCliente VARCHAR(40) NOT NULL,
    EstadoCliente VARCHAR(40) NOT NULL,
    PaisCliente VARCHAR(40) NOT NULL
);

INSERT INTO DimCliente (IdCliente, NomeCliente, CidadeCliente, EstadoCliente, PaisCliente)
SELECT DISTINCT IdCliente, NomeCliente, CidadeCliente, EstadoCliente, PaisCliente
FROM TbCliente;

SELECT * FROM DimCliente;

DROP TABLE TbCliente;


CREATE TABLE DimCarro (
    IdCarro INTEGER PRIMARY KEY,
    ModeloCarro VARCHAR(80) NOT NULL,
    AnoCarro INTEGER NOT NULL,
    MarcaCarro VARCHAR(80) NOT NULL,
    ClassiCarro VARCHAR(50) NOT NULL,
    IdCombustivel INTEGER NOT NULL,
    FOREIGN KEY (IdCombustivel) REFERENCES DimCombustivel (IdCombustivel)
);


INSERT INTO DimCarro (IdCarro, ModeloCarro, AnoCarro, MarcaCarro, ClassiCarro, IdCombustivel)
SELECT IdCarro, ModeloCarro, AnoCarro, MarcaCarro, ClassiCarro, IdCombustivel
FROM TbCarro;

SELECT * FROM DimCarro;

DROP TABLE TbCarro;

CREATE TABLE DimCombustivel (
    IdCombustivel INTEGER PRIMARY KEY,
    TipoCombustivel VARCHAR(20) NOT NULL
);

INSERT INTO DimCombustivel (IdCombustivel, TipoCombustivel)
SELECT DISTINCT IdCombustivel, TipoCombustivel
FROM TbCombustivel;

SELECT * FROM DimCombustivel;

DROP TABLE TbCombustivel;

CREATE TABLE DimVendedor (
    IdVendedor INTEGER PRIMARY KEY,
    NomeVendedor VARCHAR(15) NOT NULL,
    SexoVendedor INTEGER NOT NULL,
    EstadoVendedor VARCHAR(40) NOT NULL
);

INSERT INTO DimVendedor (IdVendedor, NomeVendedor, SexoVendedor, EstadoVendedor)
SELECT DISTINCT IdVendedor, NomeVendedor, SexoVendedor, EstadoVendedor
FROM TbVendedor;

SELECT * FROM DimVendedor;

DROP TABLE TbVendedor;

CREATE TABLE FatoLocacao (
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
    FOREIGN KEY (IdCliente) REFERENCES DimCliente (IdCliente),
    FOREIGN KEY (IdCarro) REFERENCES DimCarro (IdCarro),
    FOREIGN KEY (IdVendedor) REFERENCES DimVendedor (IdVendedor)
);


INSERT INTO FatoLocacao (IdLocacao, IdCliente, IdCarro, IdVendedor, DataLocacao, HoraLocacao, QtdDiaria, VlrDiaria, DataEntrega, HoraEntrega, KmCarro)
SELECT DISTINCT IdLocacao, IdCliente, IdCarro, IdVendedor, DataLocacao, HoraLocacao, QtdDiaria, VlrDiaria, DataEntrega, HoraEntrega, KmCarro
FROM TbLocacao;

DROP TABLE TbLocacao;






