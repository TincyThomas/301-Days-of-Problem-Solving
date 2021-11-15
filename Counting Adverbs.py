def count_adverbs(sentence):
    s = sentence.split(" ")
    count = 0
    for i in s:
        if i[-2:] == "ly" or i[-3:] =="ly.":
            count = count + 1
    return count


print(count_adverbs("She ate the lasagna heartily and noisily."))
