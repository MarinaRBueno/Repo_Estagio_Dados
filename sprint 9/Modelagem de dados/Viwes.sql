CREATE VIEW ViewDimCliente AS
SELECT IdCliente, NomeCliente, CidadeCliente, EstadoCliente, PaisCliente
FROM DimCliente;

CREATE VIEW ViewDimCarro AS
SELECT IdCarro, ModeloCarro, AnoCarro, MarcaCarro, ClassiCarro, IdCombustivel
FROM DimCarro;

CREATE VIEW ViewDimCombustivel AS
SELECT IdCombustivel, TipoCombustivel
FROM DimCombustivel;

CREATE VIEW ViewDimVendedor AS
SELECT IdVendedor, NomeVendedor, SexoVendedor, EstadoVendedor
FROM DimVendedor;
    
CREATE VIEW ViewFatoLocacao AS
SELECT IdLocacao, IdCliente, IdCarro, IdVendedor, DataLocacao, HoraLocacao, QtdDiaria, VlrDiaria, DataEntrega, HoraEntrega, KmCarro
FROM FatoLocacao;


'Testando as Views'

SELECT *
FROM ViewDimCliente;

SELECT *
FROM ViewDimCarro;

SELECT *
FROM ViewDimCombustivel;

SELECT *
FROM ViewDimVendedor;

SELECT *
FROM ViewFatoLocacao;
