def retrieve_major(semver):
	return semver[0]

def retrieve_minor(semver):
	return semver[2]

def retrieve_patch(semver):
	return semver[4]

print(retrieve_patch("6.1.9"))
