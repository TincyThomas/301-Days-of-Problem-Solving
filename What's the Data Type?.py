import datetime
def data_type(value):
	if type(value) == list:
		return "list"
	elif type(value) == dict:
		return "dictionary"
	elif type(value) == str:
		return "string"
	elif type(value) == int:
		return "integer"
	elif type(value) == float:
		return "float"
	elif type(value) == bool:
		return "boolean"
	elif type(value) == datetime.date:
		return "date"
print(data_type(datetime.date(2018,1,1)))
