def get_xp(d):
	a = []
	b = 0
	for k,v in d.items():
		a = a + [v]
	a[0] = a[0]*5
	a[1] = a[1]*10		
	a[2] = a[2]*20
	a[3] = a[3]*40
	a[4] = a[4]*80
	for i in a:
		b = b + i
	return str(b)+ "XP"
print(get_xp({
  "Very Easy" : 254,
  "Easy" : 32,
  "Medium" : 65,
  "Hard" : 51,
  "Very Hard" : 34
}))
