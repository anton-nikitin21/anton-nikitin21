CREATE FUNCTION GetClientsReportByPeriod

(

    @StartDate DATE,

    @EndDate DATE

)

RETURNS TABLE

AS

RETURN

(

    WITH ClientStats AS (

        -- Собираем статистику по клиентам за период

        SELECT 

            c.LOGINS AS Логин,

            -- Предполагаем, что в LOGINS хранится полное имя. Если нужно разбить на части:

            -- Извлекаем фамилию (первое слово)

            CASE 

                WHEN CHARINDEX(' ', c.LOGINS) > 0 

                THEN LEFT(c.LOGINS, CHARINDEX(' ', c.LOGINS) - 1)

                ELSE c.LOGINS

            END AS Фамилия,

            -- Извлекаем имя (второе слово, если есть)

            CASE 

                WHEN LEN(c.LOGINS) - LEN(REPLACE(c.LOGINS, ' ', '')) >= 2

                THEN SUBSTRING(

                    c.LOGINS, 

                    CHARINDEX(' ', c.LOGINS) + 1,

                    CHARINDEX(' ', c.LOGINS + ' ', CHARINDEX(' ', c.LOGINS) + 1) - CHARINDEX(' ', c.LOGINS) - 1

                )

                ELSE NULL

            END AS Имя,

            -- Извлекаем отчество (третье слово, если есть)

            CASE 

                WHEN LEN(c.LOGINS) - LEN(REPLACE(c.LOGINS, ' ', '')) >= 3

                THEN REVERSE(LEFT(REVERSE(c.LOGINS), CHARINDEX(' ', REVERSE(c.LOGINS)) - 1))

                ELSE NULL

            END AS Отчество,

            -- Количество заказов

            COUNT(DISTINCT o.NUM_ORDERS) AS КоличествоЗаказов,

            -- Сумма заказов

            SUM(b.COUNT * p.COSTS_RETAIL) AS СуммаЗаказов

            

        FROM dbo.CLIENTS c

        INNER JOIN dbo.ORDERS o ON c.LOGINS = o.LOGIN_CLIENT

        INNER JOIN dbo.BASKET b ON o.NUM_ORDERS = b.NUM_ORDER

        INNER JOIN dbo.PRODUCTS p ON b.ID_ARTICLES = p.ARTICLES

        

        WHERE o.DATA_DILIVERY BETWEEN @StartDate AND @EndDate

        

        GROUP BY c.LOGINS

    ),

    RankedClients AS (

        SELECT 

            *,

            -- Место по количеству заказов (с учетом совпадений)

            DENSE_RANK() OVER (ORDER BY КоличествоЗаказов DESC) AS МестоПоКоличеству,

            -- Место по сумме заказов (с учетом совпадений)

            DENSE_RANK() OVER (ORDER BY СуммаЗаказов DESC) AS МестоПоСумме

        FROM ClientStats

    )

    SELECT 

        Фамилия,

        Имя,

        Отчество,

        КоличествоЗаказов,

        МестоПоКоличеству AS [Место по количеству заказов],

        СуммаЗаказов,

        МестоПоСумме AS [Место по сумме заказов],

        Логин,

        -- Дополнительные показатели

        CASE 

            WHEN КоличествоЗаказов > 0 

            THEN FORMAT(СуммаЗаказов / КоличествоЗаказов, 'N2') 

            ELSE '0.00'

        END AS [Средний чек],

        -- Процент от общей суммы

        CASE 

            WHEN SUM(СуммаЗаказов) OVER() > 0

            THEN FORMAT(СуммаЗаказов * 100.0 / SUM(СуммаЗаказов) OVER(), 'N2') + '%'

            ELSE '0.00%'

        END AS [Доля в общей выручке]

    FROM RankedClients

);