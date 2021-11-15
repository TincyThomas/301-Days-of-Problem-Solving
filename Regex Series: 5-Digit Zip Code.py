#x = # Write your regular expression here
import re
x = "\d\d\d\d\d"

print(bool(re.search(x, "32594")))
