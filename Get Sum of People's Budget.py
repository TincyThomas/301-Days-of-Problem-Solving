def get_budgets(lst):
	a = 0
	for i in lst:
		a = a + i["budget"]
	return a
print(get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]))
