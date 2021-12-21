def find_it(items, name):
    for k, v in items.items():
        if k == name:
            return name + " is gone..."
    else:
        return name + " is here!"


print(find_it({
    "tv": 30,
    "timmy": 20,
    "stereo": 50,
},"timmy"))
