def who_wins_tonight(coins, space, price, size):

  if int(space/size) == int(coins/price):                      # do as question says

    return "Tie"

	elif int(space/size) <  int(coins/price):
    return "Bill"

	else: 

	  return "Will"

print(who_wins_tonight(40, 95, 5, 10)).                         # function calling and printing
