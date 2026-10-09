CREATE PROCEDURE AddToBasket

    @ClientLogin NVARCHAR(50),

    @PurchaseDate DATE, -- Дата покупки (будем использовать как дату создания заказа)

    @DeliveryDate DATE, -- Дата доставки

    @ProductArticle INT, -- Артикул товара

    @Quantity INT -- Количество товара

AS

BEGIN

    SET NOCOUNT ON;

    

    DECLARE @OrderNum INT;

    DECLARE @StockQuantity INT;

    DECLARE @OrderExists INT;

    

    -- Проверяем существование клиента

    IF NOT EXISTS (SELECT 1 FROM dbo.CLIENTS WHERE LOGINS = @ClientLogin)

    BEGIN

        PRINT 'Ошибка: Клиент с логином "' + @ClientLogin + '" не найден.';

        RETURN;

    END

    

    -- Проверяем существование товара

    IF NOT EXISTS (SELECT 1 FROM dbo.PRODUCTS WHERE ARTICLES = @ProductArticle)

    BEGIN

        PRINT 'Ошибка: Товар с артикулом ' + CAST(@ProductArticle AS NVARCHAR(10)) + ' не найден.';

        RETURN;

    END

    

    -- Проверяем количество товара на складе

    SELECT @StockQuantity = COUNT 

    FROM dbo.PRODUCTS 

    WHERE ARTICLES = @ProductArticle;

    

    IF @StockQuantity < @Quantity

    BEGIN

        PRINT 'Ошибка: Недостаточно товара на складе. На складе: ' + 

              CAST(@StockQuantity AS NVARCHAR(10)) + ', запрошено: ' + 

              CAST(@Quantity AS NVARCHAR(10));

        RETURN;

    END

    

    BEGIN TRY

        BEGIN TRANSACTION;

        

        -- Проверяем, существует ли заказ у клиента на указанную дату покупки

        -- (Предполагаем, что дата покупки = дата создания заказа)

        SELECT @OrderExists = COUNT(*) 

        FROM dbo.ORDERS 

        WHERE LOGIN_CLIENT = @ClientLogin 

          AND CAST(DATA_DILIVERY AS DATE) = @PurchaseDate;

        

        -- Если заказа нет - создаем новый заказ

        IF @OrderExists = 0

        BEGIN

            -- Получаем следующий номер заказа

            SELECT @OrderNum = ISNULL(MAX(NUM_ORDERS), 0) + 1 

            FROM dbo.ORDERS;

            

            -- Получаем адрес клиента

            DECLARE @ClientAddress NVARCHAR(200);

            SELECT @ClientAddress = ADRESS 

            FROM dbo.CLIENTS 

            WHERE LOGINS = @ClientLogin;

            

            -- Создаем новый заказ

            INSERT INTO dbo.ORDERS (NUM_ORDERS, LOGIN_CLIENT, ADRESS_ACTUAL, DATA_DILIVERY, DATA_DIL_ACT)

            VALUES (@OrderNum, @ClientLogin, @ClientAddress, @DeliveryDate, NULL);

            

            PRINT 'Создан новый заказ №' + CAST(@OrderNum AS NVARCHAR(10)) + ' для клиента ' + @ClientLogin;

        END

        ELSE

        BEGIN

            -- Получаем номер существующего заказа

            SELECT @OrderNum = NUM_ORDERS 

            FROM dbo.ORDERS 

            WHERE LOGIN_CLIENT = @ClientLogin 

              AND CAST(DATA_DILIVERY AS DATE) = @PurchaseDate;

        END

        

        -- Проверяем, не добавлен ли уже этот товар в корзину этого заказа

        IF EXISTS (SELECT 1 FROM dbo.BASKET 

                   WHERE NUM_ORDER = @OrderNum AND ID_ARTICLES = @ProductArticle)

        BEGIN

            -- Обновляем количество существующего товара в корзине

            UPDATE dbo.BASKET 

            SET COUNT = COUNT + @Quantity

            WHERE NUM_ORDER = @OrderNum AND ID_ARTICLES = @ProductArticle;

            

            PRINT 'Товар ' + CAST(@ProductArticle AS NVARCHAR(10)) + 

                  ' уже был в корзине. Количество увеличено на ' + CAST(@Quantity AS NVARCHAR(10));

        END

        ELSE

        BEGIN

            -- Добавляем новый товар в корзину

            INSERT INTO dbo.BASKET (NUM_ORDER, ID_ARTICLES, COUNT)

            VALUES (@OrderNum, @ProductArticle, @Quantity);

            

            PRINT 'Товар ' + CAST(@ProductArticle AS NVARCHAR(10)) + 

                  ' добавлен в корзину заказа №' + CAST(@OrderNum AS NVARCHAR(10));

        END

        

        -- Уменьшаем количество товара на складе

        UPDATE dbo.PRODUCTS 

        SET COUNT = COUNT - @Quantity 

        WHERE ARTICLES = @ProductArticle;

        

        PRINT 'Товар успешно добавлен. Остаток на складе: ' + 

              CAST((@StockQuantity - @Quantity) AS NVARCHAR(10));

        

        COMMIT TRANSACTION;

    END TRY

    BEGIN CATCH

        ROLLBACK TRANSACTION;

        PRINT 'Ошибка при добавлении товара в корзину: ' + ERROR_MESSAGE();

    END CATCH

END;