names = ["Dennis", "Vera", "Mabel", "Annette", "Sussan"]
jobs = ["Butcher", "Programmer", "Doctor", "Teacher", "Lecturer"]

def assign_person_to_job(names, jobs):        
    d ={}                                     # empty dictionary
    j = 0                                     # initialization
    for i in names:                           # looping names list
        d[i] = jobs[j]                        # assigning key value
        j = j +1                              # incrementing value location
    return d                                  # ultimate dictionary
print(assign_person_to_job(names, jobs))
