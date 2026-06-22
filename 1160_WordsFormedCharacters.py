# words = ["cat","bt","hat","tree"]
# chars = "atach"
# Output =  6

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
Output =  10

 


def countCharacters(words,chars):
    sum_lengths = []
    # for i in range(0,len(words)):
    #     x = words[i].split(',')
    #     print(x)
    #     if (words[i] in chars):
    #         sum_lengths.append(words[i])
    # print(sum_lengths)
    for i in words:
        for k in i:
            print(k,chars)



print(countCharacters(words,chars))