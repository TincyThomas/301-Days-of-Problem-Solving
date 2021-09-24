def letter_counter(lst, letter):
    count = 0
    for i in lst:
        for j in i:
            if j == letter:
                count = count+1
    return count
print(letter_counter([
  ["D", "E", "Y", "H", "A", "D"],
  ["C", "B", "Z", "Y", "J", "K"],
  ["D", "B", "C", "A", "M", "N"],
  ["F", "G", "G", "R", "S", "R"],
  ["V", "X", "H", "A", "S", "S"]
], "D"))
