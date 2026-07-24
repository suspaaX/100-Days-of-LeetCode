'''

1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


# words = ["cat","bt","hat","tree"]
# chars = "atach"
# Output =  6

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
Output =  10


'''



words = ["dyiclysmffuhibgfvapygkorkqllqlvokosagyelotobicwcmebnpznjbirzrzsrtzjxhsfpiwyfhzyonmuabtlwin",
         "ndqeyhhcquplmznwslewjzuyfgklssvkqxmqjpwhrshycmvrb",
         "ulrrbpspyudncdlbkxkrqpivfftrggemkpyjl",
         "boygirdlggnh",
         "xmqohbyqwagkjzpyawsydmdaattthmuvjbzwpyopyafphx",
         "nulvimegcsiwvhwuiyednoxpugfeimnnyeoczuzxgxbqjvegcxeqnjbwnbvowastqhojepisusvsidhqmszbrnynkyop",
         "hiefuovybkpgzygprmndrkyspoiyapdwkxebgsmodhzpx",
         "juldqdzeskpffaoqcyyxiqqowsalqumddcufhouhrskozhlmobiwzxnhdkidr",
         "lnnvsdcrvzfmrvurucrzlfyigcycffpiuoo",
         "oxgaskztzroxuntiwlfyufddl",
         "tfspedteabxatkaypitjfkhkkigdwdkctqbczcugripkgcyfezpuklfqfcsccboarbfbjfrkxp",
         "qnagrpfzlyrouolqquytwnwnsqnmuzphne",
         "eeilfdaookieawrrbvtnqfzcricvhpiv",
         "sisvsjzyrbdsjcwwygdnxcjhzhsxhpceqz",
         "yhouqhjevqxtecomahbwoptzlkyvjexhzcbccusbjjdgcfzlkoqwiwue",
         "hwxxighzvceaplsycajkhynkhzkwkouszwaiuzqcleyflqrxgjsvlegvupzqijbornbfwpefhxekgpuvgiyeudhncv",
         "cpwcjwgbcquirnsazumgjjcltitmeyfaudbnbqhflvecjsupjmgwfbjo","teyygdmmyadppuopvqdodaczob",
         "qaeowuwqsqffvibrtxnjnzvzuuonrkwpysyxvkijemmpdmtnqxwekbpfzs",
         "qqxpxpmemkldghbmbyxpkwgkaykaerhmwwjonrhcsubchs"]

chars = "usdruypficfbpfbivlrhutcgvyjenlxzeovdyjtgvvfdjzcmikjraspdfp"
Output = 0
# print(len(chars))

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
Output =  10

words = ["cat","bt","hat","tree"]
chars = "atach"
Output =  6

def countCharacters(words,chars):
    dict1 = {}
    for i in chars:
        m = chars.count(i)
        dict1.update({i:m})

    dict1_key = dict1.keys()
    # print(dict1_key)
    


    lst1 = []
    for k in words:
        dict2 = {}
        for l in k:
            j = k.count(l)
            dict2.update({l:j})
        lst1.append(dict2)
    # print(lst1)

# {'c': 1, 'a': 1, 't': 1} {'a': 2, 't': 1, 'c': 1, 'h': 1}
# {'b': 1, 't': 1} {'a': 2, 't': 1, 'c': 1, 'h': 1}
# {'h': 1, 'a': 1, 't': 1} {'a': 2, 't': 1, 'c': 1, 'h': 1}
# {'t': 1, 'r': 1, 'e': 2} {'a': 2, 't': 1, 'c': 1, 'h': 1}

    result = []
    for dict in lst1:
        x = dict.keys()
        if (set(x).issubset(set(dict1_key))):
            result.append(dict)

    result2 = []
    for i in result:
        # print(i,dict1)
        for k in i:
            print(k)
    #         if i.get(k) <= dict1.get(k):
    #             result2.append(i)

    # # print(result2)






print(countCharacters(words,chars))