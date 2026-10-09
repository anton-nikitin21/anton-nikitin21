CREATE PROCEDURE AddProductReview

    @ClientLogin NVARCHAR(100),

    @ProductArticle INT,

    @Grade INT,

    @Comment NVARCHAR(2000) = NULL

AS

BEGIN

    SET NOCOUNT ON;

    

    BEGIN TRY

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

        

        -- Проверяем, что оценка находится в допустимом диапазоне (1-5)

        IF @Grade < 1 OR @Grade > 5

        BEGIN

            PRINT 'Ошибка: Оценка должна быть от 1 до 5. Указано: ' + CAST(@Grade AS NVARCHAR(2));

            RETURN;

        END

        

        -- Проверяем, заказывал ли клиент этот товар

        IF NOT EXISTS (

            SELECT 1 

            FROM dbo.ORDERS o

            INNER JOIN dbo.BASKET b ON o.NUM_ORDERS = b.NUM_ORDER

            WHERE o.LOGIN_CLIENT = @ClientLogin

              AND b.ID_ARTICLES = @ProductArticle

        )

        BEGIN

            DECLARE @ProductName NVARCHAR(100);

            SELECT @ProductName = NAMES_PRODUCT FROM dbo.PRODUCTS WHERE ARTICLES = @ProductArticle;

            

            PRINT 'Ошибка: Клиент "' + @ClientLogin + '" не заказывал товар "' + 

                  ISNULL(@ProductName, CAST(@ProductArticle AS NVARCHAR(10))) + 

                  '". Отзыв можно оставить только на приобретенные товары.';

            RETURN;

        END

        

        -- Добавляем отзыв

        INSERT INTO dbo.OTZOV (LOGIN_CLIENT, grade, ARTICLES, comment)

        VALUES (@ClientLogin, @Grade, @ProductArticle, @Comment);

        

        PRINT 'Отзыв успешно добавлен!';

        PRINT 'Клиент: "' + @ClientLogin + '"';

        PRINT 'Товар: ' + CAST(@ProductArticle AS NVARCHAR(10));

        PRINT 'Оценка: ' + CAST(@Grade AS NVARCHAR(2));

        

        IF @Comment IS NOT NULL AND LEN(@Comment) > 0

            PRINT 'Комментарий: ' + LEFT(@Comment, 100) + 

                  CASE WHEN LEN(@Comment) > 100 THEN '...' ELSE '' END;

        

    END TRY

    BEGIN CATCH

        PRINT 'Ошибка при добавлении отзыва: ' + ERROR_MESSAGE();

    END CATCH

END;