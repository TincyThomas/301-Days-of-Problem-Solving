def chinese_zodiac(year):
	Rat =[]
	Ox=[]
	Tiger=[]
	Rabbit=[]
	Dragon=[]
	Snake=[]
	Horse=[]
	Sheep=[]
	Monkey=[]
	Rooster=[]
	Dog=[]
	Pig=[]
	for r in range(1924,2033,12):
		at = Rat.append(r)
	for o in range(1925,2034,12):
		at = Ox.append(o)
	for t in range(1926,2035,12):
		at = Tiger.append(t)
	for ra in range(1927,2036,12):
		at = Rabbit.append(ra)
	for d in range(1928,2037,12):
		at = Dragon.append(d)
	for s in range(1929,2038,12):
		at = Snake.append(s)
	for m in range(1930,2039,12):
		at = Monkey.append(m)
	for ro in range(1931,2040,12):
		at = Rooster.append(ro)
	for do in range(1932,2041,12):
		at = Dog.append(do)
	for p in range(1933,2042,12):
		at = Pig.append(p)
	lst = [Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Sheep, Monkey, Rooster, Dog,Pig]
	ma = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog','Pig']
	for li in lst:
		ind = lst.index(li)
		for y in li:
			if y == year:
				return ma[ind]
print(chinese_zodiac(1998))
