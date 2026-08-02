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
    dict2 = {}
    for i in chars:
        if i in dict2:
            dict2[i] = dict2[i]+1
        else:
            dict2[i] = 1

    lst = []
    for wd in words:
        dict1 = {}
        for alpha in wd:
            if alpha in dict1:
                dict1[alpha] = dict1[alpha]+1
            else:
                dict1[alpha] = 1


        if set(dict1).issubset(dict2): 
            lst.append(dict1)
 
    for k in lst:
        result = []
        for key,val in k.items():
            if val <= dict2.get(key):
                result.append(k)

                return result

print(countCharacters(words,chars))