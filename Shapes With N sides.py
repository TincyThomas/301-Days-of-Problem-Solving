def n_sided_shape(n):
    d = {1:"circle",2:"semi-circle",3:"triangle",4:"square",5:"pentagon",6:"hexagon",7:"heptagon",8:"octagon",9:"nonagon",10:"decagon"}      # making dictionary
    if n in d.keys():                                                                                                                        # looping keys
        return d[n]                                                                                                                          # print matched value
print(n_sided_shape(9))
