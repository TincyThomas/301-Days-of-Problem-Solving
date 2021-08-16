def simple_timer(seconds):
    if seconds > 60:
        min = int(seconds/60)
        if min >60:
            hr = int(min/60)
            #if hr>60:
            return str(hr) + ":" +str(min-(hr*60))+ ":" + str(seconds-(min*60))
        else:
            return "00:" + str(min)+ ":" + str(seconds-(min*60))
    else:
        return "00:" + "00" + ":" + str(seconds)
print(simple_timer(7220))
