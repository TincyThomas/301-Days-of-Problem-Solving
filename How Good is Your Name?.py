scores = {"A": 100, "B": 14, "C": 9, "D": 28, "E": 145, "F": 12, "G": 3,
          "H": 10, "I": 200, "J": 100, "K": 114, "L": 100, "M": 25,
          "N": 450, "O": 80, "P": 2, "Q": 12, "R": 400, "S": 113, "T": 405,
          "U": 11, "V": 10, "W": 10, "X": 3, "Y": 210, "Z": 23}

def name_score(name):
	a = 0
	for k,v in scores.items():
		for i in name:
			if i == k:
				a = a + v
	if a <= 60:
		return "NOT TOO GOOD"
	elif 61 <= a <= 300:
		return "PRETTY GOOD"
	elif 301 <= a <= 599:
		return "VERY GOOD"
	elif a >= 600:
		return "THE BEST"
print(name_score("MARY"))
