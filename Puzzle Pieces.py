def puzzle_pieces(a1, a2):
    a = []
    if len(a1) == len(a2):
        for i in range(0,len(a1)):
            a = a + [a1[i]+a2[i]]
        return True if len(set(a)) == 1 else False
    else:
        return False

print(puzzle_pieces([1, 2], [-1, -1]))
