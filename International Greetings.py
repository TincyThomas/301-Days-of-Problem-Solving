GUEST_LIST = {
	"Randy": "Germany",
	"Karla": "France",
	"Wendy": "Japan",
	"Norman": "England",
	"Sam": "Argentina"
}

def greeting(name):
	for k,v in GUEST_LIST.items():
		if name==k:
			return "Hi! I'm "+ k+ ", and I'm from " + v+ "."
		else:
			return "Hi! I'm a guest."
print(greeting("Randy"))
