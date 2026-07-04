
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
Output =  "the cat was rat by the bat"


def replaceWords(dictionary, sentence) :
    lst = []
    for k in sentence.split():
        # print(k,dictionary)
        if k[0:4] in dictionary:
            lst.append(k)
    print(lst)


replaceWords(dictionary, sentence)