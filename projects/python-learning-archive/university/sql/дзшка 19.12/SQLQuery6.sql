-- Создаем функцию с детализацией по месяцам и годам

CREATE FUNCTION GetSalesReportByMonthYear

(

    @StartDate DATE,

    @EndDate DATE

)

RETURNS TABLE

AS

RETURN

(

    SELECT 

        -- Месяц

        DATEPART(MONTH, o.DATA_DILIVERY) AS [Месяц],

        

        -- Год

        DATEPART(YEAR, o.DATA_DILIVERY) AS [Год],

        

        -- Форматированная дата "Месяц Год"

        FORMAT(o.DATA_DILIVERY, 'yyyy-MM') AS [Период],

        

        -- Название месяца на русском

        CASE DATEPART(MONTH, o.DATA_DILIVERY)

            WHEN 1 THEN 'Январь'

            WHEN 2 THEN 'Февраль'

            WHEN 3 THEN 'Март'

            WHEN 4 THEN 'Апрель'

            WHEN 5 THEN 'Май'

            WHEN 6 THEN 'Июнь'

            WHEN 7 THEN 'Июль'

            WHEN 8 THEN 'Август'

            WHEN 9 THEN 'Сентябрь'

            WHEN 10 THEN 'Октябрь'

            WHEN 11 THEN 'Ноябрь'

            WHEN 12 THEN 'Декабрь'

        END AS [Название месяца],

        

        -- Количество заказов

        COUNT(DISTINCT o.NUM_ORDERS) AS [Количество заказов],

        

        -- Количество уникальных клиентов

        COUNT(DISTINCT o.LOGIN_CLIENT) AS [Количество клиентов],

        

        -- Выручка (сумма розничных цен * количество товаров)

        SUM(b.COUNT * p.COSTS_RETAIL) AS [Выручка],

        

        -- Прибыль (сумма (розничная - оптовая) * количество)

        SUM(b.COUNT * (p.COSTS_RETAIL - p.COSTS_OPT)) AS [Прибыль],

        

        -- Средний чек

        AVG(b.COUNT * p.COSTS_RETAIL) AS [Средний чек],

        

        -- Количество проданных товаров

        SUM(b.COUNT) AS [Количество проданных товаров]

    

    FROM dbo.ORDERS o

    INNER JOIN dbo.BASKET b ON o.NUM_ORDERS = b.NUM_ORDER

    INNER JOIN dbo.PRODUCTS p ON b.ID_ARTICLES = p.ARTICLES

    

    WHERE o.DATA_DILIVERY BETWEEN @StartDate AND @EndDate

    

    GROUP BY 

        DATEPART(YEAR, o.DATA_DILIVERY),

        DATEPART(MONTH, o.DATA_DILIVERY),

        FORMAT(o.DATA_DILIVERY, 'yyyy-MM')

);

GO