'''
# Fix this incorrect code!
def check_all_even(lst):
  return all(x % 2 == 0)
  '''


def check_all_even(lst):

  return all(x % 2 == 0 for x in lst)
print(check_all_even([6, 2, 8, 1]))
