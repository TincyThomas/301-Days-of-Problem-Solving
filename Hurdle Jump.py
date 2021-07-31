def hurdle_jump(hurdles, jump_height):
    for i in hurdles:
        if i > jump_height:
            return False
    else:
        return True


print(hurdle_jump([1, 2, 3, 4, 1], 5))
