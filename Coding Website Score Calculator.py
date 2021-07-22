def score_calculator(easy, med, hard):
	if easy<0 or med<0 or hard<0:
		return "Invalid"
	else:
		return 5* easy+10*med+20*hard
print(score_calculator(1, 0, -10))
