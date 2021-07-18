arr = ["cars", "planes", ["trains", ["motorcycles"]]]

# Fix the following using destructuring
# Only edit what's inside of [ trans1, trans2, trans3, trans4 ]
# this statement, as written, will cause a ValueError

# [ trans1, trans2, trans3, trans4 ] = arr

[ trans1, trans2, trans3, trans4 ] = [arr[0],arr[1],arr[2][0],arr[2][1][0]]                     # changes are made in this statement


print(trans1) # should output "cars"
print(trans2) # should output "planes"
print(trans3) # should output "trains"
print(trans4) # should output "motorcycles"
