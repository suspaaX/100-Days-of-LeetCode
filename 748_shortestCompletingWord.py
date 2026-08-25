licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]
Output =  "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.


# licensePlate = "1s3 456"
# words = ["looks","pest","stew","show"]
# Output= "pest"


def shortestCompletingWord(licensePlate,words) :
    x = licensePlate.casefold()
    corr_wd = ''
    for i in x:
        if i.isalpha():
            corr_wd = corr_wd+i


    dict_lic = {}
    for k in corr_wd:
        if k in dict_lic:
            dict_lic[k] = dict_lic[k]+1
        else:
            dict_lic[k] = 1


    for word in words:
        dict2 = {}
        for alphabet in word:
            if alphabet in dict2:
                dict2[alphabet] = dict2[alphabet] +1
            else:
                dict2[alphabet] =1
        # print(dict2)
        
        result = []
        for key,val in dict_lic.items():
            print(corr_wd,dict2)
            # if key in dict2 and val<=dict2.get(key):
            #     result.append(word)
            # print(result)
    # print(result)

    # result = []
    # for key1,val1 in dict_lic.items():
    #     print(key1)

            # for key2,val2 in dict2.items():
                # print(val2)

                # if key1 in val2 and val2.get(key1)>=val1:
                #     result.append(key2)

    # print(result)    

    # return result[0]



(shortestCompletingWord(licensePlate,words))