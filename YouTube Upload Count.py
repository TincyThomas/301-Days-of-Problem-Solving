def upload_count(dates, month):
        a = len(month)
        b =[]
        for i in dates:
            b = b + [i[:a]]
        return b.count("Sept")
print(upload_count(["Sept 22", "Sept 21", "Oct 15"], "Sept"))
