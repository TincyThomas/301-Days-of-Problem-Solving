def generation(x, y):
    g = {
        -3: {
            "m": "great grandfather",
            "f": "great grandmother",
        },
        -2: {
            "m": "grandfather",
            "f": "grandmother",
        },
        -1: {
            "m": "father",
            "f": "mother",
        },
        0: {
            "m": "me!",
            "f": "me!",
        },
        1: {
            "m": "son",
            "f": "daughter",
        },
        2: {
            "m": "grandson",
            "f": "granddaughter",
        },
        3: {
            "m": "great grandson",
            "f": "great granddaughter",
        }
    }

    for key,value in g.items():                     # looping lkey and value
        if key == x:                                # when key matches
            for k,j in value.items():               # in values, there is another dictionary. Looping key value in values
                if k == y:                          # when key equals input
                    return j                        # return subsequant value


print(generation(-3, "m"))
