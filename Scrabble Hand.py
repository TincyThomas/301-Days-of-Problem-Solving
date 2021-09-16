def maximum_score(tile_hand):
    a = 0
    for i in tile_hand:
        for k,v in i.items():
            if type(v) == int:
                a = a + v
    return a
print(maximum_score([
  { "tile": "B", "score": 2 },
  { "tile": "V", "score": 4 },
  { "tile": "F", "score": 4 },
  { "tile": "U", "score": 1 },
  { "tile": "D", "score": 2 },
  { "tile": "O", "score": 1 },
  { "tile": "U", "score": 1 }
]))
