def sub_reddit(link):
    word = ''
    for i in range(len(link)-2,0,-1):
        if link[i] != "/":
            word =  link[i] + word
        else:
            return word
print(sub_reddit("https://www.reddit.com/r/wondrfulll/"))
