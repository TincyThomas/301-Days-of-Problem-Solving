def grade_percentage(user_score, pass_score):
	s=''
	if int(user_score[:-1])<int(pass_score[:-1]) :
		s=s+'FAILED'
	if int(user_score[:-1])>=int(pass_score[:-1]) :
		s=s+'PASSED'
	return 'You'+' '+s+' '+'the Exam'

print(grade_percentage("65%", "90%"))
