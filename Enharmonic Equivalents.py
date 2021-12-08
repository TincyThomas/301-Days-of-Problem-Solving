def get_equivalent(note):
	d = {"C#":"Db","D#":"Eb","F#":"Gb","G#":"Ab","A#":"Bb"}
	for k,v in d.items():
		if note == k:
			return v
		if note == v:
			return k
print(get_equivalent("D#"))
