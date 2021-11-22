def profit(info):
	a = []
	for k,v in info.items():
		a = a + [v]
	return int((a[1]*a[2])-(a[0]*a[2]))
print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))
