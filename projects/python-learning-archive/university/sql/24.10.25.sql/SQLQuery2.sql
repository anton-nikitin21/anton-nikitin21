select

	ARTICLES, NAMES_PRODUCT, COSTS_RETAIL, count,

	COSTS_RETAIL * count stoim

from PRODUCTS

order by stoim