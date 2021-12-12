def like_or_dislike(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[-1] == lst[-2]:
            return "Nothing"
        else:
            return lst[-1]


print(like_or_dislike(["Like", "Dislike", "Dislike"]))
