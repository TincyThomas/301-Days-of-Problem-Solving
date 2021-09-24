def profit_margin(cost_price, sales_price):
	return str(round((((sales_price - cost_price ) / (sales_price))*100),1)) + "%"
print(profit_margin(28, 39))
