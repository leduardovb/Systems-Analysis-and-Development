/* Exercicio 01 */

UPDATE LOCACAO 
	SET dataDevolucao = '2019/17/12'
WHERE
	fitaId = 14
GO

UPDATE LOCACAO 
	SET dataDevolucao = '2019/17/12'
WHERE
	fitaId = 26
GO

UPDATE LOCACAO 
	SET dataDevolucao = '2019/17/12'
WHERE
	fitaId = 27
GO

UPDATE LOCACAO 
	SET dataDevolucao = '2019/01/12'
WHERE
	fitaId = 1
GO

UPDATE LOCACAO 
	SET dataDevolucao = '2019/19/11'
WHERE
	fitaId = 4
GO

UPDATE LOCACAO 
	SET dataDevolucao = '2019/19/11'
WHERE
	fitaId = 9
GO

/* Exercicio 02 */ *

SELECT 
	L.clienteId AS ID_CLIENTE,
	COUNT(DISTINCT F.id) AS QTD_FILME
FROM LOCACAO L
INNER JOIN FITA FT
	ON L.fitaId = FT.id
INNER JOIN FILME F
	ON FT.filmeId = F.id
GROUP BY
	L.clienteId

/* Exercicio 03 */

SELECT
	F.id AS ID_FILME,
	F.descricao AS NOME_FILME,
	COUNT(FT.id) AS QUANT_FITA
FROM FITA FT
RIGHT JOIN FILME F
	ON FT.filmeId = F.id
GROUP BY 
	F.id,
	F.descricao
	
/* Exercicio 04 */ 

SELECT
	C.categoriaId AS ID_CATEGORIA,
	COUNT(DISTINCT FT.filmeId) AS QUANT_FILMES
FROM FILME F
RIGHT JOIN CATEGORIA C
	ON F.categoriaId = C.id
INNER JOIN FITA FT
	ON F.id = FT.filmeId
INNER JOIN LOCACAO L
	ON FT.id = L.fitaId
GROUP BY
	C.categoriaId

/* Exercicio 05 */ 

SELECT 
	COUNT(DISTINCT F.id) AS QTD_FILMES_LOCADO
FROM LOCACAO L
INNER JOIN FITA FT
	ON L.fitaId = FT.id
INNER JOIN FILME F
	ON FT.filmeId = F.id

/* Exercicio 06 */

SELECT
	L.clienteId AS ID_CLIENTE,
	AVG(F.valor) AS 'VALOR MÉDIO GASTO'
FROM LOCACAO L
INNER JOIN FITA FT
	ON L.fitaId = FT.id
INNER JOIN FILME F 
	ON FT.filmeId = F.id
GROUP BY 
	L.clienteId

/* Exercicio 07 */

SELECT
	F.categoriaId AS ID_CATEGORIA,
	AVG(F.valor) AS 'VALOR MÉDIO'
FROM LOCACAO L
INNER JOIN FITA FT
	ON L.fitaId = FT.id
INNER JOIN FILME F 
	ON FT.filmeId = F.id
GROUP BY 
	F.categoriaId

/* Exercicio 08  */ 

SELECT 
	L.clienteId AS ID_CLIENTE,
	COUNT(DISTINCT F.id) AS QTD_FILME_DEVOLVER
FROM LOCACAO L
INNER JOIN FITA FT
	ON L.fitaId = FT.id
INNER JOIN FILME F
	ON FT.filmeId = F.id
WHERE 
	L.dataDevolucao IS NULL
GROUP BY 
	L.clienteId

/* Exercicio 09 */

SELECT
	L.clienteId AS ID_CLIENTE,
	L.dataLocacao,
	COUNT(L.fitaId) AS QUANT_LOCADA
FROM LOCACAO L
GROUP BY 
	L.clienteId, 
	L.dataLocacao
ORDER BY 
	L.clienteId

/* Exercicio 10 */  

SELECT 
	COUNT(DISTINCT FT.filmeId) AS QTD_FILMES_LOCADO
FROM LOCACAO L
INNER JOIN FITA FT
	ON L.fitaId = FT.id
WHERE 
	MONTH(dataLocacao) = 11 OR MONTH(dataLocacao) = 12 AND YEAR(dataLocacao) = 2019 

/* Exercicio 11 */ 

SELECT 
	C.id AS ID_CLIENTE,
	C.nome AS NOME,
	COUNT(DISTINCT FT.filmeId) AS QTD_FILMES_LOCADO,
CASE 
	WHEN C.ativo = 0 THEN 'INATIVO'
	WHEN C.ativo = 1 THEN 'ATIVO'
END AS STATUS
FROM CLIENTE C
INNER JOIN LOCACAO L
	ON C.id = L.clienteId
INNER JOIN FITA FT
	ON L.fitaId = FT.id
GROUP BY 
	C.id, 
	C.nome, 
	C.ativo

/* Exercicio 12 */

SELECT
	F.id AS ID_FILME,
	F.descricao AS NOME_FILME,
	C.descricao AS CATEGORIA,
CASE
	WHEN F.valor < 15 THEN 'VALOR ABAIXO DE R$ 15,00'
	WHEN F.valor >= 15 AND F.valor <= 20 THEN 'VALOR ENTRE R$ 15,00 E R$ 20,00'
	WHEN F.valor > 20 THEN 'VALOR ACIMA DE R$ 20,00'
END AS 'FAIXA DE VALOR'
FROM FILME F
INNER JOIN CATEGORIA C
	ON F.categoriaId = C.id
	
/* Exercicio 13 */

SELECT
	C.id AS ID_CLIENTE,
	C.nome AS NOME,
	SUM(F.valor) AS VALOR_TOTAL,
	SUM(F.valor) * 1.10 AS VALOR_TOTAL_ACRESCIMO,
CASE 
	WHEN C.ativo = 0 THEN 'INATIVO'
	WHEN C.ativo = 1 THEN 'ATIVO'
END AS STATUS
FROM CLIENTE C
INNER JOIN LOCACAO L
	ON C.id = L.clienteId
INNER JOIN FITA FT
	ON L.fitaId = FT.id
INNER JOIN FILME F
	ON FT.filmeId = F.id
WHERE 
	L.dataDevolucao IS NULL
GROUP BY
	C.id, 
	C.nome, 
	C.ativo

/* Exercicio 14 */

SELECT
	COUNT(L.fitaId) AS QTD_LOCACAO,
	AVG(F.valor) AS 'VALOR MÉDIO TICKET',
	MIN(F.valor) AS 'MENOR VALOR TICKET',
	MAX(F.valor) AS 'MAIOR VALOR TICKET'
FROM LOCACAO L 
INNER JOIN FITA FT
	ON L.fitaId = FT.id
INNER JOIN FILME F
	ON FT.filmeId = F.id
WHERE 
	YEAR(L.dataLocacao) = 2019


/* Exercico 15 */

SELECT
	C.id AS ID_CLIENTE,
	C.nome AS NOME,
	COUNT(L.fitaId) AS QTD_LOCADO
FROM CLIENTE C
INNER JOIN LOCACAO L
	ON C.id = L.clienteId
GROUP BY 
	C.id, 
	C.nome
HAVING 
	COUNT(L.fitaId) > 5

/* Exercicio 16 */

SELECT
	F.id AS ID_FILME,
	F.descricao AS NOME_FILME,
	COUNT(L.fitaId) AS QTD_LOCADO
FROM FILME F
INNER JOIN FITA FT
	ON F.id = FT.filmeId
INNER JOIN LOCACAO L
	ON FT.id = L.fitaId
GROUP BY 
	F.id, 
	F.descricao
HAVING 
	COUNT(L.fitaId) > 1
	
/* Exercicio 17 */

SELECT
	C.id AS ID_CATEGORIA,
	C.descricao AS CATEGORIA,
	COUNT(L.fitaId) AS QTD_LOCADA
FROM CATEGORIA C
INNER JOIN FILME FL
	ON C.id = FL.categoriaId
INNER JOIN FITA FT
	ON FL.id = FT.filmeId
INNER JOIN LOCACAO L
	ON FT.id = L.fitaId
GROUP BY 
	C.id, 
	C.descricao
HAVING 
	COUNT(L.fitaId) > 1