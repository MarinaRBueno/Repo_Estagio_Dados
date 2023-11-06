SELECT 
    L.IdLocacao,
    C.IdCliente,
    C.NomeCliente,
    L.IdCarro,
    Ca.ModeloCarro,
    Ca.IdCombustivel,
    Co.TipoCombustivel,
    L.IdVendedor,
    V.NomeVendedor,
    L.DataLocacao,
    L.HoraLocacao,
    L.QtdDiaria,
    L.VlrDiaria,
    L.DataEntrega,
    L.HoraEntrega,
    L.KmCarro
FROM TbLocacao L
JOIN TbCliente C ON L.IdCliente = C.IdCliente
JOIN TbCarro Ca ON L.IdCarro = Ca.IdCarro
JOIN TbCombustivel Co ON Ca.IdCombustivel = Co.IdCombustivel
JOIN TbVendedor V ON L.IdVendedor = V.IdVendedor;
