def is_potential_friend(set1, set2):
  count = 0
  for i in set1:
    for j in set2:
      if i ==j:
        count = count+1
    if set1 == set2:
      return True
    elif count ==2:
      return True
    else: return False
print(is_potential_friend({"history","s"},
  {"history",}))
