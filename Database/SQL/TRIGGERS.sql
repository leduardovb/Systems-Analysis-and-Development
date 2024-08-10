/* EX 01 */

CREATE TRIGGER TGR_PRODUCT_STORAGE
ON itempedido
AFTER INSERT
AS
BEGIN
	DECLARE
	@ID_PRODUTO INT,
	@QUANTIDADE INT

	SELECT
		@ID_PRODUTO = codproduto,
		@QUANTIDADE = quantidade
	FROM
		INSERTED

	UPDATE
		produto
	SET
		quantidade = quantidade - @QUANTIDADE
	WHERE
		codproduto = @ID_PRODUTO
END

/* EX 02 */

CREATE TRIGGER TGR_COSTUMER_LOG
ON cliente
FOR UPDATE
AS
BEGIN
	DECLARE
	@ID_CLIENTE INT,
	@DESCRICAO VARCHAR(255)

	SELECT
		@ID_CLIENTE = codcliente
	FROM
		DELETED

	@DESCRICAO = CONCAT('CLIENTE ' , CAST(@ID_CLIENTE AS VARCHAR) , ' ATUALIZADO.')

	INSERT INTO log (data, descricao) values(GETDATE() , @DESCRICAO)
END

CREATE OR ALTER TRIGGER TGRE_EX02
ON cliente
AFTER UPDATE
AS
BEGIN
	INSERT INTO
		log
	SELECT
		(SELECT ISNULL(MAX(codlog) + 1, 1) FROM log),
		GETDATE(),
		CONCAT('Ação: Update | Cliente ID: ', i.codcliente) 
	FROM
		inserted i
END;
GO

/* EX 03 */

CREATE TRIGGER TGR_PRODUCT_LOG
ON produto
FOR UPDATE
AS
BEGIN
	DECLARE
	@ID_PRODUTO INT,
	@DESCRICAO VARCHAR(255)

	SELECT
		@ID_PRODUTO = codproduto
	FROM
		DELETED

	@DESCRICAO = CONCAT('PRODUTO ' CAST(@ID_PRODUTO AS VARCHAR) , ' ATUALIZADO')

	INSERT INTO log (data, descricao) values(GETDATE() , @DESCRICAO)
END

CREATE OR ALTER TRIGGER TGRE_EX03
ON produto
AFTER UPDATE
AS
BEGIN
	INSERT INTO
		log
	SELECT
		(SELECT ISNULL(MAX(codlog) + 1, 1) FROM log),
		GETDATE(),
		CONCAT('Ação: Update | Produto ID: ', i.codproduto) 
	FROM
		inserted i
END;
GO

/* EX 04 */

CREATE TRIGGER TGR_PRODUCT_QUANTITY_LOG
ON itempedido
FOR INSERT
AS
BEGIN
	DECLARE
	@ID_PRODUTO INT,
	@QUANTIDADE INT,
	@ESTOQUE INT,
	@DESCRICAO VARCHAR(255)

	SELECT
		@ID_PRODUTO = codproduto,
		@QUANTIDADE = quantidade
	FROM
		INSERTED

	SELECT
		@ESTOQUE = quantidade
	FROM
		produto P
	WHERE
		P.codproduto = @ID_PRODUTO

	IF @ESTOQUE - @QUANTIDADE < 0
	BEGIN
		ROLLBACK TRANSACTION
		SET @DESCRICAO = CONCAT('PRODUTO ' , CAST(@ID_PRODUTO AS VARCHAR), ' COM ESTOQUE NEGATIVO')
		INSERT INTO log (codlog, data, descricao) values(1, GETDATE() , @DESCRICAO)
	END
END

CREATE OR ALTER TRIGGER TRGR_EX04
ON itempedido
FOR INSERT
AS
BEGIN
	DECLARE @quantidade INT,
			@codproduto INT,
			@estoque INT,
			@descricao VARCHAR(255)

	SELECT
		@quantidade = i.quantidade,
		@codproduto = i.codproduto,
		@estoque = p.quantidade
	FROM	
		inserted i
		JOIN produto p
			ON p.codproduto = i.codproduto
	
	IF @estoque < @quantidade
	BEGIN
		SET @descricao = CONCAT('Produto sem estoque suficiente. ', @codproduto)
		ROLLBACK TRANSACTION
		EXEC SP_INSERE_LOG @descricao
		RETURN
	END

END;
GO

/* EX 05 */

CREATE OR ALTER TRIGGER TGR_PRODUCT_REQUISITION
ON itempedido
AFTER INSERT
AS
BEGIN
	DECLARE
	@ID_PRODUTO INT,
	@ESTOQUE INT,
	@QTD_VENDA_MENSAL INT

	SELECT
		@ID_PRODUTO = codproduto
	FROM
		INSERTED

	SELECT
		@ESTOQUE = P.quantidade
	FROM
		produto P
	WHERE
		P.codproduto = @ID_PRODUTO

	SELECT
		@QTD_VENDA_MENSAL = SUM(I.quantidade)
	FROM
		itempedido I
	INNER JOIN pedido P
		ON I.codpedido = P.codpedido
	WHERE
		I.codproduto = @ID_PRODUTO AND MONTH(P.datapedido) = MONTH(GETDATE())
	GROUP BY
		I.codproduto

	IF @ESTOQUE <= (@QTD_VENDA_MENSAL / 2)
	BEGIN
		INSERT INTO requisicao_compra (codrequisicaocompra, codproduto, data, quantidade) 
			VALUES 
			(
				(SELECT
					ISNULL(MAX(r.codrequisicaocompra) , 1)
				FROM
					requisicao_compra r) + 1, 
				@ID_PRODUTO, 
				GETDATE(), 
				@QTD_VENDA_MENSAL / 2
			)
	END
END


/* IDENTITY ID */

CREATE FUNCTION FN_AUTO_ID_LOG()
RETURNS INT
AS
	BEGIN
		RETURN
		(
			SELECT
				MAX(numeroitem) + 1
			FROM
				itempedido
		)
	END

/* EX 06 */

CREATE TRIGGER TGR_PRODUCT_ORDER_DELETE_LOG
ON itempedido
AFTER DELETE
AS
BEGIN
	DECLARE
	ID_ITEM INT

	SELECT
		@ID_ITEM = numeroitem
	FROM
		DELETED

	INSERT INTO log VALUES
		(FN_AUTO_ID_LOG(), GETDATE(), CONCAT('Ação Delete | Item pedido: ' , CAST(@ID_ITEM AS VARCHAR)))
END

/* EX 07 */

CREATE TRIGGER TGR_ORDERED_TOTAL_MORE_THAN_1000
ON pedido
FOR INSERT
AS
	BEGIN
		DECLARE
		@ID_PEDIDO INT
		@TOTAL DECIMAL(10, 2)


		SELECT
			@ID_PEDIDO = codpedido,
			@TOTAL = valortotal
		FROM 
			INSERTED


		IF @TOTAL > 1000
			BEGIN
				INSERT INTO LOG VALUES(FN_AUTO_ID_LOG(), GETDATE(), CONCAT('Pedido maior que R$ 1000,00 | Pedido: ' , CAST(@ID_PEDIDO AS VARCHAR)))
			END
	END

/* EX 08 */

CREATE TRIGGER TGR_NOT_NEGATIVE_VALUES_ITEM_PEDIDO
ON itempedido
FOR INSERT
AS
	BEGIN
		DECLARE
		@COD_PEDIDO INT
		@NUMERO_ITEM INT
		@VALOR_UNIT DECIMAL(10, 2)
		@QUANT INT
		@COD_PRODUTO INT

		SELECT
			@COD_PEDIDO = codpedido,
			@NUMERO_ITEM = numeroitem,
			@VALOR_UNIT = valorunitario,
			@QUANT = quantidade,
			@COD_PRODUTO = codproduto
		FROM
			INSERTED

		IF (@COD_PEDIDO < 0 OR @NUMERO_ITEM < 0 OR @VALOR_UNIT < 0 OR QUANT < 0 OR COD_PRODUTO < 0)
			BEGIN
				ROLLBACK TRANSACTION
			END
	END

/* EX 09 */

CREATE TRIGGER TGR_BIRTHDAY_DATE
ON cliente
FOR UPDATE OR INSERT
AS
	BEGIN

		DECLARE 
		@DATA DATE

		SELECT
			@DATA = datanascimento
		FROM
			INSERTED

		IF DATEDIFF(DAY, GETDATE(), @DATA) >= 0
		BEGIN
			ROLLBACK TRANSACTION
		END
	END

/* EX 10 */


tiago.marciano@grupointegrado.br
