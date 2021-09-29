def end_corona(recovers, new_cases, active_cases):
    import math
    return math.ceil(active_cases/(recovers - new_cases))
print(end_corona(4000, 2000, 77000))
