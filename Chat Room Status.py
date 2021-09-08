def chatroom_status(users):
    count = 0
    for i in users:
        count = count + 1
    if count == 0:
        return "no one online"
    elif count == 1:
        return "user1 online"
    elif count == 2:
        return "user1 and user2 online"
    else:
        return users[0]+users[1]+"and n-2 more online"
print(chatroom_status(["paRIE_to"]))
