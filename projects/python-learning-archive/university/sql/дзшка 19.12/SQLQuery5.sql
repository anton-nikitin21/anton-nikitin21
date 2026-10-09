-- Удаляем представление если оно существует

IF OBJECT_ID('ProductInfoView', 'V') IS NOT NULL

    DROP VIEW ProductInfoView;

GO



-- Создаем представление

CREATE VIEW ProductInfoView

AS

SELECT 

    -- Код товара

    p.ARTICLES AS [Код товара],

    

    -- Название товара

    p.NAMES_PRODUCT AS [Название товара],

    

    -- Количество на складе

    p.COUNT AS [Количество на складе],

    

    -- Количество заказов (в которых есть этот товар)

    ISNULL((

        SELECT COUNT(DISTINCT b.NUM_ORDER)

        FROM dbo.BASKET b

        WHERE b.ID_ARTICLES = p.ARTICLES

    ), 0) AS [Количество заказов],

    

    -- Количество клиентов (которые заказывали этот товар)

    ISNULL((

        SELECT COUNT(DISTINCT o.LOGIN_CLIENT)

        FROM dbo.ORDERS o

        INNER JOIN dbo.BASKET b ON o.NUM_ORDERS = b.NUM_ORDER

        WHERE b.ID_ARTICLES = p.ARTICLES

    ), 0) AS [Количество клиентов],

    

    -- Количество купленного (общее количество проданных единиц)

    ISNULL((

        SELECT SUM(b.COUNT)

        FROM dbo.BASKET b

        WHERE b.ID_ARTICLES = p.ARTICLES

    ), 0) AS [Количество купленного],

    

    -- Название категории товара

    ISNULL(c.NAME_CATEGORY, 'Не указана') AS [Название категории товара]

FROM dbo.PRODUCTS p

LEFT JOIN dbo.CATEGORII c ON p.ID_CATEGORII = c.ID;

GO



-- Проверяем создание представления

SELECT * FROM ProductInfoView;