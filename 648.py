
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
Output =  "the cat was rat by the bat"


def replaceWords(dictionary, sentence) :
    x = sentence.split(' ')
    for word in x:
        print(word,dictionary)
        # if word[0:4] in dictionary[0:len(dictionary)]:
        #     print('yes')


replaceWords(dictionary, sentence)