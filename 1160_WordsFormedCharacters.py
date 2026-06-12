words = ["cat","bt","hat","tree"]
chars = "atach"
Output =  6

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
Output =  10

 


def countCharacters(words,chars):

    result = []
    for i in range(0,len(words)):
        if set(words[i]).issubset(set(chars)):
            result.append(words[i])

    sum1 = ''
    for i in result:
        sum1 = sum1+i

    return len(sum1)


        
print(countCharacters(words,chars))