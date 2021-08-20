import datetime
def time_for_milk_and_cookies(date):
    d = date
    if d.day == 24:
        return True
    else:
        return False


print(time_for_milk_and_cookies(datetime.date(2013, 12, 3)))
