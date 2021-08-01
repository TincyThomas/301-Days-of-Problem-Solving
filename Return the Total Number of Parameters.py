# You have to make the parameter list yourself


def number_args(*argv):
  count = 0
  for i in argv:
    count = count + 1
  return count
print(number_args(10, 20, 30, 40, 50))

