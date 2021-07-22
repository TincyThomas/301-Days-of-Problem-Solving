def volume_of_box(sizes):
    a = 1
    for key, value in sizes.items():
        a = a * value
    return a


print(volume_of_box({"width": 2, "length": 3, "height": 5}))
