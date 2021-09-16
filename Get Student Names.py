def get_student_names(students):
	a = []
	for k,v in students.items():
		a = a + [v]
	return sorted(a)
print(get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}))
